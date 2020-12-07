from .sql import *
import sqlite3


class ParPipeline:
	conn = sqlite3.connect('names.db')
	cursor = conn.cursor()
	name_counter = 1
	places, professions, languages, parties = [[], [], [], []]

	def open_spider(self, spider):

		self.cursor.execute('DROP TABLE names;')
		self.cursor.execute('DROP TABLE places;')
		self.cursor.execute('DROP TABLE professions;')
		self.cursor.execute('DROP TABLE languages;')
		self.cursor.execute('DROP TABLE parties;')
		self.cursor.execute('DROP TABLE profession_to_name;')
		self.cursor.execute('DROP TABLE language_to_name;')
		self.cursor.execute('DROP TABLE parties_to_name;')
		self.conn.commit()

	def process_item(self, item, spider):

		self.cursor.execute(sql_main_table)
		self.cursor.execute(sql_place_table)
		self.cursor.execute(sql_profession_table)
		self.cursor.execute(sql_language_table)
		self.cursor.execute(sql_party_table)
		self.cursor.execute(sql_prof_to_name_table)
		self.cursor.execute(sql_lang_to_name_table)
		self.cursor.execute(sql_party_to_name_table)

		name = item['name'][0]
		date = item['date'][0]
		place = item['place'][0].split(',')
		profs = item['prof'][0].split(';')
		langs = item['lang'][0].split(';')
		parties = item['party'][0].split(', ')
		email = item['email'][0]

		print(place)

		self.cursor.execute(f"""insert into places
		(town, country) 
		values (?, ?)""", (place[0], place[1].strip()))
		if place not in self.places:
			self.places.append(place)

		for prof in profs:
			if prof == '':
				prof = 'w'
			if prof not in self.professions:
				self.cursor.execute(f"""insert into professions (profession) values ('{prof}')""")
				self.professions.append(prof)
			self.cursor.execute(f"""insert into profession_to_name 
			values ({self.name_counter}, (select distinct id from professions where profession = '{prof}'))""")

		for lang in langs:
			if lang == '':
				lang = 'w'

			if lang not in self.languages:
				self.cursor.execute(f"""insert into languages (language) values ('{lang}')""")
				self.languages.append(lang)
			self.cursor.execute(f"""insert into language_to_name 
			values ({self.name_counter}, (select distinct id from languages where language = '{lang}'))""")

		for party in parties:
			if party not in self.parties:
				self.cursor.execute(f"""insert into parties (party) values ('{party}')""")
				self.parties.append(party)
			self.cursor.execute(f"""insert into parties_to_name 
			values ({self.name_counter}, (select distinct id from parties where party = '{party}'))""")

		self.cursor.execute(f"""insert into names 
		(name, date, place_id, email) 
		values ('{name}', '{date}', (select distinct id from places where town = '{place[0]}'), '{email}')""")
		self.conn.commit()

		self.name_counter += 1
		return item

	def close_spider(self, spider):
		self.cursor.close()
		self.conn.close()
