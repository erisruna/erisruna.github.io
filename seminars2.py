from typing import Any
from dateutil.parser import parse
import os
import re
import click
import sys
import re
import pdb
import datetime
import pandas as pd
from functools import cache


coffe_break_color = "#2C5F2D"
workshop_color = "#2F3C7E"
course_color = "#990011"

url = "https://docs.google.com/spreadsheets/d/1hsAkaOYdDQ5tc3cYlUxSEZpnGJ6-Fn95MK7dkMOmKDA/export?gid=0#gid=0&format=xlsx"


def get_tags(fname):
    with open(fname, 'r') as f:
        tmp = f.read()
    res=  re.findall(r"""tags.*=.*['"](\w*)['"]""", tmp)
    if res:
        return res[0]
    return ""

def format_time(data: str):
    data = str(data)
    dt = parse(data)
    res = dt.strftime("%Y/%m/%d  %H:%M:%S")
    return  res


def get_fnames() -> list[str]:
    fnames = []
    for x,y,z in os.walk("content"):
        fnames +=[os.path.join(x,t) for t in z if '.md' in t] 
    return fnames

def get_link_title(fname: str) -> str:
    with open(fname, 'r') as f:
        tmp = f.read()
    res=  re.findall(r"""LinkTitle.*=.*['"](\w*)['"]""", tmp)
    if res:
        return res[0]
    return ""

def get_title(fname: str) -> str:
    with open(fname, 'r') as f:
        tmp = f.read()
    res = re.findall(r"""title.*=.*['"](.*)['"]""", tmp)
    if res:
        return res[0]
    return ""

def get_subtitle(fname: str) -> str:
    with open(fname, 'r') as f:
        tmp = f.read()
    res = re.findall(r"""subtitle.*=.*['"](.*)['"]""", tmp)
    if res:
        return res[0]
    return ""

def get_begin(fname: str) -> str:
    with open(fname, 'r') as f:
        tmp = f.read()
    res = re.findall(r"""\n *begin.*=.*['"](.*)['"]""", tmp)
    if res:
        return res[0]
    return ""

def get_end(fname: str) -> str:
    with open(fname, 'r') as f:
        tmp = f.read()
    res = re.findall(r"""\n *end.*=.*['"](.*)['"]""", tmp)
    if res:
        return res[0]
    return ""


@cache
def _get_data(url) -> pd.DataFrame:
    df: pd.DataFrame = pd.read_excel(url)
    activity_type = df.columns[1]
    df[activity_type] = df[activity_type].str.lower()
    return df

def get_data(url) -> pd.DataFrame:
    return _get_data(url).copy()



