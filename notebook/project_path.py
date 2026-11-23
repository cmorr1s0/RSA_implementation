# This code was copied from Gerges on StackOverflow

import sys
import os

module_path = os.path.abspath(os.path.join(os.path.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)