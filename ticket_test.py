#coding=UTF-8
from splinter import Browser
import time
import datetime

data1 = raw_input('Write your Data(yyyy-mm-dd):')
data = time.strptime(data1,"%Y-%m-%d")
datimeStarp = int(time.mktime(data))

days = raw_input('Write your Days:')
number = raw_input('Write your number:')
url = 'https://kyfw.12306.cn/otn/leftTicket/init'
days=int(days)
time.sleep(5)

b = Browser()

for i in range(days):
    b.visit(url)
    time.sleep(10)
    date1 = datetime.datetime.utcfromtimestamp(datimeStarp)
    dates = (date1+datetime.timedelta(days=i+1))
    datas = dates.strftime("%Y-%m-%d") 
    b.cookies.add({"_jc_save_fromDate":"%s" % (datas)})
    b.cookies.add({"_jc_save_fromStation":"%u5317%u4EAC%u897F%2CBXP"})
    b.cookies.add({"_jc_save_toStation":"%u8D35%u9633%u5317%2CKQW"})
    time.sleep(10)
    b.reload()
    b.find_by_id('query_ticket').click()
    time.sleep(10)
    b.find_by_text('预订').first.click()
    time.sleep(40)
    b.cookies.delete()
