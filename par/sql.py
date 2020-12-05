sql_main_table = '''create table if not exists "names" (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name text,
date DATE,
place_id int,
email text)'''

sql_place_table = '''create table if not exists places (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
town text,
country)
'''

sql_profession_table = '''create table if not exists professions (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
profession text)
'''

sql_language_table = '''create table if not exists languages (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
language text)
'''

sql_party_table = '''create table if not exists parties (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
party text)
'''

sql_prof_to_name_table = '''create table if not exists profession_to_name (
name_id int NOT NULL,
prof_id int NOT NULL)
'''

sql_lang_to_name_table = '''create table if not exists language_to_name (
name_id int NOT NULL,
lang_id int NOT NULL)
'''

sql_party_to_name_table = '''create table if not exists parties_to_name (
name_id int NOT NULL,
party_id int NOT NULL)
'''
