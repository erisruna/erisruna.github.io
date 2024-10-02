import os
import pdb
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1THM-kbxazn22yNlZoufK-KvEvmduqzvwdtC7DyIe6-A/export?gid=0#gid=0&format=xlsx"
#
seminar_directory = "content/seminars"
TAG = 'tags = "seminars'


def clean_item(x):
    x = x if x else ""
    return x

def get_text_short(row):
    res = {}
    row = row.to_dict()
    for k in row:
        res[k] = clean_item(row[k])
    abstract = res['Abstract']
    title = res['Title']
    if not abstract:
        abstract = "TBA"


    if not title:
        title = "TBA"
    abstract.replace(r'\n', ' '*4 + r"\n")

    txt = f"""+++
title = "{title}"
speaker = "{res['Speaker']}"
date = "{res['Date']}"
publishDate = 2023-10-19T00:40:04-07:00
{TAG}_short"
+++

* {res['Date']}, {res['Place']}
* Speaker: __{res['Speaker']}__ ({res['University']})
* Abstract: {abstract}

"""
    return txt


def get_text_long(row):

    row = row.to_dict()
    res = {}
    for k in row:
        res[k] = clean_item(row[k])

    abstract = res.get('Abstract', "")
    title = res['Title']
    if not abstract:
        abstract = "TBA"
    abstract.replace(r'\n', ' '*4 + r"\n")

    txt = f"""+++
title = "{title}"
speaker = "{res['Speaker']}"
date = "{res['Date']}"
publishDate = 2023-10-19T00:40:04-07:00
{TAG}_long"
+++

{{{{< br >}}}}
# {res['Title']}
#### Speaker: __{res['Speaker']}__ ({res['University']})
*    __{res['Date']}, {res['Place']}__
*    Abstract: {abstract}

"""
    return txt


def get_fname(row, appendix):
    return f"{seminar_directory}/{row['ShortName'].lower().replace(' ', '_')}_{appendix}"

def clean():
    lista = os.listdir(seminar_directory)
    for l in lista:
        fname = os.path.join(seminar_directory, l)
        with open(fname, 'r') as f:
            tmp = f.read()
        if TAG in tmp:
            print(fname)
            os.remove(fname)


def generate(df):
    df.fillna("", inplace=True)
    for idx, row in df.iterrows():
        ##
        txt_short = get_text_short(row)
        txt_long = get_text_long(row)
        # print(txt_short)
        ##
        fname_short = f"{get_fname(row, idx)}_short.md"
        fname_long = f"{get_fname(row, idx)}.md"
        ##
        with open(fname_short, "w") as f:
            f.write(txt_short)

        with open(fname_long, "w") as f:
            f.write(txt_long)

if __name__ == '__main__':
    # df = pd.read_excel(url)
    clean()
    # generate(df)
