import sqlite3
import sys
import os.path
from pprint import pprint


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
k = []
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
'''
c.execute('CREATE TABLE {tn} ({nf} {ft_id},{nf1} {ft},{nf2} {ft_id})'\
        .format(tn=table_name1, nf=Terms_id_column, nf1=term_name_column, nf2=Terms_bio_column ,ft=field_type, ft_id=field_type_id))

c.execute('CREATE TABLE {tn} ({nf} {ft_id} PRIMARY KEY,{nf1} {ft},{nf2} {ft},{nf3} {ft} DEFAULT "{df}")'\
        .format(tn=table_name2, nf=Bionums_id_column, nf1=Bionums_name_column, nf2=Bionums_user_column ,ft=field_type, nf3 = Bionums_desc_column,ft_id=field_type_id, df = default_val))


'''
i = 0
while i< 695:
	c.execute("INSERT INTO {tn} ('term_id','term_name','bionum_ids')VALUES ({id_s}, '{term}', {numm});".\
	format(tn=table_name1, id_s =5, term='microbial', numm=i ))
	i+=1
'''

c.execute('SELECT DISTINCT term_name FROM Terms;')
d = c.fetchall()
s=[]
for it in d:
	s.append(it[0].encode("utf-8"))
print(s)
'''

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()