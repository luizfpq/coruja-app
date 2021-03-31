#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""main.py: Inicializa a aplicação."""

__author__ = "Luiz Quirino"
__copyright__ = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.5"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"

# importing the requests library
from app.getters import get_name, get_cpu, get_mem, get_disk, get_mac_address, get_time, get_ip

import configparser
import os
import requests
import hashlib
import json




def start(file_path, action) :
    
    config = configparser.ConfigParser()
    config.read(file_path)

    dados="{}{}{}{}{}".format(get_name(), get_cpu(), get_mem(), get_disk()[0].get('total'), get_mac_address())
    hash=str(hashlib.md5(dados.encode('utf-8')).hexdigest())
    
    ip=get_ip()

    if config.get('DEFAULT','HARD_HASH') == hash:
        status = "0"
    else:
        status = "1"

    data={
                "hard_hash":'{}'.format(hash),
                "ip":'{}'.format(ip),
                "status":'{}'.format(status),
                "action":'{}'.format(action)
    }

    headers = {'user-agent': 'coruja/{}'.format(__version__)}
    result=requests.post(url='https://ironqui-301.herokuapp.com/api/logAdd',  data=data, headers=headers)

    if not result:
        #TODO: implementar salvamento em arquivo local
        print(data)
        print(result)
    else:
        print(result.text)