"""
      Explore the OFT plotting

"""

from poptics.wavefront import WaveFront,ZernikeWaveFront,AnnularMask
import matplotlib.pyplot as plt

def main():
    wave = ZernikeWaveFront(2.0,0.0,0.0,0.0,0.25)
    wave.setMask(AnnularMask(wave.radius,0.7))
    #WaveFront().fromFile()
    print(repr(wave))
    
    wave.plotOTF(100,"h",grid=50)
    
    
    plt.show()
    
        
    
main()
