#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from essaySelenium import test_search 
import argparse
from appartment_group_handler import validatePrice
from selenium import webdriver

def args():
    parser=argparse.ArgumentParser(description="Retrouve toutes les annonces correspondant aux critères mis en paramètres")

    parser.add_argument("-n","--number", help="Donne le carré du nombre", type=int)

    parser.add_argument("--gf","--facebookGroup", help="Groupe dans lequelle vous voulez chercher", type=str)

    parser.add_argument("--pr", "--priceRange", help="Intervalle de prix pou filtrer les annonces ->exemple 450 & 550 ", required=False, type=str)

    parser.add_argument("-l", "--localisation", help="Filtre sur les lieu des annonces", required=False, type=str)
    
    parser.add_argument("--lk","--link", help="Lien de la page", type=str )

    return parser.parse_args()

if __name__ == '__main__':
    arguments=args()   
    if arguments.number is not None:
        print(arguments.number**2)
    if arguments.pr is not None:
        validatePrice(arguments.pr)
    else:
        pass

    test_search()

