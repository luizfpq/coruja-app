#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run.py: Inicializa a aplicação, verifica se está atualizada e se necessário se auto atualiza."""

__author__      = "Luiz Quirino"
__copyright__   = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.2"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"

import requests
import os,sys
from app.update import update
from app.main import *
from app.setup import install

path=(os.path.dirname(__file__))

if ('install' in sys.argv[1:]) :
    install()

update(path)
start()