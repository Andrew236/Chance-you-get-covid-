from tkinter import *

import tkinter as tk

from PIL import ImageTk, Image

import requests

from tkinter import font


statepop_dict = {
    'al': 4903185, 'ak': 731545, 'as': 49437, 'az': 7278717, 'ar': 3017804,
    'ca': 39512223, 'co': 5758736, 'ct': 3565287, 'de': 973764, 'dc': 705749,
    'fl': 21477737, 'ga': 10617423, 'gu': 168485, 'hi': 1415872, 'id': 1787065,
    'il': 12671821, 'in': 6732219, 'ia': 3155070, 'ks': 2913314, 'ky': 4467673,
    'la': 4648794, 'me': 1344212, 'md': 6045680, 'ma': 6892503, 'mi': 9986857,
    'mn': 5639632, 'ms': 2976149, 'mo': 6137428, 'mt': 1068778, 'ne': 1934408,
    'nv': 3080156, 'nh': 1359711, 'nj': 8882190, 'nm': 2096829, 'ny': 19453561,
    'nc': 10488084, 'nd': 762062, 'oh': 11689100, 'ok': 3956971, 'or': 4217737,
    'pa': 12801989, 'pr': 3193694, 'ri': 1059361, 'sc': 5148714, 'sd': 884659,
    'tn': 6892174, 'tx': 28995881, 'ut': 3205958, 'vt': 623989, 'va': 8535519,
    'vi': 106235, 'wa': 7614893, 'wv': 1792147, 'wi': 5822434, 'wy': 578759
    }

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


def get_covid_per_state(entry1):
    if len(entry1) > 2:
        entry1 = us_state_abbrev[entry1.capitalize()].lower()
        entry1.lower()
        print(entry1)
    url = 'https://api.covidtracking.com/v1/states/'\
          '{}/current.json'.format(entry1)

    if entry1 not in statepop_dict or entry1 not in us_state_abbrev:
        data_label['text'] = "Please enter a valid abbreviated state ex: or"
    response = requests.get(url)
    covid_cases_state = response.json()['positive']

    population = statepop_dict[entry1]
    Stats = (covid_cases_state / population)
    FinalStats = round((100 * Stats), 3)
    data_label['text'] = "Your chances of getting Covid in"\
        "{} is: {} percent ".format(entry1.upper(), FinalStats)


HEIGHT = 700
WIDTH = 900
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("covid.jpg"))
main_label = tk.Label(root, image=img)
main_label.place(relwidth=1, relheight=1)


button = tk.Button(
    root,
    text=("Get statistics"),
    bg='#7094db',
    command=lambda: get_covid_per_state(entry_one.get())
)

button.place(
    relx=0.37,
    rely=0.35,
    height=50,
    width=200
)


label = tk.Label(
    root,
    text=("Enter a state to see what"
          "your chances of getting covid-19 are"),
    fg="white",
    bg="#800000",
    font=("Helvetica", 12)
)

label.place(
    relx=0.2,
    rely=0.1,
    width=500,
    height=50
)

label_two = tk.Label(
    root,
    text="Enter a state below!",
    bg="white",
    fg="black"
)

label_two.place(
    relx=0.35,
    rely=0.2,
    width=225
)

entry_one = tk.Entry(root)

entry_one.place(
    relx=0.4,
    rely=0.25
)
data_label = tk.Label(
    root,
    bg="white")

data_label.place(
    relx=0.15,
    rely=0.65,
    width=600,
    height=200
)

root.mainloop()

