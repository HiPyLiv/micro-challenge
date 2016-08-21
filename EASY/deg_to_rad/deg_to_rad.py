import numpy as np
import sys

def deg_to_rad(deg):
    
    return float(deg)*np.pi/180

def rad_to_deg(rad):

    return float(rad)*180/np.pi

if __name__ == "__main__":
    print('{0} deg = {1:.2f} rad'.format(sys.argv[1], deg_to_rad(sys.argv[1])))
