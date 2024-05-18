'''
Drawing Ellipse Animation

https://en.wikipedia.org/wiki/Ellipse#Drawing_ellipses

    de La Hire's point construction
'''
import numpy as np
import libvgl as vgl

if __name__ == "__main__":
    import chkfld
else:
    from . import chkfld

if not chkfld.create_folder("./elpani"):
    exit()

r1, r2 = 1, 1.4
nth = 100

# for gif
#dur = 10 # sec
#fps = 10 # frames per sec

dur = 20
fps = 20

npnt = dur*fps
dth = 2*np.pi/npnt

fmm = vgl.FrameManager()
frm = fmm.create(0,0,3,3,vgl.Data(-r2,r2,-r2,r2))

def plot(dev):
    dev.set_device(frm)
    dev.circle(0,0,r1,lcol=vgl.RED, lthk=0.003)
    dev.circle(0,0,r2,lcol=vgl.BLUE, lthk=0.003)
    pis = np.linspace(0,2*np.pi,nth)
    x1  = r2*np.cos(pis)
    y1  = r1*np.sin(pis)
    dev.polyline(x1,y1,lcol=vgl.MAGENTA, lthk=0.004)
    vgl.draw_center_axis(dev)
    dev.close()

def anim(t):
    global dev, pxx, pyy
    dev.fill_white()
    dev.circle(0,0,r1,lcol=vgl.Gray(190), lthk=0.005)
    dev.circle(0,0,r2,lcol=vgl.Gray(190), lthk=0.005)
    the = dth*t*fps
    x2 = r2*np.cos(the)
    y2 = r2*np.sin(the)
    x1 = r1*np.cos(the)
    y1 = r1*np.sin(the)
    
    dev.line(x1,y1,x2,y1,lcol=vgl.GRAY60, lthk=0.004,lpat=vgl.get_dash(0.004))
    dev.line(x2,0,x2,y2,lcol=vgl.GRAY60, lthk=0.004,lpat=vgl.get_dash(0.004))
    dev.line(0,0,x2,y2,lcol=vgl.BLUE, lthk=0.004)
    pxx = [x2]+pxx[:npnt]
    pyy = [y1]+pyy[:npnt]
    
    dev.polyline(pxx,pyy,lcol=vgl.MAGENTA, lthk=0.004)
    vgl.draw_center_axis(dev)
    vgl.print_top_center(dev, "wikipedia: Ellipse")
    
def save():
    dev_img = vgl.DeviceIMG(chkfld.f_jpg(), fmm.get_gbbox(), 200)
    dev_img.set_device(frm)
    plot(dev_img)
    
def save_gif():
    global dev, pxx, pyy
    pxx, pyy = [],[]
    dev = vgl.DeviceIMG("", fmm.get_gbbox(), 150)
    dev.set_device(frm)
    dev_ani = vgl.DeviceCairoAnimation(chkfld.f_gif(),dev,anim,fps=fps,duration=dur)
    dev_ani.save_gif()
    
def save_mp4():
    global dev, pxx, pyy
    pxx, pyy = [], []
    dev = vgl.DeviceIMG("", fmm.get_gbbox(), 400)
    dev.set_device(frm)
    dev_ani = vgl.DeviceCairoAnimation(chkfld.f_mp4(),dev,anim,fps=fps,duration=dur)
    dev_ani.save_video()
                
if __name__ == "__main__":
    #save()
    save_mp4()
    #save_gif()