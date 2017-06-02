#!/usr/local/bin/python

import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from bs4 import BeautifulSoup as bs
from lxml import html
import requests
from urllib2 import urlopen
import numpy as np

url = "http://www.basketball-reference.com/leaders/pts_per_g_season.html"
soup = bs(urlopen(url),"html.parser")
players = soup.find("table",attrs={"id":"stats_NBA"})
headings = [th.get_text() for th in players.find("tr").find_all("th")]
pdata = []
pdata.append(headings)
for row in players.find_all("tr")[1:]:
    pdata_row = (td for td in row.find_all("td"))
    pdata.append(pdata_row)
index = np.arange(len(pdata)-1)
playerdf_raw = pd.DataFrame(data=pdata[1:][0:],index=index,columns=pdata[0][0:])
playerdf_raw.head()
print playerdf_raw['PPG'][0]

pdata_better = []
pdata_better.append(["Name","Page","PPG"])
base = "www.basketball-reference.com"
for i in index:
    pname = playerdf_raw['Player'][i].get_text()
    pname = pname.replace('*', '')
    ppage = base+str(playerdf_raw['Player'][i]).split("\"")[1]
    ppgnum = str(playerdf_raw['PPG'][i])
    ppgnum = ppgnum.replace('<td', '')
    ppgnum = ppgnum.replace('align="right">', '')
    ppgnum = ppgnum.replace('</td>', '')
    ppgnum = ppgnum.replace(' ', '')
    row = (pname,ppage,ppgnum)
    pdata_better.append(row)
index = np.arange(len(pdata_better)-1)
playerdf = pd.DataFrame(data=pdata_better[1:][0:],index=index,columns=pdata_better[0][0:])
playerdf.head()
print playerdf['Name'][15]
