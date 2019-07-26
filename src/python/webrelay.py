#!/usr/bin/env python
#
# webrelay.py
#
# Web application for control of RPi relay boards
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
# The index HTML
import index
import webrelay_gpio
import webrelay_model

#=====================================================
# The main application class
#===================================================== 
class WebRelay:

    def __init__(self, name, model, num_relays):
        self.__name = name
        self.__model = model
        self.__num_relays = num_relays
        
    # Expose the index method through the web
    @cherrypy.expose
    def index(self):
        # CherryPy will call this method for the root URI ("/") and send
        # its return value to the client.
        return index.get_index(self.__name, self.__model, self.__num_relays)

#=====================================================
# The web service class
#=====================================================
@cherrypy.expose
class WebRelayWebService(object):
    
    def __init__(self, num_relays, pin_map, ch_map_on, ch_map_off, inverse):
        # Create web relay instance
        self.GPIO = webrelay_gpio.GPIOControl(num_relays, pin_map, ch_map_on, ch_map_off, inverse)
        
    @cherrypy.tools.accept(media='text/plain')
    #-------------------------------------------------
    # Called by a GET request
    def GET(self):
        return "GET called"

    #-------------------------------------------------
    # Called by a POST request
    def POST(self, data):
        return "POST called"
    
    #-------------------------------------------------
    # Called by a DELETE request
    def DELETE(self):
        return "DELETE called"

