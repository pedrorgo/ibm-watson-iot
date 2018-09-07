#!/usr/bin/env python
# coding: utf-8
# References:
# https://opensource.org/licenses

#https://askubuntu.com/questions/762354/where-can-ubuntu-snaps-write-data
#https://docs.python.org/2/howto/argparse.html
#https://wiki.python.org/moin/ConfigParserExamples

import os
import sys
import argparse
import ConfigParser

__version__ = '0.1.1'


def quit(s, code=0):
    if s is not None:
        print(s)
    sys.exit(code)


def print_help():
    help = """
Usage: ibm-watson-iot <test string>
"""[1:-1]
    print(help)

def getSnapPath():
    return os.getenv('SNAP_USER_DATA', os.getenv('HOME'))

def createConfigFile():
    Config = ConfigParser.ConfigParser()
    cfgfile = open(getSnapPath() + "/.watson.iot.ini",'w')

    Config.add_section('Connection')
    Config.set('Connection','host',"https://server")
    Config.set ('Connection','port', 1575)
    Config.write(cfgfile)
    cfgfile.close()
    print "Configuration file created"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--init", help="Initializes config file", action="store_true")
    args = parser.parse_args()
    if args.init:
        createConfigFile()
        quit(None,0)

    print("Python IBM Watson IoT ")

if __name__ == '__main__':
    main()
