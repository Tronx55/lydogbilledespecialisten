import scrapy

class LydogbilledeSpecialisten(scrapy.Spider):
	name = 'webscraper'
	start_urls = ['https://www.lbs.dk/produkter']

	def pars(self, response):
		for price in response.xpath("//div[@class='views-field views-field-commerce-price']"):
			yield {
				'field-content': price.xpath(".//div[@class='views-field views-field-commerce-price']/div".extract_first()
			}