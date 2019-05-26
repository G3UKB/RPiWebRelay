#!/usr/bin/env python
#
# webrelay_model.py
#
# Model for Web Relay application
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
import pickle

# Library imports

# Application imports

#=====================================================
# The main Model class
#===================================================== 
class WebRelayModel:
    
    model_path = "webrelay.model"
    def __init__(self, num_relays):
        
        self.__num_relays = num_relays
        self.__PATH = "webrelay.model"
        self.__model = None
    
    #==============================================================================================
    # PUBLIC
    #==============================================================================================
    
    #-------------------------------------------------
    # Restore current model
    def restore_model(self):
        self.__model = self.__restore_model()
        if self.__model == None:
            # Use default
            print("Model not found, using default!")
            self.__model = self.__get_dafault_model(self.__num_relays)
            self.__save_model()    
            
    #-------------------------------------------------
    # Save current model
    def save_model(self):
        self.__save_model()
    
    #-------------------------------------------------
    # Update current model
    def update_model(self, relay, name):
        self.__model[relay] = name
    
    #-------------------------------------------------
    # Get current model
    def get_model(self):
        return self.__model

    #==============================================================================================
    # PRIVATE
    #==============================================================================================
    
    #-------------------------------------------------
    # Default model
    def __get_dafault_model(self, num_relays):
        relay_map = {}
        for relay in range(1,num_relays+1):
           relay_map[relay] = ""
        return relay_map
    
    #-------------------------------------------------
    # Implementation of restore from disk
    def __restore_model(self):
        """
        Restore the saved model
        
        Arguments:
                
        """
        
        model = None
        if os.path.exists(self.__PATH):
            try:       
                f = open(self.__PATH, 'rb')
                model = pickle.load(f)
            except Exception as e:
                # Error retrieving model file
                print('Model File - Exception','Exception [%s]' % (str(e)))
            finally:
                try:
                    f.close()
                except:
                    pass
        return model

    #-------------------------------------------------
    # Implementation of save to disk
    def __save_model(self):
        """
        Save the model
        
        Arguments:

        """
        
        try:       
            f = open(self.__PATH, 'wb')
            pickle.dump(self.__model, f)
        except Exception as e:
            # Error saving model file
            print('Model File - Exception','Exception [%s]' % (str(e)))
        finally:
            try:
                f.close()
            except:
                pass

