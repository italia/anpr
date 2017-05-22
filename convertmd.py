#!/usr/bin/env python
import os
import subprocess

DOCUMENTATION_SOURCE_DIR = 'documentation/source/'

DOCUMENTATION_SOURCE_DIR = 'src/'

SOURCE_EXTENSION = '.md'
OUTPUT_EXTENSION = '.rst'

for _, __, filenames in os.walk(DOCUMENTATION_SOURCE_DIR):
    for filename in filenames:
        if filename.endswith('.md'):
            filename_stem = filename.split('.')[0]
            source_file = DOCUMENTATION_SOURCE_DIR + filename_stem + SOURCE_EXTENSION
            output_file = DOCUMENTATION_SOURCE_DIR + filename_stem + OUTPUT_EXTENSION
            command = 'pandoc -s {0} -o {1}'.format(source_file, output_file)
            print(command)
            subprocess.call(command.split(' '))
