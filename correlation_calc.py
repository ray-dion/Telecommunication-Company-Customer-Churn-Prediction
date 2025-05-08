import pandas as pd
import numpy as np
import scipy as sc

def calc_corr(df, main_cols, method='pearson'):
    '''Function ini bertugas dalam menghitung nilai korelasi dari antara target dengan feature menggunakan metode pearson'''
    
    hasil = {
        'Kolom':[],
        'Korelasi':[]
    }

    # Menghitung nilai korelasi antar kolom menggunakan metode pearson
    if method.casefold() == 'pearson':
        for cols in df.columns:
            if cols != main_cols and np.issubdtype(df[cols].dtype, np.number):
                r, p_val = sc.stats.pearsonr(df[main_cols], df[cols])
                hasil['Kolom'].append(cols)
                hasil['Korelasi'].append(r)

    # Menghitung nilai korelasi antar kolom menggunakan metode spearman
    if method.casefold() == 'spearman':
        for cols in df.columns:
            if cols != main_cols and np.issubdtype(df[cols].dtype, np.number):
                p, p_val = sc.stats.spearmanr(df[main_cols], df[cols])
                hasil['Kolom'].append(cols)
                hasil['Korelasi'].append(p)

    # Menghitung nilai korelasi antar kolom menggunakan metode kendall
    if method.casefold() == 'kendall':
        for cols in df.columns:
            if cols != main_cols and np.issubdtype(df[cols].dtype, np.number):
                df = df.fillna(0)
                tau, p_val = sc.stats.kendalltau(df[main_cols], df[cols])
                hasil['Kolom'].append(cols)
                hasil['Korelasi'].append(tau)

    # Menghitung nilai korelasi antar kolom menggunakan metode ANOVA
    elif method.casefold() == 'anova':
        for cols in df.columns:
            if cols != main_cols and df[cols].dtype == 'object': 
                '''
                Karena ANOVA membandingkan antara data Numerikal dengan Kategori maka 
                perlu validasi bahwa yang akan dibandingkan adalah beneran sebuah string
                '''

                groups = [group[main_cols].values for name, group in df.groupby(cols)]
                overall_mean = df[main_cols].mean()
                ss_between = sum(len(group) * (group.mean() - overall_mean) ** 2 for group in groups)
                ss_total = sum((value - overall_mean) ** 2 for value in df[main_cols])
                eta_squared = ss_between / ss_total
                hasil['Kolom'].append(cols)
                hasil['Korelasi'].append(eta_squared)

    # Menghitung nilai korelasi antar kolom menggunakan metode Chi-Squared
    elif method.casefold() == 'chi-squared':
        for cols in df.columns:
            if cols != main_cols and df[cols].dtype == 'object':
                '''
                Karena Chi-Squared membandingkan antara kategori dengan kategori, 
                maka perlu validasi bahwa yang akan dibandingkan adalah beneran sebuah string
                '''

                contingency_table = pd.crosstab(df[main_cols], df[cols])
                chi2 = sc.stats.chi2_contingency(contingency_table)[0]
                n = contingency_table.sum().sum()
                phi2 = chi2 / n
                r, k = contingency_table.shape
                denom = min(k - 1, r - 1)
                CramerV = np.sqrt(phi2 / denom) if denom > 0 else 0
                hasil['Kolom'].append(cols)
                hasil['Korelasi'].append(CramerV)


    df_hasil = pd.DataFrame(hasil)
    
    return df_hasil