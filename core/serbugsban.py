#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/theInfectedDrake/TIDoS-Framework  

import time
from colors import *
import os

def serbugsban():

    time.sleep(0.5)
    os.system('clear')
    
    print C+'''

\033[1;34m
  +------------------------------------------------------+
  |     \033[1;37mTIDoS Dialog                       \033[1;33m[-] [口] [×]  \033[1;34m|
  | ---------------------------------------------------- |
\033[1;36m  |                                                      |
  |  \033[1;33mTIDoS has detected that you want to hunt for bugs! \033[1;36m |
  |   \033[1;33mDo you wish to continue?                          \033[1;36m |
  |                                                      |
  |     \033[1;37m.----------.   .----------.    .----------.      \033[1;36m|  
  |     \033[1;37m|    Yes   \033[1;37m|   |    No    \033[1;37m|    |   Maybe  \033[1;37m|      \033[1;36m|
  |     \033[1;37m'----------'   '----------'    '----------'     \033[1;36m |
  |______________________________________________________|

'''

    print B+'  [1]'+C+' Local File Inclusion'+W+' (Root Directories)'
    time.sleep(0.1)
    print B+'  [2]'+C+' Remote File Inclusion'+W+' (Executable Scripts)'
    time.sleep(0.1)
    print B+'  [3]'+C+' OS Command Injection'+W+' (Windows & Linux)'
    time.sleep(0.1)
    print B+'  [4]'+C+' Path Traversal '+W+'(Sensitive Paths)'
    time.sleep(0.1)
    print B+'  [5]'+C+' Cross-Site Request Forgery '+W+'(Absolute)'
    time.sleep(0.1)
#    print B+'  [6]'+C+' Cross-Site Scripting '+W+'(Absolute)'
#    time.sleep(0.1)
    print B+'  [7]'+C+' SQL Injection '+W+'(Error & Blind Based)'
    time.sleep(0.1)
    print B+'  [8]'+C+' LDAP Entity Injection '+W+'(Error Enumeration)'
    time.sleep(0.1)
    print B+'  [9]'+C+' HTML Code Injection '+W+'(Handcoded Payloads)'
    time.sleep(0.1)
    print B+'  [10]'+C+' HTTP Response Splitting '+W+'(CRLF Injection)'
    time.sleep(0.1)
    print B+'  [11]'+C+' PHP Code Injection '+W+'(Windows + Linux)'
    time.sleep(0.1)
    print B+'  [12]'+C+' Shellshock Vulnerabilities'+W+' (Bash RCE)'
    time.sleep(0.1)
    print B+'  [13]'+C+' Unvalidated URL Redirects'+W+' (Open Redirects)'
    time.sleep(0.1)
    print B+'  [14]'+C+' Sub-domain Takeover'+W+' (50+ Services)\n'
    time.sleep(0.1)
    print B+'  [A]'+C+' Load all the modules 1 by 1\n'
    time.sleep(0.1)
    print B+'  [99]'+C+' Back\n'

