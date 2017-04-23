#!/usr/bin/env python
import os
import sys
import shutil
import argparse
import virtualenv
from os import path, getcwd
from datetime import datetime

SRC_TEMPLATES_DIR = 'templates'
ERR_EXISTS = """The directory %s contains files that could conflict.
Try using a new directory name."""
CONVERT_TARGET = ['.py', '.rst']
CONVERT_FORMAT = '${{ %s }}'
TERM_COLOR_GREEN = '\033[92m'
TERM_COLOR_CYAN ='\033[36m'
TERM_COLOR_ENDC = '\033[0m'

class CreateApp():

    def __init__(self, src, dest, project):
        self.src = src
        self.dest = dest
        self.project = project

        if path.exists(self.dest):
            print(ERR_EXISTS % project)
            sys.exit(1)

        self.config = {
            'PROJECT_NAME': project,
            'AUTHOR': os.getlogin(),
            'LICENSE': 'MIT',
            'VERSION': '0.1.0',
            'SECRET_KEY': str(os.urandom(24)),
            'YEAR': str(datetime.now().year),
        }

    def create(self):
        print('Creating a new React app in %s' % self.dest)
        self.walkdir()
        self.create_venv()
        self.print_complete()

    def print_complete(self):
        help_table = {
            'python manager.py runserver':
            'Start the development server.',
            'python manager.py db init':
            'Initialize database and migrations with configuration.',
            'python manager.py db migrate':
            'Create migration with database changed.',
            'python manager.py db upgrade':
            'Change db structure with migrations.',
            'python manager.py db shell':
            'Run python REPL with flask application.',
        }

        command_helps = '\n'.join([
            ('{ws}{cyan}{command}{endc}\n' +
            '{ws}{ws}{description}\n').format(
                cyan=TERM_COLOR_CYAN,
                command=k,
                endc=TERM_COLOR_ENDC,
                description=help_table[k],
                ws='  '
            ) for k in help_table
        ])

        print(
            ('\n{green}Success!{endc} Created {project} at {dest}\n' +
            'First you have to install dependencies with virtualenv:\n\n' +
            '{cyan}${endc} cd {dest}\n' +
            '{cyan}${endc} cd ./venv/bin/activate\n' +
            '{cyan}${endc} pip install -r ./requirements.txt\n\n' +
            'Then you can run several commands:\n\n' +
            '{command_helps}\n' +
            'Happy hacking!!'
            ).format(
                project=self.project,
                dest=self.dest,
                cyan=TERM_COLOR_CYAN,
                green=TERM_COLOR_GREEN,
                endc=TERM_COLOR_ENDC,
                command_helps=command_helps
            )
        )

    def create_venv(self):
        if os.environ.get('WORKING_ENV'):
            print('ERROR: you cannot run virtualenv while in a workingenv')
            print('Please deactivate your workingenv, then re-run this script')
            sys.exit(3)

        if 'PYTHONHOME' in os.environ:
            print('PYTHONHOME is set.  You *must* activate the virtualenv before using it')
            del os.environ['PYTHONHOME']

        virtualenv.create_environment(path.join(self.dest, 'venv'))

    def convert_config(self, srcfile, dstfile):
        dst = open(dstfile, 'w')

        with open(srcfile, 'r') as f:
            content = f.read()
            for key in self.config.keys():
                content = content.replace(CONVERT_FORMAT % key, self.config[key])
            dst.write(content)

        dst.flush()
        dst.close()

    def walkfiles(self, srcroot, dstroot, files):
        if not os.path.exists(dstroot):
            os.makedirs(dstroot)

        for file in files:
            if file == '.keep':
                # Ignore keep file
                continue
            srcfile = path.join(srcroot, file)
            dstfile = path.join(dstroot, file)
            _, ext = path.splitext(dstfile)

            if ext in CONVERT_TARGET:
                self.convert_config(srcfile, dstfile)
            else:
                shutil.copy(srcfile, dstfile)

    def walkdir(self):
        for root, dirs, files in os.walk(self.src):
            # replace src path to dst
            dstroot = root.replace(self.src, self.dest, 1)
            self.walkfiles(root, dstroot, files)


def main():
    parser = argparse.ArgumentParser(description='create flask application')
    parser.add_argument('project', metavar='<project-directory>', type=str,
                        help='directory')

    args = parser.parse_args()
    src = path.join(path.dirname(path.abspath(__file__)), '..', SRC_TEMPLATES_DIR)
    src = path.abspath(src)
    dest = path.join(getcwd(), args.project)

    capp = CreateApp(src, dest, args.project)
    capp.create()


if __name__ == '__main__':
    main()
