# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:49:48 2019

@author: 13115
"""

import urllib
import bs4
import csv
# import random


# ---> get some proxy ip

def getiplist(url = 'https://www.xicidaili.com/'):
    '''This url contains fome proxy ip divided by proxy time region, so in order to get long-time ip address, the funcion is created'''
    req = urllib.request.Request(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'})
    res = urllib.request.urlopen(req)
    soup = bs4.BeautifulSoup(res,'html.parser')
    ts = soup.findAll('tr',{'class':'odd'})
    iplist = []
    for each in ts:
        s = each.findAll('td')[6].string
        h = each.findAll('td')[5].string
        if '1分钟' not in s and h == 'HTTPS':
            iplist.append(each.findAll('td')[1].string)
    return iplist

# ---> function belows are used for get the attributs of jobs
    
def getsoup(url):
    requ = urllib.request.Request(url,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'})
    response = urllib.request.urlopen(requ)
    soup = bs4.BeautifulSoup(response,'html.parser')
    return soup
    
def getnext(url):
    soup = getsoup(url)
    next_url = soup.findAll('li',{'class':'bk'})[1].a.attrs['href']
    n = str(next_url)
    # next_url.encode('Unicode')
    return n

def getlo(url):
    """  Get a part of html which contains the job information from the whole 
    soup, also contains a lot of others useless information!"""
    soup = getsoup(url)
    target_set = soup.findAll('div',{'class':'el'})
    return target_set
 
def getsn(target_set):
    """ Because of some unpredictable reasons , the return from fuction 'getts'
    involves some unexpected and useless content.In order to get rid of that, 
    this funcion was being created. But this funcion works only in this case. 
    So it's not a good mathod to deal with the useless information.Should be 
    imporved """
    s = 0
    for i in target_set:
        s += 1
        l = len(i)
        if l == 3:
            start_num = s + 1
    return start_num

def getinfo(ele):
    """ Analyse each elements from target_set and get the attribute"""
    title = ele.find('span').a.attrs['title']
    href = ele.find('span').a.attrs['href']
    company = ele.findAll('span')[1].string
    salary = ele.findAll('span')[3].string
    date = ele.findAll('span')[4].string
    return [title,href,company,salary,date]

""" 
def getdict(url):
    # Get the finally dictionary
    total_info = {}
    ts = getlo(url)
    sn = getsn(ts)
    i = 0
    for each in ts[sn + 1:]:
        ee = getinfo(each)
        total_info[i] = ee
        i += 1
    return total_info
"""

# ---> function belows are used for get the qulifications of jobs.

def getqua(url):
    """ Get qualifiction description of every jobs"""
    response = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(response,'lxml')
    qua_set = soup.find('div',{'class':'tBorderTop_box'}).find('div',{'class':'bmsg job_msg inbox'}).findAll('p')
    qualification = 'qualification: '
    for each in qua_set:
        if each.string != None:
            qualification = qualification + each.string
    return qualification

def getcominfo(url):
    comp = []
    soup = getsoup(url)
    m = soup.find('div',{'class':'com_tag'}).findAll('p')
    for i in range(len(m)):
        comp.append(m[i].attrs['title'])
    return comp
        

# ---> final funcion
def getlist(url,listx):
    ts = getlo(url)
    sn = getsn(ts)
    for each in ts[sn:]:
        try:
            info = getinfo(each)
        except ValueError:
            continue
        uurl = info[1]
        try:
            qua = getqua(uurl)
            info.append(qua)
        except AttributeError:
            qua = ['nothing']
            info.append(qua)
        try:
            cominfo = getcominfo(uurl)
            info.extend(cominfo)
        except AttributeError:
            cominfo = ['nothing','nothing','nothing']
            info.extend(cominfo)
        listx.append(info)
    return listx

# START : 

final_dict = {}
for i in range(1,50):
    try:
        s = str(i)
        url = 'https://search.51job.com/list/020000,000000,0000,00,9,05%252C06%252C07,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,' + s + '.html?lang=c&postchannel=0000&workyear=01%2C02&cotype=99&degreefrom=04&jobterm=01&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        final_dict[i] = getlist(url,[])
    except (urllib.error.URLError,urllib.error.HTTPError):
        continue

# ---> save the data
l = len(final_dict)

csvFile = open('filter_all.csv', 'w')
writer = csv.writer(csvFile)
writer.writerow(('title', 'href', 'company','salary','date','qualification','comtype','comsize','comtrade'))
try:
    for i in final_dict.keys():
        for r in range(1,len(final_dict[i]) + 1):
            try:
                title = str(final_dict[i][r][0])
                href = str(final_dict[i][r][1])
                company = str(final_dict[i][r][2])
                salary = str(final_dict[i][r][3])
                date = str(final_dict[i][r][4])
                qualification = str(final_dict[i][r][5])
                comtype = str(final_dict[i][r][6])
                comsize = str(final_dict[i][r][7])
                comtrade = str(final_dict[i][r][8])
                writer.writerow((title,href,company,salary,date,qualification,comtype,comsize,comtrade))
            except (UnicodeEncodeError,IndexError,KeyError):
                continue
finally:
    csvFile.close()

