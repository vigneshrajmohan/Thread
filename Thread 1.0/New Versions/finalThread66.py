#Thread: Traverse in Reverse
#by Vignesh Rajmohan
#15-112 Term Project
#Mentor: Tegjeev Singh
#Professors: Kelly Rivers and Mike Taylors

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#can only be run on Pythonista
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
from time import gmtime, strftime


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

        theHour = int(strftime("%H", gmtime())) #if the hour is between 6PM and 6AM put into dark Mode
        if theHour == 23 or theHour < 11:
            self.theme = self.darkMode
            self.themeSwitch = 1
        else: #else put into lightMode
            self.theme = self.lightMode
            self.themeSwitch = 2

        self.background_color = self.theme["backgroundColor"]
        self.measuringOn = False  #am i taking in location coordinates?
        self.functionState = 0  #counter for the mode
        #(things happen sequentially so this works)
        # self.locations = [] #array of recorded coordinates
        self.locations = [(40.429,-79.9594),(40.4288,-79.9598),(40.4285,-79.9601),(40.4284,-79.9605),(40.4281,-79.9608),(40.4279,-79.9612),(40.4277,-79.9616),(40.4275,-79.962),(40.4273,-79.9623),(40.4273,-79.9628),(40.4275,-79.9632),(40.4277,-79.9635),(40.4278,-79.9637),(40.4279,-79.9639),(40.4281,-79.9642),(40.4287,-79.965)]
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

        #photo displaying variables
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

        #image currently
        self.img = None

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
        #set the background color to the theme's background color
        self.background_color = self.theme["backgroundColor"]

        time.sleep(0.05) #time between each redraw
        self.timerCount += 1 #add to the timer to animate and do things

        #Title Text
        tint(self.theme["titleColor"])
        # text('Thread', font_name='Courier', font_size=16.0, x=self.centerX2, y=self.centerY2+self.scale+400, alignment=5)

        #Locations recorded count
        tint(self.theme["locationCount"])
        locationCountText = "Locations: " + str(len(self.locations))
        text(locationCountText, font_name='Verdana', font_size=10, x=50, \
        y=self.centerY2+self.scale+400, alignment=5)

        #print the amount of locations left on the journey
        def remainingText(self):
            locationLeftText = "Remaining: " + str(len(self.locationsLeft))
            text(locationLeftText, font_name='Verdana', font_size=10, \
            x=self.size.x-60, y=self.centerY2+self.scale+400, alignment=5)

        if self.functionState == 4:
            remainingText(self)

        #motion vectors
        gravX,gravY,gravZ= motion.get_gravity()
        gravityVectors=motion.get_attitude()
        pitch = gravityVectors[0]
        roll = gravityVectors[1]
        yaw = gravityVectors[2]

        #convert yaw to degrees
        yaw = -yaw*180/math.pi
        pitch = -pitch*180/math.pi
        roll = -roll*180/math.pi

        #draw Reset Button
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
        #latLong will be the location used through every redraw
        latLong = (round(current['latitude'],4), round(current['longitude'],4))
        #solved the close points problem using rounding
        picTaken = latLong in self.photoLocations

        #orientation calculation
        yawSin = math.sin(math.radians(yaw))
        yawCos = math.cos(math.radians(yaw))

        #derive the direction (NSEW) from the degrees
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

        #draw the compass on the bottom right and make it work
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


        #Center Screen Text (decide what is being displayed)
        def centerScreenText(self):
            tint(self.theme["mainTextColor"])
            if self.measuringOn == False and self.functionState == 0:
                text('Tap to Start', font_name='Verdana', font_size=16.0, \
                x=self.centerX2, y=self.centerY2+self.scale+150, alignment=5)
            elif self.measuringOn == True and self.functionState == 1:
                if self.timerCount//20 % 3 == 0:
                    text('Recording Journey.', font_name='Verdana', \
                    font_size=16.0, x=self.centerX2, \
                    y=self.centerY2+self.scale+150, alignment=5)
                elif self.timerCount//20 % 3 == 1:
                    text('Recording Journey..', font_name='Verdana', \
                    font_size=16.0, x=self.centerX2, \
                    y=self.centerY2+self.scale+150, alignment=5)
                elif self.timerCount//20 % 3 == 2:
                    text('Recording Journey...', font_name='Verdana', \
                    font_size=16.0, x=self.centerX2, \
                    y=self.centerY2+self.scale+150, alignment=5)
                text('Tap to Stop', font_name='Verdana', font_size=16.0, \
                x=self.centerX2, y=self.centerY2+self.scale+120, alignment=5)
            elif self.measuringOn == False and self.functionState == 2:
                text('Calculating', font_name='Verdana', font_size=16.0, \
                x=self.centerX2, y=self.centerY2+self.scale+150, alignment=5)


            #if not enough values are recorded, say that they need more
            tint(self.theme["needMoreText"])
            if self.needMore == True:
                text("Need to record more locations.", font_name='Verdana', \
                font_size=16.0, x=self.size.x/2, y=self.size.y/2-20, \
                alignment=5)


        makeResetButton(self)

        drawCompass(self)

        centerScreenText(self)

        #When measuring is on record locations and put into array of locations
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

            #to avoid repeats, only add if the location is not in the list
            if latLong not in self.locations:
                self.locations += [latLong]
                if self.activator == True:
                    self.activator = False
                self.loopPromptState = 0

            #if you travel in a loop ask the user if they want to keep the loop
            #or break it and get rid of the points in the loop from the path
            elif latLong in self.locations[0:-5] and self.activator == False:
                #sound.play_effect('arcade:Laser_1')
                self.loopPrompt = True
                self.activator = True

            #if you say tes to continuing, then you it will keep Recording
            #repeated points until you reach a point not in the list.
            if self.loopPromptState == 1:
                if self.currentLoc != latLong:
                    self.currentLoc = latLong
                    self.locations += [latLong]

            #if they say yes to breaking the loop, remove everything from the
            #end til that point in the list
            elif self.loopPromptState == 2:
                loc = self.locations.index(latLong)
                self.locations = self.locations[0:loc]
                self.loopPromptState = 0

        #when its in measuring state, measure.
        if self.measuringOn == True:
            measuring(self)

        #after measuring is off, setup array to use on the way back
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

        #function state 4 is about getting back to the original location
        elif self.functionState == 4:

            #tracing back steps
            if latLong in self.locationsLeft:
                 loc = self.locationsLeft.index(latLong)

                 #chopping off everything til the point that it recognizes in
                 #the list is way better than using .remove because now if I
                 #loop into the list or the location sensor picks up late, I
                 #can subvert those problems and allow Thread to work seamlessly

                 # self.locationsLeft.remove(latLong) #dont use this
                 self.locationsLeft = self.locationsLeft[0:loc]

            #pull the last location, that is the destination
            x,y = self.locations[0]
            x = round(x,10)
            y = round(y,10)
            loc = "[" + str(x) + ", " + str(y) + "]"
            fill(self.theme["buttonFill"])
            stroke(self.theme["titleColor"])
            stroke_weight(0)
            # rect(0,560,self.size.w,50)
            # # text('Destination:', font_name='Verdana', font_size=12.0, x=70, y=550, alignment=5)
            # # text(loc, font_name='Verdana', font_size=12.0, x=230, y=550, alignment=5)

            #calculate total distance traveled by using the distance formula
            totalDistanceTraveled = 0
            for i in range(len(self.locations)-1):
                firstPosX, firstPosY = self.locations[i]
                nextPosX, nextPosY = self.locations[i+1]
                dist = ((nextPosX - firstPosX)**2 + \
                (nextPosY - firstPosY)**2)**0.5
                totalDistanceTraveled += dist

            #not displaying the distance traveled because it is unnecessary
            #and usually incorrect because of the nature of the data
            # text('Distance Traveled:', font_name='Verdana', font_size=12.0, \
            # x=70, y=585, alignment=5)
            # text(str(totalDistanceTraveled), font_name='Verdana', \
            # font_size=12.0, x=230, y=585, alignment=5)

            #formatting
            textPosX = self.size.x/2
            textPosY = self.size.y/2

            #displaying the arrow that guides you back
            #if you have more than one, an arrow will point you back
            #if not it will say "Welcome Back."
            if (len(self.locationsLeft) > 1):
                #if you have more than 5 points left, use the average location
                #of the next 4 points on the path to get an accurate direction
                #back because points are recorded on a grid, so going from
                #point to point will be either left right forward or backward
                #and nothing in between.
                if (len(self.locationsLeft) > 4):
                    currPosX, currPosY = latLong
                    # currPosX, currPosY = self.locationsLeft[-1]
                    nextPosX, nextPosY = self.locationsLeft[-2]
                    secondPosX, secondPosY = self.locationsLeft[-3]
                    thirdPosX, thirdPosY = self.locationsLeft[-4]
                    fourthPosX, fourthPosY = self.locationsLeft[-5]

                    #use the average location to get a good direction
                    xNextAverage = (nextPosX + secondPosX + \
                    thirdPosX + fourthPosX)/4
                    yNextAverage = (nextPosY + secondPosY + \
                    thirdPosY + fourthPosY)/4

                #if there are 3 or 2 points left then just use what's left
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

                #this formula was from: "https://www.igismap.com/formula
                #-to-find-bearing-or-heading-angle-between-two-points-
                #latitude-longitude/"
                xVal = math.cos(math.radians(xNextAverage))*\
                math.sin(math.radians(yNextAverage-currPosY))

                yVal = math.cos(math.radians(currPosX))*\
                math.sin(math.radians(xNextAverage))-\
                math.sin(math.radians(currPosX))*\
                math.cos(math.radians(xNextAverage))*\
                math.cos(math.radians(yNextAverage-currPosY))

                radianAngle = (math.atan2(xVal,yVal))
                degreeAngle = math.degrees(radianAngle)

                #had to derive this method on my own
                if degreeAngle < 0:
                    degreeAngle = 360 + degreeAngle

                trueDegree = degreeAngle

                #draw directing arrow: have to use this formula
                #it allow you to spin the phone and it will still point you in
                #the right direction
                tempYaw1 = - (360 - yaw + trueDegree)
                trueDegreeSin = math.sin(math.radians(tempYaw1))
                trueDegreeCos = math.cos(math.radians(tempYaw1))

                #draw the arrow that points you back
                def pointMaker(self,roll,pitch, yaw):
                    stroke_weight(20)
                    stroke(self.theme["guiderBack"])
                    line(self.centerX2-trueDegreeCos*130, \
                    self.centerY-trueDegreeSin*130, \
                    self.centerX2+trueDegreeCos*130, \
                    self.centerY+trueDegreeSin*130 )
                    stroke(self.theme["compassStrokeNorth"])
                    #make the point by increasing length
                    #and reducing stroke weight (thickness)
                    for i in range(20):
                        stroke_weight(20-i)
                        line(self.centerX2+trueDegreeCos*(130+(i*2)), \
                        self.centerY+trueDegreeSin*(130+(i*2)), \
                        self.centerX2 ,self.centerY )

                #draw the point
                pointMaker(self,roll,pitch, yaw)

                stroke_weight(0)
                #display images when you are in the location that
                #an image is in
                if latLong in self.photoLocations \
                and self.imageModeOpen == False:

                    photoLoc = len(self.photoLocations) - \
                    self.photoLocations.index(latLong)

                    self.imageMode = True

                    tint(self.theme["textColor2"])
                    fill(self.theme["notificationColor"])
                    stroke(self.theme["notificationColor"])

                    #display a banner that says there is a landmark here!
                    rect(0,150,self.size.w,50)
                    text("Landmark! Tap here to see!", font_name='Verdana', \
                    font_size=16.0, x=self.centerX2, y=150+25, alignment=5)
                    self.currentImage = self.photoLibrary.assets[-photoLoc]
                    self.photoWidth = self.currentImage.pixel_width
                    self.photoHeight = self.currentImage.pixel_height

                    #get the image ready for display when the banner is tapped
                    self.ui_image = self.currentImage.get_ui_image()

            else:
                #when there are no locations left display Welcome Back.
                text("Welcome Back.", font_name='Verdana', font_size=16.0, \
                x=textPosX, y=textPosY, alignment=5)

        #the more state buttons to be displayed
        fill(self.theme["needMoreText"])
        tint(self.theme["textColor2"])
        if self.MoreState == True:
            #to seperate the active buttons from the non active ones
            fill(self.theme["transparentFill"])
            rect(0,0,self.size.x,self.size.y)

            #SOS Button draw
            fill(self.theme["needMoreText"])
            tint(self.theme["textColor2"])
            ellipse(self.centerX2-0.0-self.scale,self.centerY2-self.scale-130,\
            self.scale*2,self.scale*2)
            text('SOS', font_name='Verdana', font_size=12.0, x=self.centerX2, \
            y=self.centerY2+self.scale-167, alignment=5)

            #only display certain buttons when it is over an amount of points
            if len(self.locations) >= 2:

                #MAP Button draw
                fill(self.theme["mapButton"])
                tint(self.theme["otherButtonTexts"])
                ellipse(self.centerX2-self.scale*3-self.scale,\
                self.centerY2-self.scale-20,self.scale*2,self.scale*2)
                text('Map View', font_name='Verdana', font_size=12.0, \
                x=self.centerX2-112, y=self.centerY2+self.scale-57,alignment=5)

                #Share Button Draw
                fill(self.theme["shareButton"])
                tint(self.theme["otherButtonTexts"])
                ellipse(self.centerX2-self.scale,self.centerY2-self.scale-20,\
                self.scale*2,self.scale*2)
                text('Share', font_name='Verdana', font_size=12.0, \
                x=self.centerX2, y=self.centerY2+self.scale-57, alignment=5)

                #let user know the text was copied after pressing share
                tint(self.theme["copiedText"])
                if self.clipState == True:
                    text('Copied to Clipboard', font_name='Verdana', \
                    font_size=16.0, x=self.size.x/2, y=self.size.y/2-65, \
                    alignment=5)

            #trace button draw
            fill(self.theme["traceButton"])
            tint(self.theme["otherButtonTexts"])
            ellipse(self.centerX2+self.scale*3-self.scale,\
            self.centerY2-self.scale-20,self.scale*2,self.scale*2)
            text('Trace', font_name='Verdana', font_size=12.0, \
            x=self.centerX2+112, y=self.centerY2+self.scale-57, alignment=5)

            #SOS Button Draw
            fill(self.theme["SOScolor"])
            tint(self.theme["otherButtonTexts"])
            ellipse(self.centerX2-0.0-self.scale,\
            self.centerY2-self.scale-130,self.scale*2,self.scale*2)
            text('SOS', font_name='Verdana', font_size=12.0, \
            x=self.centerX2, y=self.centerY2+self.scale-167, alignment=5)

            #Theme switching button draw
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

        #photo border when the photo is displayed
        if self.imageModeOpen == True:
            fill(0,0,0,0.5)
            rect(0,0,self.size.x, self.size.y)
            fill(self.theme["photoBorder"])
            rect(5, self.halfScreenFrame, self.widthFrame, self.heightFrame)

        #this function draws the path out in the frame that you can access
        #after pressing the trace button.
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

            #take the differences between the latLong points and essentially
            #simplify the data
            for loc in self.locations[1:]:
                nPointX, nPointY = loc
                dataX = (iPointX - nPointX) * 100000
                dataY = (iPointY - nPointY) * 100000
                newLocs += [(dataX,dataY)]

            #split up x and y values
            for loc in newLocs:
                xSepVals += [loc[0]]
                ySepVals += [loc[1]]

            #look for the maximum difference between the x vals and y values
            maxDiffX = (max(xSepVals) - min(xSepVals))
            maxDiffY = (max(ySepVals) - min(ySepVals))

            #scale it based on the maximum difference so the graph looks scaled
            #properly and one axis isn't many times smaller than the other
            generalMaxDiff = max(maxDiffX, maxDiffY)

            #make everything positive
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

            #start drawing in the frame
            #the color changes from red to black as you go farther from your
            #current location
            #changes from red to blue in dark mode
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
                #draw lines between points
                line((335/generalMaxDiff)*xLoc1+20,(222/generalMaxDiff)*\
                yLoc1+yCenter, (335/generalMaxDiff)*xLoc2+20,\
                (222/generalMaxDiff)*yLoc2+yCenter)
                #draw points, but they will be one shade lighter than the
                #line they are between because it looks cooler and stands out
                if len(self.locations) > 20:
                    ellipse((335/generalMaxDiff)*xLoc1+20-1,\
                    (222/generalMaxDiff)*yLoc1+yCenter-1,2,2)
                else:
                    ellipse((335/generalMaxDiff)*xLoc1+20-2,\
                    (222/generalMaxDiff)*yLoc1+yCenter-2,4,4)
            ellipse((335/generalMaxDiff)*evenedLocsX[-1]+20-2,\
            (222/generalMaxDiff)*evenedLocsY[-1]+yCenter-2,4,4)

        #if you push the trace button and you have locations, reveal the path
        if self.pathState == True and len(self.locations) > 0:
            drawPath(self)

        #when someone walks in a circle, prompt the user to decide what to do:
        #delete the looped area, or keep that path of travel.
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

        #prompt when the user goes in a loop/crosses paths with recorded path
        if self.loopPrompt == True:
            loopPromptBox(self)

    #tells you if the screen is touched and where
    def touch_began(self, touch):

        #creates a query of the locations recorded and opens it on google maps
        #because the query accepts at most around 20 points, if you have more
        #than 20 points it will create a new list and get points evenly spaced
        #throughout the path to a total of less than 20. Looks representative
        #and accurate.
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

        #when you run across a landmark (photo) you placed down, it will
        #notify you its present and you can tap to reveal the photo
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

            #asked a question on the omz (Pythonista) forum and they answered!
            #'https://forum.omz-software.com/topic/5263/displaying-an-image-
            #from-album-in-photos-onto-screen-in-scene-module'
            #opens the image and has it hidden.
            self.img = ui.Button(name='image')
            self.img.frame = (10,self.halfScreen,self.widthPhoto,self.heightPhoto)
            self.img.background_image = self.ui_image
            self.img.enable = False
            self.img.hidden = False
            self.view.add_subview(self.img)

        #when you tap, get the current location to perform functions
        current = location.get_location()
        #solved the close points problem using rounding
        latLong = (round(current['latitude'],4), round(current['longitude'],4))
        picTaken = latLong in self.photoLocations

        #get the location on the screen of the touch
        x,y = touch.location

        #if the image is open, close it when you tap (has to be off the image)
        if self.imageModeOpen == True:
            self.imageModeOpen = False
            self.img.hidden = True

        #if you have the loop Prompt, you must tap an answer in order to use
        #the other functions
        if self.loopPrompt == True:
            if x > 50 and x < self.size.x/2 and y < self.size.y/2 \
            and y > self.size.y/2 - 50:
                self.loopPrompt = False
                self.loopPromptState = 1
            elif x > self.size.x/2 and x < self.size.x-50 \
            and y < self.size.y/2 and y > self.size.y/2 - 50:
                self.loopPrompt = False
                self.loopPromptState = 2

        #when it has the more menu open, you must are not able to tap any of
        #the other buttons, other than the ones in the more menu
        elif self.MoreState == True:
            #SOS State tap, call the cops if you tap
            if x < self.size.w/2 + 30 and x > self.size.w/2 - 30 \
            and y > 50 and y < 100 and self.MoreState == True:
                webbrowser.open('tel:911')

            #MapView tap
            elif x < 100 and x > 50 and y < 220 and y > 160 and \
            len(self.locations) >= 2:
                mapView(self)

            #create the query, but make it a link for phone users, and copy
            #it to the clipboard
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

            #tap on Trace button to reveal the path
            elif x < self.size.x-50 and x > self.size.x-100 and y < 220 \
            and y > 160 and len(self.locations) > 2:
                self.pathState = True

            #tap on theme button to switch the theme
            elif x < self.size.w/2 + 30 and x > self.size.w/2 - 30 \
            and y > self.size.y-95-40 and y < self.size.y-95+40:
                self.themeSwitch += 1
                if self.themeSwitch % 2  == 0:
                    self.theme = self.lightMode
                elif self.themeSwitch % 2 == 1:
                    self.theme = self.darkMode

            #tap off a button while in the more menu, and it exits the menu
            else:
                self.MoreState = False
                self.clipState = False
                self.pathState = False


        #open landmark by tapping on the banner
        elif y > 150 and y < 200 and self.imageMode == True:
            openLandmark(self)

        #if in image mode, tap off the image to get rid of it off the screen
        elif y < 150 and y > 200 and self.imageMode == True:
            self.imageMode = False

        #reset button resets everything
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

        #more button is a small and out of the way, opens up more menu
        elif x < self.size.w/2 + 25 and x > self.size.w/2 - 25 and y < 30 \
        and y > 0:
            self.MoreState = True

        #take photos and add to album
        elif x < self.size.w/2 + 30 and x > self.size.w/2 - 30 \
        and y > 50 and y < 100 and self.MoreState == False and \
        self.measuringOn == True and picTaken == False:
            imageree = photos.capture_image()
            if imageree != None:
                #open up the camera and you can take photo
                photos.save_image(imageree)
                time.sleep(1)
                self.photoCount += 1
                allAssets = photos.get_assets()
                theImage = allAssets[-1]
                #if there is no album, create album 'Thread'
                try:
                    self.photoLibrary = [a for a in photos.get_albums() \
                    if a.title == 'Thread'][0]
                except IndexError:
                    self.photoLibrary = photos.create_album('Thread')

                #add the image to the album for the user to have and for
                #future use in the app's use (landmarks!)
                theImage = allAssets[len(allAssets)-1]
                self.photoLibrary.add_assets([theImage])

                self.photoLocations += [latLong]

        #compass State: Letters (NWSE) or degrees
        elif x < 325 and x > 275 and y < 100 and y > 50:
            self.compassStat = not(self.compassStat)

        #go to measuring mode when tapped for the first time
        elif self.measuringOn == False and self.functionState == 0:
            self.measuringOn = True
            self.background_color = self.theme["backgroundColor"]
            self.functionState += 1

        #if you need more values do not let the user stop recording
        elif self.measuringOn == True and self.functionState == 1 \
        and len(self.locations) < 4:
            self.needMore = True

        #if you have enough locations, when you tap you can move to next state
        elif self.measuringOn == True and self.functionState == 1 \
        and len(self.locations) > 3:
            #sound.play_effect('arcade:Laser_1')
            self.needMore = False
            self.measuringOn = False
            self.background_color = self.theme["backgroundColor"]
            self.functionState += 1

        #move function state up to state 4 so you can begin tracing back
        elif self.measuringOn == False and self.functionState == 3:
            #sound.play_effect('arcade:Laser_1')
            self.background_color = self.theme["backgroundColor"]
            self.functionState += 1

#run the app
run(MyScene(), PORTRAIT)
