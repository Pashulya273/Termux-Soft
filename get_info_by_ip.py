import requests
from pyfiglet import Figlet
import folium
import sys

import requests
from bs4 import BeautifulSoup
import os

import os
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

 
from pystyle import Colorate, Colors
import banner
import webbrowser


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
os.system("pip install pystyle phonenumbers requests whois python-whois py-whois pywhois pythonwhois colorama")
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

import requests
from pyfiglet import Figlet
import folium

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
import time
import pystyle
import colorama
import time

import subprocess 
import pyfiglet

COLOR_CODE = {
        "GREEN": "\033[32m",
        "BOLD": "\033[01m",
        "RESET": "\033[0m",
    }


def get_info_by_ip(ip='127.0.0.1'):
	try:
     
		ip = input(Colorate.Horizontal(Colors.red_to_yellow, ('Введите целевой ip: ').strip()))
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		data = {
			'ip': response.get('query'),
			'провайдер': response.get('isp'),
			'организация': response.get('org'),
			'страна': response.get('country'),
			'имя региона': response.get('regionName'),
			'город': response.get('city'),
			'почтовый индекс': response.get('zip'),
			'широта': response.get('lat'),
			'долгота': response.get('lon'),
		}

		for k, v in data.items():
			print(Colorate.Horizontal(Colors.red_to_yellow, (f'{k} : {v}').strip()))

		area = folium.Map(location=[response.get('lat'), response.get('lon')])
		area.save(f'{response.get("query")}_{response.get("city")}.html')

	except requests.exceptions.ConnectionError:
		print(Colorate.Horizontal(Colors.red_to_yellow, ('[!] Проверьте подключение!').strip()))


def main():
	preview_text = Figlet(font='slant')
	print(preview_text.renderText(''))
	print(Colorate.Horizontal(Colors.red_to_yellow, ('\t\t').strip()))
	try:
		ip = input(Colorate.Horizontal(Colors.red_to_yellow, ('Введите целевой ip: ').strip()))
		get_info_by_ip(ip=ip)
	except KeyboardInterrupt:
		print(Colorate.Horizontal(Colors.red_to_yellow, ('\n[+] Отмена...').strip()))


if __name__ == '__main__':
	main()