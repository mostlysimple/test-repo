"""Module providing Function printing python version."""

# import math
# import os
import sys

import requests




#print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    """Function to greet."""
    greeting = f"{'Hello,'} {who_to_greet}"
    return greeting

r = requests.get('https://coreyms.com', timeout = 10)

print(r.status_code)
print(greet('Johnny'))
