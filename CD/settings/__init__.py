import os

if os.getenv("ENVIROMENT") == "production":
    from .production import *
else:
    from .local import *
