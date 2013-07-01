'''
    startproject.main.py
'''
import os
import sys
import commands
from run_command import run_command, make_file, make_dir
from generate_template import make_init_py, make_new_from_template
from init_git import init_git
from startproject import make_project

def print_usage():
    USAGE = '''
    usage: startproject [-f <file>] [-d <dir>] [-n <newname>]

    -f, --file <file>   create new file from template
                        with name <file>

    -d, --dir <dir>     create new project dir with
                        name <dir>. the new dir will
                        contain a __init__.py file

    -n, --new <name>    create new python project
                        with dirname <name> and
                        filename <name> with an
                        __init__.py file

    -h, --help          print this help message


    by: kyle roux(jstacoder@gmail.com)
    '''
    print USAGE
    sys.exit(1)


def main():
    templateType = False

    if len(sys.argv) == 1:
        print_usage()
    else:
        arg = sys.argv[1]

    if arg == '-f' or arg == '--file':
        if len(sys.argv) >= 3:
            fileName = sys.argv[2]
            if len(sys.argv) >= 4:
                if sys.argv[3].lower() == '-t' or sys.argv[3] == '--template-type':
                    templateType = sys.argv[4]
        else:
            fileName = raw_input("Enter Filename: ")
        if templateType:
            make_new_from_template(fileName, templateType)
        else:
            make_new_from_template(fileName) # allow for second argument here for template type, optional
        #sys.exit(0)

    elif arg == '-d' or arg == '--dir':
        if len(sys.argv) >= 3:
            dirName = sys.argv[2]
        else:
            dirName = raw_input("Enter Dir name: ")
	try:
       	    make_dir(dirName)
            os.chdir(dirName)
            make_init_py()
            os.chdir('../')
            print 'made directory: {0}'.format(dirName)
        except:
	    print 'Im in {}'.format(commands.getoutput('pwd'))
	    os.rmdir(dirName)
	    sys.exit(0)

    elif arg == '-n' or arg == '--new':
        if len(sys.argv) < 3:
            print_usage()
        else:
            projectName = sys.argv[2]
            make_project(projectName)

    else:
        print_usage()

if __name__ == "__main__":
    main()
