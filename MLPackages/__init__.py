import os
import sys
path1 = os.getcwd()
path2 = os.path.dirname(path1)
path3 = os.path.dirname(path2)
sys.path.append(path2)

from MLPackages.config import config

# def if_working():
#     word = print("Working well without import errors")
#     return word

# if __name__ == '__main__':
#     if_working()

with open(os.path.join(config.ROOT_PACKAGES, 'VERSION'), 'r') as f:
    __version__ = f.read().strip()


# with open(os.path.join(config.ROOT_PACKAGES)) as f:
#     __version__ = f.read().strip()


# While importing the MLPackages, if used the command 'MLPackages.__version__', it'll display the version of the package
# That's stored in the VERSION file
