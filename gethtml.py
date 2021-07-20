from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_candoiketoan(url_candoiketoan):
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

url_ketquakinhdoanh = "https://s.cafef.vn/bao-cao-tai-chinh/DHT/IncSta/2021/0/0/0/bao-cao-tai-chinh-cong-ty-co-phan-duoc-pham-ha-tay.chn"
url_candoiketoan = "https://s.cafef.vn/bao-cao-tai-chinh/DHT/BSheet/2021/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-duoc-pham-ha-tay.chn"
url_luuchuyengt = "https://s.cafef.vn/bao-cao-tai-chinh/DHT/CashFlow/2021/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-duoc-pham-ha-tay.chn"
url_luuchuyentt = "https://s.cafef.vn/bao-cao-tai-chinh/DHT/CashFlowDirect/2021/0/0/0/luu-chuyen-tien-te-gian-tiep-cong-ty-co-phan-duoc-pham-ha-tay.chn"

def get_rawData(url_ketquakinhdoanh, url_candoiketoan, url_luuchuyengt, url_luuchuyentt):

	html_kt = get_candoiketoan(url_candoiketoan)
	html_gt = get_luuchuyengt(url_luuchuyengt)
	html_kd = get_ketquakd(url_ketquakinhdoanh)
	html_tt  =get_luuchuyentt(url_luuchuyentt)
	Datas = [html_kt, html_kd, html_gt, html_tt]
	return Datas

Datas = get_rawData(url_ketquakinhdoanh, url_candoiketoan, url_luuchuyengt, url_luuchuyentt)
