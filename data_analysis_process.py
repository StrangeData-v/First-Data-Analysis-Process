# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:30:21 2019

@author: 13115
"""
import csv
import re
import jieba

def getsallev(s):
    ''' s is a sting of salary description. This function is used to standerize
    the salary info into level descreiption'''
    if '-' in s:
        p = s.index('-')
        adjust_dict = {'万/月':12,'千/月':12/10,'万/年':1,'元/天':365/10000}
        r = adjust_dict[s[-3:]]
        ss = ( float(s[:p]) + float(s[p+1:-3]) ) / 2 * r
    else:
        ss = float(s[:-3]) * 365/10000
    if ss <= 8:
        level = 'G'
    elif ss > 8 and ss <= 12:
        level = 'F'
    elif ss >12 and ss <= 16:
        level = 'E'
    elif ss > 16 and ss <= 22:
        level = 'D'
    elif ss > 22 and ss <= 30:
        level = 'C'
    elif ss > 30 and ss <= 40:
        level = 'B'
    elif ss > 40 and ss <= 60:
        level = 'A'
    else:
        level = 'S'
    return level

list0 = []
file = open('C:\\Users\\13115\\epy\\delete_none.csv')
cr = csv.reader(file)
for each in cr:
    l = getsallev(each[3])
    s = str(each[4])
    sc = jieba.lcut(s)
    pat1 = '[0-9A-Za-z\u4e00-\u9fa5]' # Filter the spercific symbol.
    pat2 = '[0-9]' # Filter numbers.
    for i in sc:
        if i != 'qualification': # Filter the 'qualification' word.
            if re.match(pat1,i) is not None:
                if re.match(pat2,i) is None:
                    i = i.upper()
                    list0.append(i + ':' + l)
                    # Final get a list like ['word1:A','word2:B'...]

fin_dict = {}
# A sily filtering method which will occuping lots of rescource.  
# This function runing spends 7 min!
for i in list0:
    c = list0.count(i)
    fin_dict[i] = c
    
'''Result:
len(list0)
Out: 171716

len(fin_dict)
Out: 22854
'''

xx = open('C:\\Users\\13115\\epy\\dict_test.csv','w')
cw = csv.writer(xx)
for each in fin_dict:
    word_name = each[0].split(':')[0]
    level = each[0].split(':')[1]
    num = fin_dict[each]
    if len(word_name) > 1 and num > 2:
        cw.writerow([word_name,level,num])
xx.close()

list1 = []
with open('C:\\Users\\13115\\epy\\delete_none.csv') as fr:
    cr = csv.reader(fr)
    for each in cr:
        list1.append(getsallev(each[3]))
for i in ['A','B','C','D','E','F','G','S']:
    print(i,list1.count(i))
        


                    
                  


  