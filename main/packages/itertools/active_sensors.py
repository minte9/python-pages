""" Active sensors (compress example)
    We want to process or display only active sensors.
    It easier to handle and process only the relevant data.
"""

from itertools import compress
from icecream import ic

# Sample data from sensor readings
sensors = [
    {'sensor_id': 101, 'reading': 75.2, 'active': True},
    {'sensor_id': 102, 'reading': 76.5, 'active': False},
    {'sensor_id': 103, 'reading': 74.8, 'active': True},
    {'sensor_id': 104, 'reading': 78.1, 'active': False},
    {'sensor_id': 105, 'reading': 75.9, 'active': True}
]

# Extract active status
active_status = [s['active'] for s in sensors]

# Use compress to filter active sensors
active_sensors = compress(sensors, active_status)

# Output 
ic("Active sensors:", list(active_sensors))

"""
    [{'active': True, 'reading': 75.2, 'sensor_id': 101},
    {'active': True, 'reading': 74.8, 'sensor_id': 103},
    {'active': True, 'reading': 75.9, 'sensor_id': 105}]
"""
