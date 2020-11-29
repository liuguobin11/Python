from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pandas.core.frame import DataFrame
import time

"""
根据table的id属性和table中的某一个元素定位其在table中的位置
table包括表头，位置坐标都是从1开始算
tableXPATH：table的XPATH属性
"""
def get_table_content(tableXPATH):
    # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
    table_tr_list = driver.find_element(By.XPATH, tableXPATH).find_elements(
        By.TAG_NAME, "tr")
    table_list = []  #存放table数据
    for tr in table_tr_list:  #遍历每一个tr
        #将每一个tr的数据根据td查询出来，返回结果为list对象
        table_td_list = tr.find_elements(By.TAG_NAME, "td")
        row_list = []
        print(table_td_list)
        for td in table_td_list:  #遍历每一个td
            row_list.append(td.text)  #取出表格的数据，并放入行列表里
        if len(row_list)!=0:
            table_list.append(row_list)
    return table_list

lineName='L60-0 MSM'
driver = webdriver.Chrome()
# 设置等待时间
#wait = ui.WebDriverWait(driver, 5)
driver.get("http://djmesasv1.cw01.contiwan.com:8861/iGate/pulse")
print(driver.title)

#wait = ui.WebDriverWait(driver,10)
#wait.until(lambda driver: driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[1]/td/table/tbody/tr[1]/td[4]/table/tbody/tr/td[1]/a'))
#通过contains函数，提取匹配特定文本的所有元素
iframe = driver.find_element_by_xpath("/html/body/div[1]/div[2]/iframe")
#进入iframe页面
driver.switch_to.frame(iframe)
#获取select标签
driver.find_element_by_xpath('//*[@id="mi_14"]').click()#Reporting
driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td').click()#OEE Analysis
driver.find_element_by_xpath('/html/body/table[3]/tbody/tr[1]/td/a').click()#OEE Analysis  

#进入下半部分frame
driver.switch_to.frame(
    driver.find_element_by_xpath(
        "/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[2]/iframe"))
#进入侧边选择frame
driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frame[1]"))

driver.find_element_by_xpath('//*[@id="line_reporting"]').click()#点击Line reporting
driver.find_element_by_xpath('//*[@id="aec_4"]/img').click()#点击CEP Line Performance Backend - non standard
driver.find_element_by_xpath('//*[@id="aec_5"]/img').click()#点击CCN
driver.find_element_by_xpath('//*[contains(text(),"{}")]'.format(lineName)).click()#点击lineName
#driver.find_element_by_xpath('//*[@id="as_8"]').click()#点击L60-0 MSM

driver.switch_to.parent_frame()  #返回上一级
driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frame[2]"))#进入右侧frame
driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frame[1]"))#进入右侧顶端筛选frame
Select(driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/select')).select_by_value('detail')#选择detail
time.sleep(2)#选择后会刷新界面，等待几秒钟
driver.switch_to.parent_frame()  #返回上一级
driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frame[1]"))#重新进入右侧顶端筛选frame
Select(driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[6]/select')).select_by_value('1')#on last选择1 day
driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[12]/button').click()#点击show

driver.switch_to.parent_frame()  #返回上一级
driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frame[2]"))#进入右侧下面内容frame

OEEAnalysis = get_table_content("/html/body/table/tbody/tr[1]/td[1]/table")#获取OEEAnalysis表格内容
OEETimeAnalysis = get_table_content("/html/body/table/tbody/tr[2]/td[1]/table")#获取OEETimeAnalysis表格内容

time.sleep(3)
driver.close()

