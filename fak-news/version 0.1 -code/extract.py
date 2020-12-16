import pandas as pd
import numpy as np
import re


def tip_filter(headline):
    headline=headline.lower()
    if 'buy' in headline:
        return headline
    elif 'sell' in headline:
        return headline
    if 'hold' in headline:
        return headline
    if 'accumulate' in headline:
        return headline
    if 'target' in headline:
        return headline
    
    else: 
        pass

def price(headline):
    price=re.compile(r'\d+\..\d+')
    a=price.findall(headline)
    try:
        return float(a[0])
    except:
        pass
    else:
        return np.nan
    