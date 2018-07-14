#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 tmurata <tmurata@ubuntu>
#
# Distributed under terms of the MIT license.

"""
JSON to YAML
"""

import yaml
import json
import sys

sys.stdout.write(yaml.dump(json.load(sys.stdin)))
