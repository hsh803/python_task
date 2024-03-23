from sys import stdin
import math
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def get_unigram(corpus):
    my_dic = {}
    for sen in corpus:
        for w in range(len(sen)-1):
            uni_str = sen[w].strip(" :;.,!?-_\'\"")
            if uni_str in my_dic:
                my_dic[uni_str] += 1
            else:
                my_dic[uni_str] = 1
    return my_dic

def get_bigram(corpus):
    my_dic = {}
    for sen in corpus:
        for w in range(len(sen)-1):
            bi_str = (sen[w].strip(" :;.,!?-_\'\""), sen[w+1].strip(" :;.,!?-_\'\""))
            if bi_str in my_dic:
                my_dic[bi_str] += 1
            else:
                my_dic[bi_str] = 1
    return my_dic

def c_uni(my_uni, word):
    for i in my_uni:
        if i == word:
            return my_uni[i]

def get_p(my_uni, my_bi):
    p_lst = []
    for dic_key in my_bi:
        c = c_uni(my_uni, dic_key[0])
        p = my_bi[dic_key]/c
        p_lst.append([dic_key[1], p])
    return p_lst

def get_s(my_p):
    s_lst = []
    for i in my_p:
        s_lst.append([i[0], math.log2(1/i[1])])
    return s_lst

def get_duration():
    df = pd.read_csv("file.csv", sep=';')
    duration = df.groupby('TOKEN').agg({'ORT': pd.Series.unique, 'DURATION': 'sum'})
    #duration = duration.groupby('ORT').agg({'DURATION': 'mean'})
    dic = []
    for row in duration.itertuples():
        word = str(row.ORT).strip("\'[]").lower()
        duration = row.DURATION/44100 
        dic.append((word, duration))
    return dic

def average_c(arg):
    c = {}
    for w in arg:
        if w[0] in c:
            c[w[0]] += 1
        else:
            c[w[0]] = 1
    new_dic = {}
    for i in arg:
        if i[0] in new_dic:
            new_dic[i[0]] += i[1]
        else:
            new_dic[i[0]] = i[1]      
    for i in new_dic:
        if i in c:
            new_dic[i] = new_dic[i]/c[i]
    return new_dic

def csv_duration_surprisal(my_duration, my_surprisal_average):
    cat = ['Surprisal', 'Duration']
    row = []
    for i in my_duration:
        if i[0] in my_surprisal_average:
            row.append([my_surprisal_average[i[0]], i[1]])
    filename = "duration_sursprisal.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(cat)
        csvwriter.writerows(row)
    return filename
def get_plot(file, x_par, y_par, save_img):
    df = pd.read_csv(file)
    plt.scatter(df[x_par], df[y_par])
    plt.xlabel(x_par)
    plt.ylabel(y_par)
    sns.regplot(x = x_par, y = y_par, data = df, scatter_kws = {"s": 10}, line_kws = {"color": "purple", "linewidth": 1}) 
    plt.savefig(save_img)
    plt.show()                                            
    slope, intercept, r_value, p_value, std_err = stats.linregress(df[x_par], df[y_par])
    print('Intercept: ', intercept)
    print('Coefficient: ', slope)
    print('R-squared: ', r_value**2)
    print('P-value: ', p_value)

def main():
    corpus = []
    for line in stdin: 
        word_lst = line.lower().split()
        if word_lst != []:
            corpus.append(word_lst)
    my_uni = get_unigram(corpus)
    my_bi = get_bigram(corpus)
    my_p = get_p(my_uni, my_bi)
    my_s = get_s(my_p)
    my_duration = get_duration()
    my_surprisal_average = average_c(my_s)
    my_csv = csv_duration_surprisal(my_duration, my_surprisal_average)
    get_plot(my_csv, 'Surprisal', 'Duration', 'plot')

main()
