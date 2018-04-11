# -*- coding: UTF-8 -*-
from jobparameters import cities, coltype, companysize, degree
from jobparameters import salary, releasedate, workyear
"""
if we don't want to use mysql, set USE_MYSQL = 0, else set USE_MYSQL = 1
if we want to save data into database, we must provide PASSWD and DATABASE,
and DATABASE should be existed in MySQL
"""

USE_MYSQL = 0
# MYSQL SETTINGS
# HOST = "localhost"
# USER = "root"
# PASSWD = "password"
# DATABASE = "job"
# PORT = 3306
"""
# PAGES used to specify how many pages you want to crawl,
# if we want all the pages, uncomment PAGES
"""
# PAGES = 2

"""
## CONTENT is the job you want to search
use the following parameters to specify search result,
CITIES should be a list or tuple,
if we uncomment an item, it will search the aspect by default,
for example, if we uncomment WORK_YEAR, then WORK_YEAR will not be a limitation to
our result
"""
CITIES = [cities.WUXI, cities.ZHENGJIANG, cities.SHANGHAI]
CONTENT = "编程"
#WORK_YEAR = workyear.ONE_THREE_YEAR
#COMPANY_TYPE = coltype.FOREIGN_CAPITAL_AE
#DEGREE_FROM = degree.BACHELOR
#COMPANY_SIZE = companysize.SIZE_150_TO_500
#SALARY = salary.SALARY_10K_TO_15K
RELEASE_DATE = releasedate.WITHIN_ONE_DAY





