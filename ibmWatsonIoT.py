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
import ibmiotf.device

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

    #Config.add_section('Connection')
    #Config.set('Connection','host',"https://server")
    #Config.set ('Connection','port', 1575)
    Config.add_section('device')
    Config.set('device','org','org1id')
    Config.set('device','type','rpi-3')
    Config.set('device','id','00ef08ac05')
    Config.set('device','auth-method','token')
    Config.set('device','auth-token','00ef08ac05')
    Config.set('device','clean-session','true')
    Config.set('device','domain','internetofthings.ibmcloud.com')
    Config.set('device','port',8883)

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

    try:
        options = ibmiotf.device.ParseConfigFile(getSnapPath() + "/.watson.iot.ini")
        client = ibmiotf.device.Client(options)
    except ibmiotf.ConnectionException  as e:
            pass

    #client.connect()
    #qos=0
    #myData={'name' : 'foo', 'cpu' : 60, 'mem' : 50}
    #client.publishEvent("status", "json", myData, qos)



if __name__ == '__main__':
    main()
