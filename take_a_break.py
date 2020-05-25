# define a function in which the time duration for break will be of 15 mins every 2 hours 3 times

# wait for 2 hours
# open browser
# 3 times

import webbrowser
import time
break_count = 0
total_break = 3
print(time.ctime())
print("The program started on"+time.ctime())
while break_count < total_break:
    time.sleep(10)  #we can add up 2*60*60 for duration 2 hours as the .sleep takes params in sec
    webbrowser.open("https://www.youtube.com/watch?v=NSbOtYzIQI0")
    break_count = break_count + 1


