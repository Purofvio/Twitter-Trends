__author__ = 'Purofvio'

import ConfigParser


config = ConfigParser.RawConfigParser()
config.read('settings.cfg')

connection_string = config.get('TwitterDB','connection_string')