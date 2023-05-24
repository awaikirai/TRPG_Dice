#!/usr/bin/env python3
# coding: UTF-8

import random
import re

# 0からdまでの数
def dice(d):
    num = random.randrange(d)
    return num+1

def formula(f):
    su = 0
    if re.findall("[^dD0-9+]+", f):
        print("1D100 で出直してまいれ")

    else:
        if re.findall("[dD+]+", f):
            if re.match("[0-9]+[dD][0-9]+?(([+][0-9]+([dD][0-9]+)?)+)?", f):
                fs = re.split("[+]", f)
                for i in range(len(fs)):
                    if re.findall("[dD]+", fs[i]):
                        fm = re.split("[dD]", fs[i])
                        for j in range(int(fm[0])):
                            su += dice(int(fm[1]))
                    else:
                        su += int(fs[i])
                print(su)

            else:
                print("1D100 で出直してまいれ")
        else:
            print(dice(int(f)))


if __name__ == "__main__":
    d = input("ダイスを振ってください -> ")
    formula(d)

