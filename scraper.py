# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:43:06 2018

@author: JNSMAR043
"""
import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            pass
        