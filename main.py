#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

def args():
    parser=argparse.ArgumentParser(description="Retrouve toutes les annonces correspondant aux critères mis en paramètres")

    parser.add_argument("-n","--number", help="Donne le carré du nombre", type=int)
    args=parser.parse_args()

    parser.add_argument("--gf", "--facebook_group", help="Groupe dans lequelle vous voulez chercher", required=False, type=str)

    parser.add_argument("--pr", "-price_range", help="Intervalle de prix pou filtrer les annonces ->exemple 450 & 550 ", required=False, type=str)

    parser.add_argument("-l", "-localisation", help="Filtre sur les lieu des annonces", required=False, type=str)
    
    return parser.parse_args()

if __name__ == '__main__':
    arguments=args()   
    print(arguments.number**2)

