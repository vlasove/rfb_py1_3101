"""
Модуль, в котором я работаю
"""

from example_a import MAX_ATTEMPTS, add
import zap_logger_to_http_server as zap # Aliacing (местоимение)
from geometry.rectangle import perimeter
import geometry.circle as circle
import geometry

# from math import cos, pi
# from typing import List
# import math
# import typing

MAX_ATTEMPTS = 22 # Import collision

print("From example b:", MAX_ATTEMPTS)
print("Current max attempts:", MAX_ATTEMPTS)
print("Add(2,3):", add(2,3))
print("Config:", zap.ZAP_CONFIG)

print("Perimeter(2,3):", perimeter(2,3))
print("Circle area(10.5):", circle.area(10.5))