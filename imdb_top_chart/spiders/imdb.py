import scrapy

from imdb_top_chart.items import ImdbTopChartItem

class ImdbTopChart(scrapy.Spider):
	name = "imdb"
	allowed_domains = ["imdb.com",]
	start_urls = ("https://www.imdb.com/chart/top",)

	def parse(self, response):
		links = response.xpath('//tbody[@class="lister-list"]/tr/td[@class="titleColumn"]/a/@href').extract()
		i = 1
		for link in links:
			abs_urls = response.urljoin(link)
			url_next = '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr['+str(i)+']/td[3]/strong/text()'
			rating = response.xpath(url_next).extract()
			if(i <= len(links)):
				i=i+1
				yield scrapy.Request(abs_urls, callback = self.parse_indetail, meta={'rating' : rating})

	def parse_indetail(self, response):
		item = ImdbTopChartItem()

		item['title'] = response.xpath('//div[@class="title_wrapper"]/h1/text()').extract()[0][:-1]
		item['directors'] = response.xpath('//div[@class="credit_summary_item"]/a/text()').extract()[0][:-1]
		item['writer'] = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[3]/a/text()').extract()[:-1]
		item['stars']  = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[4]/a/text()').extract()[:-1]
		item['popularity'] = response.xpath('//div[@class="titleReviewBarItem"]/div[@class="titleReviewBarSubItem"]/div/span/text()').extract()[2][21:-8]

		return item