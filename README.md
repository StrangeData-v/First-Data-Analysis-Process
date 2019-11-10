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

After anlyse the site data structrue, we can get ready to write a script using Python. Python is a perfect programing language for those who are newer for IT world. It's sytanx is maybe the same as the orders we using at the usually life. So this language is so suitable for new comer. And after a months studing, I get started tp operate this project.And also, as my first spider script, 'little spider' maybe seems very terrible and uncorrect complex. But fortunately, we finally successed! Ok return our process, next is runing the script files named **__dig_51job.py__**. (**ps. The code is so uncomsise that 

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


































