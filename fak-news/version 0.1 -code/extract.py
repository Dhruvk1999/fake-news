import pandas as pd
import numpy as np
import re


def price(tip):
    res = [int(i) for i in tip.split() if i.isdigit()]
    price=re.compile(r'\d+')
    a=price.findall(tip)
    try:
        return float(a[0])
    except:
        pass
    else:
        return np.nan

        
    
def company(tip):
    bsh=re.compile(r'\s\w+\s\w+')
    return bsh.findall(tip)[0]

def advice(tip):
    tip=tip.lower()
    
    if 'buy' in tip:
        return 'buy'
    elif 'sell' in tip:
        return 'sell'
    elif  'hold' in tip:
        return 'hold'
    elif  'accumulate' in tip:
        return 'accumulate'

    else: 
        pass
    
    
#for tip in tips:
 #   print(price(tip),company(tip),advice(tip))

    