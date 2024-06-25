#!/usr/bin/env python

# info: https://pypi.org/project/opencc-python-reimplemented/
# run as:
# python3.12 zh_t2s.py -p /path/to/omegat/project

from opencc import OpenCC
import os
import sys
from pathlib import Path
import pandas as pd

if len(sys.argv) < 3:
    sys.exit()

# omtprj_dpath = "/run/media/souto/ExtremePro/Work/pisa_2025ft_translation_zh-MO_final-check-review_OMT"
omtprj_dpath = sys.argv[2]

cc = OpenCC()
cc.set_conversion('t2s')

input_dpath = os.path.join(omtprj_dpath, "t2s")
output_dpath = os.path.join(omtprj_dpath, "hans2")
os.makedirs(output_dpath, exist_ok=True)

# files = [os.path.join(input_dpath, f) for f in os.listdir(input_dpath) if os.path.isfile(os.path.join(input_dpath, f))]
files = [f for f in Path(input_dpath).iterdir() if f.is_file()]

for fpath in files:
    fname = Path(fpath).stem # strip extension (allegedly .tsv)
    input_df = pd.read_csv(fpath, delimiter='\t', header=None, usecols=[0, 1], names=['en', 'zh-MO'])
    data_dict = {
        'en': list(input_df['en']), 
        'zh-Hans-MO': [cc.convert(seg) for seg in list(input_df['zh-MO'])]
    }
    output_df = pd.DataFrame(data_dict)
    output_df.drop_duplicates(inplace=True)
    
    output_fpath = os.path.join(output_dpath, f"{fname}.xlsx")
    output_df.to_excel(output_fpath, index=False)