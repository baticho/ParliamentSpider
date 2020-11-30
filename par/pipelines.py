# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ParPipeline:
	conn = sqlite3.connect('names.db')
	cursor = conn.cursor()

	def open_spider(self, spider):
		pass
		#self.cursor.execute('''delete from names''')
		#self.conn.commit()
	def process_item(self, item, spider):

		self.cursor.execute('''create table if not exists "names" (
			name text,
			date DATE,
			place text,
			prof text,
			lang text,
			party text,
			email text
			) ''')

		name = item['name'][0]
		date = item['date'][0]
		place = item['place'][0]
		prof = item['prof'][0]
		lang = item['lang'][0]
		party = item['party'][0]
		email = item['email'][0]

		self.cursor.execute(f"""insert into names (name, date, place, prof, lang, party, email) values (?, ?, ?, ?, ?, ?, ?)""", (name, date, place, prof, lang, party, email))
		self.conn.commit()

		return item

	def close_spider(self, spider):
		self.cursor.close()
		self.conn.close()