import smtplib
from bs4 import BeautifulSoup
import urllib.request
import requests
import re

l=[] #initializing a blank list in which further items(file names) we will append
def mail():    
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()    
    server.login('ENter your Email here','enter your password here')    
    msg='new episode of flash updated, regards_PYTHON' #mesage to be deleivered by mail
    server.sendmail('your email','email of whome you want to send notification',msg) #both emails can be yours
    print('mail sent')    
    server.quit()
mainurl = urllib.request.urlopen('http://dl4.melimedia.net/mersad/serial/the%20flash/s04/') #url im using to check the file(can be changed for any other shows or file too)
content = mainurl.read()
soup = BeautifulSoup(content,'html.parser')
for a in soup.findAll('a',href=True):
    #if re.findall('index',a['href']):
    x=str(a['href'])
    l.append(x)
f=open('log.txt', 'r')
if x==str(f.read()):
    print('nothing new available')
    print('last update file is'+str(l[int(len(l)-1)]))
else:
    f=open('log.txt','w')
    f.write(str(l[len(l)-1]))
    f.close()
    print('updated')
    mail()
