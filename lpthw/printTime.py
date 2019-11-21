# try another one
import time
import os
# os.environ['TZ'] = 'US/Central'
# time.tzset()
print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
