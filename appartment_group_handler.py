#!/usr/bin/env python3
# *-* coding: utf8 *-*
import re
def validatePrice(price):# type str
    regex="\w*"
    list_price=re.findall(regex,price)
    print(list_price)
    


