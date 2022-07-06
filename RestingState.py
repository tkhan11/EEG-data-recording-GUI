#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on June 13, 2022, at 12:36
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'GUI_upto_VEP1_correct'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\tanveerlaptop\\Desktop\\EEG GUI for data collection individual tasks\\RestingState_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
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
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "trial"
trialClock = core.Clock()
sound_1 = sound.Sound('A', secs=.5, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
Cross = visual.ImageStim(
    win=win,
    name='Cross', 
    image='cross.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='Relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
sound_2 = sound.Sound('A', secs=.500, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
sound_3 = sound.Sound('A', secs=.500, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(128.200000)
# update component parameters for each repeat
sound_1.setSound('A', secs=.5, hamming=True)
sound_1.setVolume(1.0, log=False)
sound_2.setSound('A', secs=.500, hamming=True)
sound_2.setVolume(1.0, log=False)
sound_3.setSound('A', secs=.500, hamming=True)
sound_3.setVolume(1.0, log=False)
# keep track of which components have finished
trialComponents = [sound_1, Cross, text, sound_2, sound_3]
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

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_1
    if sound_1.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        sound_1.frameNStart = frameN  # exact frame index
        sound_1.tStart = t  # local t and not account for scr refresh
        sound_1.tStartRefresh = tThisFlipGlobal  # on global time
        sound_1.play(when=win)  # sync with win flip
    if sound_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_1.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            sound_1.tStop = t  # not accounting for scr refresh
            sound_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
            sound_1.stop()
    
    # *Cross* updates
    if Cross.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
        # keep track of start time/frame for later
        Cross.frameNStart = frameN  # exact frame index
        Cross.tStart = t  # local t and not account for scr refresh
        Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
        Cross.setAutoDraw(True)
    if Cross.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 62.1-frameTolerance:
            # keep track of stop time/frame for later
            Cross.tStop = t  # not accounting for scr refresh
            Cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
            Cross.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 62.3-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    # start/stop sound_2
    if sound_2.status == NOT_STARTED and tThisFlip >= 67.5-frameTolerance:
        # keep track of start time/frame for later
        sound_2.frameNStart = frameN  # exact frame index
        sound_2.tStart = t  # local t and not account for scr refresh
        sound_2.tStartRefresh = tThisFlipGlobal  # on global time
        sound_2.play(when=win)  # sync with win flip
    if sound_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_2.tStartRefresh + .500-frameTolerance:
            # keep track of stop time/frame for later
            sound_2.tStop = t  # not accounting for scr refresh
            sound_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
            sound_2.stop()
    # start/stop sound_3
    if sound_3.status == NOT_STARTED and tThisFlip >= 127.7-frameTolerance:
        # keep track of start time/frame for later
        sound_3.frameNStart = frameN  # exact frame index
        sound_3.tStart = t  # local t and not account for scr refresh
        sound_3.tStartRefresh = tThisFlipGlobal  # on global time
        sound_3.play(when=win)  # sync with win flip
    if sound_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sound_3.tStartRefresh + .500-frameTolerance:
            # keep track of stop time/frame for later
            sound_3.tStop = t  # not accounting for scr refresh
            sound_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
            sound_3.stop()
    
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
sound_1.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_1.started', sound_1.tStartRefresh)
thisExp.addData('sound_1.stopped', sound_1.tStopRefresh)
thisExp.addData('Cross.started', Cross.tStartRefresh)
thisExp.addData('Cross.stopped', Cross.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
sound_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_2.started', sound_2.tStartRefresh)
thisExp.addData('sound_2.stopped', sound_2.tStopRefresh)
sound_3.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_3.started', sound_3.tStartRefresh)
thisExp.addData('sound_3.stopped', sound_3.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
