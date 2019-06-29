import requests
from requests import exceptions
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from wxpy import *
import  schedule
import  time

bot=Bot(cache_path=True) #登陆网页微信，并保存登陆状态
 
def sendblogmsg(content):
    #搜索自己的好友，注意中文字符前需要+u
    #my_friend = bot.friends().search(u'Kristen Jaymes Stewart')[0]
    my_friend = bot.groups().search(u'日常互怼')[0]
    my_friend.send(content)
    my_friend.send_image('C:/Users/LC/Pictures/Continental.png')
    #my_group = bot.groups().search(u'卿尘')[0]
    #my_group.send(content) #发送天气预报
 
def job():
    '''
    resp=urlopen('http://www.weather.com.cn/weather1d/101181401.shtml')
    soup=BeautifulSoup(resp,'html.parser')
    tagToday=soup.find('p',class_="tem")  #第一个包含class="tem"的p标签即为存放今天天气数据的标签
    try:
        temperatureHigh=tagToday.span.string  #有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
    except AttributeError as e:
        temperatureHigh=tagToday.find_next('p',class_="tem").span.string  #获取第二天的最高温度代替
 
    temperatureLow=tagToday.i.string  #获取最低温度
    weather=soup.find('p',class_="wea").string #获取天气
    #contents = '起床啦，冰冰姐' + '\n'+ '周口' + '\n' +  '最高温度:' + temperatureHigh + '\n' + '最低温度:' + temperatureLow + '\n' +  '天气:' + weather 
'''
    #contents = '起床啦，冰冰小姐姐' 
    contents = '四哥，四嫂' 

    #result3 = '最低温度:' + temperatureLow
    #print('最低温度:' + temperatureLow)
    #print('最高温度:' + temperatureHigh)
    #print('天气:' + weather)
    sendblogmsg(contents)
#定时
schedule.every().day.at("06:31").do(job) #规定每天12：30执行job()函数
while True:
    job()
    schedule.run_pending()#确保schedule一直运行
    time.sleep(1)
bot.join() #保证上述代码持续运行