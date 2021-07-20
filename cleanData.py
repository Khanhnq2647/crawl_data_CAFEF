from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from get_rawDataMD import get_rawData, Datas
Datas = Datas
def save_txt(Datas):
	for Data in range(len(Datas)):
		data = []
		for i in Datas[Data].find_all("tr"):
		    ti = i.text.replace("\r",'')
		    ti = ti.replace("\xa0","")
		    data.append(ti)
		file = open("text.txt","a", encoding = 'utf8')

		for r in data:
		    strpip = r.strip()
		    strpip = strpip.replace("\r","")
		    strpip  = strpip.replace(",",".")
		    strpip = strpip.replace("\n",",")
		    s = strpip.strip('\t\n\r')
		    s = s + "\n"
		    file.write(s)
save_txt(Datas)

with open("clean_data.csv", encoding="utf8", mode="w", newline='') as file_csv:
	header = ["Title","empty",2017,2018,2019,2020]
	writer = csv.writer(file_csv)
	writer.writerow(header)
file = open("text.txt","r", encoding ='utf8')
data = file.read()
data = data.split("\n")
for i in range(len(data)):
	data[i] = data[i].strip()
	#data[i] = data[i].replace("\n","")
unemty = []
for row in range(len(data)):
	if data[row] != '':
		unemty.append(data[row])
data = unemty
file  =open("clean_data.csv","a", encoding = "utf8")
for i in range(len(data)):
	file.write(data[i]+ "\n")
