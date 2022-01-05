#!/usr/bin/python

import os
import sys
import codecs
import json

if __name__ == "__main__":
    prediction_file = sys.argv[1]
    gold_file = sys.argv[2]
    temp_file = "tmp"
    os.system('python2 m2scorer.py %s %s > %s' % (prediction_file, gold_file, temp_file))

    dict_result = dict()
    with codecs.open(temp_file,'r','utf8') as df:
        for line in df:
            if len(line.strip()) == 0:
                continue
            l = line.strip().split(':')
            dict_result[l[0].strip()] = float(l[1].strip())
    os.remove(temp_file)
    js = json.dumps(dict_result, indent=4)
    print(js)