template = r"""<script src='https://cdn.jsdelivr.net/npm/fullcalendar@6.1.15/index.global.min.js'></script>
<link rel='stylesheet' href='https://fullcalendar.io/releases/core/4.2.0/main.min.css'>
<link rel='stylesheet' href='https://fullcalendar.io/releases/daygrid/4.2.0/main.min.css'>
<link rel='stylesheet' href='https://fullcalendar.io/releases/timegrid/4.2.0/main.min.css'>
<link rel='stylesheet' href='https://fullcalendar.io/releases/list/4.2.0/main.min.css'>
  
 <div id="fullcalendar"></div>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.26.0/moment.min.js'></script>
<script src='https://fullcalendar.io/releases/core/4.2.0/main.min.js'></script>
<script src='https://fullcalendar.io/releases/daygrid/4.2.0/main.min.js'></script>
<script src='https://fullcalendar.io/releases/timegrid/4.2.0/main.min.js'></script>
<script src='https://fullcalendar.io/releases/list/4.2.0/main.min.js'></script>
      <script id="rendered-js" >
"use strict";

function strToDT(dt, add_days=0) {
  let d = new Date(Date.parse(dt));
  d.setDate(d.getDate() + add_days);
  return d
}

function getMinMaxDate(fixedDate) {
    const today = new Date();
    const fixed = new Date(fixedDate);

    // Get the maximum (latest) date
    const maxDate = today > fixed ? today : fixed;

    // Format to YYYY-MM-DD
    return maxDate.toISOString().split('T')[0];
}

var events = [
    {
        daysOfWeek: [0, 6],
        rendering: "background",
        color: "#eee",
        overLap: false,
        allDay: false
    },

    // >>>>>>>>>>>>>>>>>>>>>> FOR1

{{ range where  (sort .Site.Pages "LinkTitle") ".Params.tags" "in" "workshop" }}
    { 
      title: '{{ .Title }}',
      start: strToDT("{{ .Params.begin }} 2025 10:00:00"),  
      end: strToDT("{{ .Params.end }} 2025 23:00:00", 1),
      allDay: true,
      description: 'workshop',
      color: 'workshop_color',
      url: {{ .Permalink }}
     },
{{ end }}
    // <<<<<<<<<<<<<<<<<<<<<< FOR1

    // >>>>>>>>>>>>>>>>>>>>>> FOR2
{{ range where  (sort .Site.Pages "LinkTitle") ".Params.tags" "in" "a_s_w" }}
    { 
      {{ if in .Params.speaker "**" }}
      title: '<strong>{{ .Params.calendar_speaker}}</strong>',
      {{ else }}
      title: '{{ .Params.speaker }}',
      {{ end }}
      start: strToDT("{{ .Params.begin }}"),  
      end: strToDT("{{ .Params.end }}", 0),
      allDay: false,
      description: '{{ .Title }}',
      color: 'workshop_color',
      url: {{ .Permalink }}
     },
{{ end }}

    // <<<<<<<<<<<<<<<<<<<<<< FOR2

    // >>>>>>>>>>>>>>>>>>>>>> FOR3


    // <<<<<<<<<<<<<<<<<<<<<< FOR3

    // >>>>>>>>>>>>>>>>>>>>>> FOR4
HEREHEREHERE
    // <<<<<<<<<<<<<<<<<<<<<< FOR4
];



$(function () {
    var calendarEl = document.getElementById("fullcalendar");
    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ["dayGrid", "timeGrid", "list", "interaction"],
        // timeZone: "UTC-2",
        themeSystem: "standard",
        eventOrder: "start,title,-duration",
        header: {
            //left: 'prevYear,prev, today next,nextYear',
            left: "prev,next, today",
            center: "title",
            // right: 'dayGridMonth,timeGridWeek,listMonth'
            right: 'dayGridMonth,listMonth'
            // right: "dayGridMonth,listYear"
        },
        defaultDate: getMinMaxDate("2025-04-01"),
        defaultView: "dayGridMonth",
        firstDay: 1,
        // weekNumbers: true,
        eventLimit: false,
        displayEventEnd: true,
        //events: 'https://fullcalendar.io/demo-events.json',
        events: events,
         eventTimeFormat: {
            hour: '2-digit',
            minute: '2-digit',
            meridiem: false,
            hour12: false
          },
        droppable: true,
        eventResizableFromStart: true,
        eventResizableFromEnd: true,
        eventDurationEditable: true,
        eventRender: function (info) {

            if (info.view.type !== "listMonth") {
                info.el.querySelectorAll('.fc-title')[0].innerHTML = info.el.querySelectorAll('.fc-title')[0].innerText;

                let eventEl = info.el.querySelector(".fc-content");
                let eventID = info.event.extendedProps.issueKey;
                if (!eventID || !eventEl)
                    return;
                let link = document.createElement("a");
                link.innerHTML = eventID;
                // link.title = "Open in Jira";
                // link.href = "https://jira.dummyurl.com/browse/" + eventID;
                link.classList.add("float-right");
                eventEl.appendChild(link);
            }
        }
    });
    calendar.render();
});
//# sourceURL=pen.js
    </script>
<div id="fullcalendar"></div>
""".replace("workshop_color", workshop_color)






def empty_str_if_na(s: str) -> str:
    if not pd.isna(s):
        return s.strip()
    return ""


