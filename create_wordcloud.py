# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:33:33 2019

@author: 13115
"""
import jieba
import matplotlib.pyplot as plt
import wordcloud

file = open('C:\\Users\\13115\\epy\\qualifiction.txt')
text = ' '.join(jieba.cut(file.read()))
font_path = 'C:\\Users\\13115\\epy\\huaweikaiti.ttf'
wc = wordcloud.WordCloud(font_path,width = 1920,height = 1080,background_color = 'white').generate(text)
plt.imshow(wc)
wordcloud.WordCloud.to_file(wc,'C:\\Users\\13115\\epy\\fenci.jpg')
