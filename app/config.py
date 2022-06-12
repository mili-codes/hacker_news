#http requests
import requests
#web scrapping
from bs4 import BeautifulSoup 
# send the mail
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#system date and time manipulation
import datetime

now = datetime.datetime.now()

content = '' #email content placeholder

underline = '-'*15
print(f'{underline}\nHaha \n {underline}')

