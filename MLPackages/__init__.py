import os
from MLPackages.config import config


with open(os.path.join(config.ROOT_PACKAGES, 'VERSION.txt'), 'r') as f:
    __version__ = f.read().strip()


# with open(os.path.join(config.ROOT_PACKAGES)) as f:
#     __version__ = f.read().strip()


# While importing the MLPackages, if used the command 'MLPackages.__version__', it'll display the version of the package
# That's stored in the VERSION file