#=====================================================
# Cherrypy matches to the number of query parameters so we need to match the number of parameters
# to the number of relays activated.
class WebRelayWebService_1(WebRelayWebService):
    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_1):
        for relay in [[0,rly_1]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"

class WebRelayWebService_2(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_1, rly_2):
        for relay in [[0,rly_1],[1,rly_2]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"

class WebRelayWebService_3(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_1, rly_2, rly_3):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"
    
class WebRelayWebService_4(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_1, rly_2, rly_3, rly_4):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"

class WebRelayWebService_5(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_5_name, rly_1, rly_2, rly_3, rly_4, rly_5):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4],[4,rly_5],[5,rly_6],[6,rly_7],[7,rly_8]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name],[5,rly_5_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"

class WebRelayWebService_6(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_5_name, rly_6_name, rly_1, rly_2, rly_3, rly_4, rly_5, rly_6):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4],[4,rly_5],[5,rly_6]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name],[5,rly_5_name],[6,rly_6_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"
    
class WebRelayWebService_7(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_5_name, rly_6_name, rly_7_name, rly_1, rly_2, rly_3, rly_4, rly_5, rly_6, rly_7):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4],[4,rly_5],[5,rly_6],[6,rly_7],[7,rly_8]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name],[5,rly_5_name],[6,rly_6_name],[7,rly_7_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"
    
class WebRelayWebService_8(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_5_name, rly_6_name, rly_7_name, rly_8_name, rly_1, rly_2, rly_3, rly_4, rly_5, rly_6, rly_7, rly_8):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4],[4,rly_5],[5,rly_6],[6,rly_7],[7,rly_8]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name],[5,rly_5_name],[6,rly_6_name],[7,rly_7_name],[8,rly_8_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"
    
class WebRelayWebService_9(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_5_name, rly_6_name, rly_7_name, rly_8_name, rly_9_name, rly_1, rly_2, rly_3, rly_4, rly_5, rly_6, rly_7, rly_8):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4],[4,rly_5],[5,rly_6],[6,rly_7],[7,rly_8],[8,rly_9],[9,rly_10],[10,rly_11],[11,rly_12]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name],[5,rly_5_name],[6,rly_6_name],[7,rly_7_name],[8,rly_8_name],[9,rly_9_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"
    
class WebRelayWebService_10(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_5_name, rly_6_name, rly_7_name, rly_8_name, rly_9_name, rly_10_name, rly_1, rly_2, rly_3, rly_4, rly_5, rly_6, rly_7, rly_8, rly_9, rly_10):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4],[4,rly_5],[5,rly_6],[6,rly_7],[7,rly_8],[8,rly_9],[9,rly_10]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name],[5,rly_5_name],[6,rly_6_name],[7,rly_7_name],[8,rly_8_name],[9,rly_9_name],[10,rly_10_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"
    
class WebRelayWebService_11(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_5_name, rly_6_name, rly_7_name, rly_8_name, rly_9_name, rly_10_name, rly_11_name, rly_1, rly_2, rly_3, rly_4, rly_5, rly_6, rly_7, rly_8, rly_9, rly_10, rly_11):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4],[4,rly_5],[5,rly_6],[6,rly_7],[7,rly_8],[8,rly_9],[9,rly_10],[10,rly_11]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name],[5,rly_5_name],[6,rly_6_name],[7,rly_7_name],[8,rly_8_name],[9,rly_9_name],[10,rly_10_name],[11,rly_11_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"
    
class WebRelayWebService_12(WebRelayWebService):

    #-------------------------------------------------
    # Called by a PUT request
    def PUT(self, rly_1_name, rly_2_name, rly_3_name, rly_4_name, rly_5_name, rly_6_name, rly_7_name, rly_8_name, rly_9_name, rly_10_name, rly_11_name, rly_12_name, rly_1, rly_2, rly_3, rly_4, rly_5, rly_6, rly_7, rly_8, rly_9, rly_10, rly_11, rly_12):
        for relay in [[0,rly_1],[1,rly_2],[2,rly_3],[3,rly_4],[4,rly_5],[5,rly_6],[6,rly_7],[7,rly_8],[8,rly_9],[9,rly_10],[10,rly_11],[11,rly_12]]:
            self.GPIO.set_channel(relay[0], relay[1])
        for name in [[1,rly_1_name],[2,rly_2_name],[3,rly_3_name],[4,rly_4_name],[5,rly_5_name],[6,rly_6_name],[7,rly_7_name],[8,rly_8_name],[9,rly_9_name],[10,rly_10_name],[11,rly_11_name],[12,rly_12_name]]:
            model.update_model(name[0], name[1])
        model.save_model()
        return "Relays set!"
    
#==============================================================================================
# Main code
#==============================================================================================
# Entry point

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root.
    
    if len(sys.argv) == 1:
        print("Please provide a configuration file path!")
    else:
        conf_path = sys.argv[1]
        if os.path.isfile(conf_path):
            try:
                with open(conf_path) as json_data_file:
                    app_conf = json.load(json_data_file)
            except Exception as e:
                print("Unable to load Json configuration file! [%s]" % (str(e)))
                sys.exit()
            
            name = app_conf["name"]    
            num_relays = app_conf["num_relays"]
            pin_map = app_conf["pin_map"]
            ch_map_on = None
            if "ch_map_on" in app_conf):
                ch_map_on = app_conf["ch_map_on"]
            ch_map_off = None
            if "ch_map_off" in app_conf):
                ch_map_on = app_conf["ch_map_off"]
                
            inverse = app_conf["inverse"]
            
            # Create and restore the model
            model = webrelay_model.WebRelayModel(num_relays)
            model.restore_model()
            
            # Get configuration file
            cherrypy_conf = os.path.join(os.path.dirname(__file__), 'cherrypy.conf')
            # Create web app instances
            webapp = WebRelay(name, model, num_relays)
            webService = [WebRelayWebService_1, WebRelayWebService_2, WebRelayWebService_3, WebRelayWebService_4,
                          WebRelayWebService_5,WebRelayWebService_6,WebRelayWebService_7,WebRelayWebService_8,
                          WebRelayWebService_9,WebRelayWebService_10,WebRelayWebService_11,WebRelayWebService_12]
            webapp.webrelay_service = webService[num_relays-1](num_relays, pin_map, ch_map_on, ch_map_off, inverse)
        
            # Start
            cherrypy.quickstart(webapp, config=cherrypy_conf)
        else:
            print("Configuration file not found!")
    