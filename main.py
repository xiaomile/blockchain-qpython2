#qpy:webapp:Hello Django
#qpy://127.0.0.1:8000/

import os,sys
mf = os.path.dirname(__file__)+'/manage.py'

os.system(sys.executable+" "+mf+' runserver')
