import sys
import os.path
from libsbml import *
from bioservices import BioModels
from django.utils.encoding import smart_str, smart_unicode

s = BioModels()
li =[]
al = s.getAllCuratedModelsId()
for m in s.getModelsIdByName('flu'):
	if m in al:
		li.append(m)
print(li)
'''
for it in li:
	mo_str = smart_str(s.getModelSBMLById(it))
	f=open(str(it)+'.xml','w')
	f.write(mo_str)
	f.close()

'''

