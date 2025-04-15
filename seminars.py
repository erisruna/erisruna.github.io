from typing import Any
import os
import click
import sys
import re
import datetime
import pandas as pd
from functools import cache
from dateutil.parser import parse

url = "https://docs.google.com/spreadsheets/d/1hsAkaOYdDQ5tc3cYlUxSEZpnGJ6-Fn95MK7dkMOmKDA/export?gid=0#gid=0&format=xlsx"

def format_time(data: str):
    data = str(data)
    dt = parse(data)
    res = dt.strftime("%Y/%m/%d  %H:%M:%S")
    return  res




@cache
def get_data(url):
    df = pd.read_excel(url)
    df["Workshop #"] = df["Workshop #"].str.lower()
    return df

def switch_schedule(idx: int, how):
    dir_name = f"content/workshop{idx}"
    fname = f"{dir_name}/_index.md"
    with open(fname, 'r') as f:
        txt = f.read()
    if how is True:
        txt = re.sub(r'\nschedule *= *"\w*"', r'\nschedule = "True"' , txt)
    elif how is False:
        txt = re.sub(r'\nschedule *= *"\w*"', r'\nschedule = "False"' , txt)
    with open(fname, 'w') as f:
        _ = f.write(txt)


def get_google_link(name: str)-> str:
    if pd.isna(name):
        name = ""

    tmp_name = name.lower()
    url = ""
    if 'isef' in tmp_name or 'main lecture hall' in tmp_name:
        url = "https://www.google.com/maps/dir//Gran+Sasso+Science+Institute,+Viale+Francesco+Crispi,+7+Rectorate,+Via+Michele+Iacobucci,+2,+67100+L'Aquila+AQ,+Italy/@42.3445687,13.31408"
    elif 'inps' in tmp_name:
        url = "https://www.google.com/maps/dir//Gran+Sasso+Science+Institute+(Ex-INPS+Building),+Viale+Luigi+Rendina,+26-28,+67100+L'Aquila+AQ,+Italy/@42.3451348,13.3177662"
    elif 'rectorate' in tmp_name or "auditorium" in tmp_name:
        url = "https://www.google.com/maps/dir//Rettorato+GSSI+-+Palazzo+ex+GIL,+Via+Michele+Iacobucci,+2,+67100+L'Aquila+AQ,+Italy/@42.3443938,13.3153852"
    if url:
        return f"<a href='{url}'>{name}</a>"
    else:
        return name


def sanitize(speaker: str) -> str:
    speaker = speaker.strip().lower()
    speaker = speaker.replace(" ", "_").replace("*", "")
    return speaker

def escape_string(s: str) -> str:
    try:
        s = s.replace("\\", "\\\\").replace("”", "\"")
        return s
    except:
        return s



def empty_str_if_na(s: str) -> str:
    if not pd.isna(s):
        return s.strip()
    return ""

def get_title_workshop(idx: int):
    dir_workshop = f"content/workshop{idx}"
    with open(dir_workshop+"/_index.md", 'r') as f:
        txt = f.read()
    res = re.findall(r"""\ntitle *= +['"](.*)['"]""", txt)[0]
    return res

def strf_f_dt(dt: datetime.datetime) -> str:
    if pd.isna(dt):
        return ""
    return dt.strftime('%H:%M')


def row_to_line(row: dict[str, Any]) -> str:
    dt_start = pd.to_datetime(row['StartTime'])
    dt_end = pd.to_datetime(row['EndTime'])
    Speaker = empty_str_if_na(row['Speaker'])
    workshop = empty_str_if_na(row['Workshop #'])
    Affiliation = f"({row['Affiliation']})" if  not pd.isna(row['Affiliation']) else ""
    Title = f"{empty_str_if_na(escape_string(row['Title']))}"
    if not Title:
        Title = "TBA"
    Title = f"*{Title.strip()}*"
    if Speaker + Affiliation:
        res = f"""|{dt_start.strftime('%H:%M')}-{strf_f_dt(dt_end)}|{Speaker} {Affiliation}|
|  |[{Title}](/{workshop}/{sanitize(Speaker)})|"""
    else:
        res = f"""|{dt_start.strftime('%H:%M')}-{strf_f_dt(dt_end)}| {Title}|"""
    return res

