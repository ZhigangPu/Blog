#! encoding=utf8

import os
from blog import create_app
from dotenv import load_dotenv

path = os.path.join(os.path.dirname(__file__)  + '.env')
if os.path.exists(path):
    load_dotenv(path)

app = create_app('development')

