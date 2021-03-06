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
    
    def __init__(self, num_relays, pin_map, aux_map, inverse):
        
        self.__num_relays = num_relays
        self.__pin_map = pin_map
        self.__aux_map = aux_map
        self.__inverse = inverse
        
        self.__ch_on = []
        
        if not testing:
            # Set to use actual port numbering rather than pin numbering
            GPIO.setmode(GPIO.BCM)
            # Set all to output and state off (note inverted logic) as we are driving relays
            for channel in range(0,num_relays):
                # We can have a number of relay sets to activate for one channel
                for pin_set in pin_map:
                    self.__set_pin(pin_set, channel, inverse)
            # See if we have any additional relays
            if self.__aux_map != None:
                for pin in self.__aux_map[1]:
                    GPIO.setup(pin, GPIO.OUT)
                    if inverse:
                        GPIO.output(pin, GPIO.HIGH)
                    else:
                        GPIO.output(pin, GPIO.LOW)
                            
    #-------------------------------------------------
    # Set the pin mode
    def __set_pin(self, a_map, channel, inverse):
        pin = self.__pin_for_ch(a_map, channel)
        if pin != None:
            GPIO.setup(pin, GPIO.OUT)
            if inverse:
                GPIO.output(pin, GPIO.HIGH)
            else:
                GPIO.output(pin, GPIO.LOW)
                            
    #==============================================================================================
    # PUBLIC
    #==============================================================================================
    
    #-------------------------------------------------
    # Set the channel to the given state
    def set_channel(self, channel, state):
        
        # Set relays for channel
        self.__ch_on.clear()
        for pin_set in self.__pin_map:
            pin = self.__pin_for_ch(pin_set, channel)
            if pin != None:
                if testing:
                    print("Setting pin %d to state %s" % (pin, state))
                    if state == 'on':
                        self.__ch_on.append(channel+1)
                else:
                    if state == 'on':
                        self.__ch_on.append(channel+1)
                        if self.__inverse:
                            GPIO.output(pin, GPIO.LOW)
                        else:
                            GPIO.output(pin, GPIO.HIGH)
                    else:
                        if self.__inverse:
                            GPIO.output(pin, GPIO.HIGH)
                        else:
                            GPIO.output(pin, GPIO.LOW)
        # Process additional relays
        self.__postcal()
    
    #-------------------------------------------------
    # Cleanup else next invocation will fail.
    def cleanup(self):
        if not testing:
            GPIO.cleanup() # cleanup all GPIO
        
    
    #==============================================================================================
    # PRIVATE
    #==============================================================================================
    
    #-------------------------------------------------
    # Return a GPIO pin for a channel number in the given set
    def __pin_for_ch(self, a_map, channel):
        return a_map[channel]
    
    #-------------------------------------------------
    # Channels post proc                       
    def __postcal(self):
        
        # See if we have any additional relays
        if self.__aux_map != None:
            if len(list(set(self.__aux_map[0]).intersection(self.__ch_on))) > 0:
                # At least one channel requires the relays to be on
                for relay in self.__aux_map[1]:
                    if testing:
                        print("Setting pin %d to state %s" % (relay, 'on'))
                    else:
                        if self.__inverse:
                            GPIO.output(relay, GPIO.LOW)
                        else:
                            GPIO.output(relay, GPIO.HIGH)
            else:
                # Otherwise turn the relays off
                for relay in self.__aux_map[1]:
                    if testing:
                        print("Setting pin %d to state %s" % (relay, 'off'))
                    else:
                        if self.__inverse:
                            GPIO.output(relay, GPIO.HIGH)
                        else:
                            GPIO.output(relay, GPIO.LOW)