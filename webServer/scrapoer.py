from urllib import response
# from bs4 import BeautifulSoup
import requests


def getMagis():
  url = "https://magisrent.nl/assets/php/getapartments.php"
  parms={
      "action":"fetch_data",
      "min_price":"400",
      "max_price":"1300",
      "min_size":"0",
      "max_size":"130",
      "city[]":"eindhoven"
  }
  response = requests.post(url = url,data=parms)
  page_data = response.text
  #print(page_data)
  res="Displaying 0 available offer(s)" not in page_data
  # print(res)

  with open("housing.html","w",encoding="utf-8") as f:
    f.write(page_data)
    f.close()
  return res


def getH2s():
    url="https://holland2stay.com/residences.html?available_to_book=179&city=29&price=450-950"
    response = requests.get(url)
    page_data2 = response.text
    #print(page_data2)
    res='At the moment there are no available residences matching your selected criteria.'not in page_data2
    # print("Another",res)
    with open("housing2.html","w",encoding="utf-8") as f:
        f.write(page_data2)
        f.close()
    return res
    
getH2s()

# dxanxpgsgwieiegj

#发送多种类型的邮件
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
msg_from = ' ' # 发送方邮箱
passwd = ' ' #就是上面的授权码
 
to= ['augustinolss@gmail.com'] #接受方邮箱
#设置邮件内容
#MIMEMultipart类可以放任何内容
msg = MIMEMultipart()
if(getH2s() == True):
  conntent="登录h2s网站查看消息。网址：https://holland2stay.com/residences.html?available_to_book=179&city=29&price=450-950"
  #把内容加进去
  msg.attach(MIMEText(conntent,'plain','utf-8'))
  
  #设置邮件主题
  msg['Subject']="Holland2Stay Housing message, please check the website"
  
  #发送方信息
  msg['From']=msg_from
  
  #开始发送
  
  #通过SSL方式发送，服务器地址和端口
  s = smtplib.SMTP_SSL("smtp.qq.com", 465)
  # 登录邮箱
  s.login(msg_from, passwd)
  #开始发送
  s.sendmail(msg_from,to,msg.as_string())
  print("邮件发送成功")

if(getMagis() == True):
  conntent="登录Magis网站查看消息"
  #把内容加进去
  msg.attach(MIMEText(conntent,'plain','utf-8'))
  
  #设置邮件主题
  msg['Subject']="Magis Housing message, please check the website."
  
  #发送方信息
  msg['From']=msg_from
  
  #开始发送
  
  #通过SSL方式发送，服务器地址和端口
  s = smtplib.SMTP_SSL("smtp.qq.com", 465)
  # 登录邮箱
  s.login(msg_from, passwd)
  #开始发送
  s.sendmail(msg_from,to,msg.as_string())
  print("邮件发送成功")