from __future__ import absolute_import
from ConfigParser import SafeConfigParser

#Defaults
config = SafeConfigParser()
config.read('config.ini')

#Variables
var1 = config.get('config_settings','var1')
var2 = config.get('config_settings' ,'var2')
var3 = config.get('config_settings', 'var3')

