'''
    startproject.startproject.py

    def for make_project
'''
import os
from init_git import init_git
from run_command import make_dir, make_file
from generate_template import make_init_py, make_new_from_template

def make_project(name):
    make_dir(name)
    os.chdir(name)
    make_new_from_template(name)
    make_init_py()
    init_git()



