import numpy as np


def get_spaced_colors(n):
    ''' Function used for creating evenly spaced colors for n number of unique stimulus parameters 
        
        INPUT
        - n (int/float) = number of colors needed 
        
        OUTPUT
        - (list) = list of colors that are uniformly spaced visually
    
    '''
    max_value = 16581375 #255**3
    interval = int(max_value / n)
    colors = [hex(I)[2:].zfill(6) for I in range(0, max_value, interval)]

    return [(int(i[:2], 16)/float(255), int(i[2:4], 16)/float(255), int(i[4:], 16)/float(255)) for i in colors]






