import requests
from bs4 import BeautifulSoup
from pystyle import Colorate, Colors
import banner


from colorama import init, Fore, Style
import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored
import platform
import os

import socket
import pystyle
import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
import requests
import whois
import random
import colorama
import threading
import string
import faker
import bs4
import urllib.parse
import colorama
import concurrent.futures
import csv

import urllib.request
import json
import os
import time
import pystyle
import colorama
import time, sys


COLOR_CODE = {
        "GREEN": "\033[32m",
        "BOLD": "\033[01m",
        "RESET": "\033[0m",
    }

if os.path.isfile('last.txt'):
    os.remove('last.txt')

phone = input(Colorate.Horizontal(Colors.red_to_yellow, ("[+] Введите номер").strip()))
service = "http://phoneradar.ru/phone/"
link = service + phone

         
def get_html(link, params=None):
    r = requests.get(link, params=params)
    return r 
def parse():
    html = get_html(link)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('''Ошибка!
Вы ввели некорректный номер телефона!
Убедитесь, что введённый Вами номер, не содержит лишних символов.''')
        stop()
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('tbody')
    file = open("trash.tr", "w")
    file.write(result.text)
    file.close()
    with open("trash.tr") as a:
        with open("last.txt", 'a') as out:
            for line in filter(lambda x: x != '\n', a):
                out.write(line)
    os.remove('trash.tr')
    print("Номер:", phone)
    print("\n"+"Результат:"+"\n")
    file1 = open("last.txt", "r")
    while True:
        line = file1.readline()
        if not line:
            break
        print(Colorate.Horizontal(Colors.red_to_yellow, line.strip()))
    file1.close
    print(Colorate.Horizontal(Colors.red_to_yellow, ('''
Последний результат сохраняется в файле: last.txt
Он исчезнет при следующем запуске софта.''').strip()))
print(Colorate.Horizontal(Colors.red_to_yellow, ("Проверьте эти ссылки:").strip()))
print(Colorate.Horizontal(Colors.red_to_yellow, ("https://t.me/"+ phone).strip()))
print(Colorate.Horizontal(Colors.red_to_yellow, ("https://wa.me/"+ phone).strip()))
print(Colorate.Horizontal(Colors.red_to_yellow, ("https://viber.click/"+ phone).strip()))
parse()
    




 
 


