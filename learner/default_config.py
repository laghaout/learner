# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 08:39:41 2024

@author: amine
"""

import json
import os

JSON_FILE = ('..', 'default_config.json')

default_config = dict(
     wrangler=dict(
         nrows=1981,
         save_to="lesson"),
     learner=dict(
         save_to=("lesson", "more")))

with open(os.path.join(*JSON_FILE), 'w') as f:
    json.dump(default_config, f)