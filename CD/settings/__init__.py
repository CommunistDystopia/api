import os

if os.environ.get("ENVIROMENT") == "production":
    from .production import *
else:
    from .local import *
