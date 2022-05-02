import googlemaps
import pandas as pd
from datetime import datetime


def unitcov(st):
    kilo = 0
    temp = st[-2]
    if (temp == 'k'):
        kilo = 1
    temp = st.split(" ")[0]
    temp = temp.split(",")
    s = ""
    for t in temp:
        s = s + t
    temp = float(s)
    if kilo:
        return temp*1000
    else:
        return temp
        

df = pd.read_excel("./output.xlsx")

raw = df

raw['distance'] = 0

gmaps = googlemaps.Client(key='AIzaSyCrQIO8NlrMYuNgLoIm_XhjIOtXX1jKMUM')

now = datetime(2022, 2, 18,12,0)

l = len(raw)


for i in range(l):
    print(i)

    dest = raw['col 1'][i]
    try:
        directions_result = gmaps.directions("799 Islington Ave, Etobicoke, ON M8Z 5W8",dest,mode="driving",departure_time=now,region='ca')
        raw['distance'][i] = directions_result[0]['legs'][0]['distance']['value']
    except:
        print(directions_result)

raw.to_excel("output2.xlsx")
