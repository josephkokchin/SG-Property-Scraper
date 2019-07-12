# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
#from w3lib.html import remove_tags



def clean_price(value):
    value = value.replace('/mo', '').strip()
    value = value.replace('S$', '').strip()
    value = value.replace(',', '').strip()
    return int(value)


def clean_psf(value):
    value = value.replace('psf', '').strip()
    value = value.replace('S$', '').strip()
    value = value.replace(',', '').strip()
    return float(value)

def clean_mrt(value):
    value = value.replace('MRT', '').strip()
    return str(value)


def clean_size(value):
    value = value.replace(',', '').strip()
    return int(value.replace('sqft (built up)', '').strip())


def clean_bed(value):
    if "None" in str(value):
        value = value.replace('Beds', '').strip()
        return str('0')
    elif "Beds" in str(value):
        value = value.replace('Beds', '').strip()
        return str(value)
    elif "Bed" in str(value):
        value = value.replace('Bed', '').strip()
        return str(value)
    else:
        return str(value)


def clean_posted(value):
    value = value.replace('ago', '').strip()
    return str(value)


def clean_bath(value):
    if "None" in str(value):
        value = value.replace('Baths', '').strip()
        return int(0)
    elif "Baths" in str(value):
        value = value.replace('Baths', '').strip()
        return int(value)
    elif "Bath" in str(value):
        value = value.replace('Bath', '').strip()
        return int(value)
    elif "" in str(value):
        return int(0)
    else:
        return int(value)


def clean_address(value):
    return value.split(',')[0].strip()


def clean_tunit(value):
    if "" in str(value):
        return None
    else:
        return int(value)


class SgpropbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    propname = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    proptype = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    address = scrapy.Field(
        input_processor=MapCompose(clean_address, str.strip),
        output_processor=TakeFirst()
    )

    bednum = scrapy.Field(
        input_processor=MapCompose(str.strip, clean_bed),
        output_processor=TakeFirst()
    )

    bathnum = scrapy.Field(
        input_processor=MapCompose(str.strip, clean_bath),
        output_processor=TakeFirst()
    )

    propsize = scrapy.Field(
        input_processor=MapCompose(str.strip, clean_size),
        output_processor=TakeFirst()
    )

    rental = scrapy.Field(
        input_processor=MapCompose(str.strip, clean_price),
        output_processor=TakeFirst()
    )

    completionyear = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    totalunit = scrapy.Field(
        input_processor=MapCompose(str.strip, clean_tunit),
        output_processor=TakeFirst()
    )

    tenure = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    amenities = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=Join(',')
    )

    keydetails = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=Join(',')
    )

    rental_psf = scrapy.Field(
        input_processor=MapCompose(str.strip, clean_psf),
        output_processor=TakeFirst()
    )

    nearestmrt = scrapy.Field(
        input_processor=MapCompose(str.strip,clean_mrt),
        output_processor=TakeFirst()
    )

    nearestmrt_dist = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    posted_ago = scrapy.Field(
        input_processor=MapCompose(str.strip, clean_posted),
        output_processor=TakeFirst()
    )

    scraped_at = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )

    

