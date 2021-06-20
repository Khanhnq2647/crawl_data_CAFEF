from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_candoiketoan(url_candoiketoan):
	#url = "https://s.cafef.vn/bao-cao-tai-chinh/DBT/BSheet/2021/0/0/0/bao-cao-tai-chinh-cong-ty-co-phan-duoc-pham-ben-tre.chn"
	html = urlopen(url_candoiketoan).read()
	soup_packtpage = BeautifulSoup(html, "html.parser")
	res = soup_packtpage.find('table', attrs = {"id":"tableContent"})
	return res
def get_ketquakd(url_ketquakinhdoanh):
	html = urlopen(url_ketquakinhdoanh).read()
	soup_packtpage = BeautifulSoup(html, "html.parser")
	res = soup_packtpage.find('table', attrs = {"id":"tableContent"})
	return res
def get_luuchuyengt(url_luuchuyengt):
	html = urlopen(url_luuchuyengt).read()
	soup_packtpage = BeautifulSoup(html, "html.parser")
	res = soup_packtpage.find('table', attrs = {"id":"tableContent"})
	return res
def get_luuchuyentt(url_luuchuyentt):
	html = urlopen(url_luuchuyentt).read()
	soup_packtpage = BeautifulSoup(html, "html.parser")
	res = soup_packtpage.find('table', attrs = {"id":"tableContent"})
	return res
'''def main():
	url_ketquakinhdoanh = "https://s.cafef.vn/bao-cao-tai-chinh/DBT/IncSta/2021/0/0/0/bao-cao-tai-chinh-cong-ty-co-phan-duoc-pham-ben-tre.chn"
	url_candoiketoan = "https://s.cafef.vn/bao-cao-tai-chinh/DBT/BSheet/2021/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-duoc-pham-ben-tre.chn"
'''