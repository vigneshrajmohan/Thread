#Thread: Traverse in Reverse
#by Vignesh Rajmohan

#!!!!!!!!!!!!!!!!!!!!!!!!!!!
#can only be run on Pythonista
#!!!!!!!!!!!!!!!!!!!!!!!!!!!
#In this version did not worry about style because I asked a TA and he said that it did not matter for TP1
import motion
from scene import *
import math
import numpy
import time
import sound
import location
import copy
import webbrowser

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
        self.SOSState = False
        #self.query = 'safari-http://maps.apple.com/?q=%s,%s'
        self.query = 'safari-https://www.google.com/maps/dir/'

        #compass in NSEW mode or degrees
        self.compassStat = False

        #motion updates for compass
        motion.start_updates()

        #location start updates
        location.start_updates()
        self.radius = scale

    def draw(self):
        self.centerX = self.size.w/2
        self.centerY = self.size.h/2
        self.centerX2 = self.size.w/2
        self.centerY2 = self.size.h * (1/2)-scale*3.5
        time.sleep(0.1)
        self.testCounter += 1

        #Title Text
        tint(0,0,0,1)
        text('Thread 1.0', font_name='Courier', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+400, alignment=5)

        #motion
        gravX,gravY,gravZ= motion.get_gravity()
        gravity_vectors=motion.get_attitude()
        yaw = gravity_vectors[2]

        #convert yaw to degrees
        yaw = -yaw*180/math.pi

        #############redraw screen############
        #Reset Button
        fill(0.9,0.9,0.9)
        stroke_weight(0)
        ellipse(self.centerX2-scale*3-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)
        tint(0.4,0.4,0.4,1)
        text('Reset', font_name='Verdana', font_size=12.0, x=self.centerX2-112, y=self.centerY2+self.radius-167, alignment=5)


        #ellipse(self.centerX2-scale*3-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)

        #SOS Button and
        fill(0.95,0.6,0.6)
        tint(1,1,1,1)
        if self.SOSState == True:
            ellipse(self.centerX2-0.0-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)
            text('SOS', font_name='Verdana', font_size=12.0, x=self.centerX2, y=self.centerY2+self.radius-167, alignment=5)
        elif self.SOSState == False:
            ellipse(self.size.x/2-self.radius/2,0-self.radius/2-5,self.radius,self.radius)



        #compass draw
        tint(0.4,0.4,0.4,1)
        stroke(0.4,0.4,0.4)
        stroke_weight(0)
        fill(0.9,0.9,0.9)
        ellipse(self.centerX2+scale*3-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)
        stroke_weight(0)
        ellipse(self.centerX2+scale*3-self.radius+3,self.centerY2-self.radius-127,self.radius*1.85,self.radius*1.85)
        ellipse(self.centerX2+scale*3-self.radius+6,self.centerY2-self.radius-124,self.radius*1.7,self.radius*1.7)
        yawSin = math.sin(math.radians(yaw))
        yawCos = math.cos(math.radians(yaw))
        stroke(0.4,0.4,0.4)
        stroke_weight(2)
        line(self.centerX2-yawCos*self.radius+scale*3,self.centerY2-yawSin*self.radius-130,self.centerX2+yawCos*self.radius+scale*3,self.centerY2+yawSin*self.radius-130)
        stroke(1,0.3,0.3)
        line(300,72.5,self.centerX2+yawCos*self.radius+scale*3,self.centerY2+yawSin*self.radius-130)
        #circle on top of compass
        stroke_weight(0)
        stroke(0.4,0.4,0.4)
        #fill(0.95,0.95,0.95)
        fill(1,1,1)
        ellipse(self.centerX2+scale*3-self.radius+9.5,self.centerY2-self.radius-120.5,self.radius*1.5,self.radius*1.5)

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


        tint(0.4,0.4,0.4,1)
        if self.measuringOn == False and self.checkedOnce == 0:
            text('Tap to Start', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
        elif self.measuringOn == True and self.checkedOnce == 1:
            if self.testCounter//10 % 3 == 0:
                text('Measuring.', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
            elif self.testCounter//10 % 3 == 1:
                text('Measuring..', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
            elif self.testCounter//10 % 3 == 2:
                text('Measuring...', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
            text('Tap to Stop', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+120, alignment=5)
        elif self.measuringOn == False and self.checkedOnce == 2:
            text('Calculating', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+120, alignment=5)


        #compass text
        if self.compassStat == False:
            text(directionText(yaw), font_name='Verdana', font_size=10.0, x=self.centerX2+scale*3, y=self.centerY2+self.radius-167, alignment=5)
        else:
            tempYaw = yaw+180+90
            if tempYaw > 360:
                tempYaw = tempYaw % 360
            yawString = str(round(tempYaw,2)) + chr(186)
            text(yawString, font_name='Verdana', font_size=10.0, x=self.centerX2+scale*3, y=self.centerY2+self.radius-167, alignment=5)

        if self.measuringOn == True:
            if self.testCounter % 500:
                current = location.get_location()
                latLong = (current['latitude'], current['longitude'])
                if latLong not in self.locations:
                    self.locations += [latLong]

        elif self.checkedOnce == 2 and len(self.locations) > 2:
            self.locations.pop(0)
            self.locations.pop()
            self.locationsReversed = copy.deepcopy(self.locations)
            self.locationsReversed.reverse()

            #now use the locations and map it onto a map so you know the direciton between points (NWSE)
            #start saying stuff like "Point North and Move Forward"
            #Now it makes sense why we use the compass.

            #test texts
            self.checkedOnce += 1

        elif self.checkedOnce == 3:

            text('Tap to return to start', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+120, alignment=5)

            locationList = str(self.locations[0]) + ' ' + str(self.locations[-1])
            text(locationList, font_name='Verdana', font_size=5.0, x=self.centerX2, y=self.centerY2+self.radius+80, alignment=5)
            locationListReversed = str(self.locationsReversed[0]) + ' ' + str(self.locationsReversed[-1])
            text(locationListReversed, font_name='Verdana', font_size=5.0, x=self.centerX2, y=self.centerY2+self.radius+60, alignment=5)

        elif self.checkedOnce == 4:
            x,y = self.locations[-1]
            x = round(x,10)
            y = round(y,10)
            loc = "[" + str(x) + ", " + str(y) + "]"
            fill(0.9,0.9,0.9)
            stroke(0,0,0)
            stroke_weight(0)
            rect(0,525,self.size.w,50)
            text('Destination:', font_name='Verdana', font_size=12.0, x=70, y=550, alignment=5)
            text(loc, font_name='Verdana', font_size=12.0, x=230, y=550, alignment=5)

            currPosX, currPosY = self.locations[-1]
            nextPosX, nextPosY = self.locations[0]

            differenceX = nextPosX - currPosX
            differenceY = nextPosY - currPosY

            directionAngle = math.atan(differenceY/differenceX)
            degreeAngle = math.degrees(directionAngle)

            textPosX = self.size.x/2
            textPosY = self.size.y/2


            if (currPosX <= nextPosX and currPosY <= nextPosY):
                text(str(round(degreeAngle, 4)), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY, alignment=5)
            elif (currPosX <= nextPosX and currPosY >= nextPosY):
                text(str(round(degreeAngle, 4)+180), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY, alignment=5)
            elif (currPosX >= nextPosX and currPosY >= nextPosY):
                text(str(round(degreeAngle, 4)+180), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY, alignment=5)
            elif (currPosX >= nextPosX and currPosY <= nextPosY):
                text(str(round(degreeAngle, 4)+360), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY, alignment=5)

    def openInMaps(self, num):
        x,y = self.locations[num]
        webbrowser.open(self.query % (x,y))

    def touch_began(self, touch):
        x,y = touch.location
        if self.SOSState == True:
            if x < self.size.w/2 + 30 and x > self.size.w/2 - 30 and y > 50 and y < 100 and self.SOSState == True:
                webbrowser.open('tel:911')

            else:
                self.SOSState = False

        elif x < 30 and y < 30:
            googleMapsMaxPoints = 20
            mapLocations = copy.deepcopy(self.locations)
            if len(self.locations) > googleMapsMaxPoints:
                mapLocations = []
                jump = math.ceil(len(self.locations)/googleMapsMaxPoints)
                for i in range(0,len(self.locations),jump):
                    mapLocations += [self.locations[i]]
            self.query = 'safari-https://www.google.com/maps/dir/'
            for loc in mapLocations:
                self.query += str(loc[0])
                self.query += ","
                self.query += str(loc[1])
                self.query += "/"
            self.query = self.query[:-1]
            webbrowser.open(self.query)


        elif x < 100 and x > 50 and y < 100 and y > 50:
            self.measuringOn = False
            self.checkedOnce = 0
            self.background_color = 'white'
            self.locations = []
            self.locationsReversed = []

        #reset button
        elif x < self.size.w/2 + 20 and x > self.size.w/2 - 20 and y < 25 and y > 0:
            self.SOSState = True

        #compass
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


#http://maps.google.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=14&size=512x512&maptype=roadmap&markers=color:blue|label:S|40.702147,-74.015794&markers=color:green|label:G|40.711614,-74.012318&markers=color:red|color:red|label:C|40.718217,-73.998284&sensor=true&key=MAPS_API_KEY
