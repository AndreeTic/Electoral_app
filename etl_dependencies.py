# etl_dependencies.py

import pandas as pd
import numpy as np
import requests
from datetime import datetime
import re

import openpyxl
import xlrd

from sqlalchemy import create_engine
import pymysql
import psycopg2
import pyarrow
import fastparquet
