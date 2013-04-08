'''
    generate_template.py

    generate template from template file cache 
    to start new app or project

    kyle roux
'''
import sys
from run_command import make_file


def make_new_from_template(name):
    TEMPLATE='/Users/kyleroux/Library/Templates/template_main.py'

    #if len(sys.argv) > 1:
    #    FILE_NAME = str(sys.argv[1])
    #else:
    #    FILE_NAME = str(raw_input("Name of file: "))
    FILE_NAME = name
    template = open(TEMPLATE, 'r')
    newFile = open(FILE_NAME, 'w')
    tmpFile = ''

    for line in template:
        tmpFile = tmpFile + line

    template.close()
    newFile.writelines(tmpFile)
    newFile.close
    print 'made {0}'.format(FILE_NAME)


def make_init_py():
    FILE_NAME = '__init__.py'
    make_file(FILE_NAME)


def test():
    make_init_py()

if __name__ == "__main__":
    test()
