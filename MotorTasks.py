#!/usr/bin/env python
#coding: utf-8 
##
## AUTHOR: TANVEER AHMED KHAN
###

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
    originPath='C:\\Users\\tanveerlaptop\\Desktop\\EEG GUI for data collection individual tasks\\MotorTasks_lastrun.py',
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
LC1 = visual.ImageStim(
    win=win,
    name='LC1', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
LC2 = visual.ImageStim(
    win=win,
    name='LC2', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
Rc1 = visual.ImageStim(
    win=win,
    name='Rc1', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
lc3 = visual.ImageStim(
    win=win,
    name='lc3', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
rc2 = visual.ImageStim(
    win=win,
    name='rc2', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
rc3 = visual.ImageStim(
    win=win,
    name='rc3', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
lc4 = visual.ImageStim(
    win=win,
    name='lc4', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
lc5 = visual.ImageStim(
    win=win,
    name='lc5', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
lc6 = visual.ImageStim(
    win=win,
    name='lc6', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
rc4 = visual.ImageStim(
    win=win,
    name='rc4', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
rc5 = visual.ImageStim(
    win=win,
    name='rc5', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
lc7 = visual.ImageStim(
    win=win,
    name='lc7', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
rc6 = visual.ImageStim(
    win=win,
    name='rc6', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
rc7 = visual.ImageStim(
    win=win,
    name='rc7', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
lc8 = visual.ImageStim(
    win=win,
    name='lc8', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
MI1LC1 = visual.ImageStim(
    win=win,
    name='MI1LC1', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
text = visual.TextStim(win=win, name='text',
    text='\n\nYou can relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
MILC2 = visual.ImageStim(
    win=win,
    name='MILC2', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-18.0)
MIRC1 = visual.ImageStim(
    win=win,
    name='MIRC1', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
MILC3 = visual.ImageStim(
    win=win,
    name='MILC3', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
MIRC2 = visual.ImageStim(
    win=win,
    name='MIRC2', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
MIRC3 = visual.ImageStim(
    win=win,
    name='MIRC3', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
MILC4 = visual.ImageStim(
    win=win,
    name='MILC4', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
MILC5 = visual.ImageStim(
    win=win,
    name='MILC5', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
MILC6 = visual.ImageStim(
    win=win,
    name='MILC6', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
MIRC4 = visual.ImageStim(
    win=win,
    name='MIRC4', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-26.0)
MIRC5 = visual.ImageStim(
    win=win,
    name='MIRC5', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-27.0)
MILC7 = visual.ImageStim(
    win=win,
    name='MILC7', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-28.0)
MIRC6 = visual.ImageStim(
    win=win,
    name='MIRC6', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-29.0)
MIRC7 = visual.ImageStim(
    win=win,
    name='MIRC7', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-30.0)
MILC8 = visual.ImageStim(
    win=win,
    name='MILC8', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-31.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='\n\n\nYou can Relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-32.0);
MMLI1 = visual.ImageStim(
    win=win,
    name='MMLI1', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-33.0)
MMLI2 = visual.ImageStim(
    win=win,
    name='MMLI2', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-34.0)
MMRI1 = visual.ImageStim(
    win=win,
    name='MMRI1', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-35.0)
MMLI3 = visual.ImageStim(
    win=win,
    name='MMLI3', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-36.0)
MMRI2 = visual.ImageStim(
    win=win,
    name='MMRI2', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-37.0)
MMRI3 = visual.ImageStim(
    win=win,
    name='MMRI3', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-38.0)
MMLI4 = visual.ImageStim(
    win=win,
    name='MMLI4', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-39.0)
MMLI5 = visual.ImageStim(
    win=win,
    name='MMLI5', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-40.0)
MMLI6 = visual.ImageStim(
    win=win,
    name='MMLI6', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-41.0)
MMRi4 = visual.ImageStim(
    win=win,
    name='MMRi4', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-42.0)
MMRI5 = visual.ImageStim(
    win=win,
    name='MMRI5', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-43.0)
MMLI7 = visual.ImageStim(
    win=win,
    name='MMLI7', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-44.0)
MMRI6 = visual.ImageStim(
    win=win,
    name='MMRI6', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-45.0)
MMRI7 = visual.ImageStim(
    win=win,
    name='MMRI7', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-46.0)
MMLI8 = visual.ImageStim(
    win=win,
    name='MMLI8', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-47.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='\n\n\nYou can relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-48.0);
MILI1 = visual.ImageStim(
    win=win,
    name='MILI1', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-49.0)
MILI2 = visual.ImageStim(
    win=win,
    name='MILI2', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-50.0)
MIRI1 = visual.ImageStim(
    win=win,
    name='MIRI1', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-51.0)
MILI3 = visual.ImageStim(
    win=win,
    name='MILI3', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-52.0)
MIRi2 = visual.ImageStim(
    win=win,
    name='MIRi2', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-53.0)
MIRI3 = visual.ImageStim(
    win=win,
    name='MIRI3', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-54.0)
MILI4 = visual.ImageStim(
    win=win,
    name='MILI4', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-55.0)
MILI5 = visual.ImageStim(
    win=win,
    name='MILI5', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-56.0)
MILI6 = visual.ImageStim(
    win=win,
    name='MILI6', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-57.0)
MIRI4 = visual.ImageStim(
    win=win,
    name='MIRI4', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-58.0)
MIRI5 = visual.ImageStim(
    win=win,
    name='MIRI5', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-59.0)
MILI7 = visual.ImageStim(
    win=win,
    name='MILI7', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-60.0)
MIri6 = visual.ImageStim(
    win=win,
    name='MIri6', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-61.0)
miri7 = visual.ImageStim(
    win=win,
    name='miri7', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-62.0)
mili8 = visual.ImageStim(
    win=win,
    name='mili8', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-63.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='\n\nYou can relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-64.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='\n\n\nPress K',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-65.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='\n\n\nPress W',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-66.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='\n\nPress T',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-67.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='\n\n\nPress Z',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-68.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Press I',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-69.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='Press B',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-70.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='Press X',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-71.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='Press Y',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-72.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='Press B',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-73.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='Press C',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-74.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='Press O',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-75.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='Press R',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-76.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Press V',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-77.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='Press N',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-78.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='Press U',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-79.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='Press M',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-80.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='Press A',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-81.0);
text_22 = visual.TextStim(win=win, name='text_22',
    text='Press F',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-82.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='\n\n\nYou can Relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-83.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text='Press G',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-84.0);
text_25 = visual.TextStim(win=win, name='text_25',
    text='Press E',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-85.0);
text_26 = visual.TextStim(win=win, name='text_26',
    text='Press Z',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-86.0);
text_27 = visual.TextStim(win=win, name='text_27',
    text='Press O',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-87.0);
text_28 = visual.TextStim(win=win, name='text_28',
    text='Press I',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-88.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Press B',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-89.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='Press A',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-90.0);
text_31 = visual.TextStim(win=win, name='text_31',
    text='Press Q',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-91.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='Press B',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-92.0);
text_33 = visual.TextStim(win=win, name='text_33',
    text='Press C',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-93.0);
text_34 = visual.TextStim(win=win, name='text_34',
    text='Press O',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-94.0);
text_35 = visual.TextStim(win=win, name='text_35',
    text='Press R',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-95.0);
text_36 = visual.TextStim(win=win, name='text_36',
    text='Press V',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-96.0);
text_37 = visual.TextStim(win=win, name='text_37',
    text='Press N',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-97.0);
text_38 = visual.TextStim(win=win, name='text_38',
    text='Press U',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-98.0);
text_39 = visual.TextStim(win=win, name='text_39',
    text='Press M',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-99.0);
text_40 = visual.TextStim(win=win, name='text_40',
    text='Press L',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-100.0);
text_41 = visual.TextStim(win=win, name='text_41',
    text='Press F',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-101.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='You can Relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-102.0);
MIRM1 = visual.ImageStim(
    win=win,
    name='MIRM1', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-103.0)
MILM1 = visual.ImageStim(
    win=win,
    name='MILM1', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-104.0)
MIRM2 = visual.ImageStim(
    win=win,
    name='MIRM2', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-105.0)
MILM2 = visual.ImageStim(
    win=win,
    name='MILM2', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-106.0)
MILM3 = visual.ImageStim(
    win=win,
    name='MILM3', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-107.0)
MIRM3 = visual.ImageStim(
    win=win,
    name='MIRM3', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-108.0)
MILM4 = visual.ImageStim(
    win=win,
    name='MILM4', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-109.0)
MIRM4 = visual.ImageStim(
    win=win,
    name='MIRM4', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-110.0)
MILM5 = visual.ImageStim(
    win=win,
    name='MILM5', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-111.0)
MIRM5 = visual.ImageStim(
    win=win,
    name='MIRM5', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-112.0)
MIRM6 = visual.ImageStim(
    win=win,
    name='MIRM6', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-113.0)
MILM6 = visual.ImageStim(
    win=win,
    name='MILM6', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-114.0)
MIRM7 = visual.ImageStim(
    win=win,
    name='MIRM7', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-115.0)
MILM7 = visual.ImageStim(
    win=win,
    name='MILM7', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-116.0)
MILM8 = visual.ImageStim(
    win=win,
    name='MILM8', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-117.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(450.100000)
# update component parameters for each repeat
sound_1.setSound('A', secs=.5, hamming=True)
sound_1.setVolume(1.0, log=False)
# keep track of which components have finished
trialComponents = [sound_1, LC1, LC2, Rc1, lc3, rc2, rc3, lc4, lc5, lc6, rc4, rc5, lc7, rc6, rc7, lc8, MI1LC1, text, MILC2, MIRC1, MILC3, MIRC2, MIRC3, MILC4, MILC5, MILC6, MIRC4, MIRC5, MILC7, MIRC6, MIRC7, MILC8, text_2, MMLI1, MMLI2, MMRI1, MMLI3, MMRI2, MMRI3, MMLI4, MMLI5, MMLI6, MMRi4, MMRI5, MMLI7, MMRI6, MMRI7, MMLI8, text_3, MILI1, MILI2, MIRI1, MILI3, MIRi2, MIRI3, MILI4, MILI5, MILI6, MIRI4, MIRI5, MILI7, MIri6, miri7, mili8, text_4, text_5, text_6, text_7, text_8, text_9, text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19, text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29, text_30, text_31, text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, text_40, text_41, text_42, MIRM1, MILM1, MIRM2, MILM2, MILM3, MIRM3, MILM4, MIRM4, MILM5, MIRM5, MIRM6, MILM6, MIRM7, MILM7, MILM8]
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
    
    # *LC1* updates
    if LC1.status == NOT_STARTED and tThisFlip >= 2.6-frameTolerance:
        # keep track of start time/frame for later
        LC1.frameNStart = frameN  # exact frame index
        LC1.tStart = t  # local t and not account for scr refresh
        LC1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LC1, 'tStartRefresh')  # time at next scr refresh
        LC1.setAutoDraw(True)
    if LC1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > LC1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            LC1.tStop = t  # not accounting for scr refresh
            LC1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(LC1, 'tStopRefresh')  # time at next scr refresh
            LC1.setAutoDraw(False)
    
    # *LC2* updates
    if LC2.status == NOT_STARTED and tThisFlip >= 6.5-frameTolerance:
        # keep track of start time/frame for later
        LC2.frameNStart = frameN  # exact frame index
        LC2.tStart = t  # local t and not account for scr refresh
        LC2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LC2, 'tStartRefresh')  # time at next scr refresh
        LC2.setAutoDraw(True)
    if LC2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > LC2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            LC2.tStop = t  # not accounting for scr refresh
            LC2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(LC2, 'tStopRefresh')  # time at next scr refresh
            LC2.setAutoDraw(False)
    
    # *Rc1* updates
    if Rc1.status == NOT_STARTED and tThisFlip >= 10.4-frameTolerance:
        # keep track of start time/frame for later
        Rc1.frameNStart = frameN  # exact frame index
        Rc1.tStart = t  # local t and not account for scr refresh
        Rc1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Rc1, 'tStartRefresh')  # time at next scr refresh
        Rc1.setAutoDraw(True)
    if Rc1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Rc1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            Rc1.tStop = t  # not accounting for scr refresh
            Rc1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Rc1, 'tStopRefresh')  # time at next scr refresh
            Rc1.setAutoDraw(False)
    
    # *lc3* updates
    if lc3.status == NOT_STARTED and tThisFlip >= 14.3-frameTolerance:
        # keep track of start time/frame for later
        lc3.frameNStart = frameN  # exact frame index
        lc3.tStart = t  # local t and not account for scr refresh
        lc3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lc3, 'tStartRefresh')  # time at next scr refresh
        lc3.setAutoDraw(True)
    if lc3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lc3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            lc3.tStop = t  # not accounting for scr refresh
            lc3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lc3, 'tStopRefresh')  # time at next scr refresh
            lc3.setAutoDraw(False)
    
    # *rc2* updates
    if rc2.status == NOT_STARTED and tThisFlip >= 18.1-frameTolerance:
        # keep track of start time/frame for later
        rc2.frameNStart = frameN  # exact frame index
        rc2.tStart = t  # local t and not account for scr refresh
        rc2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rc2, 'tStartRefresh')  # time at next scr refresh
        rc2.setAutoDraw(True)
    if rc2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rc2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            rc2.tStop = t  # not accounting for scr refresh
            rc2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rc2, 'tStopRefresh')  # time at next scr refresh
            rc2.setAutoDraw(False)
    
    # *rc3* updates
    if rc3.status == NOT_STARTED and tThisFlip >= 22-frameTolerance:
        # keep track of start time/frame for later
        rc3.frameNStart = frameN  # exact frame index
        rc3.tStart = t  # local t and not account for scr refresh
        rc3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rc3, 'tStartRefresh')  # time at next scr refresh
        rc3.setAutoDraw(True)
    if rc3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rc3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            rc3.tStop = t  # not accounting for scr refresh
            rc3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rc3, 'tStopRefresh')  # time at next scr refresh
            rc3.setAutoDraw(False)
    
    # *lc4* updates
    if lc4.status == NOT_STARTED and tThisFlip >= 25.8-frameTolerance:
        # keep track of start time/frame for later
        lc4.frameNStart = frameN  # exact frame index
        lc4.tStart = t  # local t and not account for scr refresh
        lc4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lc4, 'tStartRefresh')  # time at next scr refresh
        lc4.setAutoDraw(True)
    if lc4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lc4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            lc4.tStop = t  # not accounting for scr refresh
            lc4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lc4, 'tStopRefresh')  # time at next scr refresh
            lc4.setAutoDraw(False)
    
    # *lc5* updates
    if lc5.status == NOT_STARTED and tThisFlip >= 29.6-frameTolerance:
        # keep track of start time/frame for later
        lc5.frameNStart = frameN  # exact frame index
        lc5.tStart = t  # local t and not account for scr refresh
        lc5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lc5, 'tStartRefresh')  # time at next scr refresh
        lc5.setAutoDraw(True)
    if lc5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lc5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            lc5.tStop = t  # not accounting for scr refresh
            lc5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lc5, 'tStopRefresh')  # time at next scr refresh
            lc5.setAutoDraw(False)
    
    # *lc6* updates
    if lc6.status == NOT_STARTED and tThisFlip >= 33.4-frameTolerance:
        # keep track of start time/frame for later
        lc6.frameNStart = frameN  # exact frame index
        lc6.tStart = t  # local t and not account for scr refresh
        lc6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lc6, 'tStartRefresh')  # time at next scr refresh
        lc6.setAutoDraw(True)
    if lc6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lc6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            lc6.tStop = t  # not accounting for scr refresh
            lc6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lc6, 'tStopRefresh')  # time at next scr refresh
            lc6.setAutoDraw(False)
    
    # *rc4* updates
    if rc4.status == NOT_STARTED and tThisFlip >= 37.2-frameTolerance:
        # keep track of start time/frame for later
        rc4.frameNStart = frameN  # exact frame index
        rc4.tStart = t  # local t and not account for scr refresh
        rc4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rc4, 'tStartRefresh')  # time at next scr refresh
        rc4.setAutoDraw(True)
    if rc4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rc4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            rc4.tStop = t  # not accounting for scr refresh
            rc4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rc4, 'tStopRefresh')  # time at next scr refresh
            rc4.setAutoDraw(False)
    
    # *rc5* updates
    if rc5.status == NOT_STARTED and tThisFlip >= 41-frameTolerance:
        # keep track of start time/frame for later
        rc5.frameNStart = frameN  # exact frame index
        rc5.tStart = t  # local t and not account for scr refresh
        rc5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rc5, 'tStartRefresh')  # time at next scr refresh
        rc5.setAutoDraw(True)
    if rc5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rc5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            rc5.tStop = t  # not accounting for scr refresh
            rc5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rc5, 'tStopRefresh')  # time at next scr refresh
            rc5.setAutoDraw(False)
    
    # *lc7* updates
    if lc7.status == NOT_STARTED and tThisFlip >= 44.8-frameTolerance:
        # keep track of start time/frame for later
        lc7.frameNStart = frameN  # exact frame index
        lc7.tStart = t  # local t and not account for scr refresh
        lc7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lc7, 'tStartRefresh')  # time at next scr refresh
        lc7.setAutoDraw(True)
    if lc7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lc7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            lc7.tStop = t  # not accounting for scr refresh
            lc7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lc7, 'tStopRefresh')  # time at next scr refresh
            lc7.setAutoDraw(False)
    
    # *rc6* updates
    if rc6.status == NOT_STARTED and tThisFlip >= 48.6-frameTolerance:
        # keep track of start time/frame for later
        rc6.frameNStart = frameN  # exact frame index
        rc6.tStart = t  # local t and not account for scr refresh
        rc6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rc6, 'tStartRefresh')  # time at next scr refresh
        rc6.setAutoDraw(True)
    if rc6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rc6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            rc6.tStop = t  # not accounting for scr refresh
            rc6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rc6, 'tStopRefresh')  # time at next scr refresh
            rc6.setAutoDraw(False)
    
    # *rc7* updates
    if rc7.status == NOT_STARTED and tThisFlip >= 52.4-frameTolerance:
        # keep track of start time/frame for later
        rc7.frameNStart = frameN  # exact frame index
        rc7.tStart = t  # local t and not account for scr refresh
        rc7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rc7, 'tStartRefresh')  # time at next scr refresh
        rc7.setAutoDraw(True)
    if rc7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rc7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            rc7.tStop = t  # not accounting for scr refresh
            rc7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rc7, 'tStopRefresh')  # time at next scr refresh
            rc7.setAutoDraw(False)
    
    # *lc8* updates
    if lc8.status == NOT_STARTED and tThisFlip >= 56.3-frameTolerance:
        # keep track of start time/frame for later
        lc8.frameNStart = frameN  # exact frame index
        lc8.tStart = t  # local t and not account for scr refresh
        lc8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(lc8, 'tStartRefresh')  # time at next scr refresh
        lc8.setAutoDraw(True)
    if lc8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > lc8.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            lc8.tStop = t  # not accounting for scr refresh
            lc8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(lc8, 'tStopRefresh')  # time at next scr refresh
            lc8.setAutoDraw(False)
    
    # *MI1LC1* updates
    if MI1LC1.status == NOT_STARTED and tThisFlip >= 60.1-frameTolerance:
        # keep track of start time/frame for later
        MI1LC1.frameNStart = frameN  # exact frame index
        MI1LC1.tStart = t  # local t and not account for scr refresh
        MI1LC1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MI1LC1, 'tStartRefresh')  # time at next scr refresh
        MI1LC1.setAutoDraw(True)
    if MI1LC1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MI1LC1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MI1LC1.tStop = t  # not accounting for scr refresh
            MI1LC1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MI1LC1, 'tStopRefresh')  # time at next scr refresh
            MI1LC1.setAutoDraw(False)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 64-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 4.5-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # *MILC2* updates
    if MILC2.status == NOT_STARTED and tThisFlip >= 68.6-frameTolerance:
        # keep track of start time/frame for later
        MILC2.frameNStart = frameN  # exact frame index
        MILC2.tStart = t  # local t and not account for scr refresh
        MILC2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILC2, 'tStartRefresh')  # time at next scr refresh
        MILC2.setAutoDraw(True)
    if MILC2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILC2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILC2.tStop = t  # not accounting for scr refresh
            MILC2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILC2, 'tStopRefresh')  # time at next scr refresh
            MILC2.setAutoDraw(False)
    
    # *MIRC1* updates
    if MIRC1.status == NOT_STARTED and tThisFlip >= 72.4-frameTolerance:
        # keep track of start time/frame for later
        MIRC1.frameNStart = frameN  # exact frame index
        MIRC1.tStart = t  # local t and not account for scr refresh
        MIRC1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRC1, 'tStartRefresh')  # time at next scr refresh
        MIRC1.setAutoDraw(True)
    if MIRC1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRC1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRC1.tStop = t  # not accounting for scr refresh
            MIRC1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRC1, 'tStopRefresh')  # time at next scr refresh
            MIRC1.setAutoDraw(False)
    
    # *MILC3* updates
    if MILC3.status == NOT_STARTED and tThisFlip >= 76.2-frameTolerance:
        # keep track of start time/frame for later
        MILC3.frameNStart = frameN  # exact frame index
        MILC3.tStart = t  # local t and not account for scr refresh
        MILC3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILC3, 'tStartRefresh')  # time at next scr refresh
        MILC3.setAutoDraw(True)
    if MILC3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILC3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILC3.tStop = t  # not accounting for scr refresh
            MILC3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILC3, 'tStopRefresh')  # time at next scr refresh
            MILC3.setAutoDraw(False)
    
    # *MIRC2* updates
    if MIRC2.status == NOT_STARTED and tThisFlip >= 80.1-frameTolerance:
        # keep track of start time/frame for later
        MIRC2.frameNStart = frameN  # exact frame index
        MIRC2.tStart = t  # local t and not account for scr refresh
        MIRC2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRC2, 'tStartRefresh')  # time at next scr refresh
        MIRC2.setAutoDraw(True)
    if MIRC2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRC2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRC2.tStop = t  # not accounting for scr refresh
            MIRC2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRC2, 'tStopRefresh')  # time at next scr refresh
            MIRC2.setAutoDraw(False)
    
    # *MIRC3* updates
    if MIRC3.status == NOT_STARTED and tThisFlip >= 84-frameTolerance:
        # keep track of start time/frame for later
        MIRC3.frameNStart = frameN  # exact frame index
        MIRC3.tStart = t  # local t and not account for scr refresh
        MIRC3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRC3, 'tStartRefresh')  # time at next scr refresh
        MIRC3.setAutoDraw(True)
    if MIRC3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRC3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRC3.tStop = t  # not accounting for scr refresh
            MIRC3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRC3, 'tStopRefresh')  # time at next scr refresh
            MIRC3.setAutoDraw(False)
    
    # *MILC4* updates
    if MILC4.status == NOT_STARTED and tThisFlip >= 87.8-frameTolerance:
        # keep track of start time/frame for later
        MILC4.frameNStart = frameN  # exact frame index
        MILC4.tStart = t  # local t and not account for scr refresh
        MILC4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILC4, 'tStartRefresh')  # time at next scr refresh
        MILC4.setAutoDraw(True)
    if MILC4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILC4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILC4.tStop = t  # not accounting for scr refresh
            MILC4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILC4, 'tStopRefresh')  # time at next scr refresh
            MILC4.setAutoDraw(False)
    
    # *MILC5* updates
    if MILC5.status == NOT_STARTED and tThisFlip >= 91.6-frameTolerance:
        # keep track of start time/frame for later
        MILC5.frameNStart = frameN  # exact frame index
        MILC5.tStart = t  # local t and not account for scr refresh
        MILC5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILC5, 'tStartRefresh')  # time at next scr refresh
        MILC5.setAutoDraw(True)
    if MILC5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILC5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILC5.tStop = t  # not accounting for scr refresh
            MILC5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILC5, 'tStopRefresh')  # time at next scr refresh
            MILC5.setAutoDraw(False)
    
    # *MILC6* updates
    if MILC6.status == NOT_STARTED and tThisFlip >= 95.4-frameTolerance:
        # keep track of start time/frame for later
        MILC6.frameNStart = frameN  # exact frame index
        MILC6.tStart = t  # local t and not account for scr refresh
        MILC6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILC6, 'tStartRefresh')  # time at next scr refresh
        MILC6.setAutoDraw(True)
    if MILC6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILC6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILC6.tStop = t  # not accounting for scr refresh
            MILC6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILC6, 'tStopRefresh')  # time at next scr refresh
            MILC6.setAutoDraw(False)
    
    # *MIRC4* updates
    if MIRC4.status == NOT_STARTED and tThisFlip >= 99.2-frameTolerance:
        # keep track of start time/frame for later
        MIRC4.frameNStart = frameN  # exact frame index
        MIRC4.tStart = t  # local t and not account for scr refresh
        MIRC4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRC4, 'tStartRefresh')  # time at next scr refresh
        MIRC4.setAutoDraw(True)
    if MIRC4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRC4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRC4.tStop = t  # not accounting for scr refresh
            MIRC4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRC4, 'tStopRefresh')  # time at next scr refresh
            MIRC4.setAutoDraw(False)
    
    # *MIRC5* updates
    if MIRC5.status == NOT_STARTED and tThisFlip >= 103-frameTolerance:
        # keep track of start time/frame for later
        MIRC5.frameNStart = frameN  # exact frame index
        MIRC5.tStart = t  # local t and not account for scr refresh
        MIRC5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRC5, 'tStartRefresh')  # time at next scr refresh
        MIRC5.setAutoDraw(True)
    if MIRC5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRC5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRC5.tStop = t  # not accounting for scr refresh
            MIRC5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRC5, 'tStopRefresh')  # time at next scr refresh
            MIRC5.setAutoDraw(False)
    
    # *MILC7* updates
    if MILC7.status == NOT_STARTED and tThisFlip >= 106.8-frameTolerance:
        # keep track of start time/frame for later
        MILC7.frameNStart = frameN  # exact frame index
        MILC7.tStart = t  # local t and not account for scr refresh
        MILC7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILC7, 'tStartRefresh')  # time at next scr refresh
        MILC7.setAutoDraw(True)
    if MILC7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILC7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILC7.tStop = t  # not accounting for scr refresh
            MILC7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILC7, 'tStopRefresh')  # time at next scr refresh
            MILC7.setAutoDraw(False)
    
    # *MIRC6* updates
    if MIRC6.status == NOT_STARTED and tThisFlip >= 110.6-frameTolerance:
        # keep track of start time/frame for later
        MIRC6.frameNStart = frameN  # exact frame index
        MIRC6.tStart = t  # local t and not account for scr refresh
        MIRC6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRC6, 'tStartRefresh')  # time at next scr refresh
        MIRC6.setAutoDraw(True)
    if MIRC6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRC6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRC6.tStop = t  # not accounting for scr refresh
            MIRC6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRC6, 'tStopRefresh')  # time at next scr refresh
            MIRC6.setAutoDraw(False)
    
    # *MIRC7* updates
    if MIRC7.status == NOT_STARTED and tThisFlip >= 114.4-frameTolerance:
        # keep track of start time/frame for later
        MIRC7.frameNStart = frameN  # exact frame index
        MIRC7.tStart = t  # local t and not account for scr refresh
        MIRC7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRC7, 'tStartRefresh')  # time at next scr refresh
        MIRC7.setAutoDraw(True)
    if MIRC7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRC7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRC7.tStop = t  # not accounting for scr refresh
            MIRC7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRC7, 'tStopRefresh')  # time at next scr refresh
            MIRC7.setAutoDraw(False)
    
    # *MILC8* updates
    if MILC8.status == NOT_STARTED and tThisFlip >= 118.2-frameTolerance:
        # keep track of start time/frame for later
        MILC8.frameNStart = frameN  # exact frame index
        MILC8.tStart = t  # local t and not account for scr refresh
        MILC8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILC8, 'tStartRefresh')  # time at next scr refresh
        MILC8.setAutoDraw(True)
    if MILC8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILC8.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILC8.tStop = t  # not accounting for scr refresh
            MILC8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILC8, 'tStopRefresh')  # time at next scr refresh
            MILC8.setAutoDraw(False)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 122.1-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 4.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # *MMLI1* updates
    if MMLI1.status == NOT_STARTED and tThisFlip >= 126.7-frameTolerance:
        # keep track of start time/frame for later
        MMLI1.frameNStart = frameN  # exact frame index
        MMLI1.tStart = t  # local t and not account for scr refresh
        MMLI1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMLI1, 'tStartRefresh')  # time at next scr refresh
        MMLI1.setAutoDraw(True)
    if MMLI1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMLI1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMLI1.tStop = t  # not accounting for scr refresh
            MMLI1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMLI1, 'tStopRefresh')  # time at next scr refresh
            MMLI1.setAutoDraw(False)
    
    # *MMLI2* updates
    if MMLI2.status == NOT_STARTED and tThisFlip >= 130.6-frameTolerance:
        # keep track of start time/frame for later
        MMLI2.frameNStart = frameN  # exact frame index
        MMLI2.tStart = t  # local t and not account for scr refresh
        MMLI2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMLI2, 'tStartRefresh')  # time at next scr refresh
        MMLI2.setAutoDraw(True)
    if MMLI2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMLI2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMLI2.tStop = t  # not accounting for scr refresh
            MMLI2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMLI2, 'tStopRefresh')  # time at next scr refresh
            MMLI2.setAutoDraw(False)
    
    # *MMRI1* updates
    if MMRI1.status == NOT_STARTED and tThisFlip >= 134.4-frameTolerance:
        # keep track of start time/frame for later
        MMRI1.frameNStart = frameN  # exact frame index
        MMRI1.tStart = t  # local t and not account for scr refresh
        MMRI1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMRI1, 'tStartRefresh')  # time at next scr refresh
        MMRI1.setAutoDraw(True)
    if MMRI1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMRI1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMRI1.tStop = t  # not accounting for scr refresh
            MMRI1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMRI1, 'tStopRefresh')  # time at next scr refresh
            MMRI1.setAutoDraw(False)
    
    # *MMLI3* updates
    if MMLI3.status == NOT_STARTED and tThisFlip >= 138.2-frameTolerance:
        # keep track of start time/frame for later
        MMLI3.frameNStart = frameN  # exact frame index
        MMLI3.tStart = t  # local t and not account for scr refresh
        MMLI3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMLI3, 'tStartRefresh')  # time at next scr refresh
        MMLI3.setAutoDraw(True)
    if MMLI3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMLI3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMLI3.tStop = t  # not accounting for scr refresh
            MMLI3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMLI3, 'tStopRefresh')  # time at next scr refresh
            MMLI3.setAutoDraw(False)
    
    # *MMRI2* updates
    if MMRI2.status == NOT_STARTED and tThisFlip >= 142-frameTolerance:
        # keep track of start time/frame for later
        MMRI2.frameNStart = frameN  # exact frame index
        MMRI2.tStart = t  # local t and not account for scr refresh
        MMRI2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMRI2, 'tStartRefresh')  # time at next scr refresh
        MMRI2.setAutoDraw(True)
    if MMRI2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMRI2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMRI2.tStop = t  # not accounting for scr refresh
            MMRI2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMRI2, 'tStopRefresh')  # time at next scr refresh
            MMRI2.setAutoDraw(False)
    
    # *MMRI3* updates
    if MMRI3.status == NOT_STARTED and tThisFlip >= 145.8-frameTolerance:
        # keep track of start time/frame for later
        MMRI3.frameNStart = frameN  # exact frame index
        MMRI3.tStart = t  # local t and not account for scr refresh
        MMRI3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMRI3, 'tStartRefresh')  # time at next scr refresh
        MMRI3.setAutoDraw(True)
    if MMRI3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMRI3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMRI3.tStop = t  # not accounting for scr refresh
            MMRI3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMRI3, 'tStopRefresh')  # time at next scr refresh
            MMRI3.setAutoDraw(False)
    
    # *MMLI4* updates
    if MMLI4.status == NOT_STARTED and tThisFlip >= 149.6-frameTolerance:
        # keep track of start time/frame for later
        MMLI4.frameNStart = frameN  # exact frame index
        MMLI4.tStart = t  # local t and not account for scr refresh
        MMLI4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMLI4, 'tStartRefresh')  # time at next scr refresh
        MMLI4.setAutoDraw(True)
    if MMLI4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMLI4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMLI4.tStop = t  # not accounting for scr refresh
            MMLI4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMLI4, 'tStopRefresh')  # time at next scr refresh
            MMLI4.setAutoDraw(False)
    
    # *MMLI5* updates
    if MMLI5.status == NOT_STARTED and tThisFlip >= 153.4-frameTolerance:
        # keep track of start time/frame for later
        MMLI5.frameNStart = frameN  # exact frame index
        MMLI5.tStart = t  # local t and not account for scr refresh
        MMLI5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMLI5, 'tStartRefresh')  # time at next scr refresh
        MMLI5.setAutoDraw(True)
    if MMLI5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMLI5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMLI5.tStop = t  # not accounting for scr refresh
            MMLI5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMLI5, 'tStopRefresh')  # time at next scr refresh
            MMLI5.setAutoDraw(False)
    
    # *MMLI6* updates
    if MMLI6.status == NOT_STARTED and tThisFlip >= 157.2-frameTolerance:
        # keep track of start time/frame for later
        MMLI6.frameNStart = frameN  # exact frame index
        MMLI6.tStart = t  # local t and not account for scr refresh
        MMLI6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMLI6, 'tStartRefresh')  # time at next scr refresh
        MMLI6.setAutoDraw(True)
    if MMLI6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMLI6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMLI6.tStop = t  # not accounting for scr refresh
            MMLI6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMLI6, 'tStopRefresh')  # time at next scr refresh
            MMLI6.setAutoDraw(False)
    
    # *MMRi4* updates
    if MMRi4.status == NOT_STARTED and tThisFlip >= 161-frameTolerance:
        # keep track of start time/frame for later
        MMRi4.frameNStart = frameN  # exact frame index
        MMRi4.tStart = t  # local t and not account for scr refresh
        MMRi4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMRi4, 'tStartRefresh')  # time at next scr refresh
        MMRi4.setAutoDraw(True)
    if MMRi4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMRi4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMRi4.tStop = t  # not accounting for scr refresh
            MMRi4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMRi4, 'tStopRefresh')  # time at next scr refresh
            MMRi4.setAutoDraw(False)
    
    # *MMRI5* updates
    if MMRI5.status == NOT_STARTED and tThisFlip >= 164.8-frameTolerance:
        # keep track of start time/frame for later
        MMRI5.frameNStart = frameN  # exact frame index
        MMRI5.tStart = t  # local t and not account for scr refresh
        MMRI5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMRI5, 'tStartRefresh')  # time at next scr refresh
        MMRI5.setAutoDraw(True)
    if MMRI5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMRI5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMRI5.tStop = t  # not accounting for scr refresh
            MMRI5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMRI5, 'tStopRefresh')  # time at next scr refresh
            MMRI5.setAutoDraw(False)
    
    # *MMLI7* updates
    if MMLI7.status == NOT_STARTED and tThisFlip >= 168.6-frameTolerance:
        # keep track of start time/frame for later
        MMLI7.frameNStart = frameN  # exact frame index
        MMLI7.tStart = t  # local t and not account for scr refresh
        MMLI7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMLI7, 'tStartRefresh')  # time at next scr refresh
        MMLI7.setAutoDraw(True)
    if MMLI7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMLI7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMLI7.tStop = t  # not accounting for scr refresh
            MMLI7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMLI7, 'tStopRefresh')  # time at next scr refresh
            MMLI7.setAutoDraw(False)
    
    # *MMRI6* updates
    if MMRI6.status == NOT_STARTED and tThisFlip >= 172.4-frameTolerance:
        # keep track of start time/frame for later
        MMRI6.frameNStart = frameN  # exact frame index
        MMRI6.tStart = t  # local t and not account for scr refresh
        MMRI6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMRI6, 'tStartRefresh')  # time at next scr refresh
        MMRI6.setAutoDraw(True)
    if MMRI6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMRI6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMRI6.tStop = t  # not accounting for scr refresh
            MMRI6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMRI6, 'tStopRefresh')  # time at next scr refresh
            MMRI6.setAutoDraw(False)
    
    # *MMRI7* updates
    if MMRI7.status == NOT_STARTED and tThisFlip >= 176.2-frameTolerance:
        # keep track of start time/frame for later
        MMRI7.frameNStart = frameN  # exact frame index
        MMRI7.tStart = t  # local t and not account for scr refresh
        MMRI7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMRI7, 'tStartRefresh')  # time at next scr refresh
        MMRI7.setAutoDraw(True)
    if MMRI7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMRI7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMRI7.tStop = t  # not accounting for scr refresh
            MMRI7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMRI7, 'tStopRefresh')  # time at next scr refresh
            MMRI7.setAutoDraw(False)
    
    # *MMLI8* updates
    if MMLI8.status == NOT_STARTED and tThisFlip >= 180-frameTolerance:
        # keep track of start time/frame for later
        MMLI8.frameNStart = frameN  # exact frame index
        MMLI8.tStart = t  # local t and not account for scr refresh
        MMLI8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MMLI8, 'tStartRefresh')  # time at next scr refresh
        MMLI8.setAutoDraw(True)
    if MMLI8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MMLI8.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MMLI8.tStop = t  # not accounting for scr refresh
            MMLI8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MMLI8, 'tStopRefresh')  # time at next scr refresh
            MMLI8.setAutoDraw(False)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 183.9-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 4.5-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # *MILI1* updates
    if MILI1.status == NOT_STARTED and tThisFlip >= 188.5-frameTolerance:
        # keep track of start time/frame for later
        MILI1.frameNStart = frameN  # exact frame index
        MILI1.tStart = t  # local t and not account for scr refresh
        MILI1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILI1, 'tStartRefresh')  # time at next scr refresh
        MILI1.setAutoDraw(True)
    if MILI1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILI1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILI1.tStop = t  # not accounting for scr refresh
            MILI1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILI1, 'tStopRefresh')  # time at next scr refresh
            MILI1.setAutoDraw(False)
    
    # *MILI2* updates
    if MILI2.status == NOT_STARTED and tThisFlip >= 192.3-frameTolerance:
        # keep track of start time/frame for later
        MILI2.frameNStart = frameN  # exact frame index
        MILI2.tStart = t  # local t and not account for scr refresh
        MILI2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILI2, 'tStartRefresh')  # time at next scr refresh
        MILI2.setAutoDraw(True)
    if MILI2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILI2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILI2.tStop = t  # not accounting for scr refresh
            MILI2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILI2, 'tStopRefresh')  # time at next scr refresh
            MILI2.setAutoDraw(False)
    
    # *MIRI1* updates
    if MIRI1.status == NOT_STARTED and tThisFlip >= 196.1-frameTolerance:
        # keep track of start time/frame for later
        MIRI1.frameNStart = frameN  # exact frame index
        MIRI1.tStart = t  # local t and not account for scr refresh
        MIRI1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRI1, 'tStartRefresh')  # time at next scr refresh
        MIRI1.setAutoDraw(True)
    if MIRI1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRI1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRI1.tStop = t  # not accounting for scr refresh
            MIRI1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRI1, 'tStopRefresh')  # time at next scr refresh
            MIRI1.setAutoDraw(False)
    
    # *MILI3* updates
    if MILI3.status == NOT_STARTED and tThisFlip >= 199.9-frameTolerance:
        # keep track of start time/frame for later
        MILI3.frameNStart = frameN  # exact frame index
        MILI3.tStart = t  # local t and not account for scr refresh
        MILI3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILI3, 'tStartRefresh')  # time at next scr refresh
        MILI3.setAutoDraw(True)
    if MILI3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILI3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILI3.tStop = t  # not accounting for scr refresh
            MILI3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILI3, 'tStopRefresh')  # time at next scr refresh
            MILI3.setAutoDraw(False)
    
    # *MIRi2* updates
    if MIRi2.status == NOT_STARTED and tThisFlip >= 203.7-frameTolerance:
        # keep track of start time/frame for later
        MIRi2.frameNStart = frameN  # exact frame index
        MIRi2.tStart = t  # local t and not account for scr refresh
        MIRi2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRi2, 'tStartRefresh')  # time at next scr refresh
        MIRi2.setAutoDraw(True)
    if MIRi2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRi2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRi2.tStop = t  # not accounting for scr refresh
            MIRi2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRi2, 'tStopRefresh')  # time at next scr refresh
            MIRi2.setAutoDraw(False)
    
    # *MIRI3* updates
    if MIRI3.status == NOT_STARTED and tThisFlip >= 207.5-frameTolerance:
        # keep track of start time/frame for later
        MIRI3.frameNStart = frameN  # exact frame index
        MIRI3.tStart = t  # local t and not account for scr refresh
        MIRI3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRI3, 'tStartRefresh')  # time at next scr refresh
        MIRI3.setAutoDraw(True)
    if MIRI3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRI3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRI3.tStop = t  # not accounting for scr refresh
            MIRI3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRI3, 'tStopRefresh')  # time at next scr refresh
            MIRI3.setAutoDraw(False)
    
    # *MILI4* updates
    if MILI4.status == NOT_STARTED and tThisFlip >= 211.3-frameTolerance:
        # keep track of start time/frame for later
        MILI4.frameNStart = frameN  # exact frame index
        MILI4.tStart = t  # local t and not account for scr refresh
        MILI4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILI4, 'tStartRefresh')  # time at next scr refresh
        MILI4.setAutoDraw(True)
    if MILI4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILI4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILI4.tStop = t  # not accounting for scr refresh
            MILI4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILI4, 'tStopRefresh')  # time at next scr refresh
            MILI4.setAutoDraw(False)
    
    # *MILI5* updates
    if MILI5.status == NOT_STARTED and tThisFlip >= 215.1-frameTolerance:
        # keep track of start time/frame for later
        MILI5.frameNStart = frameN  # exact frame index
        MILI5.tStart = t  # local t and not account for scr refresh
        MILI5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILI5, 'tStartRefresh')  # time at next scr refresh
        MILI5.setAutoDraw(True)
    if MILI5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILI5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILI5.tStop = t  # not accounting for scr refresh
            MILI5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILI5, 'tStopRefresh')  # time at next scr refresh
            MILI5.setAutoDraw(False)
    
    # *MILI6* updates
    if MILI6.status == NOT_STARTED and tThisFlip >= 218.9-frameTolerance:
        # keep track of start time/frame for later
        MILI6.frameNStart = frameN  # exact frame index
        MILI6.tStart = t  # local t and not account for scr refresh
        MILI6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILI6, 'tStartRefresh')  # time at next scr refresh
        MILI6.setAutoDraw(True)
    if MILI6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILI6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILI6.tStop = t  # not accounting for scr refresh
            MILI6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILI6, 'tStopRefresh')  # time at next scr refresh
            MILI6.setAutoDraw(False)
    
    # *MIRI4* updates
    if MIRI4.status == NOT_STARTED and tThisFlip >= 222.7-frameTolerance:
        # keep track of start time/frame for later
        MIRI4.frameNStart = frameN  # exact frame index
        MIRI4.tStart = t  # local t and not account for scr refresh
        MIRI4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRI4, 'tStartRefresh')  # time at next scr refresh
        MIRI4.setAutoDraw(True)
    if MIRI4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRI4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRI4.tStop = t  # not accounting for scr refresh
            MIRI4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRI4, 'tStopRefresh')  # time at next scr refresh
            MIRI4.setAutoDraw(False)
    
    # *MIRI5* updates
    if MIRI5.status == NOT_STARTED and tThisFlip >= 226.5-frameTolerance:
        # keep track of start time/frame for later
        MIRI5.frameNStart = frameN  # exact frame index
        MIRI5.tStart = t  # local t and not account for scr refresh
        MIRI5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRI5, 'tStartRefresh')  # time at next scr refresh
        MIRI5.setAutoDraw(True)
    if MIRI5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRI5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRI5.tStop = t  # not accounting for scr refresh
            MIRI5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRI5, 'tStopRefresh')  # time at next scr refresh
            MIRI5.setAutoDraw(False)
    
    # *MILI7* updates
    if MILI7.status == NOT_STARTED and tThisFlip >= 230.3-frameTolerance:
        # keep track of start time/frame for later
        MILI7.frameNStart = frameN  # exact frame index
        MILI7.tStart = t  # local t and not account for scr refresh
        MILI7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILI7, 'tStartRefresh')  # time at next scr refresh
        MILI7.setAutoDraw(True)
    if MILI7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILI7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILI7.tStop = t  # not accounting for scr refresh
            MILI7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILI7, 'tStopRefresh')  # time at next scr refresh
            MILI7.setAutoDraw(False)
    
    # *MIri6* updates
    if MIri6.status == NOT_STARTED and tThisFlip >= 234.1-frameTolerance:
        # keep track of start time/frame for later
        MIri6.frameNStart = frameN  # exact frame index
        MIri6.tStart = t  # local t and not account for scr refresh
        MIri6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIri6, 'tStartRefresh')  # time at next scr refresh
        MIri6.setAutoDraw(True)
    if MIri6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIri6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIri6.tStop = t  # not accounting for scr refresh
            MIri6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIri6, 'tStopRefresh')  # time at next scr refresh
            MIri6.setAutoDraw(False)
    
    # *miri7* updates
    if miri7.status == NOT_STARTED and tThisFlip >= 237.9-frameTolerance:
        # keep track of start time/frame for later
        miri7.frameNStart = frameN  # exact frame index
        miri7.tStart = t  # local t and not account for scr refresh
        miri7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(miri7, 'tStartRefresh')  # time at next scr refresh
        miri7.setAutoDraw(True)
    if miri7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > miri7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            miri7.tStop = t  # not accounting for scr refresh
            miri7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(miri7, 'tStopRefresh')  # time at next scr refresh
            miri7.setAutoDraw(False)
    
    # *mili8* updates
    if mili8.status == NOT_STARTED and tThisFlip >= 241.7-frameTolerance:
        # keep track of start time/frame for later
        mili8.frameNStart = frameN  # exact frame index
        mili8.tStart = t  # local t and not account for scr refresh
        mili8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mili8, 'tStartRefresh')  # time at next scr refresh
        mili8.setAutoDraw(True)
    if mili8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mili8.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            mili8.tStop = t  # not accounting for scr refresh
            mili8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mili8, 'tStopRefresh')  # time at next scr refresh
            mili8.setAutoDraw(False)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 245.5-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 4.5-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 250.1-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    if text_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_5.tStop = t  # not accounting for scr refresh
            text_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
            text_5.setAutoDraw(False)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 253.9-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
            text_6.setAutoDraw(False)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 257.7-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 261.5-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    if text_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_8.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_8.tStop = t  # not accounting for scr refresh
            text_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
            text_8.setAutoDraw(False)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 265.3-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    if text_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_9.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_9.tStop = t  # not accounting for scr refresh
            text_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
            text_9.setAutoDraw(False)
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 269.1-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    if text_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_10.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_10.tStop = t  # not accounting for scr refresh
            text_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
            text_10.setAutoDraw(False)
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 272.9-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    if text_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_11.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            text_11.tStop = t  # not accounting for scr refresh
            text_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
            text_11.setAutoDraw(False)
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 276.7-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    if text_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_12.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_12.tStop = t  # not accounting for scr refresh
            text_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
            text_12.setAutoDraw(False)
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 280.5-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    if text_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_13.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_13.tStop = t  # not accounting for scr refresh
            text_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
            text_13.setAutoDraw(False)
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 284.3-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    if text_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_14.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_14.tStop = t  # not accounting for scr refresh
            text_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
            text_14.setAutoDraw(False)
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 288.1-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    if text_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_15.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_15.tStop = t  # not accounting for scr refresh
            text_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_15, 'tStopRefresh')  # time at next scr refresh
            text_15.setAutoDraw(False)
    
    # *text_16* updates
    if text_16.status == NOT_STARTED and tThisFlip >= 291.9-frameTolerance:
        # keep track of start time/frame for later
        text_16.frameNStart = frameN  # exact frame index
        text_16.tStart = t  # local t and not account for scr refresh
        text_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    if text_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_16.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_16.tStop = t  # not accounting for scr refresh
            text_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
            text_16.setAutoDraw(False)
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 295.7-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    if text_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_17.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_17.tStop = t  # not accounting for scr refresh
            text_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
            text_17.setAutoDraw(False)
    
    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 299.5-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    if text_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_18.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_18.tStop = t  # not accounting for scr refresh
            text_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
            text_18.setAutoDraw(False)
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 303.3-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    if text_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_19.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_19.tStop = t  # not accounting for scr refresh
            text_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_19, 'tStopRefresh')  # time at next scr refresh
            text_19.setAutoDraw(False)
    
    # *text_20* updates
    if text_20.status == NOT_STARTED and tThisFlip >= 307.1-frameTolerance:
        # keep track of start time/frame for later
        text_20.frameNStart = frameN  # exact frame index
        text_20.tStart = t  # local t and not account for scr refresh
        text_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
        text_20.setAutoDraw(True)
    if text_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_20.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_20.tStop = t  # not accounting for scr refresh
            text_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
            text_20.setAutoDraw(False)
    
    # *text_21* updates
    if text_21.status == NOT_STARTED and tThisFlip >= 310.9-frameTolerance:
        # keep track of start time/frame for later
        text_21.frameNStart = frameN  # exact frame index
        text_21.tStart = t  # local t and not account for scr refresh
        text_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
        text_21.setAutoDraw(True)
    if text_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_21.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_21.tStop = t  # not accounting for scr refresh
            text_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
            text_21.setAutoDraw(False)
    
    # *text_22* updates
    if text_22.status == NOT_STARTED and tThisFlip >= 314.7-frameTolerance:
        # keep track of start time/frame for later
        text_22.frameNStart = frameN  # exact frame index
        text_22.tStart = t  # local t and not account for scr refresh
        text_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
        text_22.setAutoDraw(True)
    if text_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_22.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_22.tStop = t  # not accounting for scr refresh
            text_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_22, 'tStopRefresh')  # time at next scr refresh
            text_22.setAutoDraw(False)
    
    # *text_23* updates
    if text_23.status == NOT_STARTED and tThisFlip >= 318.5-frameTolerance:
        # keep track of start time/frame for later
        text_23.frameNStart = frameN  # exact frame index
        text_23.tStart = t  # local t and not account for scr refresh
        text_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
        text_23.setAutoDraw(True)
    if text_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_23.tStartRefresh + 4.5-frameTolerance:
            # keep track of stop time/frame for later
            text_23.tStop = t  # not accounting for scr refresh
            text_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_23, 'tStopRefresh')  # time at next scr refresh
            text_23.setAutoDraw(False)
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 323.1-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        text_24.setAutoDraw(True)
    if text_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_24.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_24.tStop = t  # not accounting for scr refresh
            text_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_24, 'tStopRefresh')  # time at next scr refresh
            text_24.setAutoDraw(False)
    
    # *text_25* updates
    if text_25.status == NOT_STARTED and tThisFlip >= 326.9-frameTolerance:
        # keep track of start time/frame for later
        text_25.frameNStart = frameN  # exact frame index
        text_25.tStart = t  # local t and not account for scr refresh
        text_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    if text_25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_25.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_25.tStop = t  # not accounting for scr refresh
            text_25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_25, 'tStopRefresh')  # time at next scr refresh
            text_25.setAutoDraw(False)
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 330.7-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        text_26.setAutoDraw(True)
    if text_26.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_26.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_26.tStop = t  # not accounting for scr refresh
            text_26.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_26, 'tStopRefresh')  # time at next scr refresh
            text_26.setAutoDraw(False)
    
    # *text_27* updates
    if text_27.status == NOT_STARTED and tThisFlip >= 334.5-frameTolerance:
        # keep track of start time/frame for later
        text_27.frameNStart = frameN  # exact frame index
        text_27.tStart = t  # local t and not account for scr refresh
        text_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
        text_27.setAutoDraw(True)
    if text_27.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_27.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_27.tStop = t  # not accounting for scr refresh
            text_27.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_27, 'tStopRefresh')  # time at next scr refresh
            text_27.setAutoDraw(False)
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 338.3-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    if text_28.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_28.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_28.tStop = t  # not accounting for scr refresh
            text_28.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_28, 'tStopRefresh')  # time at next scr refresh
            text_28.setAutoDraw(False)
    
    # *text_29* updates
    if text_29.status == NOT_STARTED and tThisFlip >= 342.1-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    if text_29.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_29.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_29.tStop = t  # not accounting for scr refresh
            text_29.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_29, 'tStopRefresh')  # time at next scr refresh
            text_29.setAutoDraw(False)
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 345.9-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 349.7-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    if text_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_31.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_31.tStop = t  # not accounting for scr refresh
            text_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_31, 'tStopRefresh')  # time at next scr refresh
            text_31.setAutoDraw(False)
    
    # *text_32* updates
    if text_32.status == NOT_STARTED and tThisFlip >= 353.5-frameTolerance:
        # keep track of start time/frame for later
        text_32.frameNStart = frameN  # exact frame index
        text_32.tStart = t  # local t and not account for scr refresh
        text_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    if text_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_32.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_32.tStop = t  # not accounting for scr refresh
            text_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
            text_32.setAutoDraw(False)
    
    # *text_33* updates
    if text_33.status == NOT_STARTED and tThisFlip >= 357.3-frameTolerance:
        # keep track of start time/frame for later
        text_33.frameNStart = frameN  # exact frame index
        text_33.tStart = t  # local t and not account for scr refresh
        text_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    if text_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_33.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_33.tStop = t  # not accounting for scr refresh
            text_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_33, 'tStopRefresh')  # time at next scr refresh
            text_33.setAutoDraw(False)
    
    # *text_34* updates
    if text_34.status == NOT_STARTED and tThisFlip >= 361.1-frameTolerance:
        # keep track of start time/frame for later
        text_34.frameNStart = frameN  # exact frame index
        text_34.tStart = t  # local t and not account for scr refresh
        text_34.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_34, 'tStartRefresh')  # time at next scr refresh
        text_34.setAutoDraw(True)
    if text_34.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_34.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_34.tStop = t  # not accounting for scr refresh
            text_34.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_34, 'tStopRefresh')  # time at next scr refresh
            text_34.setAutoDraw(False)
    
    # *text_35* updates
    if text_35.status == NOT_STARTED and tThisFlip >= 364.9-frameTolerance:
        # keep track of start time/frame for later
        text_35.frameNStart = frameN  # exact frame index
        text_35.tStart = t  # local t and not account for scr refresh
        text_35.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_35, 'tStartRefresh')  # time at next scr refresh
        text_35.setAutoDraw(True)
    if text_35.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_35.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_35.tStop = t  # not accounting for scr refresh
            text_35.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_35, 'tStopRefresh')  # time at next scr refresh
            text_35.setAutoDraw(False)
    
    # *text_36* updates
    if text_36.status == NOT_STARTED and tThisFlip >= 368.7-frameTolerance:
        # keep track of start time/frame for later
        text_36.frameNStart = frameN  # exact frame index
        text_36.tStart = t  # local t and not account for scr refresh
        text_36.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_36, 'tStartRefresh')  # time at next scr refresh
        text_36.setAutoDraw(True)
    if text_36.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_36.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_36.tStop = t  # not accounting for scr refresh
            text_36.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_36, 'tStopRefresh')  # time at next scr refresh
            text_36.setAutoDraw(False)
    
    # *text_37* updates
    if text_37.status == NOT_STARTED and tThisFlip >= 372.5-frameTolerance:
        # keep track of start time/frame for later
        text_37.frameNStart = frameN  # exact frame index
        text_37.tStart = t  # local t and not account for scr refresh
        text_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
        text_37.setAutoDraw(True)
    if text_37.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_37.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_37.tStop = t  # not accounting for scr refresh
            text_37.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_37, 'tStopRefresh')  # time at next scr refresh
            text_37.setAutoDraw(False)
    
    # *text_38* updates
    if text_38.status == NOT_STARTED and tThisFlip >= 376.3-frameTolerance:
        # keep track of start time/frame for later
        text_38.frameNStart = frameN  # exact frame index
        text_38.tStart = t  # local t and not account for scr refresh
        text_38.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_38, 'tStartRefresh')  # time at next scr refresh
        text_38.setAutoDraw(True)
    if text_38.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_38.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_38.tStop = t  # not accounting for scr refresh
            text_38.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_38, 'tStopRefresh')  # time at next scr refresh
            text_38.setAutoDraw(False)
    
    # *text_39* updates
    if text_39.status == NOT_STARTED and tThisFlip >= 380.1-frameTolerance:
        # keep track of start time/frame for later
        text_39.frameNStart = frameN  # exact frame index
        text_39.tStart = t  # local t and not account for scr refresh
        text_39.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_39, 'tStartRefresh')  # time at next scr refresh
        text_39.setAutoDraw(True)
    if text_39.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_39.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_39.tStop = t  # not accounting for scr refresh
            text_39.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_39, 'tStopRefresh')  # time at next scr refresh
            text_39.setAutoDraw(False)
    
    # *text_40* updates
    if text_40.status == NOT_STARTED and tThisFlip >= 383.9-frameTolerance:
        # keep track of start time/frame for later
        text_40.frameNStart = frameN  # exact frame index
        text_40.tStart = t  # local t and not account for scr refresh
        text_40.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_40, 'tStartRefresh')  # time at next scr refresh
        text_40.setAutoDraw(True)
    if text_40.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_40.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_40.tStop = t  # not accounting for scr refresh
            text_40.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_40, 'tStopRefresh')  # time at next scr refresh
            text_40.setAutoDraw(False)
    
    # *text_41* updates
    if text_41.status == NOT_STARTED and tThisFlip >= 387.7-frameTolerance:
        # keep track of start time/frame for later
        text_41.frameNStart = frameN  # exact frame index
        text_41.tStart = t  # local t and not account for scr refresh
        text_41.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
        text_41.setAutoDraw(True)
    if text_41.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_41.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            text_41.tStop = t  # not accounting for scr refresh
            text_41.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_41, 'tStopRefresh')  # time at next scr refresh
            text_41.setAutoDraw(False)
    
    # *text_42* updates
    if text_42.status == NOT_STARTED and tThisFlip >= 391.5-frameTolerance:
        # keep track of start time/frame for later
        text_42.frameNStart = frameN  # exact frame index
        text_42.tStart = t  # local t and not account for scr refresh
        text_42.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_42, 'tStartRefresh')  # time at next scr refresh
        text_42.setAutoDraw(True)
    if text_42.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_42.tStartRefresh + 4.5-frameTolerance:
            # keep track of stop time/frame for later
            text_42.tStop = t  # not accounting for scr refresh
            text_42.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_42, 'tStopRefresh')  # time at next scr refresh
            text_42.setAutoDraw(False)
    
    # *MIRM1* updates
    if MIRM1.status == NOT_STARTED and tThisFlip >= 396.1-frameTolerance:
        # keep track of start time/frame for later
        MIRM1.frameNStart = frameN  # exact frame index
        MIRM1.tStart = t  # local t and not account for scr refresh
        MIRM1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRM1, 'tStartRefresh')  # time at next scr refresh
        MIRM1.setAutoDraw(True)
    if MIRM1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRM1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRM1.tStop = t  # not accounting for scr refresh
            MIRM1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRM1, 'tStopRefresh')  # time at next scr refresh
            MIRM1.setAutoDraw(False)
    
    # *MILM1* updates
    if MILM1.status == NOT_STARTED and tThisFlip >= 399.9-frameTolerance:
        # keep track of start time/frame for later
        MILM1.frameNStart = frameN  # exact frame index
        MILM1.tStart = t  # local t and not account for scr refresh
        MILM1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILM1, 'tStartRefresh')  # time at next scr refresh
        MILM1.setAutoDraw(True)
    if MILM1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILM1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILM1.tStop = t  # not accounting for scr refresh
            MILM1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILM1, 'tStopRefresh')  # time at next scr refresh
            MILM1.setAutoDraw(False)
    
    # *MIRM2* updates
    if MIRM2.status == NOT_STARTED and tThisFlip >= 403.7-frameTolerance:
        # keep track of start time/frame for later
        MIRM2.frameNStart = frameN  # exact frame index
        MIRM2.tStart = t  # local t and not account for scr refresh
        MIRM2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRM2, 'tStartRefresh')  # time at next scr refresh
        MIRM2.setAutoDraw(True)
    if MIRM2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRM2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRM2.tStop = t  # not accounting for scr refresh
            MIRM2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRM2, 'tStopRefresh')  # time at next scr refresh
            MIRM2.setAutoDraw(False)
    
    # *MILM2* updates
    if MILM2.status == NOT_STARTED and tThisFlip >= 407.5-frameTolerance:
        # keep track of start time/frame for later
        MILM2.frameNStart = frameN  # exact frame index
        MILM2.tStart = t  # local t and not account for scr refresh
        MILM2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILM2, 'tStartRefresh')  # time at next scr refresh
        MILM2.setAutoDraw(True)
    if MILM2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILM2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILM2.tStop = t  # not accounting for scr refresh
            MILM2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILM2, 'tStopRefresh')  # time at next scr refresh
            MILM2.setAutoDraw(False)
    
    # *MILM3* updates
    if MILM3.status == NOT_STARTED and tThisFlip >= 411.3-frameTolerance:
        # keep track of start time/frame for later
        MILM3.frameNStart = frameN  # exact frame index
        MILM3.tStart = t  # local t and not account for scr refresh
        MILM3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILM3, 'tStartRefresh')  # time at next scr refresh
        MILM3.setAutoDraw(True)
    if MILM3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILM3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILM3.tStop = t  # not accounting for scr refresh
            MILM3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILM3, 'tStopRefresh')  # time at next scr refresh
            MILM3.setAutoDraw(False)
    
    # *MIRM3* updates
    if MIRM3.status == NOT_STARTED and tThisFlip >= 415.1-frameTolerance:
        # keep track of start time/frame for later
        MIRM3.frameNStart = frameN  # exact frame index
        MIRM3.tStart = t  # local t and not account for scr refresh
        MIRM3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRM3, 'tStartRefresh')  # time at next scr refresh
        MIRM3.setAutoDraw(True)
    if MIRM3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRM3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRM3.tStop = t  # not accounting for scr refresh
            MIRM3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRM3, 'tStopRefresh')  # time at next scr refresh
            MIRM3.setAutoDraw(False)
    
    # *MILM4* updates
    if MILM4.status == NOT_STARTED and tThisFlip >= 418.9-frameTolerance:
        # keep track of start time/frame for later
        MILM4.frameNStart = frameN  # exact frame index
        MILM4.tStart = t  # local t and not account for scr refresh
        MILM4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILM4, 'tStartRefresh')  # time at next scr refresh
        MILM4.setAutoDraw(True)
    if MILM4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILM4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILM4.tStop = t  # not accounting for scr refresh
            MILM4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILM4, 'tStopRefresh')  # time at next scr refresh
            MILM4.setAutoDraw(False)
    
    # *MIRM4* updates
    if MIRM4.status == NOT_STARTED and tThisFlip >= 422.7-frameTolerance:
        # keep track of start time/frame for later
        MIRM4.frameNStart = frameN  # exact frame index
        MIRM4.tStart = t  # local t and not account for scr refresh
        MIRM4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRM4, 'tStartRefresh')  # time at next scr refresh
        MIRM4.setAutoDraw(True)
    if MIRM4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRM4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRM4.tStop = t  # not accounting for scr refresh
            MIRM4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRM4, 'tStopRefresh')  # time at next scr refresh
            MIRM4.setAutoDraw(False)
    
    # *MILM5* updates
    if MILM5.status == NOT_STARTED and tThisFlip >= 426.5-frameTolerance:
        # keep track of start time/frame for later
        MILM5.frameNStart = frameN  # exact frame index
        MILM5.tStart = t  # local t and not account for scr refresh
        MILM5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILM5, 'tStartRefresh')  # time at next scr refresh
        MILM5.setAutoDraw(True)
    if MILM5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILM5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILM5.tStop = t  # not accounting for scr refresh
            MILM5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILM5, 'tStopRefresh')  # time at next scr refresh
            MILM5.setAutoDraw(False)
    
    # *MIRM5* updates
    if MIRM5.status == NOT_STARTED and tThisFlip >= 430.3-frameTolerance:
        # keep track of start time/frame for later
        MIRM5.frameNStart = frameN  # exact frame index
        MIRM5.tStart = t  # local t and not account for scr refresh
        MIRM5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRM5, 'tStartRefresh')  # time at next scr refresh
        MIRM5.setAutoDraw(True)
    if MIRM5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRM5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRM5.tStop = t  # not accounting for scr refresh
            MIRM5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRM5, 'tStopRefresh')  # time at next scr refresh
            MIRM5.setAutoDraw(False)
    
    # *MIRM6* updates
    if MIRM6.status == NOT_STARTED and tThisFlip >= 434.1-frameTolerance:
        # keep track of start time/frame for later
        MIRM6.frameNStart = frameN  # exact frame index
        MIRM6.tStart = t  # local t and not account for scr refresh
        MIRM6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRM6, 'tStartRefresh')  # time at next scr refresh
        MIRM6.setAutoDraw(True)
    if MIRM6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRM6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRM6.tStop = t  # not accounting for scr refresh
            MIRM6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRM6, 'tStopRefresh')  # time at next scr refresh
            MIRM6.setAutoDraw(False)
    
    # *MILM6* updates
    if MILM6.status == NOT_STARTED and tThisFlip >= 437.9-frameTolerance:
        # keep track of start time/frame for later
        MILM6.frameNStart = frameN  # exact frame index
        MILM6.tStart = t  # local t and not account for scr refresh
        MILM6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILM6, 'tStartRefresh')  # time at next scr refresh
        MILM6.setAutoDraw(True)
    if MILM6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILM6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILM6.tStop = t  # not accounting for scr refresh
            MILM6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILM6, 'tStopRefresh')  # time at next scr refresh
            MILM6.setAutoDraw(False)
    
    # *MIRM7* updates
    if MIRM7.status == NOT_STARTED and tThisFlip >= 441.7-frameTolerance:
        # keep track of start time/frame for later
        MIRM7.frameNStart = frameN  # exact frame index
        MIRM7.tStart = t  # local t and not account for scr refresh
        MIRM7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MIRM7, 'tStartRefresh')  # time at next scr refresh
        MIRM7.setAutoDraw(True)
    if MIRM7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MIRM7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MIRM7.tStop = t  # not accounting for scr refresh
            MIRM7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MIRM7, 'tStopRefresh')  # time at next scr refresh
            MIRM7.setAutoDraw(False)
    
    # *MILM7* updates
    if MILM7.status == NOT_STARTED and tThisFlip >= 445.5-frameTolerance:
        # keep track of start time/frame for later
        MILM7.frameNStart = frameN  # exact frame index
        MILM7.tStart = t  # local t and not account for scr refresh
        MILM7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILM7, 'tStartRefresh')  # time at next scr refresh
        MILM7.setAutoDraw(True)
    if MILM7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILM7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILM7.tStop = t  # not accounting for scr refresh
            MILM7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILM7, 'tStopRefresh')  # time at next scr refresh
            MILM7.setAutoDraw(False)
    
    # *MILM8* updates
    if MILM8.status == NOT_STARTED and tThisFlip >= 449.3-frameTolerance:
        # keep track of start time/frame for later
        MILM8.frameNStart = frameN  # exact frame index
        MILM8.tStart = t  # local t and not account for scr refresh
        MILM8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MILM8, 'tStartRefresh')  # time at next scr refresh
        MILM8.setAutoDraw(True)
    if MILM8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MILM8.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            MILM8.tStop = t  # not accounting for scr refresh
            MILM8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MILM8, 'tStopRefresh')  # time at next scr refresh
            MILM8.setAutoDraw(False)
    
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
thisExp.addData('LC1.started', LC1.tStartRefresh)
thisExp.addData('LC1.stopped', LC1.tStopRefresh)
thisExp.addData('LC2.started', LC2.tStartRefresh)
thisExp.addData('LC2.stopped', LC2.tStopRefresh)
thisExp.addData('Rc1.started', Rc1.tStartRefresh)
thisExp.addData('Rc1.stopped', Rc1.tStopRefresh)
thisExp.addData('lc3.started', lc3.tStartRefresh)
thisExp.addData('lc3.stopped', lc3.tStopRefresh)
thisExp.addData('rc2.started', rc2.tStartRefresh)
thisExp.addData('rc2.stopped', rc2.tStopRefresh)
thisExp.addData('rc3.started', rc3.tStartRefresh)
thisExp.addData('rc3.stopped', rc3.tStopRefresh)
thisExp.addData('lc4.started', lc4.tStartRefresh)
thisExp.addData('lc4.stopped', lc4.tStopRefresh)
thisExp.addData('lc5.started', lc5.tStartRefresh)
thisExp.addData('lc5.stopped', lc5.tStopRefresh)
thisExp.addData('lc6.started', lc6.tStartRefresh)
thisExp.addData('lc6.stopped', lc6.tStopRefresh)
thisExp.addData('rc4.started', rc4.tStartRefresh)
thisExp.addData('rc4.stopped', rc4.tStopRefresh)
thisExp.addData('rc5.started', rc5.tStartRefresh)
thisExp.addData('rc5.stopped', rc5.tStopRefresh)
thisExp.addData('lc7.started', lc7.tStartRefresh)
thisExp.addData('lc7.stopped', lc7.tStopRefresh)
thisExp.addData('rc6.started', rc6.tStartRefresh)
thisExp.addData('rc6.stopped', rc6.tStopRefresh)
thisExp.addData('rc7.started', rc7.tStartRefresh)
thisExp.addData('rc7.stopped', rc7.tStopRefresh)
thisExp.addData('lc8.started', lc8.tStartRefresh)
thisExp.addData('lc8.stopped', lc8.tStopRefresh)
thisExp.addData('MI1LC1.started', MI1LC1.tStartRefresh)
thisExp.addData('MI1LC1.stopped', MI1LC1.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('MILC2.started', MILC2.tStartRefresh)
thisExp.addData('MILC2.stopped', MILC2.tStopRefresh)
thisExp.addData('MIRC1.started', MIRC1.tStartRefresh)
thisExp.addData('MIRC1.stopped', MIRC1.tStopRefresh)
thisExp.addData('MILC3.started', MILC3.tStartRefresh)
thisExp.addData('MILC3.stopped', MILC3.tStopRefresh)
thisExp.addData('MIRC2.started', MIRC2.tStartRefresh)
thisExp.addData('MIRC2.stopped', MIRC2.tStopRefresh)
thisExp.addData('MIRC3.started', MIRC3.tStartRefresh)
thisExp.addData('MIRC3.stopped', MIRC3.tStopRefresh)
thisExp.addData('MILC4.started', MILC4.tStartRefresh)
thisExp.addData('MILC4.stopped', MILC4.tStopRefresh)
thisExp.addData('MILC5.started', MILC5.tStartRefresh)
thisExp.addData('MILC5.stopped', MILC5.tStopRefresh)
thisExp.addData('MILC6.started', MILC6.tStartRefresh)
thisExp.addData('MILC6.stopped', MILC6.tStopRefresh)
thisExp.addData('MIRC4.started', MIRC4.tStartRefresh)
thisExp.addData('MIRC4.stopped', MIRC4.tStopRefresh)
thisExp.addData('MIRC5.started', MIRC5.tStartRefresh)
thisExp.addData('MIRC5.stopped', MIRC5.tStopRefresh)
thisExp.addData('MILC7.started', MILC7.tStartRefresh)
thisExp.addData('MILC7.stopped', MILC7.tStopRefresh)
thisExp.addData('MIRC6.started', MIRC6.tStartRefresh)
thisExp.addData('MIRC6.stopped', MIRC6.tStopRefresh)
thisExp.addData('MIRC7.started', MIRC7.tStartRefresh)
thisExp.addData('MIRC7.stopped', MIRC7.tStopRefresh)
thisExp.addData('MILC8.started', MILC8.tStartRefresh)
thisExp.addData('MILC8.stopped', MILC8.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('MMLI1.started', MMLI1.tStartRefresh)
thisExp.addData('MMLI1.stopped', MMLI1.tStopRefresh)
thisExp.addData('MMLI2.started', MMLI2.tStartRefresh)
thisExp.addData('MMLI2.stopped', MMLI2.tStopRefresh)
thisExp.addData('MMRI1.started', MMRI1.tStartRefresh)
thisExp.addData('MMRI1.stopped', MMRI1.tStopRefresh)
thisExp.addData('MMLI3.started', MMLI3.tStartRefresh)
thisExp.addData('MMLI3.stopped', MMLI3.tStopRefresh)
thisExp.addData('MMRI2.started', MMRI2.tStartRefresh)
thisExp.addData('MMRI2.stopped', MMRI2.tStopRefresh)
thisExp.addData('MMRI3.started', MMRI3.tStartRefresh)
thisExp.addData('MMRI3.stopped', MMRI3.tStopRefresh)
thisExp.addData('MMLI4.started', MMLI4.tStartRefresh)
thisExp.addData('MMLI4.stopped', MMLI4.tStopRefresh)
thisExp.addData('MMLI5.started', MMLI5.tStartRefresh)
thisExp.addData('MMLI5.stopped', MMLI5.tStopRefresh)
thisExp.addData('MMLI6.started', MMLI6.tStartRefresh)
thisExp.addData('MMLI6.stopped', MMLI6.tStopRefresh)
thisExp.addData('MMRi4.started', MMRi4.tStartRefresh)
thisExp.addData('MMRi4.stopped', MMRi4.tStopRefresh)
thisExp.addData('MMRI5.started', MMRI5.tStartRefresh)
thisExp.addData('MMRI5.stopped', MMRI5.tStopRefresh)
thisExp.addData('MMLI7.started', MMLI7.tStartRefresh)
thisExp.addData('MMLI7.stopped', MMLI7.tStopRefresh)
thisExp.addData('MMRI6.started', MMRI6.tStartRefresh)
thisExp.addData('MMRI6.stopped', MMRI6.tStopRefresh)
thisExp.addData('MMRI7.started', MMRI7.tStartRefresh)
thisExp.addData('MMRI7.stopped', MMRI7.tStopRefresh)
thisExp.addData('MMLI8.started', MMLI8.tStartRefresh)
thisExp.addData('MMLI8.stopped', MMLI8.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('MILI1.started', MILI1.tStartRefresh)
thisExp.addData('MILI1.stopped', MILI1.tStopRefresh)
thisExp.addData('MILI2.started', MILI2.tStartRefresh)
thisExp.addData('MILI2.stopped', MILI2.tStopRefresh)
thisExp.addData('MIRI1.started', MIRI1.tStartRefresh)
thisExp.addData('MIRI1.stopped', MIRI1.tStopRefresh)
thisExp.addData('MILI3.started', MILI3.tStartRefresh)
thisExp.addData('MILI3.stopped', MILI3.tStopRefresh)
thisExp.addData('MIRi2.started', MIRi2.tStartRefresh)
thisExp.addData('MIRi2.stopped', MIRi2.tStopRefresh)
thisExp.addData('MIRI3.started', MIRI3.tStartRefresh)
thisExp.addData('MIRI3.stopped', MIRI3.tStopRefresh)
thisExp.addData('MILI4.started', MILI4.tStartRefresh)
thisExp.addData('MILI4.stopped', MILI4.tStopRefresh)
thisExp.addData('MILI5.started', MILI5.tStartRefresh)
thisExp.addData('MILI5.stopped', MILI5.tStopRefresh)
thisExp.addData('MILI6.started', MILI6.tStartRefresh)
thisExp.addData('MILI6.stopped', MILI6.tStopRefresh)
thisExp.addData('MIRI4.started', MIRI4.tStartRefresh)
thisExp.addData('MIRI4.stopped', MIRI4.tStopRefresh)
thisExp.addData('MIRI5.started', MIRI5.tStartRefresh)
thisExp.addData('MIRI5.stopped', MIRI5.tStopRefresh)
thisExp.addData('MILI7.started', MILI7.tStartRefresh)
thisExp.addData('MILI7.stopped', MILI7.tStopRefresh)
thisExp.addData('MIri6.started', MIri6.tStartRefresh)
thisExp.addData('MIri6.stopped', MIri6.tStopRefresh)
thisExp.addData('miri7.started', miri7.tStartRefresh)
thisExp.addData('miri7.stopped', miri7.tStopRefresh)
thisExp.addData('mili8.started', mili8.tStartRefresh)
thisExp.addData('mili8.stopped', mili8.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)
thisExp.addData('text_20.started', text_20.tStartRefresh)
thisExp.addData('text_20.stopped', text_20.tStopRefresh)
thisExp.addData('text_21.started', text_21.tStartRefresh)
thisExp.addData('text_21.stopped', text_21.tStopRefresh)
thisExp.addData('text_22.started', text_22.tStartRefresh)
thisExp.addData('text_22.stopped', text_22.tStopRefresh)
thisExp.addData('text_23.started', text_23.tStartRefresh)
thisExp.addData('text_23.stopped', text_23.tStopRefresh)
thisExp.addData('text_24.started', text_24.tStartRefresh)
thisExp.addData('text_24.stopped', text_24.tStopRefresh)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)
thisExp.addData('text_26.started', text_26.tStartRefresh)
thisExp.addData('text_26.stopped', text_26.tStopRefresh)
thisExp.addData('text_27.started', text_27.tStartRefresh)
thisExp.addData('text_27.stopped', text_27.tStopRefresh)
thisExp.addData('text_28.started', text_28.tStartRefresh)
thisExp.addData('text_28.stopped', text_28.tStopRefresh)
thisExp.addData('text_29.started', text_29.tStartRefresh)
thisExp.addData('text_29.stopped', text_29.tStopRefresh)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
thisExp.addData('text_34.started', text_34.tStartRefresh)
thisExp.addData('text_34.stopped', text_34.tStopRefresh)
thisExp.addData('text_35.started', text_35.tStartRefresh)
thisExp.addData('text_35.stopped', text_35.tStopRefresh)
thisExp.addData('text_36.started', text_36.tStartRefresh)
thisExp.addData('text_36.stopped', text_36.tStopRefresh)
thisExp.addData('text_37.started', text_37.tStartRefresh)
thisExp.addData('text_37.stopped', text_37.tStopRefresh)
thisExp.addData('text_38.started', text_38.tStartRefresh)
thisExp.addData('text_38.stopped', text_38.tStopRefresh)
thisExp.addData('text_39.started', text_39.tStartRefresh)
thisExp.addData('text_39.stopped', text_39.tStopRefresh)
thisExp.addData('text_40.started', text_40.tStartRefresh)
thisExp.addData('text_40.stopped', text_40.tStopRefresh)
thisExp.addData('text_41.started', text_41.tStartRefresh)
thisExp.addData('text_41.stopped', text_41.tStopRefresh)
thisExp.addData('text_42.started', text_42.tStartRefresh)
thisExp.addData('text_42.stopped', text_42.tStopRefresh)
thisExp.addData('MIRM1.started', MIRM1.tStartRefresh)
thisExp.addData('MIRM1.stopped', MIRM1.tStopRefresh)
thisExp.addData('MILM1.started', MILM1.tStartRefresh)
thisExp.addData('MILM1.stopped', MILM1.tStopRefresh)
thisExp.addData('MIRM2.started', MIRM2.tStartRefresh)
thisExp.addData('MIRM2.stopped', MIRM2.tStopRefresh)
thisExp.addData('MILM2.started', MILM2.tStartRefresh)
thisExp.addData('MILM2.stopped', MILM2.tStopRefresh)
thisExp.addData('MILM3.started', MILM3.tStartRefresh)
thisExp.addData('MILM3.stopped', MILM3.tStopRefresh)
thisExp.addData('MIRM3.started', MIRM3.tStartRefresh)
thisExp.addData('MIRM3.stopped', MIRM3.tStopRefresh)
thisExp.addData('MILM4.started', MILM4.tStartRefresh)
thisExp.addData('MILM4.stopped', MILM4.tStopRefresh)
thisExp.addData('MIRM4.started', MIRM4.tStartRefresh)
thisExp.addData('MIRM4.stopped', MIRM4.tStopRefresh)
thisExp.addData('MILM5.started', MILM5.tStartRefresh)
thisExp.addData('MILM5.stopped', MILM5.tStopRefresh)
thisExp.addData('MIRM5.started', MIRM5.tStartRefresh)
thisExp.addData('MIRM5.stopped', MIRM5.tStopRefresh)
thisExp.addData('MIRM6.started', MIRM6.tStartRefresh)
thisExp.addData('MIRM6.stopped', MIRM6.tStopRefresh)
thisExp.addData('MILM6.started', MILM6.tStartRefresh)
thisExp.addData('MILM6.stopped', MILM6.tStopRefresh)
thisExp.addData('MIRM7.started', MIRM7.tStartRefresh)
thisExp.addData('MIRM7.stopped', MIRM7.tStopRefresh)
thisExp.addData('MILM7.started', MILM7.tStartRefresh)
thisExp.addData('MILM7.stopped', MILM7.tStopRefresh)
thisExp.addData('MILM8.started', MILM8.tStartRefresh)
thisExp.addData('MILM8.stopped', MILM8.tStopRefresh)

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
