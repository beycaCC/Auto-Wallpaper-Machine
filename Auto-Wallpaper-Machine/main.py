import os
import re
import sys
import time
import random
import subprocess
import ctypes

import getpass
USER_NAME = getpass.getuser()



class AutoWallpaperMachine:
    def __init__(self):
        pass

    def change_wallpaper(self):
        # grab the wallpaper filenames from the current directory
        wallpaper_list = [file for file in os.listdir(os.path.dirname(__file__)) if re.search(".py$", file) == None]
        print(wallpaper_list)

        # set wallpaper
        for wallpaper_filename in wallpaper_list:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(os.path.dirname(__file__), wallpaper_filename) , 0)

            change_time = random.randint(2, 10)
            print(f"Wallpaper changed to {wallpaper_filename}, sleeping for {change_time} seconds...")
            time.sleep(change_time)


    # def add_to_startup(file_path=""):
    #     if file_path == "":
    #         file_path = os.path.dirname(os.path.realpath(__file__))
    #     bat_path = f'C:\Users\{USER_NAME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
    #     with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
    #         bat_file.write(r'start "" "%s"' % file_path)


if __name__ == "__main__":
    awm = AutoWallpaperMachine()
    awm.change_wallpaper()


