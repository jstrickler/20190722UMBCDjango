#!/usr/bin/env python

import re
import os

# r'^herodetails/(?P<hero_name>.*)'

pattern = """r'^(.*?)/\(?P<(.*?)>"""


pattern = """path\("""

for curr_dir, subs, files in os.walk('.'):
    for file_name in files:
        if file_name == 'urls.py':
            file_path = os.path.join(curr_dir, file_name)
            print(file_path)
            with open(file_path) as file_in:
                for line in file_in:
                    m = re.search(pattern, line)
                    if m:
                        print(m.group(0)) # , m.group(2))
                        
