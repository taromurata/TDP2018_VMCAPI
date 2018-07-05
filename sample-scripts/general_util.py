#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 taro <taro@mba0.local>
#
# Distributed under terms of the MIT license.

"""

"""

import json
import yaml
import sys
import argparse

class GeneralUtil():
    @staticmethod
    def json2yaml(data):
        return yaml.dump(json.load(data))

    @staticmethod
    def yaml2json(data):
        return json.dumps(yaml.load(data))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', action='store', type=str)
    parser.add_argument('-t', '--type', action='store', type=str)

    args = parser.parse_args()

    if args.type == 'yaml':
        print(GeneralUtil.yaml2json(open(args.file, 'r+')))
    elif args.type == 'json':
        print(GeneralUtil.json2yaml(open(args.file, 'r+')))
    else:
        sys.exit('Unknown type, it must be either "yaml" or "json"')


