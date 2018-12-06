#coding: utf-8
# For use in pythonista on iOS
#import ui
import motion
from scene import *
import math
import numpy as np
import time
scale =80  # scale raw accelerometer values to screen
W=2
L=1
H=.5/2
class MyScene (Scene):
    def setup(self):
            global scale
            scale=self.size.w/10
            #motion start
            motion.start_updates()
            #pitch,roll,yawメータの半径
            self.R=scale
            #Boxの定義 後の計算の為arrayにしておく
            self.Box=[[[W,L,-H]],[[-W,L,-H]],[[-W,-L,-H]],[[W,-L,-H]],[[W,L,H]],[[-W,L,H]],[[-W,-L,H]],[[W,-L,H]]]
            self.Box=np.array(self.Box)

    def draw(self):
        #Boxの中心
        self.cx =self.size.w * 0.5
        self.cy = self.size.h * 0.5
        #pitch,roll,yawメータの中心
        self.cx2 =self.size.w * 0.5
        self.cy2 = self.size.h * 0.5-scale*3.5
        time.sleep(0.1)
        #motionセンサの値更新
        ax,ay,az = motion.get_user_acceleration()
        gx,gy,gz= motion.get_gravity()
        gravity_vectors=motion.get_attitude()
        mx,my,mz,ma=motion.get_magnetic_field()
        pitch, roll, yaw = [x for x in gravity_vectors]
        #ラジアン→度
        pitch=-pitch*180/3.1415926
        roll=roll*180/3.1415926
        yaw=-yaw*180/3.1415926
        #redraw screen
        background(1, 1, 1)
        fill(1,1,1)
        stroke(0,0,0)
        stroke_weight(1)

        roll_sin=math.sin(math.radians(roll))
        roll_cos=math.cos(math.radians(roll))
        pitch_sin=math.sin(math.radians(pitch))
        pitch_cos=math.cos(math.radians(pitch))
        yaw_sin=-math.sin(math.radians(yaw))
        yaw_cos=-math.cos(math.radians(yaw))

        yawMatrix = np.matrix([[-yaw_cos, yaw_sin, 0],[yaw_sin, yaw_cos, 0],[0, 0, 1]])
        pitchMatrix = np.matrix([[pitch_cos, 0, pitch_sin],[0, 1, 0],[-pitch_sin, 0, pitch_cos]])
        rollMatrix = np.matrix([[1, 0, 0],[0, roll_cos, -roll_sin],[0, roll_sin, roll_cos]])
        R = yawMatrix * pitchMatrix * rollMatrix
        R = np.array(R)
        x_3d,y_3d,z_3d=np.transpose(np.dot(self.Box,R),(2,0,1))
        #陰線処理のため1番奥の頂点を特定
        zmin = np.argmin(z_3d)
        #奥の頂点を含んでいない辺を描画
        if zmin!=0 and zmin!=1 :
            line(self.cx+x_3d[0]*scale,self.cy+y_3d[0]*scale,self.cx+x_3d[1]*scale,self.cy+y_3d[1]*scale)
        if zmin!=1 and zmin!=2 :
            line(self.cx+x_3d[1]*scale,self.cy+y_3d[1]*scale,self.cx+x_3d[2]*scale,self.cy+y_3d[2]*scale)
        if zmin!=2 and zmin!=3 :
            line(self.cx+x_3d[2]*scale,self.cy+y_3d[2]*scale,self.cx+x_3d[3]*scale,self.cy+y_3d[3]*scale)
        if zmin!=3 and zmin!=0 :
            line(self.cx+x_3d[3]*scale,self.cy+y_3d[3]*scale,self.cx+x_3d[0]*scale,self.cy+y_3d[0]*scale)

        if zmin!=4 and zmin!=5 :
            line(self.cx+x_3d[4]*scale,self.cy+y_3d[0]*scale,self.cx+x_3d[1]*scale,self.cy+y_3d[1]*scale)
        if zmin!=5 and zmin!=6 :
            line(self.cx+x_3d[5]*scale,self.cy+y_3d[1]*scale,self.cx+x_3d[2]*scale,self.cy+y_3d[2]*scale)
        if zmin!=6 and zmin!=7 :
            line(self.cx+x_3d[6]*scale,self.cy+y_3d[2]*scale,self.cx+x_3d[3]*scale,self.cy+y_3d[3]*scale)
        if zmin!=7 and zmin!=4 :
            line(self.cx+x_3d[7]*scale,self.cy+y_3d[3]*scale,self.cx+x_3d[0]*scale,self.cy+y_3d[0]*scale)

if __name__ == "__main__":
   scene = run(MyScene())
