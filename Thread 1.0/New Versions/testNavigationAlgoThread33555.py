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

#class for the whole scene
class MyScene (Scene):

    #initialize variables
    def setup(self):
        global scale
        self.background_color = 'white'
        self.measuringOn = False  #am i taking in location coordinates?
        self.checkedOnce = 0  #counter for the mode (things happen sequentially so this works)
        self.locations = [] #array of recorded coordinates
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
        self.radius = scale

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

        ############# redraw screen ############
        #Reset Button
        fill(0.9,0.9,0.9)
        stroke_weight(0)
        ellipse(self.centerX2-scale*3-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)
        tint(0.4,0.4,0.4,1)
        text('Reset', font_name='Verdana', font_size=12.0, x=self.centerX2-112, y=self.centerY2+self.radius-167, alignment=5)




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
#---------------------------------------------------------
#---------------------------------------------------------
#-----Loop Prompt Works? Test it.----------
#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------
#---------------------------------------------------------


        #after measuring is off, setup array to use (states Calculating)
        elif self.checkedOnce == 2 and len(self.locations) > 0:
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


            if (len(self.locationsLeft) > 0):
                # currPosX, currPosY = self.locationsLeft[-1]
                # nextPosX, nextPosY = self.locationsLeft[-2]
                # secondPosX, secondPosY = self.locationsLeft[-3]
                # thirdPosX, thirdPosY = self.locationsLeft[-4]

                currPosX, currPosY = [40.4465, 79.9427]
                nextPosX, nextPosY = [40.4465, 79.9428]
                secondPosX, secondPosY = [40.4466, 79.9428]
                thirdPosX, thirdPosY = [40.4466, 79.9429]


                differenceX1 = nextPosX - currPosX
                differenceY1 = nextPosY - currPosY
                differenceX2 = secondPosX - currPosX
                differenceY2 = secondPosY - currPosY
                differenceX3 = thirdPosX - currPosX
                differenceY3 = thirdPosY - currPosY
                degreeAngle1 = 0
                degreeAngle2 = 0
                degreeAngle3 = 0

                if differenceX1 == 0:
                    if currPosX > nextPosX:
                        degreeAngle1 = 180.0
                    else:
                        degreeAngle1 = 0.0
                else:
                    directionAngle1 = math.atan(differenceY1/differenceX1)
                    degreeAngle1 = math.degrees(directionAngle1)

                #point in right direction
                if (currPosX <= nextPosX and currPosY < nextPosY):
                    degreeAngle1 = 90 - round(degreeAngle1, 4)
                elif (currPosX <= nextPosX and currPosY >= nextPosY):
                    degreeAngle1 = 90 - round(degreeAngle1, 4)
                elif (currPosX >= nextPosX and currPosY >= nextPosY):
                    degreeAngle1 = round(degreeAngle1, 4) + 180
                elif (currPosX >= nextPosX and currPosY <= nextPosY):
                    degreeAngle1 = round(degreeAngle1, 4) + 180


                if differenceX2 == 0:
                    if currPosX > secondPosX:
                        degreeAngle2 = 180.0
                    else:
                        degreeAngle2 = 0.0
                else:
                    directionAngle2 = math.atan(differenceY2/differenceX2)
                    degreeAngle2 = math.degrees(directionAngle2)

                #point in right direction
                if (currPosX <= secondPosX and currPosY <= secondPosY):
                    degreeAngle2 = round(degreeAngle2, 4)
                elif (currPosX <= secondPosX and currPosY >= secondPosY):
                    degreeAngle2 = round(degreeAngle2, 4) + 180
                elif (currPosX >= secondPosX and currPosY >= secondPosY):
                    degreeAngle2 = round(degreeAngle2, 4) + 180
                elif (currPosX >= secondPosX and currPosY <= secondPosY):
                    degreeAngle2 = round(degreeAngle2, 4) + 360

                if differenceX3 == 0:
                    if currPosX > thirdPosX:
                        degreeAngle3 = 180.0
                    else:
                        degreeAngle3 = 0.0
                else:
                    directionAngle3 = math.atan(differenceY3/differenceX3)
                    degreeAngle3 = math.degrees(directionAngle3)

                #point in right direction
                if (currPosX <= thirdPosX and currPosY <= thirdPosY):
                    degreeAngle3 = round(degreeAngle3, 4)
                elif (currPosX <= thirdPosX and currPosY >= thirdPosY):
                    degreeAngle3 = round(degreeAngle3, 4) + 180
                elif (currPosX >= thirdPosX and currPosY >= thirdPosY):
                    degreeAngle3 = round(degreeAngle3, 4) + 180
                elif (currPosX >= thirdPosX and currPosY <= thirdPosY):
                    degreeAngle3 = round(degreeAngle3, 4) + 360

                trueDegree = (degreeAngle1 + degreeAngle2 + degreeAngle3)/3
                text(str(trueDegree), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY, alignment=5)
                text(str(degreeAngle1), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY-20, alignment=5)
                text(str(degreeAngle2), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY-40, alignment=5)
                text(str(degreeAngle3), font_name='Verdana', font_size=16.0, x=textPosX, y=textPosY-60, alignment=5)


                # #tracing back steps
                # current = location.get_location()
                # latLong = (round(current['latitude'],4), round(current['longitude'],4)) #solved the close points problem using rounding
                # if latLong in self.locationsLeft:
                #     loc = self.locationsLeft.index(latLong)
                #     # self.locationsLeft.remove(latLong)
                #     self.locationsLeft = self.locationsLeft[0:loc]
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

            #SOS Button
            fill(0.95,0.6,0.6)
            tint(1,1,1,1)
            ellipse(self.centerX2-0.0-self.radius,self.centerY2-self.radius-130,self.radius*2,self.radius*2)
            text('SOS', font_name='Verdana', font_size=12.0, x=self.centerX2, y=self.centerY2+self.radius-167, alignment=5)

        #More button at the bottom of screen
        elif self.MoreState == False:
            ellipse(self.size.x/2-self.radius/2,0-self.radius/2-5,self.radius,self.radius)



        if self.loopPrompt == True:
            fill(0,0,0)
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
        x,y = touch.location

        if self.loopPrompt == True:
            if x > 50 and x < self.size.x/2 and y < self.size.y/2 and y > self.size.y/2 - 50:
                self.loopPrompt = False
                self.loopPromptState = 1
            elif x > self.size.x/2 and x < self.size.x-50 and y < self.size.y/2 and y > self.size.y/2 - 50:
                self.loopPrompt = False
                self.loopPromptState = 2

#-------------------------------------------
#-------------------------------------------
#-------------------------------------------





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
            else:
                self.MoreState = False

        #reset button
        elif x < 100 and x > 50 and y < 100 and y > 50:
            self.measuringOn = False
            self.checkedOnce = 0
            self.background_color = 'white'
            self.locations = []
            self.needMore = False

        #more button
        elif x < self.size.w/2 + 25 and x > self.size.w/2 - 25 and y < 30 and y > 0:
            self.MoreState = True

        #compass State: Letters (NWSE) or degrees
        elif x < 325 and x > 275 and y < 100 and y > 50:
            self.compassStat = not(self.compassStat)

        elif self.measuringOn == False and self.checkedOnce == 0:
            #sound.play_effect('arcade:Laser_2')
            self.measuringOn = True
            self.background_color = 'white'
            self.checkedOnce += 1

        elif self.measuringOn == True and self.checkedOnce == 1 and len(self.locations) < 0:
            #sound.play_effect('arcade:Laser_1')
            self.needMore = True

        elif self.measuringOn == True and self.checkedOnce == 1 and len(self.locations) > 0:
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
