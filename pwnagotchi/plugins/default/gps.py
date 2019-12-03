__author__ = 'forrest'
__version__ = '1.0.0'
__name__ = 'gps'
__license__ = 'GPL3'
__description__ = 'Save GPS coordinates whenever a handshake is captured.'

import logging
import json
import os

RUNNING = False
OPTIONS = dict()

def on_loaded():
    logging.info("%s plugin loaded" % __name__)

def on_ready(agent):
    global RUNNING
    global OPTIONS

    logging.info("enabling gps bettercap's module for %s:%d" % (OPTIONS['gpsdHost'], OPTIONS['gpsdPort']))
    try:
        agent.run('gps off')
    except:
        pass

    agent.run('set gps.gpsdHost %s' % OPTIONS['gpsdHost'])
    agent.run('set gps.gpsdPort %d' % OPTIONS['gpsdPort'])
    agent.run('gps on')
    RUNNING = True

def on_handshake(agent, filename, access_point, client_station):
    global RUNNING

    if RUNNING:
        info = agent.session()
        gps = info['gps']
        gps_filename = filename.replace('.pcap', '.gps.json')

        logging.info("saving GPS to %s (%s)" % (gps_filename, gps))
        with open(gps_filename, 'w+t') as fp:
            json.dump(gps, fp)
