#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""main.py: Inicializa a aplicação."""

__author__ = "Luiz Quirino"
__copyright__ = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.3"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"

# importing the requests library
from app.getters import get_name, get_cpu, get_mem, get_disk, get_mac_address, get_time, get_ip

import configparser
import hashlib
import requests




def start(file_path) :
    
    config = configparser.ConfigParser()
    config.read(file_path)


    dados="{}{}{}{}{}".format(get_name, get_cpu, get_mem, get_disk()[0].get('total'), get_mac_address)
    HASH=hashlib.md5(dados.encode('utf-8')).hexdigest()
    
    IP=get_ip()

    if config.get('DEFAULT','HARD_HASH') == HASH:
        HASH_STATUS = "0"
    else:
        HASH_STATUS = "1"

    data = {
            'hard_hash': HASH,
            'ip': IP,
            'hard_hash_status': HASH_STATUS
            }
    

    result=requests.post('https://ironqui-301.herokuapp.com/api/logAdd',  data=data)

    if not result:
        #TODO: implementar salvamento em arquivo local
        print(data)
        print(result)
    else:
        print(result.text)