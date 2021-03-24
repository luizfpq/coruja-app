#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""update.py: Verifica a release e atualiza caso necessário."""

import os
import requests
__author__ = "Luiz Quirino"
__copyright__ = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"


def update():
    release = requests.get("https://raw.githubusercontent.com/luizfpq/coruja/main/app/releases")
    if(release.text > __version__):
        cmd = "git pull origin main"
        returned_value = os.system(cmd)  # returns the exit code in unix
        if(returned_value == 0):
            print("Sistema Atualizado com sucesso")
        else:
            print("Sistema possui atualizações pendentes")