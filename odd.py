from datetime import datetime

odds=[1,3,5,7,9,11,13,15,17]

right_this_minute=datetime.today().minute
print(right_this_minute)
if right_this_minute in odds:
  print("This minute seems odd")
else:
  print("Not an odd minute") 
import sys
print("Platform="+sys.platform)
import time
print("Time="+time.strftime("%H:%M"))
#import html
#print("html"+html.unescape("I &hearts; Python's &lt; Standard Lib &gt;"))

