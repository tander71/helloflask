#!/Users/Tander/Documents/Development/helloflask/bin/python

import os, sys

PROJECT_DIR = '/Library/WebServer/Documents/helloflask'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from helloflask import app as application
