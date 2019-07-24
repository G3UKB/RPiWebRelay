#!/usr/bin/env python
#
# index.py
#
# The one and only HTML page
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

#==============================================================================================
# PUBLIC
#==============================================================================================
 
#-------------------------------------------------
# Main index HTML     
def get_index(name, model, num_relays):
    
    index_html = '''
    <html>
    <head>
        <link href="/static/css/webrelay.css" rel="stylesheet">
        <script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
        <script type="text/javascript">
          $(document).ready(function() {
            $("#relays_apply").click(function(e) {
              $.ajax({
                type: "PUT",
                url: "/webrelay_service",
                data: {
                        %s
                    }
              })
              .done(function(string) {
                $("#response").val(string);
              });
              e.preventDefault();
            });
          });
        </script>
    </head>
    <body>
        <div id="container">
            <div id="header"> %s </div>
            <div id="content"> %s </div>
            <div id="update"> %s </div>
            <div id="footer"> %s </div>
        </div>
    </body>
    </html>
    ''' % (get_data(num_relays), get_header(name), get_content(model, num_relays), get_update(), get_footer())
    return index_html

#==============================================================================================
# PRIVATE
#==============================================================================================

#-------------------------------------------------
# Data HTML
def get_data(num_relays):     

    data = ''
    for id in range(1, num_relays+1):
        data = data + "\'rly_%d_name\' : $(\'input[name=\'relay-%d-name\']\').val()" % (id,id)
        
    '''    
    if num_relays == 4:
        data = 
            "rly_1_name": $("input[name='relay-1-name']").val(),
            "rly_2_name": $("input[name='relay-2-name']").val(),
            "rly_3_name": $("input[name='relay-3-name']").val(),
            "rly_4_name": $("input[name='relay-4-name']").val(),
            "rly_1": $("input[name='relay-1']:checked").val(),
            "rly_2": $("input[name='relay-2']:checked").val(),
            "rly_3": $("input[name='relay-3']:checked").val(),
            "rly_4": $("input[name='relay-4']:checked").val(),
        
    else: 
        data = 
            "rly_1_name": $("input[name='relay-1-name']").val(),
            "rly_2_name": $("input[name='relay-2-name']").val(),
            "rly_3_name": $("input[name='relay-3-name']").val(),
            "rly_4_name": $("input[name='relay-4-name']").val(),
            "rly_5_name": $("input[name='relay-5-name']").val(),
            "rly_6_name": $("input[name='relay-6-name']").val(),
            "rly_7_name": $("input[name='relay-7-name']").val(),
            "rly_8_name": $("input[name='relay-8-name']").val(),
            "rly_1": $("input[name='relay-1']:checked").val(),
            "rly_2": $("input[name='relay-2']:checked").val(),
            "rly_3": $("input[name='relay-3']:checked").val(),
            "rly_4": $("input[name='relay-4']:checked").val(),
            "rly_5": $("input[name='relay-5']:checked").val(),
            "rly_6": $("input[name='relay-6']:checked").val(),
            "rly_7": $("input[name='relay-7']:checked").val(),
            "rly_8": $("input[name='relay-8']:checked").val()
        
    '''   
    return data
        
#-------------------------------------------------
# Header HTML
def get_header(name):     
    return "<h1>%s</h1>" % (name)

#-------------------------------------------------
# Content HTML
def get_content(model, num_relays):
    
    m = model.get_model()
    content = '''
    <table id=tmain>
        <tr>
            <th>Relay</th>
            <th id="name-col">Name</th>
            <th>Control</th>
        </tr>
    '''
    
    for id in range(1, num_relays+1):
        content = content + ''' <tr>
            <td>1</td>
            <td><input type="text" class="names" name="relay-%d-name" value={}></td>
            <td>
                <input type="radio" name="relay-%d" checked="false" value="on">On
                <input type="radio" name="relay-%d" checked="true" value="off">Off
            </td>
        </tr> ''' % (id, id, id)
        content.format(m[id].replace(" ", "&nbsp;"))
    content = content + "</table>"
    
    '''
    content = 
    <table id=tmain>
        <tr>
            <th>Relay</th>
            <th id="name-col">Name</th>
            <th>Control</th>
        </tr>
        <tr>
            <td>1</td>
            <td><input type="text" class="names" name="relay-1-name" value={}></td>
            <td>
                <input type="radio" name="relay-1" checked="false" value="on">On
                <input type="radio" name="relay-1" checked="true" value="off">Off
            </td>
        </tr>
        <tr>
            <td>2</td>
            <td><input type="text" class="names" name="relay-2-name" value={}></td>
            <td>
                <input type="radio" name="relay-2" checked="false" value="on">On
                <input type="radio" name="relay-2" checked="true" value="off">Off
            </td>
        </tr>
        <tr>
            <td>3</td>
            <td><input type="text" class="names" name="relay-3-name" value={}></td>
            <td>
                <input type="radio" name="relay-3" checked="false" value="on">On
                <input type="radio" name="relay-3" checked="true" value="off">Off
            </td>
        </tr>
        <tr>
            <td>4</td>
            <td><input type="text" class="names" name="relay-4-name" value={}></td>
            <td>
                <input type="radio" name="relay-4" checked="false" value="on">On
                <input type="radio" name="relay-4" checked="true" value="off">Off
            </td>
        </tr>
    
    if num_relays == 8:
        content = content + 
        <tr>
            <td>5</td>
            <td><input type="text" class="names" name="relay-5-name" value={}></td>
            <td>
                <input type="radio" name="relay-5" checked="false" value="on">On
                <input type="radio" name="relay-5" checked="true" value="off">Off
            </td>
        </tr>
        <tr>
            <td>6</td>
            <td><input type="text" class="names" name="relay-6-name" value={}></td>
            <td>
                <input type="radio" name="relay-6" checked="false" value="on">On
                <input type="radio" name="relay-6" checked="true" value="off">Off
            </td>
        </tr>
        <tr>
            <td>7</td>
            <td><input type="text" class="names" name="relay-7-name" value={}></td>
            <td>
                <input type="radio" name="relay-7" checked="false" value="on">On
                <input type="radio" name="relay-7" checked="true" value="off">Off
            </td>
        </tr>
        <tr>
            <td>8</th>
            <td><input type="text" class="names" name="relay-8-name" value={}></th>
            <td>
                <input type="radio" name="relay-8" checked="false" value="on">On
                <input type="radio" name="relay-8" checked="true" value="off">Off
            </td>
        </tr>
    
    content = content + "</table>"
    
    m = model.get_model()
    if num_relays == 4:
        return content.format(m[1].replace(" ", "&nbsp;"),m[2].replace(" ", "&nbsp;"),m[3].replace(" ", "&nbsp;"),m[4].replace(" ", "&nbsp;"))
    else:
        return content.format(m[1].replace(" ", "&nbsp;"),m[2].replace(" ", "&nbsp;"),m[3].replace(" ", "&nbsp;"),m[4].replace(" ", "&nbsp;"),m[5].replace(" ", "&nbsp;"),m[6].replace(" ", "&nbsp;"),m[7].replace(" ", "&nbsp;"),m[8].replace(" ", "&nbsp;"))
    '''
    
#-------------------------------------------------
# Updater HTML
def get_update():
    return ''' 
    <button type="button" id="relays_apply">Apply</button> <input id="response" type="text" />
    '''

#-------------------------------------------------
# Footer HTML
def get_footer():
    return "Bob Cowdery - G3UKB"
