# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 07:40:51 2021

@author: jon.atli
"""

import subprocess as cmd
import time
from datetime import datetime

while True:
    time.sleep(300)
    print('Last start of process',datetime.now())
    try:
        cp = cmd.run("git add .", check=True, shell = True)
        cmd.run("git commit -m AutoUpdate", check=True, shell = True)
        cmd.run("git push -u origin main", check=True, shell = True)
        cmd.run("cd ..", check=True, shell = True)
    except:
        continue
    
