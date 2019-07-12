from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from scrapy.loader import ItemLoader
from sgpropbot.items import SgpropbotItem
import datetime


class PropertiesSpider(CrawlSpider):

    name = 'properties'
    allowed_domains = ['99.co']
    #scrape_count = 1
    # Scrape through each search result pages
    start_urls = [('https://www.99.co/singapore/rent?page_num=' +
                   str(i)+'&sort_field=price&sort_order=asc') for i in range(1, 401, 1)]
    #start_urls = ['https://www.99.co/singapore/rent']
    rules = (Rule(LinkExtractor(allow='(/singapore/rent/property).*'),
                  callback='parse_items'),)

    def parse_items(self, response):

        for row in response.xpath('//html'):

                    loader = ItemLoader(item=SgpropbotItem(), selector=row)

                    loader.add_value('url', response.url)
                    loader.add_xpath(
                        'propname', "//*[@id='appContent']//div[@class='Listing__titleContainer__5bjht']//h1/text()")
                    loader.add_xpath(
                        'proptype', "//*[@id='appContent']/div/div[3]/div//div[1]/ol/li[position()>=2 and position()<5]//*[not(contains(.,'For rent'))]//text()")
                    loader.add_xpath(
                        'address', "//*[@id='appContent']//div[@class='Listing__summaryContainer__1ncDT']//p[@class='Text__text__x0JSc']//text()")
                    loader.add_xpath(
                        'bednum', '//*[@id="appContent"]//div[@class="Listing__summaryTextContainer__8Oo0l"]//div[contains(.,"Studio") or contains(.,"Bed")]/p/text()')
                    loader.add_xpath(
                        'bathnum', "//*[@id='appContent']//div[@class='Listing__summaryTextContainer__8Oo0l']//p[contains(.,'Bath')]//text()")
                    loader.add_xpath(
                        'propsize', "//*[@id='appContent']//div[@class='Listing__summaryTextContainer__8Oo0l']//p[contains(.,'sqft')]//text()")
                    loader.add_xpath(
                        'rental', "//*[@id='appContent']//h3[contains(.,'S$')]//text()")
                    loader.add_xpath(
                        'rental_psf', "//*[@id='appContent']//div[@class='Listing__summaryTextContainer__8Oo0l']//p[contains(.,'psf')]//text()")
                    loader.add_xpath(
                        'keydetails', "//*[@id='keyDetails']/div//p/text()")
                    loader.add_xpath(
                        'amenities', "//*[@id='listingPageContent']/div[@class='Listing__leftColumn__3k7xe']/div[not(@id='description') and not(@id='development')and not(@id='keyDetails') and not(@id='transactions')]/div//text()")
                    loader.add_xpath(
                        'completionyear', '//*[@class="ProjectOverviewCard__info__70VMS"]//p[contains(.,"Year of Completion")]//text()[3]')
                    loader.add_xpath(
                        'totalunit', '//*[@id="development"]/div/div[2]//p[contains(.,"Total Units")]/text()[3]')
                    loader.add_xpath(
                        'tenure', '//*[@id="development"]/div/div[2]//p[contains(.,"Tenure")]/text()[3]')
                    loader.add_xpath(
                        'nearestmrt', '//p[@class="Text__text__x0JSc NearestMrt__title__iVNyM"]//text()')
                    loader.add_xpath(
                        'nearestmrt_dist', '//p[@class="Text__text__x0JSc NearestMrt__subtitle__3W5Ur"]//text()')
                    loader.add_xpath(
                        'posted_ago', '//span[@class="RepostedDate__dateFormatted__2n-fm"]//text()')
                    loader.add_value(
                        'scraped_at', str(datetime.datetime.now()))

                    yield loader.load_item()
