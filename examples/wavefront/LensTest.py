"""
        Lens wavefront test code

"""
from poptics.lens import DataBaseLens
from poptics.ray import RayPencil
from poptics.wavefront import WavePointSet,Interferometer
import poptics.tio as t
from poptics.vector import Unit3d,Vector3d
import matplotlib.pyplot as plt


def main():

    lens = DataBaseLens("Tessar-F6.3")
    lens.setIris(0.7)
    u = Unit3d().parseAngle("5")
    pencil = RayPencil().addBeam(lens,u,"array",path=True)

    pencil *= lens
    ep = lens.exitPupil()
    t.tprint(repr(ep))
    rpt = lens.imagePoint(u)
    rpt += Vector3d(0,0,0.2)
    t.tprint("Image point is ",repr(rpt))

    ws = WavePointSet(ep.getRadius()).setWithRays(pencil, ep, refpt = rpt)

    zw = ws.fitZernike(4)
    t.tprint(repr(zw))
    t.tprint("Error is : ",str(ws.zerr))      # Show the fitting error for each component
    zw.plot()

    ws.plot()

    inter = Interferometer(zw)
    inter.draw(0.0,0.0)
    plt.show()


if __name__ == "__main__" :
    main()
