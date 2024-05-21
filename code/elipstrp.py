'''
  Ellipse Paper Strip Method
  
  05/21/2024
  
  r1 : radius of outer circle
  r2 : radius of inner circle
  
  Wikipedia: Ellipse: Paper strip methods
'''
import math
import libvgl as vgl

if __name__ == "__main__":
    import chkfld
else:
    from . import chkfld

if not chkfld.create_folder("./elpstrp"):
    exit()

# Gif : dur=10, fps=10
dur = 20
fps = 20

r1 = 10
r2 = 5
max_freq = 2 # Hz
t1 = 0
t2 = 2*math.pi*max_freq
dt = (t2-t1)/(dur*fps)
max_curve_points=int((t2-t1)/dt)

elipse_trail_x = []
elipse_trail_y = []

def movie_curve(t):
    global dev, elipse_trail_x, elipse_trail_y, sym
    dev.fill_white()
    vgl.draw_axis(dev)	
    
    # draw circle
    t3 = t1 + dt * t * fps
    dev.circle(0, 0, r1, lcol = vgl.BLACK, lthk = 0.003)
    dev.line(-r1,0,r1,0,vgl.BLACK, 0.003, vgl.get_dash(0.005))
    dev.line(0,r1,0,-r1,vgl.BLACK, 0.003, vgl.get_dash(0.005))
    
    p1x = r1*math.cos(t3) 
    p1y = r1*math.sin(t3)
    c2x = p1x - r2 * math.cos(t3)
    c2y = p1y - r2 * math.sin(t3)
    dev.circle(c2x, c2y, r2, lcol = vgl.BLACK, lthk = 0.003)
    
    '''
    r1 * th = r2 * (th + al)
    al + th = r1/r2 * th
    al = (r1/r2 - 1)*th
    t4 is al(pha)
    '''    
    t4 = (r1/r2-1)*t3
    p2x = c2x - r2 * math.cos(t4)
    p2y = c2y + r2 * math.sin(t4)
    p3x = c2x + r2 * math.cos(t4)
    p3y = c2y - r2 * math.sin(t4)
    dev.line(p2x, p2y, p3x, p3y, vgl.royalblue , 0.005, vgl.get_dash(0.006))
    dev.symbol(p2x, p2y, sym)
    dev.symbol(p3x, p3y, sym)
    
    dist = math.sqrt((p3x-p2x)**2+(p3y-p2y)**2)
    abr = 0.7 # a vs b ratio
    a = dist*abr
    b = dist-a
    ax = a*math.cos(t3)
    by = b*math.sin(t3)
    elipse_trail_x = [ax]+elipse_trail_x[:max_curve_points]
    elipse_trail_y = [by]+elipse_trail_y[:max_curve_points]
    dev.polyline(elipse_trail_x, elipse_trail_y, vgl.GREEN, lthk=0.003)
    dev.symbol(ax,by, sym)
    
def save_gif():
    global dev
    dev = vgl.DeviceCairo("", fmm.get_gbbox(), 40)
    dev.set_device(frm)
    dev_mov = vgl.DeviceCairoAnimation(chkfld.f_gif(), dev, movie_curve, dur, fps)
    dev_mov.save_gif()

def save_mp4():
    global dev
    dev = vgl.DeviceCairo("", fmm.get_gbbox(), 400)
    dev.set_device(frm)
    dev_mov = vgl.DeviceCairoAnimation(chkfld.f_mp4(), dev, movie_curve, dur, fps)
    dev_mov.save_video()
    
import libvgl as vgl 
xmin,xmax,ymin,ymax=-r1*1.2,r1*1.2,-r1*1.2,r1*1.2
data = vgl.Data(xmin,xmax,ymin,ymax)
fmm = vgl.FrameManager()
frm = fmm.create(0,0,5,5, data)
sym = vgl.Circle(0.008, frm.hgt(),lcol=vgl.YELLOW)

if __name__ == "__main__":
    save_mp4()
    #save_gif()
