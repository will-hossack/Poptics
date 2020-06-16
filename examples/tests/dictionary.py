#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:15:11 2020

@author: wjh
"""

def main():


    line = "surface: spherical position:  4.8    curve: -1.5151515E-2 radius: 7.7     index: N-BAF3"
    tokens = line.split()
    print(tokens)

    d = dict()
    for i in range(0,len(tokens),2):
        d.update({tokens[i]:tokens[i+1]})

    print(d.keys())

    c = float(d["curve:"])

    print("Curvature is : " + str(c))


main()