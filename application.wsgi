#!/usr/bin/python

import os, sys

PROJECT_DIR = '/var/www/html/helloflask/'

activate_this = os.path.join(PROJECT_DIR, 'env/bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from helloflask import app as application
