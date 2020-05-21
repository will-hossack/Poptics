"""
     Basic test to ensure that the materail database is loaded
"""

from poptics.material import MaterialData
from poptics.tio import tprint

def main():
    
    md = MaterialData()            # get the database (this will load the default)
    
    while True:
        mat = md.getMaterial()     # Null call to get for interacibe mode
        tprint(repr(mat))          # trpe %exit to exit loop
        
        
main()

