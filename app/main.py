#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Foobar.py: Description of what foobar does."""

__author__      = "Luiz Quirino"
__copyright__   = "Copyleft 2021, Solar System"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Rob Knight"
__email__ = "rob@spot.colorado.edu"
__status__ = "Production"
import requests
from lxml import etree

response = requests.get("https://github.com/luizfpq/coruja/app/releases")
html = etree.HTML(response.text)
Version = html.xpath("/html/body/div[4]/div/main/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/a")
print(Version)