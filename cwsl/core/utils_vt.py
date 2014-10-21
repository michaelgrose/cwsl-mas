'''
Created on 06/02/2014

Useful utility functions for VisTrails modules.

@filename: utils_vt.py

Part of the WP2 Model Analysis Service VisTrails plugin.
Copyright CSIRO 2014

'''

import re
from datetime import date
from cwsl.core.errors_vt import BadDateStringError


DATE_REGEXS = [r"(?P<year>\d{4})(?P<month>\d{2})",
               r"(?P<year>\d{4})-(?P<month>\d+)-(?P<day>\d+)"]

def convert_to_date(input_string):
    """ Converts a date string to a date object.
    
    WARNING! Without other information, assumes that Januaries start
    on the first and that Decembers end on the 31st.
    
    """
    for regex in DATE_REGEXS:
        match = re.match(regex, input_string)
        if match:
            break
        
    if match:
        captured = match.groupdict()
        try:
            year = int(captured['year'])
            month = int(captured['month'])
            day = int(captured['day'])
        
        except KeyError:
            year = int(captured['year'])
            month = int(captured['month'])
            if month is 12:
                day = 31
            elif month is 1:
                day = 1
            else:
                raise Exception
        
        return date(year, month, day)
    else:
        print "Bad input string is: {0}".format(input_string)
        raise BadDateStringError
    
    
    