# def check_if_recrational(row):
#     recreational_activity = "lunch,coffe,tea,dinner,opening,registration"
#     title = empty_str_if_na(row['Title'])
#     for s in recreational_activity.split(","):
#         for ss in title.split(" "):
#             if s.lower() == ss.lower():
#                 print(f"{s} --> {title}")
#                 return title
#     return ""

def check_if_recrational(row)-> str:
    title = empty_str_if_na(row['Title'])
    speaker = empty_str_if_na(row['Speaker'])
    if not speaker:
        return title
    # recreational_activity = "lunch,coffe,tea,dinner,opening,registration"
    # title = empty_str_if_na(row['Title'])
    # for s in recreational_activity.split(","):
    #     for ss in title.split(" "):
    #         if s.lower() == ss.lower():
    #             print(f"{s} --> {title}")
    #             return title
    return ""




def build_calendar():
    valid_speakers = []
    df = get_data(url)
    use_col = df.columns[0]

    activity_col = df.columns[1]
    mask =  ~df[activity_col].isna() &df[activity_col].str.contains("week") #& (df['Use'] == "Yes")
    ddf = df.loc[mask]

    inject_txt = ""
    for _, _df in ddf.groupby("Speaker"):
        if any(_df[use_col] == "NO"):
            continue

        for _, row in _df.iterrows():
            if pd.isna(row['StartTime']):
                continue
            start_dt = row["StartTime"].to_pydatetime()
            end_dt = row["EndTime"].to_pydatetime()
            relative_url = f"/{row['Speaker'].strip().split(" ")[-1].lower().replace('-','_')}"
            inject_txt += rf"""
            {{ 
              title: '{row['Speaker'].strip().split(" ")[-1]}',
              start: strToDT("{format_time(str(row['StartTime']))}", 0),  
              end: strToDT("{format_time(str(row['EndTime']))}", 0),  
              allDay: false,
              description: 'Lecture',
              color: '{course_color}',
              url: '{relative_url}'
             }},
            """
            valid_speakers.append(relative_url[1:])

    fnames = get_fnames()

    for fname in fnames:
        if "course" not in get_tags(fname):
            continue
        # if 'gomez' in fname.lower():
        #     __import__("pdb").set_trace()

        linktitle = get_link_title(fname)
        if linktitle in [x.replace("-", "_") for x in valid_speakers]:
            continue

        if not get_begin(fname):
            continue

        cal_title = get_subtitle(fname)
        if not cal_title:
            cal_title = get_title(fname)
        inject_txt += rf"""
        {{ 
          title: '{cal_title.replace("given by", "by").replace("Prof.", "")}',
          start: strToDT("{str(get_begin(fname))} 2025", 0),  
          end: strToDT("{str(get_end(fname))} 2025", 0),  
          allDay: true,
          description: 'Lecture',
          color: '{course_color}',
          url: '/{linktitle}'
         }},
        """

    use_col = df.columns[0]
    activity_col = df.columns[1]

    for _, _df in df.groupby(activity_col):
        if any(_df[use_col].str.upper() == "NO"):
            continue
        for _, row in _df.iterrows():
            title = check_if_recrational(row)
            if title:
                if pd.isna(row['EndTime']):
                    end_time = row['StartTime'].to_pydatetime() + datetime.timedelta(hours=2)
                    end_time = pd.Timestamp(end_time)
                else:
                    end_time = row['EndTime']

                _title = title.lower()
                if 'contributed' in _title or 'special' in _title or 'discussion' in _title:
                    _color = workshop_color
                else:
                    _color = coffe_break_color
                inject_txt += rf"""
            {{ 
              title: '{title}',
              start: strToDT("{format_time(row['StartTime'])}", 0),  
              // end: strToDT("{format_time(end_time)}", 0),  
              allDay: false,
              description: '',
              color: '{_color}',
              url: ''
             }},
            """
    txt = template.replace("HEREHEREHERE", inject_txt)
    print(txt)
    with open("themes/mytheme/layouts/shortcodes/fullcalendar.html", 'w') as f:
        f.write(txt)



build_calendar()
