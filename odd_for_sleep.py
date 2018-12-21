from datetime import datetime
import time

odds=[1,3,5,7,9,11,13,15,17]

for i in range(5):
    right_this_minute=datetime.today().minute
    time.sleep(5)
    print(right_this_minute)
    if right_this_minute in odds:
      print("This minute seems odd")
    else:
      print("Not an odd minute") 
