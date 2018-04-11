# -*- coding: UTF-8 -*-
import urllib


class URLFactory(object):
    """
    this class is used to construct url from 51job.com
    """
    _base_url = "https://search.51job.com/list/{cities},000000,0000,00,9,99,{content},2,1.html?lang=c&" \
                "stype=&postchannel=0000&workyear={work_year}&cotype={company_type}&degreefrom={degree_from}" \
                "&jobterm={job_term}" \
                "&companysize={company_size}&providesalary={salary}&lonlat=0%2C0&radius=-1&ord_field=0" \
                "&confirmdate={confirm_date}&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

    def __init__(self, cities=["000000"], content="%2520", work_year="99", company_type="99", degree_from="99", job_term="99", company_size="99", salary="99", release_date="9"):
        if content != "%2520":
            content = urllib.quote(urllib.quote(content).decode("utf-8").encode('gbk'))
        self._url = URLFactory._base_url.format(cities="%252C".join(cities),
                                                content=content,
                                                work_year=work_year,
                                                company_type=company_type,
                                                degree_from=degree_from,
                                                job_term=job_term,
                                                company_size=company_size,
                                                salary=salary,
                                                confirm_date=release_date)

    @property
    def url(self):
        return self._url
