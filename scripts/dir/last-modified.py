import os
import datetime

def file_date(filename):
  
  fp = open(os.path.join(filename), 'w')
  fp.close()
  
  ts = os.stat(filename).st_mtime

  ts_str = str(datetime.datetime.fromtimestamp(ts))
  
  return ("{}".format(ts_str[:10])) 

print(file_date("newfile.txt")) 
