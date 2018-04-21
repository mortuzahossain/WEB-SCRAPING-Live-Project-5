# _*_ coding: utf-8 _*_

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS('phantomjs.exe')

def DownloadPageHtml(url):
	print 'Downloading : ' + url
	driver.get(url)
	html = driver.page_source
	return html


url = "https://play.google.com/store/apps/collection/recommended_for_you_POPULAR_APPS_GAMES?clp=ogoGCAQqAggB:S:ANO1ljIlc5c"

html = DownloadPageHtml(url)
soup = BeautifulSoup(html,'lxml')

main_content = soup.find('div',class_ = 'main-content')
all_app = main_content.find_all('div',class_ = 'card no-rationale square-cover apps small')

f = open('playstore.sql','w')

for app in all_app:
	image = 'http:' + app.find('img')['src'].encode('utf-8').replace("'","")
	app_details_url = app.find('div',class_ = 'details').find_all('a')[0]['href'].encode('utf-8').replace("'","")
	name = app.find('div',class_ = 'details').find_all('a')[1].text.encode('utf-8').replace("'","")
	developer_name = app.find('div',class_ = 'details').find_all('a')[2].text.encode('utf-8').replace("'","")
	developer_url = app.find('div',class_ = 'details').find_all('a')[2]['href'].encode('utf-8').replace("'","")

	writer = "INSERT INTO playstore (name,url,image,developer,developerurl) VALUES ('{}','{}','{}','{}','{}');\n".format(name,app_details_url,image,developer_name,developer_url)

	f.write(writer)

print 'Finish'

f.close()
driver.close()



