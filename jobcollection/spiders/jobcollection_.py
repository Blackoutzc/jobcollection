#-*- coding: UTF-8 -*-
import sys
from jobcollection.items import JobcollectionItem
import scrapy
import requests
from scrapy.selector import Selector
#import jobparameters.cities as cities
#import jobparameters.releasedate as release
from . import urlfactory
import jobcollection.usersetting as usersetting
reload(sys)
sys.setdefaultencoding('utf-8')


def construct_url():
    parameters_dict = {}
    for key in ["cities", "content", "work_year", "company_type", "degree_from",
                "job_term", "company_size", "salary", "release_date"]:
        key_upper = key.upper()
        if key_upper in dir(usersetting):
            parameters_dict[key] = eval("usersetting." + key_upper)
    return urlfactory.URLFactory(**parameters_dict).url


class JobSpider(scrapy.Spider):
    name = "jobcollection"
    start_urls = [construct_url()]
    allowed_domain = ["51job.com"]
    if "PAGES" in dir(usersetting):
        num = 0

    def parse(self, response):
        if "PAGES" in dir(usersetting):
            JobSpider.num += 1
            if JobSpider.num > usersetting.PAGES:
                return
        el_class = response.xpath("//div[@id = 'resultList']/div[@class='el']")
        for single_el in el_class:
            item = JobcollectionItem()
            job_name = single_el.xpath("./p//a/@title").extract_first()
            company_name = single_el.xpath("./span[@class='t2']/a/@title").extract_first()
            location = single_el.xpath("./span[@class='t3']/text()").extract_first()
            salary = single_el.xpath("./span[@class='t4']/text()").extract_first()
            update_date = single_el.xpath("./span[@class='t5']/text()").extract_first()
            # company_info_url is used to extract some information of that company
            company_info_url = single_el.xpath("./span[@class='t2']/a/@href").extract_first()
            r = requests.get(url=company_info_url)
            r.encoding = "gb2312"
            company_info = Selector(text=r.text).xpath("//p[contains(@class,'ltype')]/text()").extract_first()
            item["company_info"] = company_info if company_info else "None|None|None"
            item["job"], item["company"], item["location"] = job_name, company_name, location
            item["salary"], item["release_date"] = salary, update_date
            yield item
        next_page_url = response.xpath(u"//a[text()='下一页']/@href").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(url=next_page_url, callback=self.parse, dont_filter=True)

'''
    def deep_into_single_page(self, response):
        company_info = response.xpath("//p[contains(@class,'ltype')]/text()").extract_first()
        if company_info:
            temp_container = company_info.encode("gb18030").split('|')
            for index, item in enumerate(temp_container):
                temp_container[index] = item.strip()
            company_info = "|".join(temp_container)
            print company_info
'''