def row_to_md(row: dict) -> str:
    dt = pd.to_datetime(row['StartTime'])
    dt_end = pd.to_datetime(row['EndTime'])
    Title = empty_str_if_na(escape_string(row['Title']))
    if not Title:
        Title = "TBA"
    Abstract = empty_str_if_na(row['Abstract'])
    if not Abstract:
        Abstract = "TBA"
    txt = f"""+++
title = "{Title}"
subtitle = "by Prof. {row['Speaker']}"
speaker = "{row['Speaker']}"
begin = "{format_time(dt)}"
end = "{format_time(dt)}"
datetime = "{dt.strftime("%H:%M")}-{dt_end.strftime("%H:%M")} {datetime_to_header(row['StartTime'])}"
location = "{get_google_link(row['SeminarLocation'])}"
tags = "a_s_w"
+++

### Abstract
{Abstract}
"""
    return txt


def datetime_to_header(_d) -> str:
    res = f"{_d.strftime("%A")}, {_d.day} {_d.strftime("%B")} {_d.strftime("%Y")}"
    return res




def create_single_seminar_page_info(row):
    Speaker = row['Speaker'] if not pd.isna(row['Speaker']) else ""
    if not Speaker:
        return
    Speaker = sanitize(Speaker)
    workshop = row['Workshop #']

    if pd.isna(workshop):
        return

    txt = row_to_md(row)
    fname = ''
    if 'workshop' in workshop.lower():
        fname = f"content/{workshop}/{Speaker}.md"
    elif 'seminar' in workshop.lower():
        fname = f"content/seminars/{Speaker.replace('._', '_')}.md"
    if fname:
        if not os.path.isdir("content/seminars"):
            os.mkdir("content/seminars")
        if os.path.isfile(fname):
            fname = fname[:-3]+"_.md"

        with open(fname, "w") as f:
            print(f"Creating {fname}")
            _ = f.write(txt)


def clean_built_files():
    import os
    for idx in range(1,5):
        dir_name = f"content/workshop{idx}"
        for l in os.listdir(dir_name):
            fname = f"{dir_name}/{l}"
            with open(fname) as f:
                txt = f.read()

            if 'tags = "a_s_w"' in txt or 'subtitle = "Schedule"' in txt:
                print(f"Removing {fname}")
                os.remove(fname)


def build_seminars():
    df = get_data(url)
    activity_type = df.columns[1]
    use_col = df.columns[0]
    df = df[~df[activity_type].isna()]
    mask = df[activity_type].str.lower().str.contains('seminar')
    mask = mask & (df[use_col].str.lower() == "yes")
    ddf = df[mask]
    for _, row in ddf.iterrows():
        create_single_seminar_page_info(row)


def build_single(idx, ignore_use=False):
    df = get_data(url)
    activity_type = df.columns[1]
    mask = df[activity_type] == f"workshop{idx}"

    if any(mask) is False:
        return

    ddf: pd.DataFrame  = df.loc[mask]
    switch_schedule(idx, False)

    if all(ddf['StartTime'].isna() == True):
        return

    # if all(ddf['EndTime'].isna() == True):
    #     return

    use_col = df.columns[0]
    ddf.loc[:, use_col] = ddf[use_col].str.upper()

    if any(ddf[use_col].str.lower()  == "no") and ignore_use == False:
        switch_schedule(idx, False)
        return

    switch_schedule(idx, True)
    workshop = ddf[activity_type].values[0]
    for _, row in ddf.iterrows():
        create_single_seminar_page_info(row)

    res = f"""+++
title = "{get_title_workshop(idx)}"
subtitle = "Schedule"
+++
"""
    for _d, _df in ddf.groupby([ddf['StartTime'].dt.date]):
        _d = _d[0]
        res +=  "\n\n#####  " + datetime_to_header(_d)+"\n"
        _df.sort_values('StartTime', inplace=True)
        res += """
{{< table2 >}}
|   |   |
|---|---|"""
        for _, row in _df.iterrows():
            row = row.to_dict()
            res += f"\n" + row_to_line(row) 
        res+="\n{{</ table2 >}}"
    res += "\n{{< br >}}"
    print(res)

    fname = f"content/{workshop}/schedule.md"
    with open(fname, "w") as f:
        print(f"Creating {fname}")
        _ = f.write(res)


@click.group
def cli():
    pass

@cli.command()
def clean():
    clean_built_files()

@cli.command()
def build():
    clean_built_files()
    build_single(1)
    build_single(2)
    build_single(3)
    build_single(4)
    build_seminars()

if __name__ == "__main__":
    # build_seminar()
    # pass
    cli()
