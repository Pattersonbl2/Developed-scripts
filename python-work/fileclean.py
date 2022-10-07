from importlib.resources import path
from itertools import count
from pathlib import Path
import os.path
import glob
import shutil 

def main (): 
      p = '/Users/bpatterson/Desktop/screenshots'
      dir_exist = os.path.isdir(p)
      if dir_exist == False:   
       create_folder() 
      else:
       move_file()

def create_folder(): 
    directory = "screenshots"
    parent_dir = "/Users/bpatterson/Desktop"
    path = os.path.join(parent_dir,directory)
    os.mkdir(path) 
    print("Directory '% s' created" %directory) 
    move_file()

def move_file():
    count = 0 
    src_dir = '/Users/bpatterson/Desktop'
    des_dir = '/Users/bpatterson/Desktop/screenshots'
    for fname in glob.glob(os.path.join(src_dir,"*.png")):
      file = shutil.move(fname,des_dir)
      count += 1 
      print("Moving files",file,count)

if __name__ == "__main__":
       main()