#!/usr/bin/python2.7
"""Blank Python 2.7 file"""
import re
email=input()
regex=r"\D+"
if(re.search(regex, email)):
  print('valid')
else:
  print('invalid')