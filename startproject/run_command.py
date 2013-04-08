'''
    init_git.py
'''
import os


def make_dir(dirName):
    os.mkdir(dirName)

def run_command(cmd):
    os.system(cmd)

def make_file(name):
    cmd = 'touch '
    fileName = name
    run_command(cmd + fileName)
