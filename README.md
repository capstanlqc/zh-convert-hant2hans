# Chinese script conversion

These steps show how to convert Chinese traditional spelling to simplified spelling. 

There are two parts, and two alternative approaches for the second part. 

## First part: batch export

The goal of this part is to export a Excel or CSV/TSV file containing the source text and the target text in the Chinese version that uses traditional script. This assumes an OmegaT project with language pair, say, `en` > `zh-MO` (or similar).

### Team project

If you have one team project including a working TM (`omegat/project_save.tmx`) containing the translations in `zh-MO` you want to use, please proceed as follows:

1. Download the team project in OmegaT
2. Pack the project to make an offline copy (so that you can add/remove files or folders)
3. Remove all source files you don't want and add the files you include in your export
4. Export as TSV (using script: `Write Source and Target to TXT`) or similar.

(Repeate steps 3-4 for each bunch of files or batch you need to process.)

### Project packages

If you have one project package containing the files or batch you want to include in your export, proceed as follows:

1. Unpack the project in OmegaT.
2. Export as TSV (using script: `Write Source and Target to TXT`) or similar.

Repeat the two steps for each batch/package you want to convert.

## Second part: script conversion

You have two options to do the conversion:

### First approach: LibreOffice Calc

1. In LibreOffice Calc, go to **Tools** > **Options** > **Languages and Locales** >  **General** and tick option "Asian (or perhaps called "Asian language support").
2. Open each TSV file in LibreOffice Calc, select the column in Chinese and go to **Tools** > **Language** > **Chinese Conversion...**,  tick "Traditional Chinese to simplified Chinese" and press OK. 
3. Then Save (as Excel if you like).

### Second approach: running the `zh_t2s.py` script

You might want to define what is the original version (generic traditional or, say, Hong Kong standard) by setting the conversion with `cc.set_conversion('hk2s')` (check [docs](https://pypi.org/project/opencc-python-reimplemented/)).

1. Put all the TSV exports that you want to convert in a `t2s` subfolder in the omegat project.
2. Run `python3.12 zh_t2s.py -p /path/to/omegat/project`.
3. Collect the converted Excel files (containing the Chinese version in simplified script) from the `hans` subfolder in the omegat project.

## Third pard: convert TSV/Excel to TMX

Use TMX Editor to convert each spreadsheet in simplified script to TMX.