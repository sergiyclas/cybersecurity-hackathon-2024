alghorithm = "1 line, 2 line, 5 line"

import heapq
import json
import os
from datetime import datetime
import xml.etree.ElementTree as ET
from typing import List, Dict
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from parsing import parser_data
from parse_xml import parse_sim

COUNT_HOURS = 2

CURRENT_TIME = datetime.now()
CURRENT_DAY = CURRENT_TIME.strftime('%Y-%m-%d')
CURRENT_HOUR = int(CURRENT_TIME.strftime('%H'))
print(CURRENT_DAY, CURRENT_HOUR)

file_path_current = os.path.join('data', 'current.json')
file_path_historical = os.path.join('data', 'historical.json')
file_path_predict_weather = os.path.join('data', 'predict_weather.json')
file_path_tth = os.path.join('data', 'tth.json')
file_path_sim = os.path.join('data', 'cim_model.xml')


needed_data_current = parser_data(file_path_current, COUNT_HOURS, CURRENT_HOUR, CURRENT_DAY)
needed_data_historical = parser_data(file_path_historical, COUNT_HOURS, CURRENT_HOUR, CURRENT_DAY)
needed_data_predict_weather = parser_data(file_path_predict_weather, COUNT_HOURS, CURRENT_HOUR, CURRENT_DAY)
needed_data_sim = parse_sim(file_path_sim)

print(needed_data_current)

