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
            #pitch,roll,yaw
            self.R=scale
            self.Box=[[[W,L,-H]],[[-W,L,-H]],[[-W,-L,-H]],[[W,-L,-H]],[[W,L,H]],[[-W,L,H]],[[-W,-L,H]],[[W,-L,H]]]
            self.Box=np.array(self.Box)
    def draw(self):
        #Box
        self.cx =self.size.w * 0.5
        self.cy = self.size.h * 0.5
        #pitch,roll,yaw
        self.cx2 =self.size.w * 0.5
        self.cy2 = self.size.h * 0.5-scale*3.5
        time.sleep(0.1)
        #motion
        ax,ay,az = motion.get_user_acceleration()
        gx,gy,gz= motion.get_gravity()
        gravity_vectors=motion.get_attitude()
        mx,my,mz,ma=motion.get_magnetic_field()
        pitch, roll, yaw = [x for x in gravity_vectors]
        pitch=-pitch*180/math.pi
        roll=roll*180/math.pi
        yaw=-yaw*180/math.pi
        #redraw screen
        background(1, 1, 1)
        fill(1,1,1)
        stroke_weight(1)
        #pitch,roll,yaw描画
        # ellipse(self.cx2-scale*3-self.R,self.cy2-self.R,self.R*2,self.R*2)
        # ellipse(self.cx2-0.0-self.R,self.cy2-self.R,self.R*2,self.R*2)
        ellipse(self.cx2+scale*3-self.R,self.cy2-self.R-130,self.R*2,self.R*2)
        roll_sin = math.sin(math.radians(roll))
        roll_cos = math.cos(math.radians(roll))
        pitch_sin = math.sin(math.radians(pitch))
        pitch_cos = math.cos(math.radians(pitch))
        yaw_sin = math.sin(math.radians(yaw))
        yaw_cos = math.cos(math.radians(yaw))
        # line(self.cx2-roll_cos*self.R-scale*3,self.cy2-roll_sin*self.R,self.cx2+roll_cos*self.R-scale*3,self.cy2+roll_sin*self.R)
        # line(self.cx2-pitch_cos*self.R-0,self.cy2-pitch_sin*self.R,self.cx2+pitch_cos*self.R-0,self.cy2+pitch_sin*self.R)

        line(self.cx2-yaw_cos*self.R+scale*3,self.cy2-yaw_sin*self.R-130,self.cx2+yaw_cos*self.R+scale*3,self.cy2+yaw_sin*self.R-130)
        yawMatrix = np.matrix([[yaw_cos, -yaw_sin, 0],[yaw_sin, yaw_cos, 0],[0, 0, 1]])
        pitchMatrix = np.matrix([[pitch_cos, 0, pitch_sin],[0, 1, 0],[-pitch_sin, 0, pitch_cos]])
        rollMatrix = np.matrix([[1, 0, 0],[0, roll_cos, -roll_sin],[0, roll_sin, roll_cos]])

        R = yawMatrix * pitchMatrix * rollMatrix
        R = np.array(R)
        x_3d,y_3d,z_3d = np.transpose(np.dot(self.Box,R),(2,0,1))
        zmin = np.argmin(z_3d)

        #derive the direction (NSEW)
        def directionText(yaw):
            directionSym = ''
            #Direction
            if yaw > 60 and yaw <= 120:
                directionSym = 'N'
            elif yaw > 120 and yaw <= 150:
                directionSym = 'NE'
            elif (yaw > 150 and yaw <= 180) or (yaw >= -180 and yaw <= -150):
                directionSym = 'E'
            elif yaw > -150 and yaw <= -120:
                directionSym = 'SE'
            elif yaw > -120 and yaw <= -60:
                directionSym = 'S'
            elif yaw > -60 and yaw <= -30:
                directionSym = 'SW'
            elif yaw > -30 and yaw <= 30:
                directionSym = 'W'
            elif yaw > 30 and yaw <= 60:
                directionSym = 'NW'
            else:
                directionSym = ''

            return directionSym

        #text
        tint(0,0,0,1)
        #text('Direction:', font_name='Helvetica', font_size=16.0, x=self.cx2+scale*3, y=self.cy2+self.R-80, alignment=5)
        text(directionText(yaw), font_name='Helvetica', font_size=10.0, x=self.cx2+scale*3, y=self.cy2+self.R-100, alignment=5)

if __name__ == "__main__":
   scene = run(MyScene())
