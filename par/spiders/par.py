import scrapy, re, datetime

from scrapy.loader import ItemLoader
from par.items import ParItem
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.markup import remove_tags

class ParSpider(scrapy.Spider):
    name = 'par'
    start_urls = ['https://www.parliament.bg/en/MP']

    names_page = LinkExtractor(restrict_xpaths='//div[@class="MPinfo"]/a')

    def parse(self, response):
        names_page_links =  self.names_page.extract_links(response)
        yield from response.follow_all(names_page_links, self.parse_name)

    def parse_name(self, response):

        names = response.xpath("//div[@class='MProwD']").extract()
        
        date_and_palce = response.xpath("//div[@class='MPinfo']/ul[@class='frontList']/li[contains(.,'Date of birth')]/text()").extract()
        prof = response.xpath("//div[@class='MPinfo']/ul[@class='frontList']/li[contains(.,'Profession')]/text()").extract()
        lang = response.xpath("//div[@class='MPinfo']/ul[@class='frontList']/li[contains(.,'Languages')]/text()").extract()
        party = response.xpath("//div[@class='MPinfo']/ul[@class='frontList']/li[contains(.,'Political force')]/text()").extract()
        email = response.xpath("//div[@class='MPinfo']/ul[@class='frontList']/li[contains(.,'E-mail')]/a/text()").extract()

        name = remove_tags(str(names[0]))
        date_pattern = r'\d{2}/\d{2}/\d{4}'
        party_pattern = r'[0-9%;.]'
        date = re.findall(date_pattern, date_and_palce[0])
        date = datetime.datetime.strptime(date[0], '%d/%m/%Y')
        place = date_and_palce[0][27:].strip()
        party = re.sub(party_pattern, '', party[0])

        try:
            languages = lang[0][11:-1]
        except:
            languages = ''
        try:
            professions = prof[0][12:-1]
        except:
            professions = ''

        item = ItemLoader(item=ParItem(), response=response)
        item.add_value('name', name )
        item.add_value('date', date )
        item.add_value('place', place )
        item.add_value('prof', professions )
        item.add_value('lang', languages )
        item.add_value('party', party[17:-1] )
        item.add_value('email', email[0] )
        return item.load_item()