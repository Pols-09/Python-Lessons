import time
import webbrowser

total_breaks = 2
break_count = 0

print("this program started on "+time.ctime())
while(break_count < total_breaks):
     time.sleep(5)
     webbrowser.open("https://soundcloud.com/you/likes")
     break_count = break_count + 1

