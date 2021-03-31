#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run.py: Inicializa a aplicação, verifica se está atualizada e se necessário se auto atualiza."""

__author__      = "Luiz Quirino"
__copyright__   = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "0.0.4"
__maintainer__ = "Luiz Quirino"
__email__ = "luizfpq@gmail.com"
__status__ = "Testing"


import requests
import os,sys
path=(os.path.dirname(__file__))
from app.setup import install, register

if ('install' in sys.argv[1:]) :
    install()
elif ('register' in sys.argv[1:]) :
    install()
    register('{}/app/env/REGISTER'.format(path))
elif ('login' in sys.argv[1:]):
    action = 'login'
elif ('logout' in sys.argv[1:]) :
    action = 'logout'
elif ('shutdown' in sys.argv[1:]) :
    action = 'shutdown'
else:
    action = 'log'

from app.update import update
update(path)

from app.main import start

start('{}/app/env/REGISTER'.format(path), action)
