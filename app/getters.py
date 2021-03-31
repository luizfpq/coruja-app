#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""getters.py: Provê os dados de sistema."""

__author__ = "Luiz Quirino"
__copyright__ = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.4"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"

import cpuinfo
import datetime
import fcntl
import logging
import os
import platform
import psutil
import re
import requests
import socket
import sys
import struct
import uuid

''' HARDWARE ITENS '''
def get_cpu():
    info = cpuinfo.get_cpu_info()
    return info.get('brand_raw')

def get_mem():
    mem = psutil.virtual_memory()
    return mem.total  # total physical memory available

def get_disk():
    disk_info = []
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        disk_info.append({
            'device':  part.device,
            'total':  usage.total,
            'used': usage.used,
            'free': usage.free,
            'percent': usage.percent,
            'fstype': part.fstype,
            'mountpoint': part.mountpoint
        })
    return disk_info


''' NETWORK ITEMS '''
def get_ip():
    return requests.get('https://api.ipify.org').text

def get_mac_address():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))



''' SOFTWARE ITEMS '''

def get_name():
    return os.uname()[1]

def get_os():
    version = os.uname()[2]
    if 'ubuntu' in version:
        return 'UBUNTU'
    if 'arch' in version:
        return 'ARCH'
    
def get_time():
    # datetime object containing current date and time
    now = datetime.datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string	
