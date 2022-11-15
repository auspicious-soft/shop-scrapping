# -*- coding: utf-8 -*-
import scrapy


class ShopSpider(scrapy.Spider):
    name = 'shop'
    # allowed_domains = ['www.shop.com']
    # start_urls = ['http://www.shop.com/']
    def start_requests(self):
        url = 'https://www.tfrrs.org/results_search.html'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        meet_url=response.xpath('//td/a/@href').extract()
        meet_name=response.xpath('//td/a/text()').extract()

        # for i in men1:
        #     # print(i)
        #     url2="https:"+str(i)
        #     print(url2)
        #     self.gen="MAN"
            
        #     yield scrapy.Request(url=url2, callback=self.parse1)
            # men.append(i.strip())
        for i in meet_url:
            url2="https:"+str(i)
            # print(url2)
            yield scrapy.Request(url=url2, callback=self.parse1)
            

    def parse1(self, response):
        m_n_event=response.xpath('//td/a/@href').extract()
        for i in m_n_event:
            url3="https:"+str(i)
            # print(url3)
            yield scrapy.Request(url=url3, callback=self.parse2)



    def parse2(self, response):
        url41=response.xpath('//td/a/@href').extract()
        for i in url41:
            url4="https:"+str(i)
            # print(url4)
            yield scrapy.Request(url=url4, callback=self.parse4)


    def parse4(self, response):
        team_name=response.xpath('//th/a/text()').extract()
        date_name=response.xpath('//th/span/text()').extract()
        time_aagya=response.xpath('//td/a/text()').extract()
        sum_time=[]
        for i in time_aagya:
        #     print(i)
            if "." in i:
        #         print(i)
                sum_time.append(i)
        end_date=[]
        for i in date_name:
            i=i.strip()
            if "," in i:
                end_date.append(i)
        #         print(i)
        meet_pos=response.xpath('//td[@class="panel-heading-text"]/text()').extract()
        check=[]
        for i in meet_pos:
        #     print(i.strip())
            check.append(i.strip())
        meters=[]
        pos=[]
        for i in check:
        #     print(i.strip())
            if len(i)<=4 and len(i)!=0:
        #         print(i)
                meters.append(i)
            if len(i)>4:
                pos.append(i)
        print("done")
        for i,j,k,l,m in zip(team_name,end_date,sum_time,meters,pos):
            yield {
            'teem_name': i,
            'date': j,
            'meet_time': k,
            'meaters': l,
            'position': m,
        }
        

    	
