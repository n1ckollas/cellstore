from .base import *

try:
	from .local import *
except Exception as e:
	print e

# try:
# 	from .production import *
# except Exception as e:
# 	print e
