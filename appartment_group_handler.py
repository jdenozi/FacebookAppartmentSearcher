#!/usr/bin/env python3
# *-* coding: utf8 *-*
import re


def validatePrice(price):# type str
    regex="[0-9]*"
    list_price=re.findall(regex,price)
    list_price=[i for i in list_price if i!=""]
    print(len(list_price))
    if len(list_price)==2:
        print(list_price)
        return list_price
    else:
        return 

class groupFacebook():
    def __init__(self, groupFacebook, price, localisation):
        self.groupFacebook=groupFacebook
        self.price=price
        self.localisation=localisation

