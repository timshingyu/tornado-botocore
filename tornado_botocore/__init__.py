import logging

__version__ = '1.3.2'

try:
    from .base import Botocore
except ImportError:
    logging.warning('It looks like some requirements are missing. Debug')


__all__ = ('Botocore',)
