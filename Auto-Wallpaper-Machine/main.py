import os
import re
import sys
import time
import random
import subprocess
import ctypes
# ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(os.path.dirname(__file__), "wallpaper1.jpg") , 0)

# grab the wallpaper filenames from the current directory
wallpaper_list = [file for file in os.listdir(os.path.dirname(__file__)) if re.search(".py$", file) == None]

# set wallpaper
for wallpaper_filename in wallpaper_list:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(os.path.dirname(__file__), wallpaper_filename) , 0)

    change_time = random.randint(2, 10)
    print(f"Wallpaper changed to {wallpaper_filename}, sleeping for {change_time} seconds...")
    time.sleep(change_time)




# subprocess.run("ping google.com")
# set_wallpaper(os.path.join(os.path.dirname(__file__), "wallpaper1.jpg"))