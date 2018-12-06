#Thread: Traverse in Reverse
#by Vignesh Rajmohan

#might change name to breadcrumb

#!!!!!!!!!!!!!!!!!!!!!!!!!!!
#can only be run on Pythonista
#!!!!!!!!!!!!!!!!!!!!!!!!!!!
import motion
from scene import *
import math
import numpy
import time
import sound
import location
import copy
import webbrowser
import clipboard
import photos
import ui
import console
import datetime
import time


#class for the whole scene
class MyScene (Scene):

    #initialize variables
    def setup(self):
        global scale
        self.background_color = 'white'
        self.measuringOn = False  #am i taking in location coordinates?
        self.checkedOnce = 0  #counter for the mode (things happen sequentially so this works)
        # self.locations = [] #array of recorded coordinates
        #self.locations = [(40.4464,-79.9427),(40.4464,-79.9428),(40.4465,-79.9428),(40.4463,-79.9427),(40.4462,-79.9427),(40.4461,-79.9427),(40.446,-79.9427)]
        #self.locations = [(40.444,-79.9446),(40.444,-79.9445),(40.4441,-79.9446),(40.4441,-79.9447),(40.4442,-79.9447),(40.4443,-79.9447),(40.4444,-79.9447),(40.4444,-79.9448),(40.4445,-79.9447),(40.4446,-79.9447),(40.4446,-79.9446),(40.4447,-79.9446),(40.4448,-79.9446),(40.4449,-79.9445),(40.445,-79.9445)]
        #self.locations = [(40.444,-79.9446),(40.444,-79.9445),(40.4441,-79.9446),(40.4441,-79.9447),(40.4442,-79.9447),(40.4449,-79.9449)]
        self.locations = [(40.444,-79.9446),(40.444,-79.9445),(40.4441,-79.9446),(40.4441,-79.9447),(40.4442,-79.9447)]
        self.photoLocations = []

        self.locationsLeft = []
        self.needMore = False #need more values
        self.timerCount = 0 #timer to sync everything
        scale = self.size.w/10 #scaling and UI Design
        self.MoreState = False #activate by pressing the bottom dot
        self.loopPrompt = False #if someone travels in a circle
        self.activator = False #a temporary solution to a significant problem
        self.loopPromptState = 0 #to save circled location or not
        self.currentLoc = None
        #self.query = 'safari-http://maps.apple.com/?q=%s,%s' #apple maps
        self.query = 'safari-https://www.google.com/maps/dir/' #google maps
        self.compassStat = False  #compass in NSEW mode or degrees
        self.pathState = False
        self.radius = scale
        self.clipState = False
        self.photoCount = 0
        self.imageMode = False
        self.imageModeOpen = False
        self.photoLibrary = None
        # self.photoLibraryName = self.photoLibrary.local_id


        motion.start_updates()   #motion updates for compass
        location.start_updates()    #location start updates







    #redraw function
    def draw(self):
        #Center scaling
        self.centerX = self.size.w/2
        self.centerY = self.size.h/2
        self.centerX2 = self.size.w/2
        self.centerY2 = self.size.h * (1/2)-scale*3.5

        time.sleep(0.1) #time between each redraw
        self.timerCount += 1 #add to the timer to animate and do things

        #Title Text
        tint(0,0,0,1)
        text('Thread 1.0', font_name='Courier', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+400, alignment=5)

        #Locations recorded count
        tint(0.4,0.4,0.4,1)

        locationCountText = "Locations: " + str(len(self.locations))
        text(locationCountText, font_name='Verdana', font_size=10, x=50, y=self.centerY2+self.radius+400, alignment=5)

        if self.checkedOnce == 4:
            locationLeftText = "Left: " + str(len(self.locationsLeft))
            text(locationLeftText, font_name='Verdana', font_size=10, x=self.size.x-60, y=self.centerY2+self.radius+400, alignment=5)

        #motion
        gravX,gravY,gravZ= motion.get_gravity()
        gravity_vectors=motion.get_attitude()
        pitch = gravity_vectors[0]
        roll = gravity_vectors[1]
        yaw = gravity_vectors[2]

        #convert yaw to degrees
        yaw = -yaw*180/math.pi
        pitch = -pitch*180/math.pi
        roll = -roll*180/math.pi

        ############# redraw screen ############
        #Reset Button
        fill(0.9,0.9,0.9)
        stroke_weight(0)
        ellipse(self.centerX2-scale*3-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)
        tint(0.4,0.4,0.4,1)
        text('Reset', font_name='Verdana', font_size=12.0, x=self.centerX2-112, y=self.centerY2+self.radius-167, alignment=5)

        current = location.get_location()
        latLong = (round(current['latitude'],4), round(current['longitude'],4)) #solved the close points problem using rounding
        picTaken = latLong in self.photoLocations

        if self.measuringOn == True and picTaken == False:
            #camera mode
            stroke_weight(0)
            fill(0.9,0.9,0.9)
            tint(0.4,0.4,0.4,1)
            ellipse(self.size.x/2-self.radius/2,0-self.radius/2+72,self.radius,self.radius)
            text('Snap', font_name='Verdana', font_size=8.0, x=self.centerX2, y=self.centerY2+self.radius-167, alignment=5)


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
        rollSin=math.sin(math.radians(roll))
        rollCos=math.cos(math.radians(roll))
        pitchSin=math.sin(math.radians(pitch))
        pitchCos=math.cos(math.radians(pitch))
        stroke(0.4,0.4,0.4)
        stroke_weight(2)

        #line(self.centerX2-yawCos*self.radius+scale*3,self.centerY2-yawSin*self.radius-50,self.centerX2+yawCos*self.radius+scale*3,self.centerY2+yawSin*self.radius-50)
        #line(self.centerX2-pitchCos*self.radius-0,self.centerY2-pitchSin*self.radius,self.centerX2+pitchCos*self.radius-0,self.centerY2+pitchSin*self.radius)
        #line(self.centerX2-rollCos*self.radius-scale*3,self.centerY2-rollSin*self.radius,self.centerX2+rollCos*self.radius-scale*3,self.centerY2+rollSin*self.radius)

        stroke(0.4,0.4,0.4)
        line(self.centerX2-yawCos*self.radius+scale*3,self.centerY2-yawSin*self.radius-130,self.centerX2+yawCos*self.radius+scale*3,self.centerY2+yawSin*self.radius-130)
        stroke(1,0.3,0.3)
        line(300,72.5,self.centerX2+yawCos*self.radius+scale*3,self.centerY2+yawSin*self.radius-130)

        #circle on top of compass
        stroke_weight(0)
        stroke(0.4,0.4,0.4)
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

        #compass text
        tint(0.4,0.4,0.4,1)
        if self.compassStat == False:
            text(directionText(yaw), font_name='Verdana', font_size=10.0, x=self.centerX2+scale*3, y=self.centerY2+self.radius-167, alignment=5)
        else:
            tempYaw = yaw+180+90
            if tempYaw > 360:
                tempYaw = tempYaw % 360
            yawString = str(int(round(tempYaw,0))) + chr(186)
            text(yawString, font_name='Verdana', font_size=10.0, x=self.centerX2+scale*3, y=self.centerY2+self.radius-167, alignment=5)

        #Center Screen Text
        tint(0.4,0.4,0.4,1)
        if self.measuringOn == False and self.checkedOnce == 0:
            text('Tap to Start', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
        elif self.measuringOn == True and self.checkedOnce == 1:
            if self.timerCount//10 % 3 == 0:
                text('Measuring.', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
            elif self.timerCount//10 % 3 == 1:
                text('Measuring..', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
            elif self.timerCount//10 % 3 == 2:
                text('Measuring...', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
            text('Tap to Stop', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+120, alignment=5)
        elif self.measuringOn == False and self.checkedOnce == 2:
            text('Calculating', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)


        #if not enough values are recorded
        tint(0.95,0.6,0.6,1)
        if self.needMore == True:
            text("Need to record more locations.", font_name='Verdana', font_size=16.0, x=self.size.x/2, y=self.size.y/2-20, alignment=5)


        tint(0.4,0.4,0.4,1)
        #When measuring is on record locations and put into array
        if self.measuringOn == True:
            current = location.get_location()
            latLong = (round(current['latitude'],4), round(current['longitude'],4)) #solved the close points problem using rounding
            if latLong not in self.locations:
                self.locations += [latLong]
                if self.activator == True:
                    self.activator = False
                self.loopPromptState = 0

            elif latLong in self.locations[0:-5] and self.activator == False:
                #sound.play_effect('arcade:Laser_1')
                self.loopPrompt = True
                self.activator = True

            if self.loopPromptState == 1:
                if self.currentLoc != latLong:
                    self.currentLoc = latLong
                    self.locations += [latLong]

            elif self.loopPromptState == 2:
                loc = self.locations.index(latLong)
                self.locations = self.locations[0:loc]
                self.loopPromptState = 0

        #after measuring is off, setup array to use (states Calculating)
        elif self.checkedOnce == 2 and len(self.locations) > 3:
            self.locationsLeft = copy.deepcopy(self.locations)

            #do this to avoid tapping too early
            self.checkedOnce += 1

        #after the array set up, tap to get back to where you were
        elif self.checkedOnce == 3:
            text('Tap to return to start', font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)

        #The return back..
        elif self.checkedOnce == 4:

            x,y = self.locations[-1]
            x = round(x,10)
            y = round(y,10)

            loc = "[" + str(x) + ", " + str(y) + "]"
            fill(0.9,0.9,0.9)
            stroke(0,0,0)
            stroke_weight(0)
            # rect(0,560,self.size.w,50)
            # # text('Destination:', font_name='Verdana', font_size=12.0, x=70, y=550, alignment=5)
            # # text(loc, font_name='Verdana', font_size=12.0, x=230, y=550, alignment=5)

            totalDistanceTraveled = 0
            for i in range(len(self.locations)-1):
                firstPosX, firstPosY = self.locations[i]
                nextPosX, nextPosY = self.locations[i+1]
                dist = ((nextPosX - firstPosX)**2 + (nextPosY - firstPosY)**2)**0.5
                totalDistanceTraveled += dist

            text('Distance Traveled:', font_name='Verdana', font_size=12.0, x=70, y=585, alignment=5)
            text(str(totalDistanceTraveled), font_name='Verdana', font_size=12.0, x=230, y=585, alignment=5)

            textPosX = self.size.x/2
            textPosY = self.size.y/2


            if (len(self.locationsLeft) > 3):
                #replace with current locations
                currentPos = location.get_location()
                latLongPos = (round(currentPos['latitude'],4), round(currentPos['longitude'],4)) #solved the close points problem using rounding

                currPosX, currPosY = latLongPos
                nextPosX, nextPosY = self.locationsLeft[-1]
                secondPosX, secondPosY = self.locationsLeft[-2]
                thirdPosX, thirdPosY = self.locationsLeft[-3]

                # currPosX, currPosY = [40.4465, 79.9427]
                # nextPosX, nextPosY = [40.4465, 79.9428]
                # secondPosX, secondPosY = [40.4466, 79.9428]
                # thirdPosX, thirdPosY = [40.4466, 79.9429]


                xNextAverage = (nextPosX + secondPosX + thirdPosX)/3
                yNextAverage = (nextPosY + secondPosY + thirdPosY)/3


                xVal3 = math.cos(math.radians(xNextAverage))*math.sin(math.radians(currPosY-yNextAverage))
                yVal3 = math.cos(math.radians(currPosX))*math.sin(math.radians(xNextAverage))-math.sin(math.radians(currPosX))*math.cos(math.radians(xNextAverage))*math.cos(math.radians(currPosY-yNextAverage))
                radianAngle3 = (math.atan2(xVal3,yVal3))
                degreeAngle3 = math.degrees(radianAngle3)
                if degreeAngle3 < 0:
                    degreeAngle3 = 360 + degreeAngle3

                #take the average of the next 3 points to get a good direction.
                # trueDegree = (degreeAngle1 + degreeAngle2 + degreeAngle3)/3
                trueDegree = degreeAngle3

                #draw directing arrow
                tempYaw1 = - (360 - yaw + trueDegree)
                trueDegreeSin = math.sin(math.radians(tempYaw1))
                trueDegreeCos = math.cos(math.radians(tempYaw1))


                text(str(trueDegree), font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.radius+150, alignment=5)
                # text(str(degreeAngle1), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY-20, alignment=5)
                # text(str(degreeAngle2), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY-40, alignment=5)
                # text(str(degreeAngle3), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY-60, alignment=5)

                #experimental point on arrow. Works well! but code is ugly. Will implement for loop later
                def pointMaker(self,roll,pitch, yaw):
                    stroke_weight(20)
                    line(self.centerX2-trueDegreeCos*100-pitch*3,self.centerY-trueDegreeSin*100+roll*3,self.centerX2+trueDegreeCos*100-pitch*3,self.centerY+trueDegreeSin*100+roll*3)
                    stroke(1,0.3,0.3)
                    line(self.centerX2+trueDegreeCos*100-pitch*3,self.centerY+trueDegreeSin*100+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(19)
                    line(self.centerX2+trueDegreeCos*102-pitch*3,self.centerY+trueDegreeSin*102+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(18)
                    line(self.centerX2+trueDegreeCos*104-pitch*3,self.centerY+trueDegreeSin*104+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(17)
                    line(self.centerX2+trueDegreeCos*106-pitch*3,self.centerY+trueDegreeSin*106+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(16)
                    line(self.centerX2+trueDegreeCos*108-pitch*3,self.centerY+trueDegreeSin*108+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(15)
                    line(self.centerX2+trueDegreeCos*110-pitch*3,self.centerY+trueDegreeSin*110+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(14)
                    line(self.centerX2+trueDegreeCos*112-pitch*3,self.centerY+trueDegreeSin*112+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(13)
                    line(self.centerX2+trueDegreeCos*114-pitch*3,self.centerY+trueDegreeSin*114+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(12)
                    line(self.centerX2+trueDegreeCos*116-pitch*3,self.centerY+trueDegreeSin*116+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(11)
                    line(self.centerX2+trueDegreeCos*118-pitch*3,self.centerY+trueDegreeSin*118+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(10)
                    line(self.centerX2+trueDegreeCos*120-pitch*3,self.centerY+trueDegreeSin*120+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(9)
                    line(self.centerX2+trueDegreeCos*122-pitch*3,self.centerY+trueDegreeSin*122+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(8)
                    line(self.centerX2+trueDegreeCos*124-pitch*3,self.centerY+trueDegreeSin*124+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(7)
                    line(self.centerX2+trueDegreeCos*126-pitch*3,self.centerY+trueDegreeSin*126+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(6)
                    line(self.centerX2+trueDegreeCos*128-pitch*3,self.centerY+trueDegreeSin*128+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(5)
                    line(self.centerX2+trueDegreeCos*130-pitch*3,self.centerY+trueDegreeSin*130+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(4)
                    line(self.centerX2+trueDegreeCos*132-pitch*3,self.centerY+trueDegreeSin*132+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(3)
                    line(self.centerX2+trueDegreeCos*134-pitch*3,self.centerY+trueDegreeSin*134+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                    stroke_weight(2)
                    line(self.centerX2+trueDegreeCos*136-pitch*3,self.centerY+trueDegreeSin*136+roll*3, self.centerX2-pitch*3,self.centerY+roll*3)
                pointMaker(self,roll,pitch, yaw)

                stroke_weight(0)

                #tracing back steps
                current = location.get_location()
                latLong = (round(current['latitude'],4), round(current['longitude'],4)) #solved the close points problem using rounding
                if latLong in self.locationsLeft:
                     loc = self.locationsLeft.index(latLong)
                     # self.locationsLeft.remove(latLong)
                     self.locationsLeft = self.locationsLeft[0:loc]

                #images on the trip back
                if latLong in self.photoLocations:
                    loc = self.photoLocations.index(latLong)
                    self.imageMode = True

                tint(1,1,1)
                fill(0,0,0)
                stroke(0,0,0)
                if self.imageMode == True:
                    rect(0,150,self.size.w,50)
                    text("Landmark! Tap here to see!", font_name='Courier', font_size=16.0, x=self.centerX2, y=150+25, alignment=5)

            else:
                text("Welcome Back.", font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY, alignment=5)


















        #SOS Button and
        fill(0.95,0.6,0.6)
        tint(1,1,1,1)
        if self.MoreState == True:
            #to seperate the active buttons from the non active ones
            fill(0,0,0,0.5)
            rect(0,0,self.size.x,self.size.y)
            #SOS Button
            fill(0.95,0.6,0.6,1)
            tint(1,1,1,1)
            ellipse(self.centerX2-0.0-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)
            text('SOS', font_name='Verdana', font_size=12.0, x=self.centerX2, y=self.centerY2+self.radius-167, alignment=5)

            #MAP Button
            if len(self.locations) >= 2:
                fill(0.6,0.6,0.95)
                tint(1,1,1,1)
                ellipse(self.centerX2-scale*3-self.radius,self.centerY2-self.radius-20,self.radius*2,self.radius*2)
                text('Map View', font_name='Verdana', font_size=12.0, x=self.centerX2-112, y=self.centerY2+self.radius-57, alignment=5)

                fill(247/255,170/255,103/255)
                tint(1,1,1,1)
                ellipse(self.centerX2-self.radius,self.centerY2-self.radius-20,self.radius*2,self.radius*2)
                text('Share', font_name='Verdana', font_size=12.0, x=self.centerX2, y=self.centerY2+self.radius-57, alignment=5)

                tint(0.7,0.7,0.7,1)
                if self.clipState == True:
                    text('Copied to Clipboard', font_name='Verdana', font_size=16.0, x=self.size.x/2, y=self.size.y/2-65, alignment=5)


            fill(118/255,191/255,247/255)
            tint(1,1,1,1)
            ellipse(self.centerX2+scale*3-self.radius,self.centerY2-self.radius-20,self.radius*2,self.radius*2)
            text('Trace', font_name='Verdana', font_size=12.0, x=self.centerX2+112, y=self.centerY2+self.radius-57, alignment=5)

            #SOS Button
            fill(0.95,0.6,0.6)
            tint(1,1,1,1)
            ellipse(self.centerX2-0.0-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)
            text('SOS', font_name='Verdana', font_size=12.0, x=self.centerX2, y=self.centerY2+self.radius-167, alignment=5)

        #More button at the bottom of screen
        elif self.MoreState == False:
            ellipse(self.size.x/2-self.radius/2,0-self.radius/2-5,self.radius,self.radius)







#-----------Draw Path State---------------------------------------------------
        if self.pathState == True and len(self.locations) > 0:
            fill(0.7,0.7,0.7)
            rect(20,self.size.y/2-50,self.size.x-40,self.size.y/3)
            fill(1,1,1)
            rect(25,self.size.y/2-45,self.size.x-50,self.size.y/3-10)

            tint(1,0,0,1)
            fill(1,0,0)
            stroke(1,0,0,1)
            stroke_weight(2)
            #line(self.size.x/2, self.size.y/2, self.size.x/2 + 10, self.size.y/2 + 10)
            iPointX, iPointY = self.locations[0]
            newLocs = [(0,0)]
            maxDiffX = 0
            maxDiffY = 0
            xSepVals = []
            ySepVals = []

            # for loc in self.locations:
            #     xSepVals += [loc[0]]
            #     ySepVals += [loc[1]]
            #
            # maxDiffX = (max(xSepVals) - min(xSepVals))* 100000
            # maxDiffY = (max(ySepVals) - min(ySepVals))* 100000

            for loc in self.locations[1:]:
                nPointX, nPointY = loc
                dataX = (iPointX - nPointX) * 100000
                dataY = (iPointY - nPointY) * 100000
                newLocs += [(dataX,dataY)]

            for loc in newLocs:
                xSepVals += [loc[0]]
                ySepVals += [loc[1]]

            maxDiffX = (max(xSepVals) - min(xSepVals))
            maxDiffY = (max(ySepVals) - min(ySepVals))

            generalMaxDiff = max(maxDiffX, maxDiffY)

            miniX = min(xSepVals)
            miniY = min(ySepVals)
            generalMini = min(miniX, miniY)
            jumpG = 0 - generalMini
            evenedLocsX = []
            evenedLocsY = []
            for i in range(len(xSepVals)):
                evenedLocsX += [xSepVals[i] + jumpG]
                evenedLocsY += [ySepVals[i] + jumpG]

            xCenter = self.size.x/2
            yCenter = self.size.y/2-50 + 2
            colorCount = len(newLocs)
            for i in range(len(newLocs)-1):
                xLoc1, yLoc1 = evenedLocsX[i], evenedLocsY[i]
                xLoc2, yLoc2 = evenedLocsX[i+1], evenedLocsY[i+1]
                stroke(((255/colorCount)*i)/255, 0, 0)
                fill((255-(i*10))/255,0,0)
                text(str(i),font_name='Verdana', font_size=4.0, x=xCenter + xLoc1, y=yCenter + yLoc1 + 20, alignment=5)
                line((335/generalMaxDiff)*xLoc1+20,(222/generalMaxDiff)*yLoc1+yCenter, (335/generalMaxDiff)*xLoc2+20,(222/generalMaxDiff)*yLoc2+yCenter)
                ellipse(xCenter-2 + xLoc1,yCenter-2 + yLoc1,4,4)

#-----------END OF PATHSTATE---------------------------------------------------





        if self.loopPrompt == True:
            fill(0,0,0)
            stroke_weight(0)
            #prompt for the loop
            rect(50,self.size.y/2-50,self.size.x-100,self.size.y/6+40)
            tint(1,1,1,1)
            text("Stop Moving!", font_name='Verdana', font_size=18.0, x=self.size.x/2, y=self.size.y/2+65, alignment=5)
            text("Looks like you\'ve made a loop", font_name='Verdana', font_size=13.0, x=self.size.x/2, y=self.size.y/2+38, alignment=5)
            stroke(1,1,1,1)
            stroke_weight(3)
            line(50, self.size.y/2, self.size.x-50, self.size.y/2)
            line(self.size.x/2, self.size.y/2-50, self.size.x/2, self.size.y/2)
            text("Continue", font_name='Verdana', font_size=15.0, x=self.size.x/2-70, y=self.size.y/2-25, alignment=5)
            text("Break", font_name='Verdana', font_size=15.0, x=self.size.x/2+70, y=self.size.y/2-25, alignment=5)






    #tells you if the screen is touched and where
    def touch_began(self, touch):

        current = location.get_location()
        latLong = (round(current['latitude'],4), round(current['longitude'],4)) #solved the close points problem using rounding
        picTaken = latLong in self.photoLocations


        x,y = touch.location

        if self.loopPrompt == True:
            if x > 50 and x < self.size.x/2 and y < self.size.y/2 and y > self.size.y/2 - 50:
                self.loopPrompt = False
                self.loopPromptState = 1
            elif x > self.size.x/2 and x < self.size.x-50 and y < self.size.y/2 and y > self.size.y/2 - 50:
                self.loopPrompt = False
                self.loopPromptState = 2

        elif self.MoreState == True:
            #SOS State
            if x < self.size.w/2 + 30 and x > self.size.w/2 - 30 and y > 50 and y < 100 and self.MoreState == True:
                webbrowser.open('tel:911')

            #MapView
            elif x < 100 and x > 50 and y < 220 and y > 160 and len(self.locations) >= 2:
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

            elif x < self.size.x/2+40 and x > self.size.x/2-40 and y < 220 and y > 160 and len(self.locations) >= 2:
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
                clipboard.set(self.query[7:])
                self.clipState = True


            elif x < self.size.x-50 and x > self.size.x-100 and y < 220 and y > 160:
                self.pathState = True

            else:
                self.MoreState = False
                self.clipState = False
                self.pathState = False

        #open landmark
        elif y > 150 and y < 200 and self.imageMode == True:
            sound.play_effect('arcade:Laser_2')
            self.imageModeOpen = True
            self.imageMode = False











        #reset button
        elif x < 100 and x > 50 and y < 100 and y > 50:
            self.measuringOn = False
            self.checkedOnce = 0
            self.background_color = 'white'
            self.locations = []
            self.needMore = False
            self.photoCount = 0
            self.photoLocations = []
            self.locationsLeft = []
            self.needMore = False
            self.timerCount = 0


        #more button
        elif x < self.size.w/2 + 25 and x > self.size.w/2 - 25 and y < 30 and y > 0:
            self.MoreState = True

        #take photos and add to album
        elif x < self.size.w/2 + 30 and x > self.size.w/2 - 30 and y > 50 and y < 100 and self.MoreState == False and self.measuringOn == True and picTaken == False:
            imageree = photos.capture_image()
            if imageree != None:
                photos.save_image(imageree)
                time.sleep(1)
                self.photoCount += 1
                allAssets = photos.get_assets()
                theImage = allAssets[-1]
                #print("Divider")
                # Find the album or create it:
                try:
                    self.photoLibrary = [a for a in photos.get_albums() if a.title == 'Thread'][0]
                except IndexError:
                    self.photoLibrary = photos.create_album('Thread')
                # Add the file as an asset to the library:
                # asset = photos.create_image_asset(theImage)
                # Add the asset to the album:
                theImage = allAssets[len(allAssets)-1]
                self.photoLibrary.add_assets([theImage])

                current = location.get_location()
                latLongPic = (round(current['latitude'],4), round(current['longitude'],4)) #solved the close points problem using rounding
                self.photoLocations += [latLongPic]









        #compass State: Letters (NWSE) or degrees
        elif x < 325 and x > 275 and y < 100 and y > 50:
            self.compassStat = not(self.compassStat)

        elif self.measuringOn == False and self.checkedOnce == 0:
            #sound.play_effect('arcade:Laser_2')
            self.measuringOn = True
            self.background_color = 'white'
            self.checkedOnce += 1

        elif self.measuringOn == True and self.checkedOnce == 1 and len(self.locations) < 4:
            #sound.play_effect('arcade:Laser_1')
            self.needMore = True

        elif self.measuringOn == True and self.checkedOnce == 1 and len(self.locations) > 3:
            #sound.play_effect('arcade:Laser_1')
            self.needMore = False
            self.measuringOn = False
            self.background_color = 'white'
            self.checkedOnce += 1

        elif self.measuringOn == False and self.checkedOnce == 3:
            #sound.play_effect('arcade:Laser_1')
            self.background_color = 'white'
            self.checkedOnce += 1


run(MyScene(), PORTRAIT)
