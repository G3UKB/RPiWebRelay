#!/usr/bin/env python
#
# webrelay_min.py
#
# Web application for control of relay modules from minimal auto client
# 
# Copyright (C) 2019 by G3UKB Bob Cowdery
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#    
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#    
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#    
#  The author can be reached by email at:   
#     bob@bobcowdery.plus.com
#

# System imports
import os, sys
import json

# Library imports
import cherrypy

# Application imports
import webrelay_gpio

#=====================================================
# The main application class
#===================================================== 
class WebRelayMin(object):
    
    def __init__(self, name):
        self.__name = name
        
    @cherrypy.expose
    def index(self):
        return "%s - Minimal Web Application" % (self.__name)

    @cherrypy.expose
    def set_channel(self, relay='1', state='off'):
        print("Setting chsnnel %s to state %s." % (relay, state))
        GPIO.set_relay(int(relay), state)
        return 'Channel set!'

#==============================================================================================
# Main code
#==============================================================================================
# Entry point
if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print("Please provide a configuration file path!")
    else:
        conf_path = sys.argv[1]
        if os.path.isfile(conf_path):
            try:
                with open(conf_path) as json_data_file:
                    app_conf = json.load(json_data_file)
            except:
                print("Unable to load Json configuration file!")
                sys.exit()
            
            name = app_conf["name"]    
            num_relays = app_conf["num_relays"]
            pin_map = app_conf["pin_map"]
            ch_map_on = None
            if "ch_map_on" in app_conf:
                ch_map_on = app_conf["ch_map_on"]
            ch_map_off = None
            if "ch_map_off" in app_conf:
                ch_map_off = app_conf["ch_map_off"]
            inverse = app_conf["inverse"]
            
            # Create web relay instance
            GPIO = webrelay_gpio.GPIOControl(num_relays, pin_map, ch_map_on, ch_map_off, inverse)
            
            # Get configuration file
            cherrypy_conf = os.path.join(os.path.dirname(__file__), 'cherrypy_min.conf')
            # Start
            cherrypy.quickstart(WebRelayMin(name), config=cherrypy_conf)
        else:
            print("Configuration file not found!")
    