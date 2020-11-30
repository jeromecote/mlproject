# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.distance import haversine
import pytest

def test_haversine():
    lon1, lat1, lon2, lat2 = 48.865070, 2.380009, 45.52635057348148, -73.59503385974871
    assert haversine(lon1, lat1, lon2, lat2) == 8451.184264890737
