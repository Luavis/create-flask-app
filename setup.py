#!/usr/bin/env python
import create_flask_app
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

def install():

    setup(
        name='create-flask-app',
        version=create_flask_app.__version__,
        description='Create flask web apps with directory layout',
        long_description=readme,
        author=create_flask_app.__author__,
        author_email='me@luav.is',
        license='MIT',
        platforms=['POSIX'],
        url='https://github.com/Luavis/create-flask-app',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Environment :: Console',
            'Operating System :: POSIX',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',],
        entry_points={'console_scripts': [
            'create-flask-app = create_flask_app:main',
        ]},
        packages=find_packages(exclude=('create_flask_app.template', )),
        include_package_data=True,
        install_requires=[
            'virtualenv==15.1.0',
        ],
    )

if __name__ == "__main__":
    install()
