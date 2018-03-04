import sys
import os.path
import json
from pprint import pprint
from django.utils.encoding import smart_str, smart_unicode
import sqlite3

models_list = []
i = 0
while i<696:
	models_list.append("ex"+str(i)+".json")
	i+=1

terms_dict = {}
param_dict = {}

for mod in models_list:
	data = json.load(open(mod))
	param_dict[data["index"]] = [data["name"].encode('ascii','ignore'),data["notes"].encode('ascii','ignore')]





	for ter in data["tags"]:
		try:
			terms_dict[ter].append(data["index"])
		except:
			ter = ter.encode('ascii','ignore')
			terms_dict[ter] = [data["index"]]





#print(terms_dict)
#pprint(terms_dict.keys())

sqlite_file = 'my_first_db1.sqlite'    # name of the sqlite database file
table_name1 = 'Terms'  # name of the table to be created
table_name2 = 'Bionums'  # name of the table to be created
Terms_id_column = 'term_id' # name of the column
term_name_column = 'term_name'
Terms_bio_column = 'bionum_ids'
field_type_id = 'INTEGER'
field_type = 'TEXT'

Bionums_id_column = 'bionum_id' # name of the column
Bionums_name_column = 'bionum_name'
Bionums_user_column = 'user'
Bionums_desc_column = 'description'

default_val = 'NULL'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

"""
Insert terms and corresponding nums
"""

i = 0
'''
for key in param_dict.keys():
	c.execute("INSERT INTO {tn} ('bionum_id','bionum_name','user','description') VALUES ({id}, '{term}', 'danikstarik','{descr}');".\
		format(tn=table_name2, id=key, term=param_dict[key][0], descr=param_dict[key][1]))
'''
for key in terms_dict.keys():
	print(key)
	for num in terms_dict[key]:
		c.execute("INSERT INTO {tn} ('term_id','term_name','bionum_ids') VALUES ({id}, '{term}', {numm});".\
			format(tn=table_name1, id=i, term=str(key).replace("'",""), numm=num))
	i+=1


conn.commit()
conn.close()
