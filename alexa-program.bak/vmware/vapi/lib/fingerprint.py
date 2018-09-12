"""
Fingerprint related functions
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import hashlib
import six


def generate_fingerprint(data):
    """
    Generate fingerprint for the given data

    :rtype: :class:`str`
    :return: fingerprint of the given data
    """
    if six.PY3:
        if isinstance(data, six.string_types):
            data = data.encode('utf-8')
    return hashlib.md5(data).hexdigest()
