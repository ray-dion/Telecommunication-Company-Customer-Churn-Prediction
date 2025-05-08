import pandas as pd

def tukey_rule(df, cols, threshold=1.5):
    '''
    Function yang bertugas dalam melakukan kalkulasi upper dan lower bound outlier 
    pada sebuah kolom menggunakan Tukey's Rule
    '''
    q1 = df[cols].quantile(0.25)
    q3 = df[cols].quantile(0.75)

    iqr = q3-q1

    if threshold != 1.5 and threshold != 3:
        raise ValueError("Threshold hanya bisa antara 1.5 atau 3.")
    
    ub = q3 + (iqr*threshold)
    lb = q1 - (iqr*threshold)
    
    outliers = df[(df[cols]>ub)|(df[cols]<lb)]

    return outliers, ub, lb

def z_score(df, cols):
    '''
    Function yang bertugas dalam kalkulasi nilai upper dan lower bound outlier
    pada sebuah kolom yang berdistribusi normal menggunakan metode Gaussian/Z-Score
    '''
    ub = df[cols].mean() + (3 * df[cols].std())
    lb = df[cols].mean() - (3 * df[cols].std())
    outliers = df[(df[cols] > ub) | (df[cols] < lb)]

    return outliers, ub, lb
