# config.py

import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(name, default=None):
    """to handle the loading of environment variables. 
    This module will contain functions to fetch the required environment 
    variables for setting up the chain. 
    It will help keep the configuration logic separate from the main function.
    """
    return os.environ.get(name, default)
