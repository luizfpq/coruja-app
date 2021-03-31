#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""setup.py: Instala dependencias."""

import configparser
import os
import requests
import hashlib

from app.getters import get_name, get_cpu, get_mem, get_disk, get_mac_address, get_time, get_ip, get_os

__author__ = "Luiz Quirino"
__copyright__ = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.4"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"

#TODO: otimizar essas preferencias em um arquivo mais acessível
def install():
    depends = [
        'psutil',
        'py-cpuinfo',
        'requests'
    ]

    cmd = "which pip"
    verify_pip = os.system(cmd)
    if verify_pip != 0:
        if 'ubuntu' in get_os() :
            packmanager = "sudo apt install -y "
            packages = "python3 python3-pip"
        elif 'arch' in get_os() :
            packmanager = "sudo pacman -Syyu "
            packages = "python3 python3-pip"
        cmd = "sudo {} {}".format(packmanager, packages)
        result = os.system(cmd)
        if not result:
            print("Instalados com sucesso")

    for item in depends:
        cmd = "sudo pip install {}".format(item)
        os.system(cmd)


#TODO: status de cadastro vindo do server
def register(file_path):
    
    config = configparser.ConfigParser()
    config.read(file_path)

    # config_status = 1 habilita a escrita do arquivo
    config_status = 0

    if not config.get('DEFAULT','HARD_HASH'):
        dados="{}{}{}{}{}".format(get_name, get_cpu, get_mem, get_disk()[0].get('total'), get_mac_address)
        config['DEFAULT']['HARD_HASH'] = str(hashlib.md5(dados.encode('utf-8')).hexdigest())
        print(config.get('DEFAULT','HARD_HASH'))
        config_status = 1

    if not config.get('DEFAULT','name'):
        config['DEFAULT']['name'] = str(get_name())
        print(config.get('DEFAULT','name'))
        config_status = 1
    
    if not config.get('DEFAULT','cpu'):
        config['DEFAULT']['cpu'] = str(get_cpu())
        print(config.get('DEFAULT','cpu'))
        config_status = 1

    if not config.get('DEFAULT','mem'):
        config['DEFAULT']['mem'] = str(get_mem())
        print(config.get('DEFAULT','mem'))
        config_status = 1
    
    if not config.get('DEFAULT','disk'):
        config['DEFAULT']['disk'] = str(get_disk()[0].get('total'))
        print(config.get('DEFAULT','disk'))
        config_status = 1
    
    if not config.get('DEFAULT','mac'):
        config['DEFAULT']['mac'] = str(get_mac_address())
        print(config.get('DEFAULT','mac'))
        config_status = 1

    if config_status == 1:
        with open(file_path, 'w') as configfile:    # save
            config.write(configfile)

    data = {
            'hard_hash': config.get('DEFAULT','hard_hash'),
            'name': config.get('DEFAULT','name'),
            'cpu': config.get('DEFAULT','cpu'),
            'mem': config.get('DEFAULT','mem'),
            'disk': config.get('DEFAULT','disk'),
            'mac': config.get('DEFAULT','mac')
            }
    

    result=requests.post('https://ironqui-301.herokuapp.com/api/machineAdd',  data=data)

    if not result:
        #TODO: implementar salvamento em arquivo local
        print("deu ruim")
    else:
        print(result.text)