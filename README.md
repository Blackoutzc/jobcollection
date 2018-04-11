# jobcollection

## a convenient way to obtain job information from web

## all you have to modify is the jobcollection/usersetting.py

>> #### data is stored into excel sheet by default (and MySQL databse if set USE_MYSQL=1 in usersetting.py)

>> #### we can specify how many page numbers we want to crawl by setting PAGES

>> #### we can specify parameters to narrow down the search, for example setting CITIES, SALARY, etc.

![Image text](https://github.com/Blackoutzc/jobcollection/tree/master/pics/capture_setting.PNG)

## result display 

![Image text](https://github.com/Blackoutzc/jobcollection/tree/master/pics/capture.PNG) <br />

![Image text](https://github.com/Blackoutzc/jobcollection/tree/master/pics/MySQL_snapshot.PNG)

## usage

>> #### 1¡¢modify usersetting.py to set some parameters, at least modify content

>>>> ???????? I strongly suggest you set PAGES to 1 for testing first

>> #### 2¡¢open cmd, switch to the base directory downloaded from github /jobcollection by default, type "scrapy crawl jobcollection"

>>>> if have no clue of scrapy command, then i suggest you read the scrapy documentation first