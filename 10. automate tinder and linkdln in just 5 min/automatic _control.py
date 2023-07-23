# pip3 install pyautogui 
# this is usefull for the controlling screen

# steps:

# 1) open the app (tinder or linkdln)
# 2) placed the cursor in fix position eg placed cursor in like button 
# 3)open the terminal
# 4) type 
#          1)"import pyautogui"
#          2) pyautogui.position()  this function gives exact location on page in x y direction eg x=345 y=898
#          3)exit() and  remember the location of cursor 
# 5) create new file with .py extension 
# 6)type 

import pyautogui
import Time

for i in range(11):  #loop until 10 times
        pyautogui.click(x=971,y=748)   #put the location which we had remember in past code
        time.sleep(0.2)

# 7)save the code 
# 8)open terminal and run the File


 
