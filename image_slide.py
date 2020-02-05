#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Wed Feb  5 19:39:00 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'image_slide'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/lowe/Documents/Programmering/Python/PsychoPy projects/My own practice projects/psychopy forum sgwallner/image_slide.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text="Welcome to the image slide show.\n\nPress 'spacebar' to continue.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyboard_welcome = keyboard.Keyboard()
# enter the number of seconds that the experiment should continue
experiment_duration = 30

# Initialize components for Routine "trial"
trialClock = core.Clock()
image_trial = visual.ImageStim(
    win=win,
    name='image_trial', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
keyboard_trial = keyboard.Keyboard()
# initializing variables that will be used for flipping through
# the images

# enter the loweest/highest image 
# numbers here
min_img_no = 1
max_img_no = 3

img_no = min_img_no

# the "imgs/" part is the folder that the images are saved in.
# the ".jpg" part is the end of the file name. this script
# assumes that all images are simply named "1.jpg", "2.jpg"
# and so on
current_pic = "imgs/" + str(img_no) + ".jpg"

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text="Thank you!\n\nPlease wait for the researcher.\n\n('q' to finish the experiment)",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyboard_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
routineTimer.add(9999.000000)
# update component parameters for each repeat
keyboard_welcome.keys = []
keyboard_welcome.rt = []
# keep track of which components have finished
welcomeComponents = [text_welcome, keyboard_welcome]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "welcome"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    if text_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome.frameNStart = frameN  # exact frame index
        text_welcome.tStart = t  # local t and not account for scr refresh
        text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
        text_welcome.setAutoDraw(True)
    if text_welcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_welcome.tStartRefresh + 9999-frameTolerance:
            # keep track of stop time/frame for later
            text_welcome.tStop = t  # not accounting for scr refresh
            text_welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_welcome, 'tStopRefresh')  # time at next scr refresh
            text_welcome.setAutoDraw(False)
    
    # *keyboard_welcome* updates
    waitOnFlip = False
    if keyboard_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyboard_welcome.frameNStart = frameN  # exact frame index
        keyboard_welcome.tStart = t  # local t and not account for scr refresh
        keyboard_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyboard_welcome, 'tStartRefresh')  # time at next scr refresh
        keyboard_welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyboard_welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyboard_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyboard_welcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > keyboard_welcome.tStartRefresh + 9999-frameTolerance:
            # keep track of stop time/frame for later
            keyboard_welcome.tStop = t  # not accounting for scr refresh
            keyboard_welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(keyboard_welcome, 'tStopRefresh')  # time at next scr refresh
            keyboard_welcome.status = FINISHED
    if keyboard_welcome.status == STARTED and not waitOnFlip:
        theseKeys = keyboard_welcome.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyboard_welcome.keys = theseKeys.name  # just the last key pressed
            keyboard_welcome.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_welcome.started', text_welcome.tStartRefresh)
thisExp.addData('text_welcome.stopped', text_welcome.tStopRefresh)
# check responses
if keyboard_welcome.keys in ['', [], None]:  # No response was made
    keyboard_welcome.keys = None
thisExp.addData('keyboard_welcome.keys',keyboard_welcome.keys)
if keyboard_welcome.keys != None:  # we had a response
    thisExp.addData('keyboard_welcome.rt', keyboard_welcome.rt)
thisExp.addData('keyboard_welcome.started', keyboard_welcome.tStartRefresh)
thisExp.addData('keyboard_welcome.stopped', keyboard_welcome.tStopRefresh)
thisExp.nextEntry()
trial_loop_clock = core.Clock()

