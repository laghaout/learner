# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 11:06:21 2024

@author: amine
"""

import os
from dotenv import dotenv_values
import json
import logging
import pandas as pd
import sys
from types import SimpleNamespace

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def read_csv(directory, file, **kwargs):

    match file.split('.')[-1].lower():
        case 'csv':
            data = pd.read_csv(os.path.join(directory, file))
        case _:
            assert False, f'Invalid file {file}'

    return data


def disp(text=None, log=False):

    if log:
        logging.info(text)
    else:
        print(text)


def load_json_as_dict(file_path):
    assert os.path.isfile(file_path)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        disp(f"Directory '{directory}' created.")
    else:
        disp(f"Directory '{directory}' already exists.")


def get_env_variables(env_file='.env'):
    envars = dotenv_values(env_file)
    envars = SimpleNamespace(**envars)
    return envars
