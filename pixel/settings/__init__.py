from .base import *

try:
    from .local import *
except ImportError:
    print("you should fix local settings. you can find the content in local.py.skeleton")
