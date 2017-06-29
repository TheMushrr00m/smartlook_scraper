#! -*- coding: utf-8 -*-

"""
Cookie handling module.
"""

import logging
import os
import ssl

import requests
from requests.adapters import HTTPAdapter

try:
    from requests.packages.urllib3.poolmanager import PoolManager
except ImportError:
    from urllib3.poolmanager import PoolManager


from six.moves import StringIO
from six.moves import http_cookiejar as cookielib
