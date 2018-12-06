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
        self.lightMode = {"backgroundColor": 'white', \
        "titleColor": (0,0,0,1), \
        "locationCount": (0.4,0.4,0.4,1), \
        "buttonFill": (0.9,0.9,0.9), \
        "buttonText": (0.4,0.4,0.4,1), \
        "compassTint": (0.4,0.4,0.4,1), \
        "compassStroke": (0.4,0.4,0.4), \
        "compassFill1": (0.9,0.9,0.9), \
        "compassStrokeNorth": (1,0.3,0.3), \
        "notificationColor": (0,0,0), \
        "compassStrokeSouth": (0.4,0.4,0.4), \
        "needMoreText": (0.95,0.6,0.6,1), \
        "textColor2": (1,1,1,1), \
        "transparentFill": (0,0,0,0.5), \
        "compassTopFill": (1,1,1,1),  \
        "mapButton": (0.6,0.6,0.95), \
        "otherButtonTexts": (1,1,1,1), \
        "shareButton": (247/255,170/255,103/255), \
        "copiedText": (0.7,0.7,0.7,1), \
        "traceButton": (118/255,191/255,247/255), \
        "SOScolor": (0.95,0.6,0.6), \
        "themeButton": (1,1,1), \
        "themeText": (26/255,26/255,26/255), \
        "photoBorder": (0.2,0.2,0.2), \
        "pathBorder": (0.7,0.7,0.7), \
        "pathScreenFill":(1,1,1), \
        "pathEndColor": (1,0,0), \
        "loopPromptColor": (0,0,0), \
        "loopPromptTextColor": (1,1,1,1), \
        "mainTextColor": (0.4,0.4,0.4,1), \
        "guiderBack": (26/255,26/255,26/255), \
        "moreColor": (0.95,0.6,0.6)
        }
        self.darkMode = {"backgroundColor": (0,0,0), \
        "titleColor": (1,1,1,1), \
        "locationCount": (0.7,0.7,0.7,1), \
        "buttonFill": (26/255,26/255,26/255), \
        "buttonText": (0.7,0.7,0.7,1), \
        "compassTint": (0.4,0.4,0.4,1), \
        "compassStroke": (0.4,0.4,0.4), \
        "compassFill1": (26/255,26/255,26/255), \
        "compassStrokeNorth": (0.7,0.2,0.2), \
        "notificationColor": (0,0,0), \
        "compassStrokeSouth": (0.4,0.4,0.4), \
        "needMoreText": (0.75,0.3,0.3,1), \
        "textColor2": (1,1,1,1), \
        "transparentFill": (0,0,0,0.5), \
        "compassTopFill": (0,0,0),  \
        "mapButton": (26/255,26/255,26/255), \
        "otherButtonTexts": (1,1,1,1), \
        "shareButton": (26/255,26/255,26/255), \
        "copiedText": (0.7,0.7,0.7,1), \
        "traceButton": (26/255,26/255,26/255), \
        "SOScolor": (0.7,0.2,0.2), \
        "photoBorder": (26/255,26/255,26/255), \
        "pathBorder": (26/255,26/255,26/255), \
        "themeButton": (26/255,26/255,26/255), \
        "themeText": (1,1,1), \
        "pathScreenFill":(0,0,0), \
        "pathEndColor": (1,0,0), \
        "loopPromptColor": (0,0,0), \
        "loopPromptTextColor": (1,1,1,1), \
        "mainTextColor": (0.4,0.4,0.4,1), \
        "guiderBack": (26/255,26/255,26/255), \
        "moreColor": (1,0.3,0.3)
        }
        #self.darkRich = {"backgroundColor": (0.05,0.05,0.05), "titleColor": (0,0,0,1), "locationCount": (151/255,126/255,68/255), "buttonFill": (0,0,0), "buttonText": (151/255,126/255,68/255), "compassTint": (0.5,0.5,0.5,1), "compassStroke": (0,0,0), "compassFill1": (0,0,0), "compassStroke2": (0.7,0.2,0.2), "notificationColor": (0,0,0), "compassStrokeSouth": (0.8,0.8,0.8), "needMoreText": (0.75,0.3,0.3,1), "textColor2": (1,1,1,1), "transparentFill": (0,0,0,0.5), "compassTopFill": (0.05,0.05,0.05)}
        #self.darkMode = {"backgroundColor": (0.05,0.05,0.05), "titleColor": (0,0,0,1), "locationCount": (0.4,0.4,0.4,1), "buttonFill": (0,0,0), "buttonText": (0.5,0.5,0.5,1), "compassTint": (0.5,0.5,0.5,1), "compassStroke": (0,0,0), "compassFill1": (0,0,0), "compassStroke2": (0.7,0.2,0.2), "notificationColor": (0,0,0), "compassStrokeSouth": (0.8,0.8,0.8), "needMoreText": (0.75,0.3,0.3,1), "textColor2": (1,1,1,1), "transparentFill": (0,0,0,0.5), "compassTopFill": (0.05,0.05,0.05)}
        #self.blueDark = {"backgroundColor": (15/255,22/255,39/255), "titleColor": (0,0,0,1), "locationCount": (41/255,54/255,59/255), "buttonFill": (0.9,0.9,0.9), "buttonText": (0.4,0.4,0.4,1), "compassTint": (0.4,0.4,0.4,1), "compassStroke": (0.4,0.4,0.4), "compassFill1": (0.9,0.9,0.9), "compassStroke2": (1,0.3,0.3), "notificationColor": (0,0,0), "compassStrokeSouth": (0.4,0.4,0.4), "needMoreText": (0.95,0.6,0.6,1), "textColor2": (1,1,1,1), "transparentFill": (0,0,0,0.5), "compassTopFill": (1,1,1,1)}
        #self.skyMode = {"backgroundColor": 'lightblue', "titleColor": (1,1,1,1), "locationCount": (41/255,54/255,59/255), "buttonFill": (244/255,225/255,137/255), "buttonText": 'white', "compassTint": (0.4,0.4,0.4,1), "compassStroke": (0.4,0.4,0.4), "compassFill1": (244/255,225/255,137/255), "compassStroke2": (1,0.3,0.3), "notificationColor": (0,0,0), "compassStrokeSouth": (0.4,0.4,0.4), "needMoreText": (0.95,0.6,0.6,1), "textColor2": (1,1,1,1), "transparentFill": (0,0,0,0.5), "compassTopFill": (1,1,1,1)}

        self.theme = self.darkMode
        self.background_color = self.theme["backgroundColor"]
        self.measuringOn = False  #am i taking in location coordinates?
        self.functionState = 0  #counter for the mode (things happen sequentially so this works)
        # self.locations = [] #array of recorded coordinates
        #self.locations = [(40.4464,-79.9427),(40.4464,-79.9428),(40.4465,-79.9428),(40.4463,-79.9427),(40.4462,-79.9427),(40.4461,-79.9427),(40.446,-79.9427)]
        #self.locations = [(40.444,-79.9446),(40.444,-79.9445),(40.4441,-79.9446),(40.4441,-79.9447),(40.4442,-79.9447),(40.4443,-79.9447),(40.4444,-79.9447),(40.4444,-79.9448),(40.4445,-79.9447),(40.4446,-79.9447),(40.4446,-79.9446),(40.4447,-79.9446),(40.4448,-79.9446),(40.4449,-79.9445),(40.445,-79.9445)]
        #self.locations = [(40.444,-79.9446),(40.444,-79.9445),(40.4441,-79.9446),(40.4441,-79.9447),(40.4442,-79.9447),(40.4449,-79.9449)]
        #self.locations = [(40.444,-79.9446),(40.444,-79.9445),(40.4441,-79.9446),(40.4441,-79.9447),(40.4442,-79.9447)]
        self.locations = [(40.429,-79.9594),(40.4288,-79.9598),(40.4285,-79.9601),(40.4284,-79.9605),(40.4281,-79.9608),(40.4279,-79.9612),(40.4277,-79.9616),(40.4275,-79.962),(40.4273,-79.9623),(40.4273,-79.9628),(40.4275,-79.9632),(40.4277,-79.9635),(40.4278,-79.9637),(40.4279,-79.9639),(40.4281,-79.9642),(40.4287,-79.965)]
        #self.locations = [(40.429,-79.9594),(40.4288,-79.9598),(40.4285,-79.9601),(40.4284,-79.9605),(40.4281,-79.9608),(40.4279,-79.9612),(40.4277,-79.9616),(40.4275,-79.962),(40.4273,-79.9623),(40.4273,-79.9628),(40.4275,-79.9632),(40.4277,-79.9635),(40.4278,-79.9637),(40.4279,-79.9639),(40.4281,-79.9642),(40.4287,-79.965),(40.4200,-79.965)]
        #self.locations = [(40.429,-79.9594),(40.4288,-79.9598)]#(40.4285,-79.9601),(40.4284,-79.9605)]#(40.4281,-79.9608),(40.4279,-79.9612),(40.4277,-79.9616),(40.4275,-79.962),(40.4273,-79.9623),(40.4273,-79.9628),(40.4275,-79.9632),(40.4277,-79.9635),(40.4278,-79.9637),(40.4279,-79.9639),(40.4281,-79.9642),(40.4287,-79.965),(40.4200,-79.965)]
        self.photoLocations = []
        self.locationsLeft = []
        self.needMore = False #need more values
        self.timerCount = 0 #timer to sync everything
        self.MoreState = False #activate by pressing the bottom dot
        self.loopPrompt = False #if someone travels in a circle
        self.activator = False #a temporary solution to a significant problem
        self.loopPromptState = 0 #to save circled location or not
        self.currentLoc = None
        #self.query = 'safari-http://maps.apple.com/?q=%s,%s' #apple maps
        self.query = 'safari-https://www.google.com/maps/dir/' #google maps
        self.compassStat = False  #compass in NSEW mode or degrees
        self.pathState = False
        self.clipState = False
        self.photoCount = 0
        self.imageMode = False
        self.imageModeOpen = False
        self.photoLibrary = None
        self.currentImage = None
        self.ui_image = None
        self.photoWidth = 0
        self.photoHeight = 0

        self.heightFrame = 0
        self.widthFrame = 0

        self.heightPhoto = 0
        self.widthPhoto = 0

        self.halfScreenFrame = 0
        self.halfScreen = 0

        self.img = None


        self.themeSwitch = 1

        #Organization/Design
        self.scale = self.size.w/10 #scaling and UI Design
        self.centerX = self.size.w/2
        self.centerY = self.size.h/2
        self.centerX2 = self.size.w/2
        self.centerY2 = self.size.h * (1/2)-self.scale*3.5

        #updates start
        motion.start_updates()   #motion updates for compass
        location.start_updates()    #location start updates


    #redraw function
    def draw(self):
        self.background_color = self.theme["backgroundColor"]

        time.sleep(0.01) #time between each redraw
        self.timerCount += 1 #add to the timer to animate and do things

        #Title Text
        tint(self.theme["titleColor"])
        # text('Thread', font_name='Courier', font_size=16.0, x=self.centerX2, y=self.centerY2+self.scale+400, alignment=5)

        #Locations recorded count
        tint(self.theme["locationCount"])
        locationCountText = "Locations: " + str(len(self.locations))
        text(locationCountText, font_name='Verdana', font_size=10, x=50, \
        y=self.centerY2+self.scale+400, alignment=5)

        def remainingText(self):
            locationLeftText = "Remaining: " + str(len(self.locationsLeft))
            text(locationLeftText, font_name='Verdana', font_size=10, \
            x=self.size.x-60, y=self.centerY2+self.scale+400, alignment=5)

        if self.functionState == 4:
            remainingText(self)

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
        def makeResetButton(self):
            fill(self.theme["buttonFill"])
            stroke_weight(0)
            ellipse(self.centerX2-self.scale*3-self.scale,\
            self.centerY2-self.scale-130,self.scale*2,self.scale*2)
            tint(self.theme["buttonText"])
            text('Reset', font_name='Verdana', font_size=12.0, \
            x=self.centerX2-112, y=self.centerY2+self.scale-167, alignment=5)

        #LOCATION GET
        current = location.get_location()
        latLong = (round(current['latitude'],4), round(current['longitude'],4))
        #solved the close points problem using rounding
        picTaken = latLong in self.photoLocations
        #print(latLong)

        #orientation calculation
        yawSin = math.sin(math.radians(yaw))
        yawCos = math.cos(math.radians(yaw))

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

        def drawCompass(self):
            #compass draw
            tint(self.theme["compassTint"])
            stroke(self.theme["compassStroke"])
            stroke_weight(0)
            fill(self.theme["compassFill1"])
            ellipse(self.centerX2+self.scale*3-self.scale,self.centerY2-\
            self.scale-130,self.scale*2,self.scale*2)
            stroke_weight(0)
            ellipse(self.centerX2+self.scale*3-self.scale+3,self.centerY2-\
            self.scale-127,self.scale*1.85,self.scale*1.85)
            ellipse(self.centerX2+self.scale*3-self.scale+6,self.centerY2-\
            self.scale-124,self.scale*1.7,self.scale*1.7)

            stroke_weight(2)
            stroke(self.theme["compassStrokeSouth"])
            line(self.centerX2-yawCos*self.scale+self.scale*3,self.centerY2-\
            yawSin*self.scale-130,self.centerX2+yawCos*self.scale+\
            self.scale*3,self.centerY2+yawSin*self.scale-130)
            stroke(self.theme["compassStrokeNorth"])
            line(300,72.5,self.centerX2+yawCos*self.scale+self.scale*3,\
            self.centerY2+yawSin*self.scale-130)

            #circle on top of compass
            stroke_weight(0)
            stroke(self.theme["compassStroke"])
            fill(self.theme["compassTopFill"])
            ellipse(self.centerX2+self.scale*3-self.scale+9.5,\
            self.centerY2-self.scale-120.5,self.scale*1.5,self.scale*1.5)

            #compass text
            tint(self.theme["buttonText"])
            if self.compassStat == False:
                text(directionText(yaw), font_name='Verdana', font_size=10.0, \
                x=self.centerX2+self.scale*3, y=self.centerY2+self.scale-167, \
                alignment=5)
            else:
                tempYaw = yaw+180+90
                if tempYaw > 360:
                    tempYaw = tempYaw % 360
                yawString = str(int(round(tempYaw,0))) + chr(186)
                text(yawString, font_name='Verdana', font_size=10.0, \
                x=self.centerX2+self.scale*3, y=self.centerY2+self.scale-167, \
                alignment=5)


        #Center Screen Text
        def centerScreenText(self):
            tint(self.theme["mainTextColor"])
            if self.measuringOn == False and self.functionState == 0:
                text('Tap to Start', font_name='Verdana', font_size=16.0, \
                x=self.centerX2, y=self.centerY2+self.scale+150, alignment=5)
            elif self.measuringOn == True and self.functionState == 1:
                if self.timerCount//50 % 3 == 0:
                    text('Recording Journey.', font_name='Verdana', \
                    font_size=16.0, x=self.centerX2, \
                    y=self.centerY2+self.scale+150, alignment=5)
                elif self.timerCount//50 % 3 == 1:
                    text('Recording Journey..', font_name='Verdana', \
                    font_size=16.0, x=self.centerX2, \
                    y=self.centerY2+self.scale+150, alignment=5)
                elif self.timerCount//50 % 3 == 2:
                    text('Recording Journey...', font_name='Verdana', \
                    font_size=16.0, x=self.centerX2, \
                    y=self.centerY2+self.scale+150, alignment=5)
                text('Tap to Stop', font_name='Verdana', font_size=16.0, \
                x=self.centerX2, y=self.centerY2+self.scale+120, alignment=5)
            elif self.measuringOn == False and self.functionState == 2:
                text('Calculating', font_name='Verdana', font_size=16.0, \
                x=self.centerX2, y=self.centerY2+self.scale+150, alignment=5)


            #if not enough values are recorded
            tint(self.theme["needMoreText"])
            if self.needMore == True:
                text("Need to record more locations.", font_name='Verdana', \
                font_size=16.0, x=self.size.x/2, y=self.size.y/2-20, \
                alignment=5)


        makeResetButton(self)

        drawCompass(self)

        centerScreenText(self)

        #When measuring is on record locations and put into array
        def measuring(self):
            tint(self.theme["buttonText"])
            if picTaken == False:
                #camera mode
                stroke_weight(0)
                fill(self.theme["buttonFill"])
                tint(self.theme["buttonText"])
                ellipse(self.size.x/2-self.scale/2,0-self.scale/2+72,\
                self.scale,self.scale)
                text('Snap', font_name='Verdana', font_size=8.0, \
                x=self.centerX2, y=self.centerY2+self.scale-167, alignment=5)

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

        if self.measuringOn == True:
            measuring(self)

        #after measuring is off, setup array to use
        elif self.functionState == 2 and len(self.locations) > 3:
            self.locationsLeft = copy.deepcopy(self.locations)

            #do this to avoid tapping too early
            self.functionState += 1

        #after the array set up, tap to get back to where you were
        elif self.functionState == 3:
            tint(self.theme["mainTextColor"])
            text('Tap to return to start', font_name='Verdana', \
            font_size=16.0, x=self.centerX2, \
            y=self.centerY2+self.scale+150, alignment=5)

        #The return back..
        elif self.functionState == 4:

            #tracing back steps
            if latLong in self.locationsLeft:
                 loc = self.locationsLeft.index(latLong)
                 # self.locationsLeft.remove(latLong)
                 self.locationsLeft = self.locationsLeft[0:loc]

            x,y = self.locations[-1]
            x = round(x,10)
            y = round(y,10)

            loc = "[" + str(x) + ", " + str(y) + "]"
            fill(self.theme["buttonFill"])
            stroke(self.theme["titleColor"])
            stroke_weight(0)
            # rect(0,560,self.size.w,50)
            # # text('Destination:', font_name='Verdana', font_size=12.0, x=70, y=550, alignment=5)
            # # text(loc, font_name='Verdana', font_size=12.0, x=230, y=550, alignment=5)

            totalDistanceTraveled = 0
            for i in range(len(self.locations)-1):
                firstPosX, firstPosY = self.locations[i]
                nextPosX, nextPosY = self.locations[i+1]
                dist = ((nextPosX - firstPosX)**2 + \
                (nextPosY - firstPosY)**2)**0.5

                totalDistanceTraveled += dist

            # text('Distance Traveled:', font_name='Verdana', font_size=12.0, x=70, y=585, alignment=5)
            # text(str(totalDistanceTraveled), font_name='Verdana', font_size=12.0, x=230, y=585, alignment=5)

            textPosX = self.size.x/2
            textPosY = self.size.y/2


            if (len(self.locationsLeft) > 1):

                # if (len(self.locationsLeft) > 8):
                #     currPosX, currPosY = self.locationsLeft[-1]
                #     backPosX, backPosY = self.locationsLeft[-5]
                #     nextPosX, nextPosY = self.locationsLeft[-6]
                #     secondPosX, secondPosY = self.locationsLeft[-7]
                #     thirdPosX, thirdPosY = self.locationsLeft[-8]
                #
                #     xNextAverage = (backPosX + nextPosX + \
                #     secondPosX + thirdPosX)/4
                #
                #     yNextAverage = (backPosY + nextPosY + \
                #     secondPosY + thirdPosY)/4


                if (len(self.locationsLeft) > 4):
                    currPosX, currPosY = self.locationsLeft[-1]
                    nextPosX, nextPosY = self.locationsLeft[-2]
                    secondPosX, secondPosY = self.locationsLeft[-3]
                    thirdPosX, thirdPosY = self.locationsLeft[-4]
                    fourthPosX, fourthPosY = self.locationsLeft[-5]


                    xNextAverage = (nextPosX + secondPosX + thirdPosX + fourthPosX)/4
                    yNextAverage = (nextPosY + secondPosY + thirdPosY + fourthPosY)/4

                elif (len(self.locationsLeft) > 2):
                    currPosX, currPosY = self.locationsLeft[-1]
                    nextPosX, nextPosY = self.locationsLeft[-2]
                    secondPosX, secondPosY = self.locationsLeft[-3]

                    xNextAverage = (nextPosX + secondPosX)/2
                    yNextAverage = (nextPosY + secondPosY)/2

                elif (len(self.locationsLeft) > 1):
                    currPosX, currPosY = self.locationsLeft[-1]
                    nextPosX, nextPosY = self.locationsLeft[-2]

                    xNextAverage = (nextPosX)/1
                    yNextAverage = (nextPosY)/1

                xVal3 = math.cos(math.radians(xNextAverage))*\
                math.sin(math.radians(yNextAverage-currPosY))

                yVal3 = math.cos(math.radians(currPosX))*\
                math.sin(math.radians(xNextAverage))-\
                math.sin(math.radians(currPosX))*\
                math.cos(math.radians(xNextAverage))*\
                math.cos(math.radians(yNextAverage-currPosY))

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


                # text(str(trueDegree), font_name='Verdana', font_size=16.0, x=self.centerX2, y=self.centerY2+self.scale+150, alignment=5)

                #experimental point on arrow. Works well! but code is ugly. Will implement for loop later
                def pointMaker(self,roll,pitch, yaw):
                    stroke_weight(20)
                    stroke(self.theme["guiderBack"])
                    line(self.centerX2-trueDegreeCos*130, \
                    self.centerY-trueDegreeSin*130, \
                    self.centerX2+trueDegreeCos*130, \
                    self.centerY+trueDegreeSin*130 )
                    stroke(self.theme["compassStrokeNorth"])
                    for i in range(20):
                        stroke_weight(20-i)
                        line(self.centerX2+trueDegreeCos*(130+(i*2)), \
                        self.centerY+trueDegreeSin*(130+(i*2)), \
                        self.centerX2 ,self.centerY )

                pointMaker(self,roll,pitch, yaw)

                stroke_weight(0)


                #images on the trip back
                if latLong in self.photoLocations \
                and self.imageModeOpen == False:

                    photoLoc = len(self.photoLocations) - \
                    self.photoLocations.index(latLong)

                    self.imageMode = True

                    tint(self.theme["textColor2"])
                    fill(self.theme["notificationColor"])
                    stroke(self.theme["notificationColor"])

                    rect(0,150,self.size.w,50)
                    text("Landmark! Tap here to see!", font_name='Verdana', \
                    font_size=16.0, x=self.centerX2, y=150+25, alignment=5)
                    self.currentImage = self.photoLibrary.assets[-photoLoc]
                    self.photoWidth = self.currentImage.pixel_width
                    self.photoHeight = self.currentImage.pixel_height

                    self.ui_image = self.currentImage.get_ui_image()

            else:
                text("Welcome Back.", font_name='Verdana', font_size=16.0, \
                x=textPosX, y=textPosY, alignment=5)

        #SOS Button and
        fill(self.theme["needMoreText"])
        tint(self.theme["textColor2"])
        if self.MoreState == True:
            #to seperate the active buttons from the non active ones
            fill(self.theme["transparentFill"])
            rect(0,0,self.size.x,self.size.y)
            #SOS Button
            fill(self.theme["needMoreText"])
            tint(self.theme["textColor2"])
            ellipse(self.centerX2-0.0-self.scale,self.centerY2-self.scale-130,\
            self.scale*2,self.scale*2)
            text('SOS', font_name='Verdana', font_size=12.0, x=self.centerX2, \
            y=self.centerY2+self.scale-167, alignment=5)

            #MAP Button
            if len(self.locations) >= 2:
                fill(self.theme["mapButton"])
                tint(self.theme["otherButtonTexts"])
                ellipse(self.centerX2-self.scale*3-self.scale,\
                self.centerY2-self.scale-20,self.scale*2,self.scale*2)
                text('Map View', font_name='Verdana', font_size=12.0, \
                x=self.centerX2-112, y=self.centerY2+self.scale-57,alignment=5)

                fill(self.theme["shareButton"])
                tint(self.theme["otherButtonTexts"])
                ellipse(self.centerX2-self.scale,self.centerY2-self.scale-20,\
                self.scale*2,self.scale*2)
                text('Share', font_name='Verdana', font_size=12.0, \
                x=self.centerX2, y=self.centerY2+self.scale-57, alignment=5)

                tint(self.theme["copiedText"])
                if self.clipState == True:
                    text('Copied to Clipboard', font_name='Verdana', \
                    font_size=16.0, x=self.size.x/2, y=self.size.y/2-65, \
                    alignment=5)


            fill(self.theme["traceButton"])
            tint(self.theme["otherButtonTexts"])
            ellipse(self.centerX2+self.scale*3-self.scale,\
            self.centerY2-self.scale-20,self.scale*2,self.scale*2)
            text('Trace', font_name='Verdana', font_size=12.0, \
            x=self.centerX2+112, y=self.centerY2+self.scale-57, alignment=5)

            #SOS Button
            fill(self.theme["SOScolor"])
            tint(self.theme["otherButtonTexts"])
            ellipse(self.centerX2-0.0-self.scale,\
            self.centerY2-self.scale-130,self.scale*2,self.scale*2)
            text('SOS', font_name='Verdana', font_size=12.0, \
            x=self.centerX2, y=self.centerY2+self.scale-167, alignment=5)

            fill(self.theme["themeButton"])
            tint(self.theme["themeText"])
            ellipse(self.centerX2-self.scale,self.size.y-115,\
            self.scale*2,self.scale*2)
            text('Theme', font_name='Verdana', font_size=12.0, \
            x=self.centerX2, y=self.size.y-77, alignment=5)



        #More button at the bottom of screen
        elif self.MoreState == False:
            fill(self.theme["moreColor"])
            ellipse(self.size.x/2-self.scale/2,0-self.scale/2-5,\
            self.scale,self.scale)

        if self.imageModeOpen == True:
            fill(0,0,0,0.5)
            rect(0,0,self.size.x, self.size.y)
            fill(self.theme["photoBorder"])
            rect(5, self.halfScreenFrame, self.widthFrame, self.heightFrame)


        def drawPath(self):
            fill(self.theme["pathBorder"])
            rect(14,self.size.y/2-55,self.size.x-28,self.size.y/3+12)
            fill(self.theme["pathScreenFill"])
            rect(19,self.size.y/2-50,self.size.x-38,self.size.y/3+2)

            tint(self.theme["pathEndColor"])
            fill(self.theme["pathEndColor"])
            stroke(self.theme["pathEndColor"])
            stroke_weight(2)
            iPointX, iPointY = self.locations[0]
            newLocs = [(0,0)]
            maxDiffX = 0
            maxDiffY = 0
            xSepVals = []
            ySepVals = []

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
            jumpX = 0 - miniX
            evenedLocsX = []
            for val in xSepVals:
                evenedLocsX += [val + jumpX]

            miniY = min(ySepVals)
            jumpY = 0 - miniY
            evenedLocsY = []
            for val in ySepVals:
                evenedLocsY += [val + jumpY]

            xCenter = self.size.x/2
            yCenter = self.size.y/2-50 + 2
            colorCount = len(newLocs)
            for i in range(len(newLocs)-1):
                xLoc1, yLoc1 = evenedLocsX[i], evenedLocsY[i]
                xLoc2, yLoc2 = evenedLocsX[i+1], evenedLocsY[i+1]
                #add if statements
                if self.theme == self.darkMode:
                    stroke(((255/colorCount)*i)/255, 0, 0.15)
                    fill(((255/colorCount)*i)/255, 0, 0.15)
                elif self.theme == self.lightMode:
                    stroke(((255/colorCount)*i)/255, 0, 0)
                    fill(((255/colorCount)*i)/255, 0, 0)
                #text(str(i),font_name='Verdana', font_size=4.0, x=(335/generalMaxDiff)*xLoc1+20, y=(222/generalMaxDiff)*yLoc1+yCenter+5, alignment=5)
                #line(xCenter + xLoc1, yCenter + yLoc1, xCenter + xLoc2, yCenter + yLoc2)
                line((335/generalMaxDiff)*xLoc1+20,(222/generalMaxDiff)*\
                yLoc1+yCenter, (335/generalMaxDiff)*xLoc2+20,\
                (222/generalMaxDiff)*yLoc2+yCenter)

                ellipse((335/generalMaxDiff)*xLoc1+20-2,(222/generalMaxDiff)*\
                yLoc1+yCenter-2,4,4)

            ellipse((335/generalMaxDiff)*evenedLocsX[-1]+20-2,\
            (222/generalMaxDiff)*evenedLocsY[-1]+yCenter-2,4,4)


