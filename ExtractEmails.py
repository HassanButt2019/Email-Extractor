import urllib.request , urllib , urllib.parse
import re
import requests
from bs4 import BeautifulSoup
import csv

url = "Enter Any Url"
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html , 'html.parser')


tags = soup('div')

Emails = { }
email = ""
count = 0
checkemail = " "
check = False
with open('Emails.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    for line in tags:
        email = str(line)
        Emails = re.findall('[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+',email)
        for mail in Emails:
                if checkemail != mail:
                    check = True
                    writer.writerow([count , mail])
                    print(mail)
                    checkemail = mail
                    count = count + 1

if check == False:
    print("Not Found")
file.close()

