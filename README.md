# mango2
#requests爬取中文网站乱码的问题
import requests
response = requests.get(url)
print(response.text.encode('ISO-8859-1').decode('gbk'))
