#!/usr/bin/env python
#
# webrelay_gpio.py
#
# Control of relay module GPIO ports
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

# Library imports
testing = False
try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    print("Error importing RPi.GPIO! Using test mode.")
    testing = True

# Application imports

#=====================================================
# The main GPIO class
#===================================================== 
class GPIOControl:
    
    def __init__(self, num_relays, pin_map):
        
        self.__num_relays = num_relays
        self.__pin_map = pin_map
        
        if not testing:
            # Set to use actual port numbering rather than pon numbering
            GPIO.setmode(GPIO.BCM)
            # Set all to output and state off (note inverted logic) as we are driving relays
            for relay in range(0,num_relays):
                pin = self.__pin_for_relay(pin_map, relay)
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, GPIO.HIGH)

    
    #==============================================================================================
    # PUBLIC
    #==============================================================================================
      
    #-------------------------------------------------
    # Set the relay to the given state
    def set_relay(self, relay, state):
        pin = self.__pin_for_relay(self.__pin_map, relay)
        if testing:
            print("Setting pin %d to state %s" % (pin, state))
        else:
            if state == 'on':
                GPIO.output(pin, GPIO.LOW)
            else:
                GPIO.output(pin, GPIO.HIGH)
    
    #==============================================================================================
    # PRIVATE
    #==============================================================================================
    
    #-------------------------------------------------
    # Return a GPIO pin for a relay number
    def __pin_for_relay(self, pin_map, relay):
        return pin_map[relay]