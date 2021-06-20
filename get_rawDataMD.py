from urllib.request import urlopen
from bs4 import BeautifulSoup
from gethtml import get_candoiketoan, get_ketquakd, get_luuchuyengt, get_luuchuyentt
url_ketquakinhdoanh = "https://s.cafef.vn/bao-cao-tai-chinh/DBT/IncSta/2021/0/0/0/bao-cao-tai-chinh-cong-ty-co-phan-duoc-pham-ben-tre.chn"
url_candoiketoan = "https://s.cafef.vn/bao-cao-tai-chinh/DBT/BSheet/2021/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-duoc-pham-ben-tre.chn"
url_luuchuyengt = "https://s.cafef.vn/bao-cao-tai-chinh/DBT/CashFlow/2021/0/0/0/luu-chuyen-tien-te-gian-tiep-cong-ty-co-phan-duoc-pham-ben-tre.chn"
url_luuchuyentt = "https://s.cafef.vn/bao-cao-tai-chinh/DBT/CashFlowDirect/2021/0/0/0/luu-chuyen-tien-te-gian-tiep-cong-ty-co-phan-duoc-pham-ben-tre.chn"

def get_rawData(url_ketquakinhdoanh, url_candoiketoan, url_luuchuyengt, url_luuchuyentt):
	html_kt = get_candoiketoan(url_candoiketoan)
	html_gt = get_luuchuyengt(url_luuchuyengt)
	html_kd = get_ketquakd(url_ketquakinhdoanh)
	html_tt  =get_luuchuyentt(url_luuchuyentt)
	Datas = [html_kt, html_kd, html_gt, html_tt]
	return Datas
Datas = get_rawData(url_ketquakinhdoanh, url_candoiketoan, url_luuchuyengt, url_luuchuyentt)
