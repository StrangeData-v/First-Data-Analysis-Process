# Hello World!

Hi everybody! This is my first attempt to make a data analysis process! The whole process is quite simple: spidering data , analysizing data ,and finally get conclusion. Tools used in this project is Python and Excel. In order to master Python as soon as possible, so we will use Python more in this project. Well, because this is my first project and at the same time I am the newer of Python, there will be a lot of bugs and flaws in the project . So this project is just a attemptation involved less reference meaning. But truth is , which I believe , my second project will be better that could provide a good insight for readers. I hope that day comes soon! And welcome to commit me your precious views.

## How do we finish this project:
1. Find data structrue of 51job.com, then dig it via  python spider.
2. Clean up the data.
3. Use python to find the hide information from disposed data.
4. Express info via chart and graph.
5. Write it to Github.
6. Make a cup of coffee.


# FILES:
1. Spider code: [dig_51job.py](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/dig_51job.py)
3. Data analysing code: [data_analysis_process.py](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/data_analysis_process.py)
3. Visual graph: *.png 

HERE WE START !

# Step1: Coding a spider + Clean up initial data.
    Before coiding a python spider, we should visit the web page first.In this project, our target web page is [51job.com](https://search.51job.com/list/020000,000000,0000,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=) . We can filter the results via adjust the key bottoms. Such as change the __location__ into __Shanghai__.And after that, the web url will __changed__!.So, for getting the correct data, we can filter the jobs data via web-builded-in funcions.After set a lot of constrains. We can get the **url** , but this **url** is just a list of job info. For getting every job's demand info , we should click the hyperlink and see the job demand. So we should get the hyperlink list first and then get every jobs info of list.

    In the [dig_51job.py](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/dig_51job.py) , we have definded some functions to finish every steps. The function __getiplist__ is used to get a proxy ip list from [www.xicidaili.com](https://www.xicidaili.com/) which is a web site provided free proxy ip address. But there are a lots of temparery ip whose valid time span is just 1 minutes so that can't finish our digging task. So our function set a filter model to filter this useless site. Other function is used for getting data from 51jobs. The sepcific digging process contains two important parts which we have mentioned just now. It is getting url list and getting each jobs demand of url list. 

    After anlyse the site data structrue, we can get ready to write a script using Python. Python is a perfect programing language for those who are newer for IT world. It's sytanx is maybe the same as the orders we using at the usually life. So this language is so suitable for new comer. And after a months studing, I get started tp operate this project.And also, as my first spider script, 'little spider' maybe seems very terrible and uncorrect complex. But fortunately, we finally successed! Ok return our process, next is runing the script files named **__dig_51job.py__**.

```
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
```

After you run the script ,you will get a csv typed files. Files contains any numbers of items you want, and each items involved __8__   fields:

> __title__ , __href__ , __salary__ , __posted date__ , __qualification__ , __company type__ , __company scale__ , __company categroy__

Like this:
![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/Initial.png)

But as you can see, the intial data contains lots of unpleasent none field. So next we will clean up our initial data. The method is using __csv__ package of Python to drop up the None field and uncompleted field such as that in picture in yellow color. Below is the spcific code.

```
with open('filter_all.csv','r') as fr:
    with open('filter_all_1.csv','w') as fw:
        csvr = csv.reader(fr)
        csvw = csv.writer(fw)
        header = next(csvr)
        csvw.writerow(header)
        for i in range(1404):
            m = next(csvr)
            if len(m[5]) > 50:
                csvw.writerow(m)
```

Fortunataly our initial data is not very unsuitable for our next analysis, so one clean procerdure is enough. So we will get the cleared data table:
![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/Processed.png)

When we prepared all the things, then it is time for analysis!

# Step2: Analysis Process + Visual presentation
When we come to this part, things has been succesful half. In this part we should analyse the data we get from 51jobs and find fome hidden secret reguler. So at first we should make clear that **__what is our perpose__**. Actually the data analysis process could be divided into two class.  

![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/PA%2BRA.png)

Pointed analysis and random analysis. As the name shown, pointed analysis required a aim before we start a project. An aim is important that can guide us into a right way so that we can improve our efficiency. Almost 90% of data analysis projects followed pointed principle. But random analysis is also usefull in some condition such as creative analysis. In our process, it is better to set a perpose such as this:
![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/aims.png)

For solve this question , maybe we should create a wordcloud first. It is so easy to use Python to make a wordcloud. All we need is __jieba__ package and __wordcloud__ package. Here is the code:
```
import jieba
import matplotlib.pyplot as plt
import wordcloud

file = open('C:\\Users\\13115\\epy\\qualifiction.txt')
text = ' '.join(jieba.cut(file.read()))
font_path = 'C:\\Users\\13115\\epy\\huaweikaiti.ttf'
wc = wordcloud.WordCloud(font_path,width = 1920,height = 1080,background_color = 'white').generate(text)
plt.imshow(wc)
wordcloud.WordCloud.to_file(wc,'C:\\Users\\13115\\epy\\fenci.jpg')
```
And show the result:
![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/wordcloud.jpg)

In order to cover our 3 questions, we should meaure the associated index of salary and qualification. But before do that, we have to sanderize the salasy. Here are one method to do that in our analysis code [data_analysis_process.py](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/data_analysis_process.py).

```
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
```

Simple and useful. Next is finding relationship between salary and qualification. In this part, we import a Python package named __jieba__ that is used for cutting the sentence string into single words , which seems like __nature language process__. After that we can create lots of matching between and salary level and single words cut from qualification. We can use a dictionary to contains the matchings. Then counts the number of every matchings from dictionary. In this step, how to count words quickly is a interesting question. There are some algorithm to solve it. But for our provety of knowledge of algorithm, we used the , mabe the most , stupid mathod. Yes we count directly:
```
fin_dict = {}

# A sily filtering method which will occuping lots of rescource.  

# This function runing spends 7 min!

for i in list0:

    c = list0.count(i)

    fin_dict[i] = c
```
Well, as the length of list0 is 171716, so this tiny code cost ablout 7 minutes...

Then we can input the result. Because we have divided the salary into 8 levels , for each levels , we made a words association graph.
For example, in E level , which means workers well get 12000 yuan to 160000 yuan every year, we can get the top 25 words in qualification highly accosiated with E level.
![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/E.png)
And other graphs are in this repository named like 'E.png'. 

Then what about skills? Make clear that which important skill is more required for different levels is also necessary. So use the same method, we get this table:
![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/Tools.png)
This table shows the priority in every salary levels. We can conclude that with the level raisings, __Python__ and __sql__ is more and more important for workers. Office app such as Excel is always a necessary tools for data analyser. That is so interesting! So if you want to be a data analyser , Excel is the fundmental tools in what you should master. 
The industry trends is also a good insight for newer. Maybe we can use sample to simulate the actual envrioment. Here is the salary level distribution and company size distribution of recuriting company.
![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/salary_destribute.png)
![alt text](https://github.com/StrangeData-v/First-Data-Analysis-Process/blob/master/company_type_distribution.jpg)

From salary level graph, we can get a strange conclusion that the share of primary data analyser whose salary level is maybe the G or F is very low, which is obviously unnormal because it is highly skewing from __Pareto‘s principle__ also named __二八定律__ . This is so weird! If it is a truth, then the new comer of data analysis industriy like me would cry so sorrowed.. We should have a deep research for this strang conclusion.

# Step3: Conclusion
After this data analysis project, we can conclude 3 important thins:

1. Python is so useful and easy to use.
2. Data anlysers' skill varied from different salary levels. Python is more important for middle level analyser.
3. The market shows a low demand for Primary data analyser.

So , that all. For give you a better report in the future, I will pay more time and patience on study. Thanks guys for reading.






