from bs4 import BeautifulSoup
from selenium import webdriver
import time
import smtplib

URL = "https://www.amazon.com.br/Applied-Logistic-Regression-Probability-Statistics-ebook/dp/B00BNFI7QK?pf_rd_r=B95NTPV6BWME1BWFC3WT&pf_rd_p=8d9d1fc6-464b-46bd-b25d-3c2fb5260667&pd_rd_r=167e6198-5c42-4af7-bcdc-fa86861c6cc4&pd_rd_w=b3fss&pd_rd_wg=iUnzi&ref_=pd_gw_ci_mcx_mr_hp_d"

def checkPrice():
    priceLimit = 700   #price i want the product to reach
    
    driver=webdriver.Chrome('C:\chrome driver\chromedriver.exe')
    #driver.maximize_window()
    driver.get(URL)
    
    #time.sleep(1) #time to visulize page
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    
    #soup = BeautifulSoup(page.content,"lxml")
    #print(soup.prettify()) #print all page html
    title=soup.find(id="productTitle").get_text()
    print(title)
    price = soup.find(class_="a-size-medium a-color-price").get_text()
    
    #####Convert price to float
    #(price)
    floatPricept1=float(price[3:7]) #numbers before "," 
    #print(floatPricept1)
    floatPricept2=float(price[8:10]) #numbers after "," 
    #print(floatPricept2)
    floatPrice=floatPricept1+(0.01)*floatPricept2 #sum integer part with decimal*0.01 part
    print(floatPrice)
    
    if floatPrice<priceLimit:
        sendMail(title)
    
    
    
    driver.quit()

def sendMail(title):
    server= smtplib.SMTP('smtp.gmail.com:587')    #connection to email protocol
    server.ehlo()
    server.starttls() #encrypt connection
    server.ehlo()
    server.login('giovanisilva24@gmail.com','kvehytdenagkuejz')
    
    
    subject = f"Price reached for {title}!"
    body = f"Check the amazon link, the price for {title} is reached! :) \n {URL}"
    msg=f"Subject: {subject} \n\n {body}"
    server.sendmail("giovanisilva24@gmail.com","geeowdk@gmail.com",msg)
    print("okkkk")
    server.quit()
    
while(True):
    checkPrice() 
    time.sleep(604800)   #will check every week if the price is reached        
    
    