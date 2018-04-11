# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook
import usersetting
from mysqlinterface import SqlInterface
import youdaotranslation
import datetime

workbook = Workbook()
worksheet = workbook.active
worksheet.append((u"职位名", u"公司名", u"工作地点", u"薪资", u"发布时间", u"公司性质", u"规模", u"分类"))


class JobcollectionPipeline(object):
    @staticmethod
    def construct_output_name():
        """
        mysql table name and excel file name is constructed within this method,
        first we translate content into english by youdao fanyi,
        current time is added behind to avoid collision
        for example:
        if we search '软件' at 2018-04-12 15:33:22, the name would be software20180412153322
        """
        try:
            jobname = youdaotranslation.translate(usersetting.CONTENT)
        except Exception:
            jobname = ""
        if len(jobname) > 30:
            jobname = jobname[:30]
        jobname = '_'.join(jobname.split(' '))
        nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        return jobname+nowtime

    def open_spider(self, spider):
        self._output_base_name = JobcollectionPipeline.construct_output_name()
        if usersetting.USE_MYSQL:
            self._mysql_object = SqlInterface()
            self._db = self._mysql_object.connect()
            self._cursor = self._mysql_object.cursor()
            self._cursor.execute("create table if not exists {} ("
                                 "id int not null auto_increment primary key,"
                                 "job varchar(60),"
                                 "company varchar(50),"
                                 "location varchar(10),"
                                 "salary varchar(25),"
                                 "release_date date,"
                                 "company_type varchar(10),"
                                 "company_size varchar(15),"
                                 "area varchar(35)) default charset=utf8;".format(self._output_base_name))

    def process_item(self, item, spider):
        company_info = self.handle_some_stuff(item["company_info"])
        worksheet.append([item["job"], item["company"], item["location"],
                          item["salary"], item["release_date"]] + company_info)
        if hasattr(self, "_cursor"):
            current_year = datetime.datetime.now().strftime("%Y")
            try:
                self._cursor.execute("insert into {name} (job, company, location, salary, release_date,"
                                     "company_type, company_size, area) values ('{job}','{company}','{location}',"
                                     "'{salary}','{release_date}','{company_type}','{company_size}','{area}')".
                                     format(name=self._output_base_name, job=item["job"], company=item["company"],
                                            location=item["location"], salary=item["salary"],
                                            release_date=current_year+"-"+item["release_date"],
                                            company_type=company_info[0], company_size=company_info[1],
                                            area=company_info[2]))
                self._db.commit()
            except Exception as e:
                print e.message
                self._db.rollback()

    @staticmethod
    def handle_some_stuff(item_company_info):
        """
        this method is used to split item['company_info'] into company_type, company_size, area
        """
        temp = item_company_info.split('|')
        for index, item in enumerate(temp):
            temp[index] = item.strip()
        return temp

    def close_spider(self, spider):
        workbook.save(self._output_base_name + ".xlsx")
        if hasattr(self, "_mysql_object"):
            self._mysql_object.close()
