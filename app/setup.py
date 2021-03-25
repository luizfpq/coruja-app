#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""setup.py: Instala dependencias."""

import os
import requests
__author__ = "Luiz Quirino"
__copyright__ = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.2"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"


def install():
    depends = [
        'psutil',
        'py-cpuinfo',
        'requests'
    ]


    for item in depends:
        cmd = "pip install {}".format(item)
        os.system(cmd)
