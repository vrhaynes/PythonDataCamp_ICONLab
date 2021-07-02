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



def gauss(x, y, center=(5, 5), sigma=3.5):
    '''
        Creates a 2-D gaussian.
        
        INPUT
        - x, y (float) = range of xs and ys
        - center (tuple/(float,float)) = mean of the gaussian
        - sigma (float) = standard deviation of gaussian
        
        OUTPUT
        - (float) = value of the gaussian at (x,y)
    
    '''
    dist = ((x-center[0])**2 + (y-center[1])**2) ** 0.5
    return 100 * np.exp(-dist**2 / sigma)