# set up handler to look after randomisation of conditions etc
trial_loop = data.TrialHandler(nReps=10000, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trial_loop')
thisExp.addLoop(trial_loop)  # add the loop to the experiment
thisTrial_loop = trial_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
if thisTrial_loop != None:
    for paramName in thisTrial_loop:
        exec('{} = thisTrial_loop[paramName]'.format(paramName))

for thisTrial_loop in trial_loop:
    currentLoop = trial_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
    if thisTrial_loop != None:
        for paramName in thisTrial_loop:
            exec('{} = thisTrial_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    routineTimer.add(9999.000000)
    # update component parameters for each repeat
    image_trial.setImage(current_pic)
    keyboard_trial.keys = []
    keyboard_trial.rt = []
    current_pic = "imgs/" + str(img_no) + ".jpg"
    # keep track of which components have finished
    trialComponents = [image_trial, keyboard_trial]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_trial* updates
        if image_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_trial.frameNStart = frameN  # exact frame index
            image_trial.tStart = t  # local t and not account for scr refresh
            image_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_trial, 'tStartRefresh')  # time at next scr refresh
            image_trial.setAutoDraw(True)
        if image_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_trial.tStartRefresh + 9999-frameTolerance:
                # keep track of stop time/frame for later
                image_trial.tStop = t  # not accounting for scr refresh
                image_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_trial, 'tStopRefresh')  # time at next scr refresh
                image_trial.setAutoDraw(False)
        
        # *keyboard_trial* updates
        waitOnFlip = False
        if keyboard_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyboard_trial.frameNStart = frameN  # exact frame index
            keyboard_trial.tStart = t  # local t and not account for scr refresh
            keyboard_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyboard_trial, 'tStartRefresh')  # time at next scr refresh
            keyboard_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyboard_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyboard_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyboard_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyboard_trial.tStartRefresh + 9999-frameTolerance:
                # keep track of stop time/frame for later
                keyboard_trial.tStop = t  # not accounting for scr refresh
                keyboard_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyboard_trial, 'tStopRefresh')  # time at next scr refresh
                keyboard_trial.status = FINISHED
        if keyboard_trial.status == STARTED and not waitOnFlip:
            theseKeys = keyboard_trial.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                keyboard_trial.keys = theseKeys.name  # just the last key pressed
                keyboard_trial.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        if trial_loop_clock.getTime() > experiment_duration:
            trial_loop.nReps = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trial_loop.addData('image_trial.started', image_trial.tStartRefresh)
    trial_loop.addData('image_trial.stopped', image_trial.tStopRefresh)
    # check responses
    if keyboard_trial.keys in ['', [], None]:  # No response was made
        keyboard_trial.keys = None
    trial_loop.addData('keyboard_trial.keys',keyboard_trial.keys)
    if keyboard_trial.keys != None:  # we had a response
        trial_loop.addData('keyboard_trial.rt', keyboard_trial.rt)
    trial_loop.addData('keyboard_trial.started', keyboard_trial.tStartRefresh)
    trial_loop.addData('keyboard_trial.stopped', keyboard_trial.tStopRefresh)
    # if the participant pressed the left key, decrease the image
    # number by one (e. g. going from "image 2" to "image 1"),
    # and if they pressed the right key, increase the image number
    # by one ("image 2" -> "image 3")
    if (keyboard_trial.keys == str('left')) or (keyboard_trial.keys == 'left'):
        img_no -= 1
    elif (keyboard_trial.keys == str('right')) or (keyboard_trial.keys == 'right'):
        img_no += 1
    
    # if the participant goes below the minimum/start value for the
    # image number, go to the last image instead. if they go above
    # the maximum image number value, go to the first image.
    if img_no < min_img_no:
        img_no = max_img_no
    elif img_no > max_img_no:
        img_no = min_img_no
    
    current_pic = "imgs/" + str(img_no) + ".jpg"
    thisExp.nextEntry()
    
# completed 10000 repeats of 'trial_loop'


# ------Prepare to start Routine "end"-------
routineTimer.add(9999.000000)
# update component parameters for each repeat
keyboard_end.keys = []
keyboard_end.rt = []
# keep track of which components have finished
endComponents = [text_end, keyboard_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if text_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_end.frameNStart = frameN  # exact frame index
        text_end.tStart = t  # local t and not account for scr refresh
        text_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    if text_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_end.tStartRefresh + 9999-frameTolerance:
            # keep track of stop time/frame for later
            text_end.tStop = t  # not accounting for scr refresh
            text_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
            text_end.setAutoDraw(False)
    
    # *keyboard_end* updates
    waitOnFlip = False
    if keyboard_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyboard_end.frameNStart = frameN  # exact frame index
        keyboard_end.tStart = t  # local t and not account for scr refresh
        keyboard_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyboard_end, 'tStartRefresh')  # time at next scr refresh
        keyboard_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyboard_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyboard_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyboard_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > keyboard_end.tStartRefresh + 9999-frameTolerance:
            # keep track of stop time/frame for later
            keyboard_end.tStop = t  # not accounting for scr refresh
            keyboard_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(keyboard_end, 'tStopRefresh')  # time at next scr refresh
            keyboard_end.status = FINISHED
    if keyboard_end.status == STARTED and not waitOnFlip:
        theseKeys = keyboard_end.getKeys(keyList=['q'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyboard_end.keys = theseKeys.name  # just the last key pressed
            keyboard_end.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)
# check responses
if keyboard_end.keys in ['', [], None]:  # No response was made
    keyboard_end.keys = None
thisExp.addData('keyboard_end.keys',keyboard_end.keys)
if keyboard_end.keys != None:  # we had a response
    thisExp.addData('keyboard_end.rt', keyboard_end.rt)
thisExp.addData('keyboard_end.started', keyboard_end.tStartRefresh)
thisExp.addData('keyboard_end.stopped', keyboard_end.tStopRefresh)
thisExp.nextEntry()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
