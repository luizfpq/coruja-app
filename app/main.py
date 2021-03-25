#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""main.py: Inicializa a aplicação."""

__author__ = "Luiz Quirino"
__copyright__ = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"

# importing the requests library
import requests
import platform,socket,re,uuid,json,psutil,logging
import hashlib
from datetime import datetime
from psutil import virtual_memory
from cpuinfo import get_cpu_info

def start() :
    dados="{} {} {}".format(get_cpu, get_mem, get_mac_address)
    HASH=hashlib.md5(dados.encode('utf-8'))
    DATE_TIME=get_time()
    IP=get_ip()
    result=submit(HASH.hexdigest(), DATE_TIME, IP)


def get_cpu() :
    info = get_cpu_info()
    return info.get('brand_raw')

def get_mem() :
    mem = virtual_memory()
    return mem.total  # total physical memory available

def get_mac_address() :
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

def get_time() :
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string	

def get_ip() :
    return requests.get('https://api.ipify.org').text

def submit(HASH,DATE_TIME, IP) :
    # defining the api-endpoint
    API_ENDPOINT = "https://ironqui-301.herokuapp.com/check"
    # your API key here
    #API_KEY = "XXXXXXXXXXXXXXXXX"
    # data to be sent to api
    data = {
            'hard_key': HASH,
            'IP': IP,
            'date_time': DATE_TIME
            }

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data)
    # extracting response text
    return_url = r.text
    return return_url
