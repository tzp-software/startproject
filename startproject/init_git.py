'''
    init_git.py
'''
from commands import GIT_INIT, GIT_ADD
from run_command import run_command


def init_git():
    run_command(GIT_INIT)

def add_all():
    runn_command(GIT_ADD)

if __name__ == "__main__":
    init_git()

