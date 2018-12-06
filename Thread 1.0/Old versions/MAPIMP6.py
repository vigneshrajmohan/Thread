#coding: utf-8
# For use in pythonista on iOS
#import ui
import motion
from scene import *
import math
import numpy
import time
import sound
import location
import copy
import webbrowser
scale = 80  # scale raw accelerometer values to screen


class MyScene (Scene):
    def setup(self):
        global scale
        self.background_color = 'white'
        self.measuringOn = False
        self.textState = ''
        self.checkedOnce = 0
        self.locations = []
        self.locationsReversed = []
        self.testCounter = 0
        scale = self.size.w/10
        self.query = 'safari-http://maps.apple.com/?q=%s,%s'


        #compass in NSEW mode or degrees
        self.compassStat = False

        #location start updates
        location.start_updates()
        self.R=scale

    def draw(self):
        #Box
        self.cx =self.size.w * 0.5
        self.cy = self.size.h * 0.5
        #pitch,roll,yaw
        self.cx2 =self.size.w * 0.5
        self.cy2 = self.size.h * 0.5-scale*3.5
        time.sleep(0.1)
        self.testCounter += 1

        #motion
        ax,ay,az = motion.get_user_acceleration()
        gx,gy,gz= motion.get_gravity()
        gravity_vectors=motion.get_attitude()
        mx,my,mz,ma=motion.get_magnetic_field()
        pitch, roll, yaw = [x for x in gravity_vectors]
        pitch = -pitch*180/math.pi
        roll=roll*180/math.pi
        yaw=-yaw*180/math.pi
        #redraw screen
        fill(0.9,0.9,0.9)
        stroke_weight(0)

        #pitch,roll,yaw
        ellipse(self.cx2-scale*3-self.R,self.cy2-self.R-130,self.R*2,self.R*2)
        tint(0.4,0.4,0.4,1)
        text('Reset', font_name='Verdana', font_size=12.0, x=self.cx2-112, y=self.cy2+self.R-167, alignment=5)

        # ellipse(self.cx2-0.0-self.R,self.cy2-self.R,self.R*2,self.R*2)
        stroke(0.4,0.4,0.4)
        stroke_weight(0)
        fill(0.9,0.9,0.9)
        #compass draw
        ellipse(self.cx2+scale*3-self.R,self.cy2-self.R-130,self.R*2,self.R*2)
        #fill(0.7,0.7,0.7)
        stroke_weight(0)
        ellipse(self.cx2+scale*3-self.R+3,self.cy2-self.R-127,self.R*1.85,self.R*1.85)
        #fill(0.8,0.8,0.8)
        ellipse(self.cx2+scale*3-self.R+6,self.cy2-self.R-124,self.R*1.7,self.R*1.7)


        # roll_sin = math.sin(math.radians(roll))
        # roll_cos = math.cos(math.radians(roll))
        # pitch_sin = math.sin(math.radians(pitch))
        # pitch_cos = math.cos(math.radians(pitch))
        yaw_sin = math.sin(math.radians(yaw))
        yaw_cos = math.cos(math.radians(yaw))
        # line(self.cx2-roll_cos*self.R-scale*3,self.cy2-roll_sin*self.R,self.cx2+roll_cos*self.R-scale*3,self.cy2+roll_sin*self.R)
        # line(self.cx2-pitch_cos*self.R-0,self.cy2-pitch_sin*self.R,self.cx2+pitch_cos*self.R-0,self.cy2+pitch_sin*self.R)
        stroke(0.4,0.4,0.4)
        stroke_weight(2)
        line(self.cx2-yaw_cos*self.R+scale*3,self.cy2-yaw_sin*self.R-130,self.cx2+yaw_cos*self.R+scale*3,self.cy2+yaw_sin*self.R-130)
        stroke(1,0.3,0.3)
        line(300,72.5,self.cx2+yaw_cos*self.R+scale*3,self.cy2+yaw_sin*self.R-130)

        #circle on top of compass
        stroke_weight(0)
        stroke(0.4,0.4,0.4)
        #fill(0.95,0.95,0.95)
        fill(1,1,1)

        ellipse(self.cx2+scale*3-self.R+9.5,self.cy2-self.R-120.5,self.R*1.5,self.R*1.5)


        # yawMatrix = numpy.matrix([[yaw_cos, -yaw_sin, 0],[yaw_sin, yaw_cos, 0],[0, 0, 1]])
        # pitchMatrix = numpy.matrix([[pitch_cos, 0, pitch_sin],[0, 1, 0],[-pitch_sin, 0, pitch_cos]])
        # rollMatrix = numpy.matrix([[1, 0, 0],[0, roll_cos, -roll_sin],[0, roll_sin, roll_cos]])
        #
        # R = yawMatrix * pitchMatrix * rollMatrix
        # R = numpy.array(R)
        #x_3d,y_3d,z_3d = numpy.transpose(numpy.dot(self.Box,R),(2,0,1))
        #zmin = numpy.argmin(z_3d)

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
        text('Thread 1.0', font_name='Courier', font_size=16.0, x=self.cx2, y=self.cy2+self.R+400, alignment=5)

        tint(0.4,0.4,0.4,1)
        if self.measuringOn == False and self.checkedOnce == 0:
            text('Tap to Start', font_name='Verdana', font_size=16.0, x=self.cx2, y=self.cy2+self.R+150, alignment=5)
        elif self.measuringOn == True and self.checkedOnce == 1:
            if self.testCounter//10 % 3 == 0:
                text('Measuring.', font_name='Verdana', font_size=16.0, x=self.cx2, y=self.cy2+self.R+150, alignment=5)
            elif self.testCounter//10 % 3 == 1:
                text('Measuring..', font_name='Verdana', font_size=16.0, x=self.cx2, y=self.cy2+self.R+150, alignment=5)
            elif self.testCounter//10 % 3 == 2:
                text('Measuring...', font_name='Verdana', font_size=16.0, x=self.cx2, y=self.cy2+self.R+150, alignment=5)
            text('Tap to Stop', font_name='Verdana', font_size=16.0, x=self.cx2, y=self.cy2+self.R+120, alignment=5)

        elif self.measuringOn == False and self.checkedOnce == 2:
            text('Calculating', font_name='Verdana', font_size=16.0, x=self.cx2, y=self.cy2+self.R+120, alignment=5)

        #compass text
        if self.compassStat == False:
            text(directionText(yaw), font_name='Verdana', font_size=10.0, x=self.cx2+scale*3, y=self.cy2+self.R-167, alignment=5)
        else:
            tempYaw = yaw+180+90
            if tempYaw > 360:
                tempYaw = tempYaw % 360
            yawString = str(round(tempYaw,2)) + chr(186)
            text(yawString, font_name='Verdana', font_size=10.0, x=self.cx2+scale*3, y=self.cy2+self.R-167, alignment=5)


        if self.measuringOn == True:
            if self.testCounter % 10:
                current = location.get_location()
                latLong = (current['latitude'], current['longitude'])
                self.locations += [latLong]

        elif self.checkedOnce == 2 and len(self.locations) > 2:
            self.locationsReversed = copy.deepcopy(self.locations)
            self.locationsReversed.reverse()

            #now use the locations and map it onto a map so you know the direciton between points (NWSE)
            #start saying stuff like "Point North and Move Forward"
            #Now it makes sense why we use the compass.

            #test texts
            self.checkedOnce += 1

        elif self.checkedOnce == 3:

            locationList = str(self.locations[0]) + ' ' + str(self.locations[-1])
            text(locationList, font_name='Verdana', font_size=5.0, x=self.cx2, y=self.cy2+self.R+80, alignment=5)
            locationListReversed = str(self.locationsReversed[0]) + ' ' + str(self.locationsReversed[-1])
            text(locationListReversed, font_name='Verdana', font_size=5.0, x=self.cx2, y=self.cy2+self.R+60, alignment=5)

        elif self.checkedOnce == 4:
            self.checkedOnce = 5
            x,y = self.locations[0]
            webbrowser.open(self.query % (x,y))
            text(str(x), font_name='Verdana', font_size=5.0, x=self.cx2, y=self.cy2+self.R+80, alignment=5)
            text(str(y), font_name='Verdana', font_size=5.0, x=self.cx2, y=self.cy2+self.R+80, alignment=5)


    def touch_began(self, touch):
        x,y = touch.location
        if x < 100 and x > 50 and y < 100 and y > 50:
            self.measuringOn = False
            self.checkedOnce = 0
            self.background_color = 'white'
            self.locations = []
            self.locationsReversed = []

        elif x < 325 and x > 275 and y < 100 and y > 50:
            if self.compassStat == False:
                self.compassStat = True
            elif self.compassStat == True:
                self.compassStat = False

        elif self.measuringOn == False and self.checkedOnce == 0:
            #sound.play_effect('arcade:Laser_2')
            self.measuringOn = True
            self.background_color = 'white'
            self.checkedOnce += 1

        elif self.measuringOn == True and self.checkedOnce == 1:
            #sound.play_effect('arcade:Laser_1')
            self.measuringOn = False
            self.background_color = 'white'
            self.checkedOnce += 1

        elif self.measuringOn == False and self.checkedOnce == 3:
            #sound.play_effect('arcade:Laser_1')
            self.background_color = 'white'
            self.checkedOnce += 1





run(MyScene(), PORTRAIT)