#-----------Draw Path State---------------------------------------------------
        if self.pathState == True and len(self.locations) > 0:
            drawPath(self)

#-----------END OF PATHSTATE---------------------------------------------------

        def loopPromptBox(self):
            fill(self.theme["loopPromptColor"])
            stroke_weight(0)
            #prompt for the loop
            rect(50,self.size.y/2-50,self.size.x-100,self.size.y/6+40)
            tint(self.theme["loopPromptTextColor"])
            text("Stop Moving!", font_name='Verdana', font_size=18.0, \
            x=self.size.x/2, y=self.size.y/2+65, alignment=5)
            text("Looks like you\'ve made a loop", font_name='Verdana', \
            font_size=13.0, x=self.size.x/2, y=self.size.y/2+38, alignment=5)
            stroke(self.theme["loopPromptTextColor"])
            stroke_weight(3)
            line(50, self.size.y/2, self.size.x-50, self.size.y/2)
            line(self.size.x/2, self.size.y/2-50, self.size.x/2, self.size.y/2)
            text("Continue", font_name='Verdana', font_size=15.0, \
            x=self.size.x/2-70, y=self.size.y/2-25, alignment=5)
            text("Break", font_name='Verdana', font_size=15.0, \
            x=self.size.x/2+70, y=self.size.y/2-25, alignment=5)

        #prompt when the user goes in a loop or crosses paths with the recorded path
        if self.loopPrompt == True:
            loopPromptBox(self)





    #tells you if the screen is touched and where
    def touch_began(self, touch):

        def mapView(self):
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


        def openLandmark(self):
            sound.play_effect('Click_1')
            self.imageModeOpen = True
            self.imageMode = False

            self.heightPhoto = (self.photoHeight/self.photoWidth) * \
            (self.size.x-20)
            self.widthPhoto = (self.photoWidth/self.photoWidth) * \
            (self.size.x-20)


            self.heightFrame = self.heightPhoto+10
            self.widthFrame = self.widthPhoto+10


            self.halfScreenFrame = self.size.y/2 - self.heightFrame/2
            self.halfScreen = self.size.y/2 - self.heightPhoto/2

            self.img = ui.Button(name='image')
            self.img.frame = (10,self.halfScreen,self.widthPhoto,self.heightPhoto)
            self.img.background_image = self.ui_image
            self.img.enable = False
            self.img.hidden = False
            self.view.add_subview(self.img)


        current = location.get_location()
        latLong = (round(current['latitude'],4), round(current['longitude'],4)) #solved the close points problem using rounding
        picTaken = latLong in self.photoLocations


        x,y = touch.location


        if self.imageModeOpen == True:
            self.imageModeOpen = False
            self.img.hidden = True

        if self.loopPrompt == True:
            if x > 50 and x < self.size.x/2 and y < self.size.y/2 \
            and y > self.size.y/2 - 50:
                self.loopPrompt = False
                self.loopPromptState = 1
            elif x > self.size.x/2 and x < self.size.x-50 \
            and y < self.size.y/2 and y > self.size.y/2 - 50:
                self.loopPrompt = False
                self.loopPromptState = 2

        elif self.MoreState == True:
            #SOS State
            if x < self.size.w/2 + 30 and x > self.size.w/2 - 30 \
            and y > 50 and y < 100 and self.MoreState == True:
                webbrowser.open('tel:911')

            #MapView
            elif x < 100 and x > 50 and y < 220 and y > 160 and \
            len(self.locations) >= 2:
                mapView(self)

            elif x < self.size.x/2+40 and x > self.size.x/2-40 and \
            y < 220 and y > 160 and len(self.locations) >= 2:
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

            elif x < self.size.x-50 and x > self.size.x-100 and y < 220 \
            and y > 160 and len(self.locations) > 2:
                self.pathState = True

            elif x < self.size.w/2 + 30 and x > self.size.w/2 - 30 \
            and y > self.size.y-95-40 and y < self.size.y-95+40:
                self.themeSwitch += 1
                if self.themeSwitch % 2  == 0:
                    self.theme = self.lightMode
                elif self.themeSwitch % 2 == 1:
                    self.theme = self.darkMode

            else:
                self.MoreState = False
                self.clipState = False
                self.pathState = False


        #open landmark
        elif y > 150 and y < 200 and self.imageMode == True:
            openLandmark(self)

        elif y < 150 and y > 200 and self.imageMode == True:
            self.imageMode = False

        #reset button
        elif x < 100 and x > 50 and y < 100 and y > 50:
            self.measuringOn = False
            self.functionState = 0
            self.background_color = self.theme["backgroundColor"]
            self.locations = []
            self.needMore = False
            self.photoCount = 0
            self.photoLocations = []
            self.locationsLeft = []
            self.needMore = False
            self.timerCount = 0

        #more button
        elif x < self.size.w/2 + 25 and x > self.size.w/2 - 25 and y < 30 \
        and y > 0:
            self.MoreState = True

        #take photos and add to album
        elif x < self.size.w/2 + 30 and x > self.size.w/2 - 30 \
        and y > 50 and y < 100 and self.MoreState == False and \
        self.measuringOn == True and picTaken == False:
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
                    self.photoLibrary = [a for a in photos.get_albums() \
                    if a.title == 'Thread'][0]
                except IndexError:
                    self.photoLibrary = photos.create_album('Thread')

                theImage = allAssets[len(allAssets)-1]
                self.photoLibrary.add_assets([theImage])

                self.photoLocations += [latLong]

        #compass State: Letters (NWSE) or degrees
        elif x < 325 and x > 275 and y < 100 and y > 50:
            self.compassStat = not(self.compassStat)

        elif self.measuringOn == False and self.functionState == 0:
            #sound.play_effect('arcade:Laser_2')
            self.measuringOn = True
            self.background_color = self.theme["backgroundColor"]
            self.functionState += 1

        elif self.measuringOn == True and self.functionState == 1 \
        and len(self.locations) < 4:
            #sound.play_effect('arcade:Laser_1')
            self.needMore = True

        elif self.measuringOn == True and self.functionState == 1 \
        and len(self.locations) > 3:
            #sound.play_effect('arcade:Laser_1')
            self.needMore = False
            self.measuringOn = False
            self.background_color = self.theme["backgroundColor"]
            self.functionState += 1

        elif self.measuringOn == False and self.functionState == 3:
            #sound.play_effect('arcade:Laser_1')
            self.background_color = self.theme["backgroundColor"]
            self.functionState += 1


run(MyScene(), PORTRAIT)
