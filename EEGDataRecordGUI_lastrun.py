#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on May 11, 2022, at 12:07
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
    originPath='C:\\Users\\tanveerlaptop\\Desktop\\EEG data recording GUI\\EEGDataRecordGUI_lastrun.py',
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
LC1 = visual.ImageStim(
    win=win,
    name='LC1', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
LC2 = visual.ImageStim(
    win=win,
    name='LC2', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
Rc1 = visual.ImageStim(
    win=win,
    name='Rc1', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
lc3 = visual.ImageStim(
    win=win,
    name='lc3', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
rc2 = visual.ImageStim(
    win=win,
    name='rc2', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
rc3 = visual.ImageStim(
    win=win,
    name='rc3', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
lc4 = visual.ImageStim(
    win=win,
    name='lc4', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
lc5 = visual.ImageStim(
    win=win,
    name='lc5', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
lc6 = visual.ImageStim(
    win=win,
    name='lc6', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-10.0)
rc4 = visual.ImageStim(
    win=win,
    name='rc4', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-11.0)
rc5 = visual.ImageStim(
    win=win,
    name='rc5', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-12.0)
lc7 = visual.ImageStim(
    win=win,
    name='lc7', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-13.0)
rc6 = visual.ImageStim(
    win=win,
    name='rc6', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-14.0)
rc7 = visual.ImageStim(
    win=win,
    name='rc7', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-15.0)
lc8 = visual.ImageStim(
    win=win,
    name='lc8', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-16.0)
MI1LC1 = visual.ImageStim(
    win=win,
    name='MI1LC1', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-17.0)
text = visual.TextStim(win=win, name='text',
    text='\n\nYou can relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-18.0);
MILC2 = visual.ImageStim(
    win=win,
    name='MILC2', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-19.0)
MIRC1 = visual.ImageStim(
    win=win,
    name='MIRC1', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-20.0)
MILC3 = visual.ImageStim(
    win=win,
    name='MILC3', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-21.0)
MIRC2 = visual.ImageStim(
    win=win,
    name='MIRC2', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-22.0)
MIRC3 = visual.ImageStim(
    win=win,
    name='MIRC3', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-23.0)
MILC4 = visual.ImageStim(
    win=win,
    name='MILC4', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-24.0)
MILC5 = visual.ImageStim(
    win=win,
    name='MILC5', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-25.0)
MILC6 = visual.ImageStim(
    win=win,
    name='MILC6', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-26.0)
MIRC4 = visual.ImageStim(
    win=win,
    name='MIRC4', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-27.0)
MIRC5 = visual.ImageStim(
    win=win,
    name='MIRC5', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-28.0)
MILC7 = visual.ImageStim(
    win=win,
    name='MILC7', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-29.0)
MIRC6 = visual.ImageStim(
    win=win,
    name='MIRC6', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-30.0)
MIRC7 = visual.ImageStim(
    win=win,
    name='MIRC7', 
    image='RC.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-31.0)
MILC8 = visual.ImageStim(
    win=win,
    name='MILC8', 
    image='LC.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-32.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='\n\n\nYou can Relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-33.0);
MMLI1 = visual.ImageStim(
    win=win,
    name='MMLI1', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-34.0)
MMLI2 = visual.ImageStim(
    win=win,
    name='MMLI2', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-35.0)
MMRI1 = visual.ImageStim(
    win=win,
    name='MMRI1', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-36.0)
MMLI3 = visual.ImageStim(
    win=win,
    name='MMLI3', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-37.0)
MMRI2 = visual.ImageStim(
    win=win,
    name='MMRI2', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-38.0)
MMRI3 = visual.ImageStim(
    win=win,
    name='MMRI3', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-39.0)
MMLI4 = visual.ImageStim(
    win=win,
    name='MMLI4', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-40.0)
MMLI5 = visual.ImageStim(
    win=win,
    name='MMLI5', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-41.0)
MMLI6 = visual.ImageStim(
    win=win,
    name='MMLI6', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-42.0)
MMRi4 = visual.ImageStim(
    win=win,
    name='MMRi4', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-43.0)
MMRI5 = visual.ImageStim(
    win=win,
    name='MMRI5', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-44.0)
MMLI7 = visual.ImageStim(
    win=win,
    name='MMLI7', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-45.0)
MMRI6 = visual.ImageStim(
    win=win,
    name='MMRI6', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-46.0)
MMRI7 = visual.ImageStim(
    win=win,
    name='MMRI7', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-47.0)
MMLI8 = visual.ImageStim(
    win=win,
    name='MMLI8', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-48.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='\n\n\nYou can relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-49.0);
MILI1 = visual.ImageStim(
    win=win,
    name='MILI1', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-50.0)
MILI2 = visual.ImageStim(
    win=win,
    name='MILI2', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-51.0)
MIRI1 = visual.ImageStim(
    win=win,
    name='MIRI1', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-52.0)
MILI3 = visual.ImageStim(
    win=win,
    name='MILI3', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-53.0)
MIRi2 = visual.ImageStim(
    win=win,
    name='MIRi2', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-54.0)
MIRI3 = visual.ImageStim(
    win=win,
    name='MIRI3', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-55.0)
MILI4 = visual.ImageStim(
    win=win,
    name='MILI4', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-56.0)
MILI5 = visual.ImageStim(
    win=win,
    name='MILI5', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-57.0)
MILI6 = visual.ImageStim(
    win=win,
    name='MILI6', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-58.0)
MIRI4 = visual.ImageStim(
    win=win,
    name='MIRI4', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-59.0)
MIRI5 = visual.ImageStim(
    win=win,
    name='MIRI5', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-60.0)
MILI7 = visual.ImageStim(
    win=win,
    name='MILI7', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-61.0)
MIri6 = visual.ImageStim(
    win=win,
    name='MIri6', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-62.0)
miri7 = visual.ImageStim(
    win=win,
    name='miri7', 
    image='RI.png', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-63.0)
mili8 = visual.ImageStim(
    win=win,
    name='mili8', 
    image='LI.png', mask=None, anchor='center-right',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-64.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text='\n\nYou can relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-65.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='\n\n\nPress K',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-66.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='\n\n\nPress W',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-67.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='\n\nPress T',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-68.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='\n\n\nPress Z',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-69.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='Press I',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-70.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text='Press B',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-71.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='Press X',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-72.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='Press Y',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-73.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='Press B',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-74.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text='Press C',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-75.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='Press O',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-76.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='Press R',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-77.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Press V',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-78.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='Press N',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-79.0);
text_19 = visual.TextStim(win=win, name='text_19',
    text='Press U',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-80.0);
text_20 = visual.TextStim(win=win, name='text_20',
    text='Press M',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-81.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='Press A',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-82.0);
text_22 = visual.TextStim(win=win, name='text_22',
    text='Press F',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-83.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text='\n\n\nYou can Relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-84.0);
text_24 = visual.TextStim(win=win, name='text_24',
    text='Press G',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-85.0);
text_25 = visual.TextStim(win=win, name='text_25',
    text='Press E',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-86.0);
text_26 = visual.TextStim(win=win, name='text_26',
    text='Press Z',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-87.0);
text_27 = visual.TextStim(win=win, name='text_27',
    text='Press O',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-88.0);
text_28 = visual.TextStim(win=win, name='text_28',
    text='Press I',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-89.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Press B',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-90.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='Press A',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-91.0);
text_31 = visual.TextStim(win=win, name='text_31',
    text='Press Q',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-92.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='Press B',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-93.0);
text_33 = visual.TextStim(win=win, name='text_33',
    text='Press C',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-94.0);
text_34 = visual.TextStim(win=win, name='text_34',
    text='Press O',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-95.0);
text_35 = visual.TextStim(win=win, name='text_35',
    text='Press R',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-96.0);
text_36 = visual.TextStim(win=win, name='text_36',
    text='Press V',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-97.0);
text_37 = visual.TextStim(win=win, name='text_37',
    text='Press N',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-98.0);
text_38 = visual.TextStim(win=win, name='text_38',
    text='Press U',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-99.0);
text_39 = visual.TextStim(win=win, name='text_39',
    text='Press M',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-100.0);
text_40 = visual.TextStim(win=win, name='text_40',
    text='Press L',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-101.0);
text_41 = visual.TextStim(win=win, name='text_41',
    text='Press F',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-102.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='You can Relax for 5 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-103.0);
MIRM1 = visual.ImageStim(
    win=win,
    name='MIRM1', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-104.0)
MILM1 = visual.ImageStim(
    win=win,
    name='MILM1', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-105.0)
MIRM2 = visual.ImageStim(
    win=win,
    name='MIRM2', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-106.0)
MILM2 = visual.ImageStim(
    win=win,
    name='MILM2', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-107.0)
MILM3 = visual.ImageStim(
    win=win,
    name='MILM3', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-108.0)
MIRM3 = visual.ImageStim(
    win=win,
    name='MIRM3', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-109.0)
MILM4 = visual.ImageStim(
    win=win,
    name='MILM4', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-110.0)
MIRM4 = visual.ImageStim(
    win=win,
    name='MIRM4', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-111.0)
MILM5 = visual.ImageStim(
    win=win,
    name='MILM5', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-112.0)
MIRM5 = visual.ImageStim(
    win=win,
    name='MIRM5', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-113.0)
MIRM6 = visual.ImageStim(
    win=win,
    name='MIRM6', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-114.0)
MILM6 = visual.ImageStim(
    win=win,
    name='MILM6', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-115.0)
MIRM7 = visual.ImageStim(
    win=win,
    name='MIRM7', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-116.0)
MILM7 = visual.ImageStim(
    win=win,
    name='MILM7', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-117.0)
MILM8 = visual.ImageStim(
    win=win,
    name='MILM8', 
    image='mug image.jpg', mask=None, anchor='center-left',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-118.0)
text_43 = visual.TextStim(win=win, name='text_43',
    text='Your can relax for 3 seconds ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-119.0);
sound_2 = sound.Sound('A', secs=.500, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
sound_3 = sound.Sound('A', secs=.500, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
VEP1I9 = visual.ImageStim(
    win=win,
    name='VEP1I9', 
    image='VEP3 protocol images/9.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-122.0)
S9 = visual.Slider(win=win, name='S9',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity','Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor=[0.6549, 0.6549, 0.6549], markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-123, readOnly=False)
vep1I18 = visual.ImageStim(
    win=win,
    name='vep1I18', 
    image='VEP3 protocol images/18.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-124.0)
S18 = visual.Slider(win=win, name='S18',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-125, readOnly=False)
VEP1I31 = visual.ImageStim(
    win=win,
    name='VEP1I31', 
    image='VEP3 protocol images/31.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-126.0)
S31 = visual.Slider(win=win, name='S31',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-127, readOnly=False)
VEP1I24 = visual.ImageStim(
    win=win,
    name='VEP1I24', 
    image='VEP3 protocol images/24.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-128.0)
S24 = visual.Slider(win=win, name='S24',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-129, readOnly=False)
VEP1I30 = visual.ImageStim(
    win=win,
    name='VEP1I30', 
    image='VEP3 protocol images/30.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-130.0)
S30 = visual.Slider(win=win, name='S30',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-131, readOnly=False)
VEp1I12 = visual.ImageStim(
    win=win,
    name='VEp1I12', 
    image='VEP3 protocol images/12.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-132.0)
S12 = visual.Slider(win=win, name='S12',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-133, readOnly=False)
VEP1I27 = visual.ImageStim(
    win=win,
    name='VEP1I27', 
    image='VEP3 protocol images/27.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-134.0)
S27 = visual.Slider(win=win, name='S27',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-135, readOnly=False)
VEP1I28 = visual.ImageStim(
    win=win,
    name='VEP1I28', 
    image='VEP3 protocol images/28.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-136.0)
S28 = visual.Slider(win=win, name='S28',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-137, readOnly=False)
VEP1I16 = visual.ImageStim(
    win=win,
    name='VEP1I16', 
    image='VEP3 protocol images/16.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-138.0)
S16 = visual.Slider(win=win, name='S16',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-139, readOnly=False)
VEP1I29 = visual.ImageStim(
    win=win,
    name='VEP1I29', 
    image='VEP3 protocol images/29.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-140.0)
S29 = visual.Slider(win=win, name='S29',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-141, readOnly=False)
VEP1I32 = visual.ImageStim(
    win=win,
    name='VEP1I32', 
    image='VEP3 protocol images/32.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-142.0)
S32 = visual.Slider(win=win, name='S32',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-143, readOnly=False)
VEP1I5 = visual.ImageStim(
    win=win,
    name='VEP1I5', 
    image='VEP3 protocol images/5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-144.0)
S5 = visual.Slider(win=win, name='S5',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-145, readOnly=False)
VEP1I23 = visual.ImageStim(
    win=win,
    name='VEP1I23', 
    image='VEP3 protocol images/23.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-146.0)
S23 = visual.Slider(win=win, name='S23',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-147, readOnly=False)
VEP1I26 = visual.ImageStim(
    win=win,
    name='VEP1I26', 
    image='VEP3 protocol images/26.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-148.0)
S26 = visual.Slider(win=win, name='S26',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-149, readOnly=False)
vep1I8 = visual.ImageStim(
    win=win,
    name='vep1I8', 
    image='VEP3 protocol images/8.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-150.0)
S8 = visual.Slider(win=win, name='S8',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-151, readOnly=False)
VEp1I17 = visual.ImageStim(
    win=win,
    name='VEp1I17', 
    image='VEP3 protocol images/17.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-152.0)
S17 = visual.Slider(win=win, name='S17',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-153, readOnly=False)
VEP1I3 = visual.ImageStim(
    win=win,
    name='VEP1I3', 
    image='VEP3 protocol images/3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-154.0)
S3 = visual.Slider(win=win, name='S3',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-155, readOnly=False)
VEP1I11 = visual.ImageStim(
    win=win,
    name='VEP1I11', 
    image='VEP3 protocol images/11.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-156.0)
S11 = visual.Slider(win=win, name='S11',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-157, readOnly=False)
VEP1I21 = visual.ImageStim(
    win=win,
    name='VEP1I21', 
    image='VEP3 protocol images/21.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-158.0)
S21 = visual.Slider(win=win, name='S21',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-159, readOnly=False)
VEP1I25 = visual.ImageStim(
    win=win,
    name='VEP1I25', 
    image='VEP3 protocol images/25.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-160.0)
s25 = visual.Slider(win=win, name='s25',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-161, readOnly=False)
VEP1I20 = visual.ImageStim(
    win=win,
    name='VEP1I20', 
    image='VEP3 protocol images/20.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-162.0)
S20 = visual.Slider(win=win, name='S20',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-163, readOnly=False)
VEP1I13 = visual.ImageStim(
    win=win,
    name='VEP1I13', 
    image='VEP3 protocol images/13.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-164.0)
S13 = visual.Slider(win=win, name='S13',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-165, readOnly=False)
VEP1I19 = visual.ImageStim(
    win=win,
    name='VEP1I19', 
    image='VEP3 protocol images/19.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-166.0)
S19 = visual.Slider(win=win, name='S19',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-167, readOnly=False)
VEP1I1 = visual.ImageStim(
    win=win,
    name='VEP1I1', 
    image='VEP3 protocol images/1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-168.0)
S1 = visual.Slider(win=win, name='S1',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-169, readOnly=False)
VEP1I7 = visual.ImageStim(
    win=win,
    name='VEP1I7', 
    image='VEP3 protocol images/7.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-170.0)
S7 = visual.Slider(win=win, name='S7',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-171, readOnly=False)
VEP1I4 = visual.ImageStim(
    win=win,
    name='VEP1I4', 
    image='VEP3 protocol images/4.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-172.0)
S4 = visual.Slider(win=win, name='S4',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-173, readOnly=False)
VEP1I6 = visual.ImageStim(
    win=win,
    name='VEP1I6', 
    image='VEP3 protocol images/6.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-174.0)
S6 = visual.Slider(win=win, name='S6',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-175, readOnly=False)
VEP1I22 = visual.ImageStim(
    win=win,
    name='VEP1I22', 
    image='VEP3 protocol images/22.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-176.0)
S22 = visual.Slider(win=win, name='S22',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-177, readOnly=False)
VEP1I2 = visual.ImageStim(
    win=win,
    name='VEP1I2', 
    image='VEP3 protocol images/2.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-178.0)
S2 = visual.Slider(win=win, name='S2',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-179, readOnly=False)
VEP1I10 = visual.ImageStim(
    win=win,
    name='VEP1I10', 
    image='VEP3 protocol images/10.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-180.0)
S10 = visual.Slider(win=win, name='S10',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-181, readOnly=False)
VEP1I15 = visual.ImageStim(
    win=win,
    name='VEP1I15', 
    image='VEP3 protocol images/15.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-182.0)
S15 = visual.Slider(win=win, name='S15',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-183, readOnly=False)
VEP1I14 = visual.ImageStim(
    win=win,
    name='VEP1I14', 
    image='VEP3 protocol images/14.jfif', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-184.0)
S14 = visual.Slider(win=win, name='S14',
    startValue=None, size=(1.0, 0.1), pos=(0,0), units=None,
    labels=('Celebrity', 'Food','Animal','Random People'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-185, readOnly=False)
text_44 = visual.TextStim(win=win, name='text_44',
    text='You can Relax for 10 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-186.0);
VEP2C1 = visual.ImageStim(
    win=win,
    name='VEP2C1', 
    image='flowers/daisy/image_0801.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-187.0)
text_45 = visual.TextStim(win=win, name='text_45',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-188.0);
d1 = visual.ImageStim(
    win=win,
    name='d1', 
    image='flowers/daisy/image_0802.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-189.0)
d2 = visual.ImageStim(
    win=win,
    name='d2', 
    image='flowers/daisy/image_0806.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-190.0)
s1 = visual.ImageStim(
    win=win,
    name='s1', 
    image='flowers/sunflower/image_0721.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-191.0)
b1 = visual.ImageStim(
    win=win,
    name='b1', 
    image='flowers/bluebell/image_0242.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-192.0)
d4 = visual.ImageStim(
    win=win,
    name='d4', 
    image='flowers/daisy/image_0814.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-193.0)
s2 = visual.ImageStim(
    win=win,
    name='s2', 
    image='flowers/sunflower/image_0726.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-194.0)
VS1 = visual.Slider(win=win, name='VS1',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-195, readOnly=False)
VEP2C2 = visual.ImageStim(
    win=win,
    name='VEP2C2', 
    image='flowers/sunflower/image_0730.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-196.0)
text_46 = visual.TextStim(win=win, name='text_46',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-197.0);
b2 = visual.ImageStim(
    win=win,
    name='b2', 
    image='flowers/sunflower/image_0741.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-198.0)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='flowers/sunflower/image_0739.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-199.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='flowers/daisy/image_0810.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-200.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='flowers/bluebell/image_0257.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-201.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='flowers/sunflower/image_0736.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-202.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='flowers/sunflower/image_0742.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-203.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='flowers/bluebell/image_0251.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-204.0)
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='flowers/daisy/image_0817.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-205.0)
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-206, readOnly=False)
VEP2C3 = visual.ImageStim(
    win=win,
    name='VEP2C3', 
    image='flowers/daisy/image_0817.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-207.0)
text_47 = visual.TextStim(win=win, name='text_47',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-208.0);
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='flowers/bluebell/image_0252.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-209.0)
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='flowers/daisy/image_0808.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-210.0)
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='flowers/sunflower/image_0721.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-211.0)
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='flowers/daisy/image_0818.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-212.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='flowers/daisy/image_0810.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-213.0)
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='flowers/bluebell/image_0248.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-214.0)
image_14 = visual.ImageStim(
    win=win,
    name='image_14', 
    image='flowers/bluebell/image_0251.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-215.0)
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='flowers/daisy/image_0805.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-216.0)
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-217, readOnly=False)
VEP2C4 = visual.ImageStim(
    win=win,
    name='VEP2C4', 
    image='flowers/bluebell/image_0262.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-218.0)
text_48 = visual.TextStim(win=win, name='text_48',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-219.0);
image_16 = visual.ImageStim(
    win=win,
    name='image_16', 
    image='flowers/sunflower/image_0728.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-220.0)
image_17 = visual.ImageStim(
    win=win,
    name='image_17', 
    image='flowers/bluebell/image_0247.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-221.0)
image_18 = visual.ImageStim(
    win=win,
    name='image_18', 
    image='flowers/bluebell/image_0242.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-222.0)
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='flowers/bluebell/image_0249.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-223.0)
image_20 = visual.ImageStim(
    win=win,
    name='image_20', 
    image='flowers/daisy/image_0812.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-224.0)
image_21 = visual.ImageStim(
    win=win,
    name='image_21', 
    image='flowers/bluebell/image_0250.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-225.0)
image_22 = visual.ImageStim(
    win=win,
    name='image_22', 
    image='flowers/bluebell/image_0257.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-226.0)
image_23 = visual.ImageStim(
    win=win,
    name='image_23', 
    image='flowers/bluebell/image_0261.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-227.0)
image_24 = visual.ImageStim(
    win=win,
    name='image_24', 
    image='flowers/daisy/image_0817.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-228.0)
slider_3 = visual.Slider(win=win, name='slider_3',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-229, readOnly=False)
C5 = visual.ImageStim(
    win=win,
    name='C5', 
    image='flowers/sunflower/image_0737.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-230.0)
text_49 = visual.TextStim(win=win, name='text_49',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-231.0);
image_26 = visual.ImageStim(
    win=win,
    name='image_26', 
    image='flowers/sunflower/image_0727.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-232.0)
image_27 = visual.ImageStim(
    win=win,
    name='image_27', 
    image='flowers/sunflower/image_0736.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-233.0)
image_28 = visual.ImageStim(
    win=win,
    name='image_28', 
    image='flowers/bluebell/image_0252.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-234.0)
image_29 = visual.ImageStim(
    win=win,
    name='image_29', 
    image='flowers/bluebell/image_0268.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-235.0)
image_30 = visual.ImageStim(
    win=win,
    name='image_30', 
    image='flowers/sunflower/image_0730.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-236.0)
image_31 = visual.ImageStim(
    win=win,
    name='image_31', 
    image='flowers/daisy/image_0809.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-237.0)
image_32 = visual.ImageStim(
    win=win,
    name='image_32', 
    image='flowers/daisy/image_0817.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-238.0)
image_33 = visual.ImageStim(
    win=win,
    name='image_33', 
    image='flowers/daisy/image_0802.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-239.0)
image_34 = visual.ImageStim(
    win=win,
    name='image_34', 
    image='flowers/sunflower/image_0737.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-240.0)
slider_4 = visual.Slider(win=win, name='slider_4',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-241, readOnly=False)
C6 = visual.ImageStim(
    win=win,
    name='C6', 
    image='flowers/bluebell/image_0312.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-242.0)
text_50 = visual.TextStim(win=win, name='text_50',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-243.0);
image_36 = visual.ImageStim(
    win=win,
    name='image_36', 
    image='flowers/daisy/image_0811.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-244.0)
image_37 = visual.ImageStim(
    win=win,
    name='image_37', 
    image='flowers/daisy/image_0818.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-245.0)
image_25 = visual.ImageStim(
    win=win,
    name='image_25', 
    image='flowers/bluebell/image_0249.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-246.0)
image_35 = visual.ImageStim(
    win=win,
    name='image_35', 
    image='flowers/sunflower/image_0731.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-247.0)
image_38 = visual.ImageStim(
    win=win,
    name='image_38', 
    image='flowers/bluebell/image_0252.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-248.0)
image_39 = visual.ImageStim(
    win=win,
    name='image_39', 
    image='flowers/daisy/image_0811.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-249.0)
image_40 = visual.ImageStim(
    win=win,
    name='image_40', 
    image='flowers/sunflower/image_0742.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-250.0)
slider_5 = visual.Slider(win=win, name='slider_5',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-251, readOnly=False)
C7 = visual.ImageStim(
    win=win,
    name='C7', 
    image='flowers/daisy/image_0818.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-252.0)
text_51 = visual.TextStim(win=win, name='text_51',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-253.0);
image_41 = visual.ImageStim(
    win=win,
    name='image_41', 
    image='flowers/sunflower/image_0726.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-254.0)
image_42 = visual.ImageStim(
    win=win,
    name='image_42', 
    image='flowers/bluebell/image_0247.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-255.0)
image_43 = visual.ImageStim(
    win=win,
    name='image_43', 
    image='flowers/sunflower/image_0728.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-256.0)
image_44 = visual.ImageStim(
    win=win,
    name='image_44', 
    image='flowers/sunflower/image_0721.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-257.0)
image_45 = visual.ImageStim(
    win=win,
    name='image_45', 
    image='flowers/daisy/image_0813.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-258.0)
image_46 = visual.ImageStim(
    win=win,
    name='image_46', 
    image='flowers/bluebell/image_0257.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-259.0)
image_47 = visual.ImageStim(
    win=win,
    name='image_47', 
    image='flowers/sunflower/image_0736.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-260.0)
image_48 = visual.ImageStim(
    win=win,
    name='image_48', 
    image='flowers/bluebell/image_0251.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-261.0)
image_49 = visual.ImageStim(
    win=win,
    name='image_49', 
    image='flowers/sunflower/image_0728.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-262.0)
slider_6 = visual.Slider(win=win, name='slider_6',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-263, readOnly=False)
C8 = visual.ImageStim(
    win=win,
    name='C8', 
    image='flowers/sunflower/image_0747.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-264.0)
text_52 = visual.TextStim(win=win, name='text_52',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-265.0);
image_50 = visual.ImageStim(
    win=win,
    name='image_50', 
    image='flowers/daisy/image_0817.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-266.0)
image_51 = visual.ImageStim(
    win=win,
    name='image_51', 
    image='flowers/bluebell/image_0247.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-267.0)
image_52 = visual.ImageStim(
    win=win,
    name='image_52', 
    image='flowers/bluebell/image_0257.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-268.0)
image_53 = visual.ImageStim(
    win=win,
    name='image_53', 
    image='flowers/sunflower/image_0746.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-269.0)
image_54 = visual.ImageStim(
    win=win,
    name='image_54', 
    image='flowers/daisy/image_0818.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-270.0)
image_55 = visual.ImageStim(
    win=win,
    name='image_55', 
    image='flowers/sunflower/image_0738.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-271.0)
image_56 = visual.ImageStim(
    win=win,
    name='image_56', 
    image='flowers/sunflower/image_0747.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-272.0)
slider_7 = visual.Slider(win=win, name='slider_7',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-273, readOnly=False)
C9 = visual.ImageStim(
    win=win,
    name='C9', 
    image='flowers/sunflower/image_0737.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-274.0)
text_53 = visual.TextStim(win=win, name='text_53',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-275.0);
image_57 = visual.ImageStim(
    win=win,
    name='image_57', 
    image='flowers/sunflower/image_0737.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-276.0)
image_58 = visual.ImageStim(
    win=win,
    name='image_58', 
    image='flowers/sunflower/image_0721.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-277.0)
image_59 = visual.ImageStim(
    win=win,
    name='image_59', 
    image='flowers/sunflower/image_0729.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-278.0)
image_60 = visual.ImageStim(
    win=win,
    name='image_60', 
    image='flowers/sunflower/image_0738.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-279.0)
image_61 = visual.ImageStim(
    win=win,
    name='image_61', 
    image='flowers/sunflower/image_0750.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-280.0)
image_62 = visual.ImageStim(
    win=win,
    name='image_62', 
    image='flowers/bluebell/image_0253.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-281.0)
image_63 = visual.ImageStim(
    win=win,
    name='image_63', 
    image='flowers/sunflower/image_0738.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-282.0)
image_64 = visual.ImageStim(
    win=win,
    name='image_64', 
    image='flowers/daisy/image_0812.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-283.0)
image_65 = visual.ImageStim(
    win=win,
    name='image_65', 
    image='flowers/daisy/image_0801.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-284.0)
image_66 = visual.ImageStim(
    win=win,
    name='image_66', 
    image='flowers/sunflower/image_0731.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-285.0)
image_67 = visual.ImageStim(
    win=win,
    name='image_67', 
    image='flowers/sunflower/image_0767.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-286.0)
slider_8 = visual.Slider(win=win, name='slider_8',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-287, readOnly=False)
C10 = visual.ImageStim(
    win=win,
    name='C10', 
    image='flowers/bluebell/image_0242.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-288.0)
text_54 = visual.TextStim(win=win, name='text_54',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-289.0);
image_68 = visual.ImageStim(
    win=win,
    name='image_68', 
    image='flowers/bluebell/image_0243.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-290.0)
image_69 = visual.ImageStim(
    win=win,
    name='image_69', 
    image='flowers/sunflower/image_0737.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-291.0)
image_70 = visual.ImageStim(
    win=win,
    name='image_70', 
    image='flowers/daisy/image_0801.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-292.0)
image_71 = visual.ImageStim(
    win=win,
    name='image_71', 
    image='flowers/bluebell/image_0249.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-293.0)
image_72 = visual.ImageStim(
    win=win,
    name='image_72', 
    image='flowers/daisy/image_0818.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-294.0)
image_73 = visual.ImageStim(
    win=win,
    name='image_73', 
    image='flowers/bluebell/image_0253.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-295.0)
slider_9 = visual.Slider(win=win, name='slider_9',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-296, readOnly=False)
C11 = visual.ImageStim(
    win=win,
    name='C11', 
    image='flowers/daisy/image_0811.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-297.0)
text_55 = visual.TextStim(win=win, name='text_55',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-298.0);
image_74 = visual.ImageStim(
    win=win,
    name='image_74', 
    image='flowers/bluebell/image_0250.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-299.0)
image_75 = visual.ImageStim(
    win=win,
    name='image_75', 
    image='flowers/sunflower/image_0721.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-300.0)
image_76 = visual.ImageStim(
    win=win,
    name='image_76', 
    image='flowers/sunflower/image_0739.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-301.0)
image_77 = visual.ImageStim(
    win=win,
    name='image_77', 
    image='flowers/sunflower/image_0727.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-302.0)
image_78 = visual.ImageStim(
    win=win,
    name='image_78', 
    image='flowers/daisy/image_0804.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-303.0)
image_79 = visual.ImageStim(
    win=win,
    name='image_79', 
    image='flowers/daisy/image_0811.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-304.0)
slider_10 = visual.Slider(win=win, name='slider_10',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-305, readOnly=False)
C12 = visual.ImageStim(
    win=win,
    name='C12', 
    image='flowers/sunflower/image_0730.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-306.0)
text_56 = visual.TextStim(win=win, name='text_56',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-307.0);
image_80 = visual.ImageStim(
    win=win,
    name='image_80', 
    image='flowers/sunflower/image_0722.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-308.0)
image_81 = visual.ImageStim(
    win=win,
    name='image_81', 
    image='flowers/bluebell/image_0300.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-309.0)
image_82 = visual.ImageStim(
    win=win,
    name='image_82', 
    image='flowers/daisy/image_0813.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-310.0)
image_83 = visual.ImageStim(
    win=win,
    name='image_83', 
    image='flowers/bluebell/image_0247.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-311.0)
image_84 = visual.ImageStim(
    win=win,
    name='image_84', 
    image='flowers/sunflower/image_0748.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-312.0)
image_85 = visual.ImageStim(
    win=win,
    name='image_85', 
    image='flowers/daisy/image_0801.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-313.0)
slider_11 = visual.Slider(win=win, name='slider_11',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-314, readOnly=False)
C13 = visual.ImageStim(
    win=win,
    name='C13', 
    image='flowers/daisy/image_0818.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-315.0)
text_57 = visual.TextStim(win=win, name='text_57',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-316.0);
image_86 = visual.ImageStim(
    win=win,
    name='image_86', 
    image='flowers/daisy/image_0812.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-317.0)
image_87 = visual.ImageStim(
    win=win,
    name='image_87', 
    image='flowers/sunflower/image_0722.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-318.0)
image_88 = visual.ImageStim(
    win=win,
    name='image_88', 
    image='flowers/daisy/image_0801.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-319.0)
image_89 = visual.ImageStim(
    win=win,
    name='image_89', 
    image='flowers/daisy/image_0815.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-320.0)
image_90 = visual.ImageStim(
    win=win,
    name='image_90', 
    image='flowers/daisy/image_0829.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-321.0)
image_91 = visual.ImageStim(
    win=win,
    name='image_91', 
    image='flowers/sunflower/image_0721.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-322.0)
image_92 = visual.ImageStim(
    win=win,
    name='image_92', 
    image='flowers/bluebell/image_0273.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-323.0)
slider_12 = visual.Slider(win=win, name='slider_12',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-324, readOnly=False)
C14 = visual.ImageStim(
    win=win,
    name='C14', 
    image='flowers/bluebell/image_0263.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-325.0)
text_58 = visual.TextStim(win=win, name='text_58',
    text='Cue Image is',
    font='Open Sans',
    pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-326.0);
image_93 = visual.ImageStim(
    win=win,
    name='image_93', 
    image='flowers/bluebell/image_0241.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-327.0)
image_94 = visual.ImageStim(
    win=win,
    name='image_94', 
    image='flowers/bluebell/image_0257.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-328.0)
image_95 = visual.ImageStim(
    win=win,
    name='image_95', 
    image='flowers/bluebell/image_0260.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-329.0)
image_96 = visual.ImageStim(
    win=win,
    name='image_96', 
    image='flowers/daisy/image_0811.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-330.0)
image_97 = visual.ImageStim(
    win=win,
    name='image_97', 
    image='flowers/bluebell/image_0268.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-331.0)
image_98 = visual.ImageStim(
    win=win,
    name='image_98', 
    image='flowers/daisy/image_0818.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-332.0)
image_99 = visual.ImageStim(
    win=win,
    name='image_99', 
    image='flowers/sunflower/image_0740.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-333.0)
image_100 = visual.ImageStim(
    win=win,
    name='image_100', 
    image='flowers/bluebell/image_0246.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-334.0)
image_101 = visual.ImageStim(
    win=win,
    name='image_101', 
    image='flowers/sunflower/image_0752.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-335.0)
slider_13 = visual.Slider(win=win, name='slider_13',
    startValue=None, size=(1.0, 0.1), pos=(0, 0), units=None,
    labels=('1-2', '3-4', '5-6', '7-8'), ticks=(1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-336, readOnly=False)
text_59 = visual.TextStim(win=win, name='text_59',
    text='You can Relax for 10 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-337.0);

# Initialize components for Routine "Checker_circle"
Checker_circleClock = core.Clock()

# Initialize components for Routine "rest"
restClock = core.Clock()
text_60 = visual.TextStim(win=win, name='text_60',
    text='You can Relax for 10 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "flashing_Wedge"
flashing_WedgeClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(772.200000)
# update component parameters for each repeat
sound_1.setSound('A', secs=.5, hamming=True)
sound_1.setVolume(1.0, log=False)
sound_2.setSound('A', secs=.500, hamming=True)
sound_2.setVolume(1.0, log=False)
sound_3.setSound('A', secs=.500, hamming=True)
sound_3.setVolume(1.0, log=False)
S9.reset()
S18.reset()
S31.reset()
S24.reset()
S30.reset()
S12.reset()
S27.reset()
S28.reset()
S16.reset()
S29.reset()
S32.reset()
S5.reset()
S23.reset()
S26.reset()
S8.reset()
S17.reset()
S3.reset()
S11.reset()
S21.reset()
s25.reset()
S20.reset()
S13.reset()
S19.reset()
S1.reset()
S7.reset()
S4.reset()
S6.reset()
S22.reset()
S2.reset()
S10.reset()
S15.reset()
S14.reset()
VS1.reset()
slider.reset()
slider_2.reset()
slider_3.reset()
slider_4.reset()
slider_5.reset()
slider_6.reset()
slider_7.reset()
slider_8.reset()
slider_9.reset()
slider_10.reset()
slider_11.reset()
slider_12.reset()
slider_13.reset()
# keep track of which components have finished
trialComponents = [sound_1, Cross, LC1, LC2, Rc1, lc3, rc2, rc3, lc4, lc5, lc6, rc4, rc5, lc7, rc6, rc7, lc8, MI1LC1, text, MILC2, MIRC1, MILC3, MIRC2, MIRC3, MILC4, MILC5, MILC6, MIRC4, MIRC5, MILC7, MIRC6, MIRC7, MILC8, text_2, MMLI1, MMLI2, MMRI1, MMLI3, MMRI2, MMRI3, MMLI4, MMLI5, MMLI6, MMRi4, MMRI5, MMLI7, MMRI6, MMRI7, MMLI8, text_3, MILI1, MILI2, MIRI1, MILI3, MIRi2, MIRI3, MILI4, MILI5, MILI6, MIRI4, MIRI5, MILI7, MIri6, miri7, mili8, text_4, text_5, text_6, text_7, text_8, text_9, text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19, text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29, text_30, text_31, text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, text_40, text_41, text_42, MIRM1, MILM1, MIRM2, MILM2, MILM3, MIRM3, MILM4, MIRM4, MILM5, MIRM5, MIRM6, MILM6, MIRM7, MILM7, MILM8, text_43, sound_2, sound_3, VEP1I9, S9, vep1I18, S18, VEP1I31, S31, VEP1I24, S24, VEP1I30, S30, VEp1I12, S12, VEP1I27, S27, VEP1I28, S28, VEP1I16, S16, VEP1I29, S29, VEP1I32, S32, VEP1I5, S5, VEP1I23, S23, VEP1I26, S26, vep1I8, S8, VEp1I17, S17, VEP1I3, S3, VEP1I11, S11, VEP1I21, S21, VEP1I25, s25, VEP1I20, S20, VEP1I13, S13, VEP1I19, S19, VEP1I1, S1, VEP1I7, S7, VEP1I4, S4, VEP1I6, S6, VEP1I22, S22, VEP1I2, S2, VEP1I10, S10, VEP1I15, S15, VEP1I14, S14, text_44, VEP2C1, text_45, d1, d2, s1, b1, d4, s2, VS1, VEP2C2, text_46, b2, image, image_2, image_3, image_4, image_5, image_6, image_7, slider, VEP2C3, text_47, image_8, image_9, image_10, image_11, image_12, image_13, image_14, image_15, slider_2, VEP2C4, text_48, image_16, image_17, image_18, image_19, image_20, image_21, image_22, image_23, image_24, slider_3, C5, text_49, image_26, image_27, image_28, image_29, image_30, image_31, image_32, image_33, image_34, slider_4, C6, text_50, image_36, image_37, image_25, image_35, image_38, image_39, image_40, slider_5, C7, text_51, image_41, image_42, image_43, image_44, image_45, image_46, image_47, image_48, image_49, slider_6, C8, text_52, image_50, image_51, image_52, image_53, image_54, image_55, image_56, slider_7, C9, text_53, image_57, image_58, image_59, image_60, image_61, image_62, image_63, image_64, image_65, image_66, image_67, slider_8, C10, text_54, image_68, image_69, image_70, image_71, image_72, image_73, slider_9, C11, text_55, image_74, image_75, image_76, image_77, image_78, image_79, slider_10, C12, text_56, image_80, image_81, image_82, image_83, image_84, image_85, slider_11, C13, text_57, image_86, image_87, image_88, image_89, image_90, image_91, image_92, slider_12, C14, text_58, image_93, image_94, image_95, image_96, image_97, image_98, image_99, image_100, image_101, slider_13, text_59]
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
    
    # *LC1* updates
    if LC1.status == NOT_STARTED and tThisFlip >= 62.2-frameTolerance:
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
    if LC2.status == NOT_STARTED and tThisFlip >= 66.1-frameTolerance:
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
    if Rc1.status == NOT_STARTED and tThisFlip >= 70-frameTolerance:
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
    if lc3.status == NOT_STARTED and tThisFlip >= 73.9-frameTolerance:
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
    if rc2.status == NOT_STARTED and tThisFlip >= 77.8-frameTolerance:
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
    if rc3.status == NOT_STARTED and tThisFlip >= 81.7-frameTolerance:
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
    if lc4.status == NOT_STARTED and tThisFlip >= 85.6-frameTolerance:
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
    if lc5.status == NOT_STARTED and tThisFlip >= 89.5-frameTolerance:
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
    if lc6.status == NOT_STARTED and tThisFlip >= 93.4-frameTolerance:
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
    if rc4.status == NOT_STARTED and tThisFlip >= 97.3-frameTolerance:
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
    if rc5.status == NOT_STARTED and tThisFlip >= 101.2-frameTolerance:
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
    if lc7.status == NOT_STARTED and tThisFlip >= 105.1-frameTolerance:
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
    if rc6.status == NOT_STARTED and tThisFlip >= 109-frameTolerance:
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
    if rc7.status == NOT_STARTED and tThisFlip >= 112.9-frameTolerance:
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
    if lc8.status == NOT_STARTED and tThisFlip >= 116.8-frameTolerance:
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
    if MI1LC1.status == NOT_STARTED and tThisFlip >= 125.7-frameTolerance:
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
    if text.status == NOT_STARTED and tThisFlip >= 120.7-frameTolerance:
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
    if MILC2.status == NOT_STARTED and tThisFlip >= 129.6-frameTolerance:
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
    if MIRC1.status == NOT_STARTED and tThisFlip >= 133.5-frameTolerance:
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
    if MILC3.status == NOT_STARTED and tThisFlip >= 137.4-frameTolerance:
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
    if MIRC2.status == NOT_STARTED and tThisFlip >= 141.3-frameTolerance:
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
    if MIRC3.status == NOT_STARTED and tThisFlip >= 145.2-frameTolerance:
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
    if MILC4.status == NOT_STARTED and tThisFlip >= 149.1-frameTolerance:
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
    if MILC5.status == NOT_STARTED and tThisFlip >= 153-frameTolerance:
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
    if MILC6.status == NOT_STARTED and tThisFlip >= 156.9-frameTolerance:
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
    if MIRC4.status == NOT_STARTED and tThisFlip >= 160.8-frameTolerance:
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
    if MIRC5.status == NOT_STARTED and tThisFlip >= 164.5-frameTolerance:
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
    if MILC7.status == NOT_STARTED and tThisFlip >= 168.4-frameTolerance:
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
    if MIRC6.status == NOT_STARTED and tThisFlip >= 172.3-frameTolerance:
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
    if MIRC7.status == NOT_STARTED and tThisFlip >= 176.2-frameTolerance:
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
    if MILC8.status == NOT_STARTED and tThisFlip >= 180.1-frameTolerance:
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
    if text_2.status == NOT_STARTED and tThisFlip >= 184-frameTolerance:
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
    if MMLI1.status == NOT_STARTED and tThisFlip >= 189-frameTolerance:
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
    if MMLI2.status == NOT_STARTED and tThisFlip >= 192.9-frameTolerance:
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
    if MMRI1.status == NOT_STARTED and tThisFlip >= 196.8-frameTolerance:
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
    if MMLI3.status == NOT_STARTED and tThisFlip >= 200.7-frameTolerance:
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
    if MMRI2.status == NOT_STARTED and tThisFlip >= 204.6-frameTolerance:
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
    if MMRI3.status == NOT_STARTED and tThisFlip >= 208.5-frameTolerance:
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
    if MMLI4.status == NOT_STARTED and tThisFlip >= 212.4-frameTolerance:
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
    if MMLI5.status == NOT_STARTED and tThisFlip >= 216.3-frameTolerance:
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
    if MMLI6.status == NOT_STARTED and tThisFlip >= 220.2-frameTolerance:
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
    if MMRi4.status == NOT_STARTED and tThisFlip >= 224.1-frameTolerance:
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
    if MMRI5.status == NOT_STARTED and tThisFlip >= 228-frameTolerance:
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
    if MMLI7.status == NOT_STARTED and tThisFlip >= 231.9-frameTolerance:
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
    if MMRI6.status == NOT_STARTED and tThisFlip >= 235.8-frameTolerance:
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
    if MMRI7.status == NOT_STARTED and tThisFlip >= 239.7-frameTolerance:
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
    if MMLI8.status == NOT_STARTED and tThisFlip >= 243.6-frameTolerance:
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
    if text_3.status == NOT_STARTED and tThisFlip >= 247.5-frameTolerance:
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
    if MILI1.status == NOT_STARTED and tThisFlip >= 252.6-frameTolerance:
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
    if MILI2.status == NOT_STARTED and tThisFlip >= 258.4-frameTolerance:
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
    if MIRI1.status == NOT_STARTED and tThisFlip >= 262.3-frameTolerance:
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
    if MILI3.status == NOT_STARTED and tThisFlip >= 266.2-frameTolerance:
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
    if MIRi2.status == NOT_STARTED and tThisFlip >= 270.1-frameTolerance:
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
    if MIRI3.status == NOT_STARTED and tThisFlip >= 274-frameTolerance:
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
    if MILI4.status == NOT_STARTED and tThisFlip >= 277.9-frameTolerance:
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
    if MILI5.status == NOT_STARTED and tThisFlip >= 281.8-frameTolerance:
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
    if MILI6.status == NOT_STARTED and tThisFlip >= 285.7-frameTolerance:
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
    if MIRI4.status == NOT_STARTED and tThisFlip >= 289.6-frameTolerance:
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
    if MIRI5.status == NOT_STARTED and tThisFlip >= 293.5-frameTolerance:
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
    if MILI7.status == NOT_STARTED and tThisFlip >= 297.4-frameTolerance:
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
    if MIri6.status == NOT_STARTED and tThisFlip >= 301.3-frameTolerance:
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
    if miri7.status == NOT_STARTED and tThisFlip >= 305.2-frameTolerance:
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
    if mili8.status == NOT_STARTED and tThisFlip >= 309.1-frameTolerance:
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
    if text_4.status == NOT_STARTED and tThisFlip >= 313-frameTolerance:
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
    if text_5.status == NOT_STARTED and tThisFlip >= 318-frameTolerance:
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
    if text_6.status == NOT_STARTED and tThisFlip >= 321.4-frameTolerance:
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
    if text_7.status == NOT_STARTED and tThisFlip >= 324.8-frameTolerance:
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
    if text_8.status == NOT_STARTED and tThisFlip >= 328.2-frameTolerance:
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
    if text_9.status == NOT_STARTED and tThisFlip >= 331.6-frameTolerance:
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
    if text_10.status == NOT_STARTED and tThisFlip >= 335-frameTolerance:
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
    if text_11.status == NOT_STARTED and tThisFlip >= 338.4-frameTolerance:
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
    if text_12.status == NOT_STARTED and tThisFlip >= 341.8-frameTolerance:
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
    if text_13.status == NOT_STARTED and tThisFlip >= 345.2-frameTolerance:
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
    if text_14.status == NOT_STARTED and tThisFlip >= 348.6-frameTolerance:
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
    if text_15.status == NOT_STARTED and tThisFlip >= 352-frameTolerance:
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
    if text_16.status == NOT_STARTED and tThisFlip >= 355.4-frameTolerance:
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
    if text_17.status == NOT_STARTED and tThisFlip >= 358.8-frameTolerance:
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
    if text_18.status == NOT_STARTED and tThisFlip >= 362.2-frameTolerance:
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
    if text_19.status == NOT_STARTED and tThisFlip >= 365.6-frameTolerance:
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
    if text_20.status == NOT_STARTED and tThisFlip >= 369-frameTolerance:
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
    if text_21.status == NOT_STARTED and tThisFlip >= 372.4-frameTolerance:
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
    if text_22.status == NOT_STARTED and tThisFlip >= 375.8-frameTolerance:
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
    if text_23.status == NOT_STARTED and tThisFlip >= 379.2-frameTolerance:
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
    if text_24.status == NOT_STARTED and tThisFlip >= 384.3-frameTolerance:
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
    if text_25.status == NOT_STARTED and tThisFlip >= 387.7-frameTolerance:
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
    if text_26.status == NOT_STARTED and tThisFlip >= 391.1-frameTolerance:
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
    if text_27.status == NOT_STARTED and tThisFlip >= 394.5-frameTolerance:
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
    if text_28.status == NOT_STARTED and tThisFlip >= 397.9-frameTolerance:
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
    if text_29.status == NOT_STARTED and tThisFlip >= 401.3-frameTolerance:
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
    if text_30.status == NOT_STARTED and tThisFlip >= 404.7-frameTolerance:
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
    if text_31.status == NOT_STARTED and tThisFlip >= 408.1-frameTolerance:
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
    if text_32.status == NOT_STARTED and tThisFlip >= 411.5-frameTolerance:
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
    if text_33.status == NOT_STARTED and tThisFlip >= 414.9-frameTolerance:
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
    if text_34.status == NOT_STARTED and tThisFlip >= 418.3-frameTolerance:
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
    if text_35.status == NOT_STARTED and tThisFlip >= 421.7-frameTolerance:
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
    if text_36.status == NOT_STARTED and tThisFlip >= 425.1-frameTolerance:
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
    if text_37.status == NOT_STARTED and tThisFlip >= 428.5-frameTolerance:
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
    if text_38.status == NOT_STARTED and tThisFlip >= 431.9-frameTolerance:
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
    if text_39.status == NOT_STARTED and tThisFlip >= 435.3-frameTolerance:
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
    if text_40.status == NOT_STARTED and tThisFlip >= 438.7-frameTolerance:
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
    if text_41.status == NOT_STARTED and tThisFlip >= 442.1-frameTolerance:
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
    if text_42.status == NOT_STARTED and tThisFlip >= 445.5-frameTolerance:
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
    if MIRM1.status == NOT_STARTED and tThisFlip >= 450.1-frameTolerance:
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
    if MILM1.status == NOT_STARTED and tThisFlip >= 454-frameTolerance:
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
    if MIRM2.status == NOT_STARTED and tThisFlip >= 457.9-frameTolerance:
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
    if MILM2.status == NOT_STARTED and tThisFlip >= 461.8-frameTolerance:
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
    if MILM3.status == NOT_STARTED and tThisFlip >= 465.7-frameTolerance:
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
    if MIRM3.status == NOT_STARTED and tThisFlip >= 469.6-frameTolerance:
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
    if MILM4.status == NOT_STARTED and tThisFlip >= 473.5-frameTolerance:
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
    if MIRM4.status == NOT_STARTED and tThisFlip >= 477.4-frameTolerance:
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
    if MILM5.status == NOT_STARTED and tThisFlip >= 481.3-frameTolerance:
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
    if MIRM5.status == NOT_STARTED and tThisFlip >= 485.2-frameTolerance:
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
    if MIRM6.status == NOT_STARTED and tThisFlip >= 489.1-frameTolerance:
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
    if MILM6.status == NOT_STARTED and tThisFlip >= 493-frameTolerance:
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
    if MIRM7.status == NOT_STARTED and tThisFlip >= 496.9-frameTolerance:
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
    if MILM7.status == NOT_STARTED and tThisFlip >= 500.8-frameTolerance:
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
    if MILM8.status == NOT_STARTED and tThisFlip >= 504.7-frameTolerance:
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
    
    # *text_43* updates
    if text_43.status == NOT_STARTED and tThisFlip >= 508.6-frameTolerance:
        # keep track of start time/frame for later
        text_43.frameNStart = frameN  # exact frame index
        text_43.tStart = t  # local t and not account for scr refresh
        text_43.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_43, 'tStartRefresh')  # time at next scr refresh
        text_43.setAutoDraw(True)
    if text_43.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_43.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_43.tStop = t  # not accounting for scr refresh
            text_43.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_43, 'tStopRefresh')  # time at next scr refresh
            text_43.setAutoDraw(False)
    # start/stop sound_2
    if sound_2.status == NOT_STARTED and tThisFlip >= 512-frameTolerance:
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
    if sound_3.status == NOT_STARTED and tThisFlip >= 572-frameTolerance:
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
    
    # *VEP1I9* updates
    if VEP1I9.status == NOT_STARTED and tThisFlip >= 574-frameTolerance:
        # keep track of start time/frame for later
        VEP1I9.frameNStart = frameN  # exact frame index
        VEP1I9.tStart = t  # local t and not account for scr refresh
        VEP1I9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I9, 'tStartRefresh')  # time at next scr refresh
        VEP1I9.setAutoDraw(True)
    if VEP1I9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I9.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I9.tStop = t  # not accounting for scr refresh
            VEP1I9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I9, 'tStopRefresh')  # time at next scr refresh
            VEP1I9.setAutoDraw(False)
    
    # *S9* updates
    if S9.status == NOT_STARTED and tThisFlip >= 574.9-frameTolerance:
        # keep track of start time/frame for later
        S9.frameNStart = frameN  # exact frame index
        S9.tStart = t  # local t and not account for scr refresh
        S9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S9, 'tStartRefresh')  # time at next scr refresh
        S9.setAutoDraw(True)
    if S9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S9.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S9.tStop = t  # not accounting for scr refresh
            S9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S9, 'tStopRefresh')  # time at next scr refresh
            S9.setAutoDraw(False)
    
    # *vep1I18* updates
    if vep1I18.status == NOT_STARTED and tThisFlip >= 576.8-frameTolerance:
        # keep track of start time/frame for later
        vep1I18.frameNStart = frameN  # exact frame index
        vep1I18.tStart = t  # local t and not account for scr refresh
        vep1I18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vep1I18, 'tStartRefresh')  # time at next scr refresh
        vep1I18.setAutoDraw(True)
    if vep1I18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > vep1I18.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            vep1I18.tStop = t  # not accounting for scr refresh
            vep1I18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(vep1I18, 'tStopRefresh')  # time at next scr refresh
            vep1I18.setAutoDraw(False)
    
    # *S18* updates
    if S18.status == NOT_STARTED and tThisFlip >= 577.7-frameTolerance:
        # keep track of start time/frame for later
        S18.frameNStart = frameN  # exact frame index
        S18.tStart = t  # local t and not account for scr refresh
        S18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S18, 'tStartRefresh')  # time at next scr refresh
        S18.setAutoDraw(True)
    if S18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S18.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S18.tStop = t  # not accounting for scr refresh
            S18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S18, 'tStopRefresh')  # time at next scr refresh
            S18.setAutoDraw(False)
    
    # *VEP1I31* updates
    if VEP1I31.status == NOT_STARTED and tThisFlip >= 579.6-frameTolerance:
        # keep track of start time/frame for later
        VEP1I31.frameNStart = frameN  # exact frame index
        VEP1I31.tStart = t  # local t and not account for scr refresh
        VEP1I31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I31, 'tStartRefresh')  # time at next scr refresh
        VEP1I31.setAutoDraw(True)
    if VEP1I31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I31.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I31.tStop = t  # not accounting for scr refresh
            VEP1I31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I31, 'tStopRefresh')  # time at next scr refresh
            VEP1I31.setAutoDraw(False)
    
    # *S31* updates
    if S31.status == NOT_STARTED and tThisFlip >= 580.5-frameTolerance:
        # keep track of start time/frame for later
        S31.frameNStart = frameN  # exact frame index
        S31.tStart = t  # local t and not account for scr refresh
        S31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S31, 'tStartRefresh')  # time at next scr refresh
        S31.setAutoDraw(True)
    if S31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S31.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S31.tStop = t  # not accounting for scr refresh
            S31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S31, 'tStopRefresh')  # time at next scr refresh
            S31.setAutoDraw(False)
    
    # *VEP1I24* updates
    if VEP1I24.status == NOT_STARTED and tThisFlip >= 582.4-frameTolerance:
        # keep track of start time/frame for later
        VEP1I24.frameNStart = frameN  # exact frame index
        VEP1I24.tStart = t  # local t and not account for scr refresh
        VEP1I24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I24, 'tStartRefresh')  # time at next scr refresh
        VEP1I24.setAutoDraw(True)
    if VEP1I24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I24.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I24.tStop = t  # not accounting for scr refresh
            VEP1I24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I24, 'tStopRefresh')  # time at next scr refresh
            VEP1I24.setAutoDraw(False)
    
    # *S24* updates
    if S24.status == NOT_STARTED and tThisFlip >= 583.3-frameTolerance:
        # keep track of start time/frame for later
        S24.frameNStart = frameN  # exact frame index
        S24.tStart = t  # local t and not account for scr refresh
        S24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S24, 'tStartRefresh')  # time at next scr refresh
        S24.setAutoDraw(True)
    if S24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S24.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S24.tStop = t  # not accounting for scr refresh
            S24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S24, 'tStopRefresh')  # time at next scr refresh
            S24.setAutoDraw(False)
    
    # *VEP1I30* updates
    if VEP1I30.status == NOT_STARTED and tThisFlip >= 585.2-frameTolerance:
        # keep track of start time/frame for later
        VEP1I30.frameNStart = frameN  # exact frame index
        VEP1I30.tStart = t  # local t and not account for scr refresh
        VEP1I30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I30, 'tStartRefresh')  # time at next scr refresh
        VEP1I30.setAutoDraw(True)
    if VEP1I30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I30.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I30.tStop = t  # not accounting for scr refresh
            VEP1I30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I30, 'tStopRefresh')  # time at next scr refresh
            VEP1I30.setAutoDraw(False)
    
    # *S30* updates
    if S30.status == NOT_STARTED and tThisFlip >= 586.1-frameTolerance:
        # keep track of start time/frame for later
        S30.frameNStart = frameN  # exact frame index
        S30.tStart = t  # local t and not account for scr refresh
        S30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S30, 'tStartRefresh')  # time at next scr refresh
        S30.setAutoDraw(True)
    if S30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S30.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S30.tStop = t  # not accounting for scr refresh
            S30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S30, 'tStopRefresh')  # time at next scr refresh
            S30.setAutoDraw(False)
    
    # *VEp1I12* updates
    if VEp1I12.status == NOT_STARTED and tThisFlip >= 588-frameTolerance:
        # keep track of start time/frame for later
        VEp1I12.frameNStart = frameN  # exact frame index
        VEp1I12.tStart = t  # local t and not account for scr refresh
        VEp1I12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEp1I12, 'tStartRefresh')  # time at next scr refresh
        VEp1I12.setAutoDraw(True)
    if VEp1I12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEp1I12.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEp1I12.tStop = t  # not accounting for scr refresh
            VEp1I12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEp1I12, 'tStopRefresh')  # time at next scr refresh
            VEp1I12.setAutoDraw(False)
    
    # *S12* updates
    if S12.status == NOT_STARTED and tThisFlip >= 588.9-frameTolerance:
        # keep track of start time/frame for later
        S12.frameNStart = frameN  # exact frame index
        S12.tStart = t  # local t and not account for scr refresh
        S12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S12, 'tStartRefresh')  # time at next scr refresh
        S12.setAutoDraw(True)
    if S12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S12.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S12.tStop = t  # not accounting for scr refresh
            S12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S12, 'tStopRefresh')  # time at next scr refresh
            S12.setAutoDraw(False)
    
    # *VEP1I27* updates
    if VEP1I27.status == NOT_STARTED and tThisFlip >= 590.8-frameTolerance:
        # keep track of start time/frame for later
        VEP1I27.frameNStart = frameN  # exact frame index
        VEP1I27.tStart = t  # local t and not account for scr refresh
        VEP1I27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I27, 'tStartRefresh')  # time at next scr refresh
        VEP1I27.setAutoDraw(True)
    if VEP1I27.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I27.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I27.tStop = t  # not accounting for scr refresh
            VEP1I27.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I27, 'tStopRefresh')  # time at next scr refresh
            VEP1I27.setAutoDraw(False)
    
    # *S27* updates
    if S27.status == NOT_STARTED and tThisFlip >= 591.7-frameTolerance:
        # keep track of start time/frame for later
        S27.frameNStart = frameN  # exact frame index
        S27.tStart = t  # local t and not account for scr refresh
        S27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S27, 'tStartRefresh')  # time at next scr refresh
        S27.setAutoDraw(True)
    if S27.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S27.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S27.tStop = t  # not accounting for scr refresh
            S27.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S27, 'tStopRefresh')  # time at next scr refresh
            S27.setAutoDraw(False)
    
    # *VEP1I28* updates
    if VEP1I28.status == NOT_STARTED and tThisFlip >= 593.6-frameTolerance:
        # keep track of start time/frame for later
        VEP1I28.frameNStart = frameN  # exact frame index
        VEP1I28.tStart = t  # local t and not account for scr refresh
        VEP1I28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I28, 'tStartRefresh')  # time at next scr refresh
        VEP1I28.setAutoDraw(True)
    if VEP1I28.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I28.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I28.tStop = t  # not accounting for scr refresh
            VEP1I28.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I28, 'tStopRefresh')  # time at next scr refresh
            VEP1I28.setAutoDraw(False)
    
    # *S28* updates
    if S28.status == NOT_STARTED and tThisFlip >= 594.5-frameTolerance:
        # keep track of start time/frame for later
        S28.frameNStart = frameN  # exact frame index
        S28.tStart = t  # local t and not account for scr refresh
        S28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S28, 'tStartRefresh')  # time at next scr refresh
        S28.setAutoDraw(True)
    if S28.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S28.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S28.tStop = t  # not accounting for scr refresh
            S28.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S28, 'tStopRefresh')  # time at next scr refresh
            S28.setAutoDraw(False)
    
    # *VEP1I16* updates
    if VEP1I16.status == NOT_STARTED and tThisFlip >= 596.4-frameTolerance:
        # keep track of start time/frame for later
        VEP1I16.frameNStart = frameN  # exact frame index
        VEP1I16.tStart = t  # local t and not account for scr refresh
        VEP1I16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I16, 'tStartRefresh')  # time at next scr refresh
        VEP1I16.setAutoDraw(True)
    if VEP1I16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I16.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I16.tStop = t  # not accounting for scr refresh
            VEP1I16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I16, 'tStopRefresh')  # time at next scr refresh
            VEP1I16.setAutoDraw(False)
    
    # *S16* updates
    if S16.status == NOT_STARTED and tThisFlip >= 597.3-frameTolerance:
        # keep track of start time/frame for later
        S16.frameNStart = frameN  # exact frame index
        S16.tStart = t  # local t and not account for scr refresh
        S16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S16, 'tStartRefresh')  # time at next scr refresh
        S16.setAutoDraw(True)
    if S16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S16.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S16.tStop = t  # not accounting for scr refresh
            S16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S16, 'tStopRefresh')  # time at next scr refresh
            S16.setAutoDraw(False)
    
    # *VEP1I29* updates
    if VEP1I29.status == NOT_STARTED and tThisFlip >= 599.2-frameTolerance:
        # keep track of start time/frame for later
        VEP1I29.frameNStart = frameN  # exact frame index
        VEP1I29.tStart = t  # local t and not account for scr refresh
        VEP1I29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I29, 'tStartRefresh')  # time at next scr refresh
        VEP1I29.setAutoDraw(True)
    if VEP1I29.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I29.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I29.tStop = t  # not accounting for scr refresh
            VEP1I29.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I29, 'tStopRefresh')  # time at next scr refresh
            VEP1I29.setAutoDraw(False)
    
    # *S29* updates
    if S29.status == NOT_STARTED and tThisFlip >= 600.1-frameTolerance:
        # keep track of start time/frame for later
        S29.frameNStart = frameN  # exact frame index
        S29.tStart = t  # local t and not account for scr refresh
        S29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S29, 'tStartRefresh')  # time at next scr refresh
        S29.setAutoDraw(True)
    if S29.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S29.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S29.tStop = t  # not accounting for scr refresh
            S29.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S29, 'tStopRefresh')  # time at next scr refresh
            S29.setAutoDraw(False)
    
    # *VEP1I32* updates
    if VEP1I32.status == NOT_STARTED and tThisFlip >= 602-frameTolerance:
        # keep track of start time/frame for later
        VEP1I32.frameNStart = frameN  # exact frame index
        VEP1I32.tStart = t  # local t and not account for scr refresh
        VEP1I32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I32, 'tStartRefresh')  # time at next scr refresh
        VEP1I32.setAutoDraw(True)
    if VEP1I32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I32.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I32.tStop = t  # not accounting for scr refresh
            VEP1I32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I32, 'tStopRefresh')  # time at next scr refresh
            VEP1I32.setAutoDraw(False)
    
    # *S32* updates
    if S32.status == NOT_STARTED and tThisFlip >= 602.9-frameTolerance:
        # keep track of start time/frame for later
        S32.frameNStart = frameN  # exact frame index
        S32.tStart = t  # local t and not account for scr refresh
        S32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S32, 'tStartRefresh')  # time at next scr refresh
        S32.setAutoDraw(True)
    if S32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S32.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S32.tStop = t  # not accounting for scr refresh
            S32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S32, 'tStopRefresh')  # time at next scr refresh
            S32.setAutoDraw(False)
    
    # *VEP1I5* updates
    if VEP1I5.status == NOT_STARTED and tThisFlip >= 604.8-frameTolerance:
        # keep track of start time/frame for later
        VEP1I5.frameNStart = frameN  # exact frame index
        VEP1I5.tStart = t  # local t and not account for scr refresh
        VEP1I5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I5, 'tStartRefresh')  # time at next scr refresh
        VEP1I5.setAutoDraw(True)
    if VEP1I5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I5.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I5.tStop = t  # not accounting for scr refresh
            VEP1I5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I5, 'tStopRefresh')  # time at next scr refresh
            VEP1I5.setAutoDraw(False)
    
    # *S5* updates
    if S5.status == NOT_STARTED and tThisFlip >= 605.7-frameTolerance:
        # keep track of start time/frame for later
        S5.frameNStart = frameN  # exact frame index
        S5.tStart = t  # local t and not account for scr refresh
        S5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S5, 'tStartRefresh')  # time at next scr refresh
        S5.setAutoDraw(True)
    if S5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S5.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S5.tStop = t  # not accounting for scr refresh
            S5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S5, 'tStopRefresh')  # time at next scr refresh
            S5.setAutoDraw(False)
    
    # *VEP1I23* updates
    if VEP1I23.status == NOT_STARTED and tThisFlip >= 607.6-frameTolerance:
        # keep track of start time/frame for later
        VEP1I23.frameNStart = frameN  # exact frame index
        VEP1I23.tStart = t  # local t and not account for scr refresh
        VEP1I23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I23, 'tStartRefresh')  # time at next scr refresh
        VEP1I23.setAutoDraw(True)
    if VEP1I23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I23.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I23.tStop = t  # not accounting for scr refresh
            VEP1I23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I23, 'tStopRefresh')  # time at next scr refresh
            VEP1I23.setAutoDraw(False)
    
    # *S23* updates
    if S23.status == NOT_STARTED and tThisFlip >= 608.5-frameTolerance:
        # keep track of start time/frame for later
        S23.frameNStart = frameN  # exact frame index
        S23.tStart = t  # local t and not account for scr refresh
        S23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S23, 'tStartRefresh')  # time at next scr refresh
        S23.setAutoDraw(True)
    if S23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S23.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S23.tStop = t  # not accounting for scr refresh
            S23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S23, 'tStopRefresh')  # time at next scr refresh
            S23.setAutoDraw(False)
    
    # *VEP1I26* updates
    if VEP1I26.status == NOT_STARTED and tThisFlip >= 610.4-frameTolerance:
        # keep track of start time/frame for later
        VEP1I26.frameNStart = frameN  # exact frame index
        VEP1I26.tStart = t  # local t and not account for scr refresh
        VEP1I26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I26, 'tStartRefresh')  # time at next scr refresh
        VEP1I26.setAutoDraw(True)
    if VEP1I26.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I26.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I26.tStop = t  # not accounting for scr refresh
            VEP1I26.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I26, 'tStopRefresh')  # time at next scr refresh
            VEP1I26.setAutoDraw(False)
    
    # *S26* updates
    if S26.status == NOT_STARTED and tThisFlip >= 611.3-frameTolerance:
        # keep track of start time/frame for later
        S26.frameNStart = frameN  # exact frame index
        S26.tStart = t  # local t and not account for scr refresh
        S26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S26, 'tStartRefresh')  # time at next scr refresh
        S26.setAutoDraw(True)
    if S26.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S26.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S26.tStop = t  # not accounting for scr refresh
            S26.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S26, 'tStopRefresh')  # time at next scr refresh
            S26.setAutoDraw(False)
    
    # *vep1I8* updates
    if vep1I8.status == NOT_STARTED and tThisFlip >= 613.2-frameTolerance:
        # keep track of start time/frame for later
        vep1I8.frameNStart = frameN  # exact frame index
        vep1I8.tStart = t  # local t and not account for scr refresh
        vep1I8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vep1I8, 'tStartRefresh')  # time at next scr refresh
        vep1I8.setAutoDraw(True)
    if vep1I8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > vep1I8.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            vep1I8.tStop = t  # not accounting for scr refresh
            vep1I8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(vep1I8, 'tStopRefresh')  # time at next scr refresh
            vep1I8.setAutoDraw(False)
    
    # *S8* updates
    if S8.status == NOT_STARTED and tThisFlip >= 614.1-frameTolerance:
        # keep track of start time/frame for later
        S8.frameNStart = frameN  # exact frame index
        S8.tStart = t  # local t and not account for scr refresh
        S8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S8, 'tStartRefresh')  # time at next scr refresh
        S8.setAutoDraw(True)
    if S8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S8.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S8.tStop = t  # not accounting for scr refresh
            S8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S8, 'tStopRefresh')  # time at next scr refresh
            S8.setAutoDraw(False)
    
    # *VEp1I17* updates
    if VEp1I17.status == NOT_STARTED and tThisFlip >= 616-frameTolerance:
        # keep track of start time/frame for later
        VEp1I17.frameNStart = frameN  # exact frame index
        VEp1I17.tStart = t  # local t and not account for scr refresh
        VEp1I17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEp1I17, 'tStartRefresh')  # time at next scr refresh
        VEp1I17.setAutoDraw(True)
    if VEp1I17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEp1I17.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEp1I17.tStop = t  # not accounting for scr refresh
            VEp1I17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEp1I17, 'tStopRefresh')  # time at next scr refresh
            VEp1I17.setAutoDraw(False)
    
    # *S17* updates
    if S17.status == NOT_STARTED and tThisFlip >= 616.9-frameTolerance:
        # keep track of start time/frame for later
        S17.frameNStart = frameN  # exact frame index
        S17.tStart = t  # local t and not account for scr refresh
        S17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S17, 'tStartRefresh')  # time at next scr refresh
        S17.setAutoDraw(True)
    if S17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S17.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S17.tStop = t  # not accounting for scr refresh
            S17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S17, 'tStopRefresh')  # time at next scr refresh
            S17.setAutoDraw(False)
    
    # *VEP1I3* updates
    if VEP1I3.status == NOT_STARTED and tThisFlip >= 618.8-frameTolerance:
        # keep track of start time/frame for later
        VEP1I3.frameNStart = frameN  # exact frame index
        VEP1I3.tStart = t  # local t and not account for scr refresh
        VEP1I3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I3, 'tStartRefresh')  # time at next scr refresh
        VEP1I3.setAutoDraw(True)
    if VEP1I3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I3.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I3.tStop = t  # not accounting for scr refresh
            VEP1I3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I3, 'tStopRefresh')  # time at next scr refresh
            VEP1I3.setAutoDraw(False)
    
    # *S3* updates
    if S3.status == NOT_STARTED and tThisFlip >= 619.7-frameTolerance:
        # keep track of start time/frame for later
        S3.frameNStart = frameN  # exact frame index
        S3.tStart = t  # local t and not account for scr refresh
        S3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S3, 'tStartRefresh')  # time at next scr refresh
        S3.setAutoDraw(True)
    if S3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S3.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S3.tStop = t  # not accounting for scr refresh
            S3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S3, 'tStopRefresh')  # time at next scr refresh
            S3.setAutoDraw(False)
    
    # *VEP1I11* updates
    if VEP1I11.status == NOT_STARTED and tThisFlip >= 621.6-frameTolerance:
        # keep track of start time/frame for later
        VEP1I11.frameNStart = frameN  # exact frame index
        VEP1I11.tStart = t  # local t and not account for scr refresh
        VEP1I11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I11, 'tStartRefresh')  # time at next scr refresh
        VEP1I11.setAutoDraw(True)
    if VEP1I11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I11.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I11.tStop = t  # not accounting for scr refresh
            VEP1I11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I11, 'tStopRefresh')  # time at next scr refresh
            VEP1I11.setAutoDraw(False)
    
    # *S11* updates
    if S11.status == NOT_STARTED and tThisFlip >= 622.5-frameTolerance:
        # keep track of start time/frame for later
        S11.frameNStart = frameN  # exact frame index
        S11.tStart = t  # local t and not account for scr refresh
        S11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S11, 'tStartRefresh')  # time at next scr refresh
        S11.setAutoDraw(True)
    if S11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S11.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S11.tStop = t  # not accounting for scr refresh
            S11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S11, 'tStopRefresh')  # time at next scr refresh
            S11.setAutoDraw(False)
    
    # *VEP1I21* updates
    if VEP1I21.status == NOT_STARTED and tThisFlip >= 624.4-frameTolerance:
        # keep track of start time/frame for later
        VEP1I21.frameNStart = frameN  # exact frame index
        VEP1I21.tStart = t  # local t and not account for scr refresh
        VEP1I21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I21, 'tStartRefresh')  # time at next scr refresh
        VEP1I21.setAutoDraw(True)
    if VEP1I21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I21.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I21.tStop = t  # not accounting for scr refresh
            VEP1I21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I21, 'tStopRefresh')  # time at next scr refresh
            VEP1I21.setAutoDraw(False)
    
    # *S21* updates
    if S21.status == NOT_STARTED and tThisFlip >= 625.3-frameTolerance:
        # keep track of start time/frame for later
        S21.frameNStart = frameN  # exact frame index
        S21.tStart = t  # local t and not account for scr refresh
        S21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S21, 'tStartRefresh')  # time at next scr refresh
        S21.setAutoDraw(True)
    if S21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S21.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S21.tStop = t  # not accounting for scr refresh
            S21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S21, 'tStopRefresh')  # time at next scr refresh
            S21.setAutoDraw(False)
    
    # *VEP1I25* updates
    if VEP1I25.status == NOT_STARTED and tThisFlip >= 627.2-frameTolerance:
        # keep track of start time/frame for later
        VEP1I25.frameNStart = frameN  # exact frame index
        VEP1I25.tStart = t  # local t and not account for scr refresh
        VEP1I25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I25, 'tStartRefresh')  # time at next scr refresh
        VEP1I25.setAutoDraw(True)
    if VEP1I25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I25.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I25.tStop = t  # not accounting for scr refresh
            VEP1I25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I25, 'tStopRefresh')  # time at next scr refresh
            VEP1I25.setAutoDraw(False)
    
    # *s25* updates
    if s25.status == NOT_STARTED and tThisFlip >= 628.1-frameTolerance:
        # keep track of start time/frame for later
        s25.frameNStart = frameN  # exact frame index
        s25.tStart = t  # local t and not account for scr refresh
        s25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(s25, 'tStartRefresh')  # time at next scr refresh
        s25.setAutoDraw(True)
    if s25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > s25.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            s25.tStop = t  # not accounting for scr refresh
            s25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(s25, 'tStopRefresh')  # time at next scr refresh
            s25.setAutoDraw(False)
    
    # *VEP1I20* updates
    if VEP1I20.status == NOT_STARTED and tThisFlip >= 630-frameTolerance:
        # keep track of start time/frame for later
        VEP1I20.frameNStart = frameN  # exact frame index
        VEP1I20.tStart = t  # local t and not account for scr refresh
        VEP1I20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I20, 'tStartRefresh')  # time at next scr refresh
        VEP1I20.setAutoDraw(True)
    if VEP1I20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I20.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I20.tStop = t  # not accounting for scr refresh
            VEP1I20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I20, 'tStopRefresh')  # time at next scr refresh
            VEP1I20.setAutoDraw(False)
    
    # *S20* updates
    if S20.status == NOT_STARTED and tThisFlip >= 630.9-frameTolerance:
        # keep track of start time/frame for later
        S20.frameNStart = frameN  # exact frame index
        S20.tStart = t  # local t and not account for scr refresh
        S20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S20, 'tStartRefresh')  # time at next scr refresh
        S20.setAutoDraw(True)
    if S20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S20.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S20.tStop = t  # not accounting for scr refresh
            S20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S20, 'tStopRefresh')  # time at next scr refresh
            S20.setAutoDraw(False)
    
    # *VEP1I13* updates
    if VEP1I13.status == NOT_STARTED and tThisFlip >= 632.8-frameTolerance:
        # keep track of start time/frame for later
        VEP1I13.frameNStart = frameN  # exact frame index
        VEP1I13.tStart = t  # local t and not account for scr refresh
        VEP1I13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I13, 'tStartRefresh')  # time at next scr refresh
        VEP1I13.setAutoDraw(True)
    if VEP1I13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I13.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I13.tStop = t  # not accounting for scr refresh
            VEP1I13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I13, 'tStopRefresh')  # time at next scr refresh
            VEP1I13.setAutoDraw(False)
    
    # *S13* updates
    if S13.status == NOT_STARTED and tThisFlip >= 633.7-frameTolerance:
        # keep track of start time/frame for later
        S13.frameNStart = frameN  # exact frame index
        S13.tStart = t  # local t and not account for scr refresh
        S13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S13, 'tStartRefresh')  # time at next scr refresh
        S13.setAutoDraw(True)
    if S13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S13.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S13.tStop = t  # not accounting for scr refresh
            S13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S13, 'tStopRefresh')  # time at next scr refresh
            S13.setAutoDraw(False)
    
    # *VEP1I19* updates
    if VEP1I19.status == NOT_STARTED and tThisFlip >= 635.6-frameTolerance:
        # keep track of start time/frame for later
        VEP1I19.frameNStart = frameN  # exact frame index
        VEP1I19.tStart = t  # local t and not account for scr refresh
        VEP1I19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I19, 'tStartRefresh')  # time at next scr refresh
        VEP1I19.setAutoDraw(True)
    if VEP1I19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I19.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I19.tStop = t  # not accounting for scr refresh
            VEP1I19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I19, 'tStopRefresh')  # time at next scr refresh
            VEP1I19.setAutoDraw(False)
    
    # *S19* updates
    if S19.status == NOT_STARTED and tThisFlip >= 636.5-frameTolerance:
        # keep track of start time/frame for later
        S19.frameNStart = frameN  # exact frame index
        S19.tStart = t  # local t and not account for scr refresh
        S19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S19, 'tStartRefresh')  # time at next scr refresh
        S19.setAutoDraw(True)
    if S19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S19.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S19.tStop = t  # not accounting for scr refresh
            S19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S19, 'tStopRefresh')  # time at next scr refresh
            S19.setAutoDraw(False)
    
    # *VEP1I1* updates
    if VEP1I1.status == NOT_STARTED and tThisFlip >= 638.4-frameTolerance:
        # keep track of start time/frame for later
        VEP1I1.frameNStart = frameN  # exact frame index
        VEP1I1.tStart = t  # local t and not account for scr refresh
        VEP1I1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I1, 'tStartRefresh')  # time at next scr refresh
        VEP1I1.setAutoDraw(True)
    if VEP1I1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I1.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I1.tStop = t  # not accounting for scr refresh
            VEP1I1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I1, 'tStopRefresh')  # time at next scr refresh
            VEP1I1.setAutoDraw(False)
    
    # *S1* updates
    if S1.status == NOT_STARTED and tThisFlip >= 639.3-frameTolerance:
        # keep track of start time/frame for later
        S1.frameNStart = frameN  # exact frame index
        S1.tStart = t  # local t and not account for scr refresh
        S1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S1, 'tStartRefresh')  # time at next scr refresh
        S1.setAutoDraw(True)
    if S1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S1.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S1.tStop = t  # not accounting for scr refresh
            S1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S1, 'tStopRefresh')  # time at next scr refresh
            S1.setAutoDraw(False)
    
    # *VEP1I7* updates
    if VEP1I7.status == NOT_STARTED and tThisFlip >= 641.2-frameTolerance:
        # keep track of start time/frame for later
        VEP1I7.frameNStart = frameN  # exact frame index
        VEP1I7.tStart = t  # local t and not account for scr refresh
        VEP1I7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I7, 'tStartRefresh')  # time at next scr refresh
        VEP1I7.setAutoDraw(True)
    if VEP1I7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I7.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I7.tStop = t  # not accounting for scr refresh
            VEP1I7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I7, 'tStopRefresh')  # time at next scr refresh
            VEP1I7.setAutoDraw(False)
    
    # *S7* updates
    if S7.status == NOT_STARTED and tThisFlip >= 642.1-frameTolerance:
        # keep track of start time/frame for later
        S7.frameNStart = frameN  # exact frame index
        S7.tStart = t  # local t and not account for scr refresh
        S7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S7, 'tStartRefresh')  # time at next scr refresh
        S7.setAutoDraw(True)
    if S7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S7.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S7.tStop = t  # not accounting for scr refresh
            S7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S7, 'tStopRefresh')  # time at next scr refresh
            S7.setAutoDraw(False)
    
    # *VEP1I4* updates
    if VEP1I4.status == NOT_STARTED and tThisFlip >= 644-frameTolerance:
        # keep track of start time/frame for later
        VEP1I4.frameNStart = frameN  # exact frame index
        VEP1I4.tStart = t  # local t and not account for scr refresh
        VEP1I4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I4, 'tStartRefresh')  # time at next scr refresh
        VEP1I4.setAutoDraw(True)
    if VEP1I4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I4.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I4.tStop = t  # not accounting for scr refresh
            VEP1I4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I4, 'tStopRefresh')  # time at next scr refresh
            VEP1I4.setAutoDraw(False)
    
    # *S4* updates
    if S4.status == NOT_STARTED and tThisFlip >= 644.9-frameTolerance:
        # keep track of start time/frame for later
        S4.frameNStart = frameN  # exact frame index
        S4.tStart = t  # local t and not account for scr refresh
        S4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S4, 'tStartRefresh')  # time at next scr refresh
        S4.setAutoDraw(True)
    if S4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S4.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S4.tStop = t  # not accounting for scr refresh
            S4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S4, 'tStopRefresh')  # time at next scr refresh
            S4.setAutoDraw(False)
    
    # *VEP1I6* updates
    if VEP1I6.status == NOT_STARTED and tThisFlip >= 646.8-frameTolerance:
        # keep track of start time/frame for later
        VEP1I6.frameNStart = frameN  # exact frame index
        VEP1I6.tStart = t  # local t and not account for scr refresh
        VEP1I6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I6, 'tStartRefresh')  # time at next scr refresh
        VEP1I6.setAutoDraw(True)
    if VEP1I6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I6.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I6.tStop = t  # not accounting for scr refresh
            VEP1I6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I6, 'tStopRefresh')  # time at next scr refresh
            VEP1I6.setAutoDraw(False)
    
    # *S6* updates
    if S6.status == NOT_STARTED and tThisFlip >= 647.7-frameTolerance:
        # keep track of start time/frame for later
        S6.frameNStart = frameN  # exact frame index
        S6.tStart = t  # local t and not account for scr refresh
        S6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S6, 'tStartRefresh')  # time at next scr refresh
        S6.setAutoDraw(True)
    if S6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S6.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S6.tStop = t  # not accounting for scr refresh
            S6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S6, 'tStopRefresh')  # time at next scr refresh
            S6.setAutoDraw(False)
    
    # *VEP1I22* updates
    if VEP1I22.status == NOT_STARTED and tThisFlip >= 649.6-frameTolerance:
        # keep track of start time/frame for later
        VEP1I22.frameNStart = frameN  # exact frame index
        VEP1I22.tStart = t  # local t and not account for scr refresh
        VEP1I22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I22, 'tStartRefresh')  # time at next scr refresh
        VEP1I22.setAutoDraw(True)
    if VEP1I22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I22.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I22.tStop = t  # not accounting for scr refresh
            VEP1I22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I22, 'tStopRefresh')  # time at next scr refresh
            VEP1I22.setAutoDraw(False)
    
    # *S22* updates
    if S22.status == NOT_STARTED and tThisFlip >= 650.5-frameTolerance:
        # keep track of start time/frame for later
        S22.frameNStart = frameN  # exact frame index
        S22.tStart = t  # local t and not account for scr refresh
        S22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S22, 'tStartRefresh')  # time at next scr refresh
        S22.setAutoDraw(True)
    if S22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S22.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S22.tStop = t  # not accounting for scr refresh
            S22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S22, 'tStopRefresh')  # time at next scr refresh
            S22.setAutoDraw(False)
    
    # *VEP1I2* updates
    if VEP1I2.status == NOT_STARTED and tThisFlip >= 652.4-frameTolerance:
        # keep track of start time/frame for later
        VEP1I2.frameNStart = frameN  # exact frame index
        VEP1I2.tStart = t  # local t and not account for scr refresh
        VEP1I2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I2, 'tStartRefresh')  # time at next scr refresh
        VEP1I2.setAutoDraw(True)
    if VEP1I2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I2.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I2.tStop = t  # not accounting for scr refresh
            VEP1I2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I2, 'tStopRefresh')  # time at next scr refresh
            VEP1I2.setAutoDraw(False)
    
    # *S2* updates
    if S2.status == NOT_STARTED and tThisFlip >= 653.3-frameTolerance:
        # keep track of start time/frame for later
        S2.frameNStart = frameN  # exact frame index
        S2.tStart = t  # local t and not account for scr refresh
        S2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S2, 'tStartRefresh')  # time at next scr refresh
        S2.setAutoDraw(True)
    if S2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S2.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S2.tStop = t  # not accounting for scr refresh
            S2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S2, 'tStopRefresh')  # time at next scr refresh
            S2.setAutoDraw(False)
    
    # *VEP1I10* updates
    if VEP1I10.status == NOT_STARTED and tThisFlip >= 655.2-frameTolerance:
        # keep track of start time/frame for later
        VEP1I10.frameNStart = frameN  # exact frame index
        VEP1I10.tStart = t  # local t and not account for scr refresh
        VEP1I10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I10, 'tStartRefresh')  # time at next scr refresh
        VEP1I10.setAutoDraw(True)
    if VEP1I10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I10.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I10.tStop = t  # not accounting for scr refresh
            VEP1I10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I10, 'tStopRefresh')  # time at next scr refresh
            VEP1I10.setAutoDraw(False)
    
    # *S10* updates
    if S10.status == NOT_STARTED and tThisFlip >= 656.1-frameTolerance:
        # keep track of start time/frame for later
        S10.frameNStart = frameN  # exact frame index
        S10.tStart = t  # local t and not account for scr refresh
        S10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S10, 'tStartRefresh')  # time at next scr refresh
        S10.setAutoDraw(True)
    if S10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S10.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S10.tStop = t  # not accounting for scr refresh
            S10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S10, 'tStopRefresh')  # time at next scr refresh
            S10.setAutoDraw(False)
    
    # *VEP1I15* updates
    if VEP1I15.status == NOT_STARTED and tThisFlip >= 658-frameTolerance:
        # keep track of start time/frame for later
        VEP1I15.frameNStart = frameN  # exact frame index
        VEP1I15.tStart = t  # local t and not account for scr refresh
        VEP1I15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I15, 'tStartRefresh')  # time at next scr refresh
        VEP1I15.setAutoDraw(True)
    if VEP1I15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I15.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I15.tStop = t  # not accounting for scr refresh
            VEP1I15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I15, 'tStopRefresh')  # time at next scr refresh
            VEP1I15.setAutoDraw(False)
    
    # *S15* updates
    if S15.status == NOT_STARTED and tThisFlip >= 658.9-frameTolerance:
        # keep track of start time/frame for later
        S15.frameNStart = frameN  # exact frame index
        S15.tStart = t  # local t and not account for scr refresh
        S15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S15, 'tStartRefresh')  # time at next scr refresh
        S15.setAutoDraw(True)
    if S15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S15.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S15.tStop = t  # not accounting for scr refresh
            S15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S15, 'tStopRefresh')  # time at next scr refresh
            S15.setAutoDraw(False)
    
    # *VEP1I14* updates
    if VEP1I14.status == NOT_STARTED and tThisFlip >= 660.8-frameTolerance:
        # keep track of start time/frame for later
        VEP1I14.frameNStart = frameN  # exact frame index
        VEP1I14.tStart = t  # local t and not account for scr refresh
        VEP1I14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP1I14, 'tStartRefresh')  # time at next scr refresh
        VEP1I14.setAutoDraw(True)
    if VEP1I14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP1I14.tStartRefresh + .8-frameTolerance:
            # keep track of stop time/frame for later
            VEP1I14.tStop = t  # not accounting for scr refresh
            VEP1I14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP1I14, 'tStopRefresh')  # time at next scr refresh
            VEP1I14.setAutoDraw(False)
    
    # *S14* updates
    if S14.status == NOT_STARTED and tThisFlip >= 661.7-frameTolerance:
        # keep track of start time/frame for later
        S14.frameNStart = frameN  # exact frame index
        S14.tStart = t  # local t and not account for scr refresh
        S14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(S14, 'tStartRefresh')  # time at next scr refresh
        S14.setAutoDraw(True)
    if S14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > S14.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            S14.tStop = t  # not accounting for scr refresh
            S14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(S14, 'tStopRefresh')  # time at next scr refresh
            S14.setAutoDraw(False)
    
    # *text_44* updates
    if text_44.status == NOT_STARTED and tThisFlip >= 664-frameTolerance:
        # keep track of start time/frame for later
        text_44.frameNStart = frameN  # exact frame index
        text_44.tStart = t  # local t and not account for scr refresh
        text_44.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_44, 'tStartRefresh')  # time at next scr refresh
        text_44.setAutoDraw(True)
    if text_44.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_44.tStartRefresh + 9.5-frameTolerance:
            # keep track of stop time/frame for later
            text_44.tStop = t  # not accounting for scr refresh
            text_44.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_44, 'tStopRefresh')  # time at next scr refresh
            text_44.setAutoDraw(False)
    
    # *VEP2C1* updates
    if VEP2C1.status == NOT_STARTED and tThisFlip >= 674-frameTolerance:
        # keep track of start time/frame for later
        VEP2C1.frameNStart = frameN  # exact frame index
        VEP2C1.tStart = t  # local t and not account for scr refresh
        VEP2C1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP2C1, 'tStartRefresh')  # time at next scr refresh
        VEP2C1.setAutoDraw(True)
    if VEP2C1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP2C1.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            VEP2C1.tStop = t  # not accounting for scr refresh
            VEP2C1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP2C1, 'tStopRefresh')  # time at next scr refresh
            VEP2C1.setAutoDraw(False)
    
    # *text_45* updates
    if text_45.status == NOT_STARTED and tThisFlip >= 674-frameTolerance:
        # keep track of start time/frame for later
        text_45.frameNStart = frameN  # exact frame index
        text_45.tStart = t  # local t and not account for scr refresh
        text_45.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_45, 'tStartRefresh')  # time at next scr refresh
        text_45.setAutoDraw(True)
    if text_45.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_45.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_45.tStop = t  # not accounting for scr refresh
            text_45.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_45, 'tStopRefresh')  # time at next scr refresh
            text_45.setAutoDraw(False)
    
    # *d1* updates
    if d1.status == NOT_STARTED and tThisFlip >= 675.4-frameTolerance:
        # keep track of start time/frame for later
        d1.frameNStart = frameN  # exact frame index
        d1.tStart = t  # local t and not account for scr refresh
        d1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(d1, 'tStartRefresh')  # time at next scr refresh
        d1.setAutoDraw(True)
    if d1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > d1.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            d1.tStop = t  # not accounting for scr refresh
            d1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(d1, 'tStopRefresh')  # time at next scr refresh
            d1.setAutoDraw(False)
    
    # *d2* updates
    if d2.status == NOT_STARTED and tThisFlip >= 676-frameTolerance:
        # keep track of start time/frame for later
        d2.frameNStart = frameN  # exact frame index
        d2.tStart = t  # local t and not account for scr refresh
        d2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(d2, 'tStartRefresh')  # time at next scr refresh
        d2.setAutoDraw(True)
    if d2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > d2.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            d2.tStop = t  # not accounting for scr refresh
            d2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(d2, 'tStopRefresh')  # time at next scr refresh
            d2.setAutoDraw(False)
    
    # *s1* updates
    if s1.status == NOT_STARTED and tThisFlip >= 676.4-frameTolerance:
        # keep track of start time/frame for later
        s1.frameNStart = frameN  # exact frame index
        s1.tStart = t  # local t and not account for scr refresh
        s1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(s1, 'tStartRefresh')  # time at next scr refresh
        s1.setAutoDraw(True)
    if s1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > s1.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            s1.tStop = t  # not accounting for scr refresh
            s1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(s1, 'tStopRefresh')  # time at next scr refresh
            s1.setAutoDraw(False)
    
    # *b1* updates
    if b1.status == NOT_STARTED and tThisFlip >= 676.9-frameTolerance:
        # keep track of start time/frame for later
        b1.frameNStart = frameN  # exact frame index
        b1.tStart = t  # local t and not account for scr refresh
        b1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b1, 'tStartRefresh')  # time at next scr refresh
        b1.setAutoDraw(True)
    if b1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b1.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            b1.tStop = t  # not accounting for scr refresh
            b1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b1, 'tStopRefresh')  # time at next scr refresh
            b1.setAutoDraw(False)
    
    # *d4* updates
    if d4.status == NOT_STARTED and tThisFlip >= 677.5-frameTolerance:
        # keep track of start time/frame for later
        d4.frameNStart = frameN  # exact frame index
        d4.tStart = t  # local t and not account for scr refresh
        d4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(d4, 'tStartRefresh')  # time at next scr refresh
        d4.setAutoDraw(True)
    if d4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > d4.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            d4.tStop = t  # not accounting for scr refresh
            d4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(d4, 'tStopRefresh')  # time at next scr refresh
            d4.setAutoDraw(False)
    
    # *s2* updates
    if s2.status == NOT_STARTED and tThisFlip >= 677.9-frameTolerance:
        # keep track of start time/frame for later
        s2.frameNStart = frameN  # exact frame index
        s2.tStart = t  # local t and not account for scr refresh
        s2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(s2, 'tStartRefresh')  # time at next scr refresh
        s2.setAutoDraw(True)
    if s2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > s2.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            s2.tStop = t  # not accounting for scr refresh
            s2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(s2, 'tStopRefresh')  # time at next scr refresh
            s2.setAutoDraw(False)
    
    # *VS1* updates
    if VS1.status == NOT_STARTED and tThisFlip >= 678.4-frameTolerance:
        # keep track of start time/frame for later
        VS1.frameNStart = frameN  # exact frame index
        VS1.tStart = t  # local t and not account for scr refresh
        VS1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VS1, 'tStartRefresh')  # time at next scr refresh
        VS1.setAutoDraw(True)
    if VS1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VS1.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            VS1.tStop = t  # not accounting for scr refresh
            VS1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VS1, 'tStopRefresh')  # time at next scr refresh
            VS1.setAutoDraw(False)
    
    # *VEP2C2* updates
    if VEP2C2.status == NOT_STARTED and tThisFlip >= 680.3-frameTolerance:
        # keep track of start time/frame for later
        VEP2C2.frameNStart = frameN  # exact frame index
        VEP2C2.tStart = t  # local t and not account for scr refresh
        VEP2C2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP2C2, 'tStartRefresh')  # time at next scr refresh
        VEP2C2.setAutoDraw(True)
    if VEP2C2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP2C2.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            VEP2C2.tStop = t  # not accounting for scr refresh
            VEP2C2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP2C2, 'tStopRefresh')  # time at next scr refresh
            VEP2C2.setAutoDraw(False)
    
    # *text_46* updates
    if text_46.status == NOT_STARTED and tThisFlip >= 680.3-frameTolerance:
        # keep track of start time/frame for later
        text_46.frameNStart = frameN  # exact frame index
        text_46.tStart = t  # local t and not account for scr refresh
        text_46.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_46, 'tStartRefresh')  # time at next scr refresh
        text_46.setAutoDraw(True)
    if text_46.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_46.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_46.tStop = t  # not accounting for scr refresh
            text_46.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_46, 'tStopRefresh')  # time at next scr refresh
            text_46.setAutoDraw(False)
    
    # *b2* updates
    if b2.status == NOT_STARTED and tThisFlip >= 681.6-frameTolerance:
        # keep track of start time/frame for later
        b2.frameNStart = frameN  # exact frame index
        b2.tStart = t  # local t and not account for scr refresh
        b2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(b2, 'tStartRefresh')  # time at next scr refresh
        b2.setAutoDraw(True)
    if b2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > b2.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            b2.tStop = t  # not accounting for scr refresh
            b2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(b2, 'tStopRefresh')  # time at next scr refresh
            b2.setAutoDraw(False)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 682-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    if image.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 682.3-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    if image_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_2.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_2.tStop = t  # not accounting for scr refresh
            image_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
            image_2.setAutoDraw(False)
    
    # *image_3* updates
    if image_3.status == NOT_STARTED and tThisFlip >= 682.7-frameTolerance:
        # keep track of start time/frame for later
        image_3.frameNStart = frameN  # exact frame index
        image_3.tStart = t  # local t and not account for scr refresh
        image_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
        image_3.setAutoDraw(True)
    if image_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_3.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_3.tStop = t  # not accounting for scr refresh
            image_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
            image_3.setAutoDraw(False)
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 683.1-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
            image_4.setAutoDraw(False)
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 683.6-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_5.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_5.tStop = t  # not accounting for scr refresh
            image_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
            image_5.setAutoDraw(False)
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 683.9-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    if image_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_6.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_6.tStop = t  # not accounting for scr refresh
            image_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
            image_6.setAutoDraw(False)
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 684.2-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    if image_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_7.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_7.tStop = t  # not accounting for scr refresh
            image_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
            image_7.setAutoDraw(False)
    
    # *slider* updates
    if slider.status == NOT_STARTED and tThisFlip >= 684.7-frameTolerance:
        # keep track of start time/frame for later
        slider.frameNStart = frameN  # exact frame index
        slider.tStart = t  # local t and not account for scr refresh
        slider.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
        slider.setAutoDraw(True)
    if slider.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider.tStop = t  # not accounting for scr refresh
            slider.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider, 'tStopRefresh')  # time at next scr refresh
            slider.setAutoDraw(False)
    
    # *VEP2C3* updates
    if VEP2C3.status == NOT_STARTED and tThisFlip >= 686.6-frameTolerance:
        # keep track of start time/frame for later
        VEP2C3.frameNStart = frameN  # exact frame index
        VEP2C3.tStart = t  # local t and not account for scr refresh
        VEP2C3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP2C3, 'tStartRefresh')  # time at next scr refresh
        VEP2C3.setAutoDraw(True)
    if VEP2C3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP2C3.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            VEP2C3.tStop = t  # not accounting for scr refresh
            VEP2C3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP2C3, 'tStopRefresh')  # time at next scr refresh
            VEP2C3.setAutoDraw(False)
    
    # *text_47* updates
    if text_47.status == NOT_STARTED and tThisFlip >= 686.6-frameTolerance:
        # keep track of start time/frame for later
        text_47.frameNStart = frameN  # exact frame index
        text_47.tStart = t  # local t and not account for scr refresh
        text_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        text_47.setAutoDraw(True)
    if text_47.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_47.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_47.tStop = t  # not accounting for scr refresh
            text_47.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_47, 'tStopRefresh')  # time at next scr refresh
            text_47.setAutoDraw(False)
    
    # *image_8* updates
    if image_8.status == NOT_STARTED and tThisFlip >= 687.9-frameTolerance:
        # keep track of start time/frame for later
        image_8.frameNStart = frameN  # exact frame index
        image_8.tStart = t  # local t and not account for scr refresh
        image_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
        image_8.setAutoDraw(True)
    if image_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_8.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_8.tStop = t  # not accounting for scr refresh
            image_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_8, 'tStopRefresh')  # time at next scr refresh
            image_8.setAutoDraw(False)
    
    # *image_9* updates
    if image_9.status == NOT_STARTED and tThisFlip >= 688.3-frameTolerance:
        # keep track of start time/frame for later
        image_9.frameNStart = frameN  # exact frame index
        image_9.tStart = t  # local t and not account for scr refresh
        image_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
        image_9.setAutoDraw(True)
    if image_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_9.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_9.tStop = t  # not accounting for scr refresh
            image_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
            image_9.setAutoDraw(False)
    
    # *image_10* updates
    if image_10.status == NOT_STARTED and tThisFlip >= 688.6-frameTolerance:
        # keep track of start time/frame for later
        image_10.frameNStart = frameN  # exact frame index
        image_10.tStart = t  # local t and not account for scr refresh
        image_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
        image_10.setAutoDraw(True)
    if image_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_10.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_10.tStop = t  # not accounting for scr refresh
            image_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_10, 'tStopRefresh')  # time at next scr refresh
            image_10.setAutoDraw(False)
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 689-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        image_11.setAutoDraw(True)
    if image_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_11.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_11.tStop = t  # not accounting for scr refresh
            image_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_11, 'tStopRefresh')  # time at next scr refresh
            image_11.setAutoDraw(False)
    
    # *image_12* updates
    if image_12.status == NOT_STARTED and tThisFlip >= 689.3-frameTolerance:
        # keep track of start time/frame for later
        image_12.frameNStart = frameN  # exact frame index
        image_12.tStart = t  # local t and not account for scr refresh
        image_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
        image_12.setAutoDraw(True)
    if image_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_12.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_12.tStop = t  # not accounting for scr refresh
            image_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_12, 'tStopRefresh')  # time at next scr refresh
            image_12.setAutoDraw(False)
    
    # *image_13* updates
    if image_13.status == NOT_STARTED and tThisFlip >= 689.7-frameTolerance:
        # keep track of start time/frame for later
        image_13.frameNStart = frameN  # exact frame index
        image_13.tStart = t  # local t and not account for scr refresh
        image_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
        image_13.setAutoDraw(True)
    if image_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_13.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_13.tStop = t  # not accounting for scr refresh
            image_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
            image_13.setAutoDraw(False)
    
    # *image_14* updates
    if image_14.status == NOT_STARTED and tThisFlip >= 690.2-frameTolerance:
        # keep track of start time/frame for later
        image_14.frameNStart = frameN  # exact frame index
        image_14.tStart = t  # local t and not account for scr refresh
        image_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
        image_14.setAutoDraw(True)
    if image_14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_14.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_14.tStop = t  # not accounting for scr refresh
            image_14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_14, 'tStopRefresh')  # time at next scr refresh
            image_14.setAutoDraw(False)
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 690.6-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    if image_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_15.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_15.tStop = t  # not accounting for scr refresh
            image_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_15, 'tStopRefresh')  # time at next scr refresh
            image_15.setAutoDraw(False)
    
    # *slider_2* updates
    if slider_2.status == NOT_STARTED and tThisFlip >= 691-frameTolerance:
        # keep track of start time/frame for later
        slider_2.frameNStart = frameN  # exact frame index
        slider_2.tStart = t  # local t and not account for scr refresh
        slider_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
        slider_2.setAutoDraw(True)
    if slider_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_2.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_2.tStop = t  # not accounting for scr refresh
            slider_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_2, 'tStopRefresh')  # time at next scr refresh
            slider_2.setAutoDraw(False)
    
    # *VEP2C4* updates
    if VEP2C4.status == NOT_STARTED and tThisFlip >= 692.9-frameTolerance:
        # keep track of start time/frame for later
        VEP2C4.frameNStart = frameN  # exact frame index
        VEP2C4.tStart = t  # local t and not account for scr refresh
        VEP2C4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VEP2C4, 'tStartRefresh')  # time at next scr refresh
        VEP2C4.setAutoDraw(True)
    if VEP2C4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > VEP2C4.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            VEP2C4.tStop = t  # not accounting for scr refresh
            VEP2C4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(VEP2C4, 'tStopRefresh')  # time at next scr refresh
            VEP2C4.setAutoDraw(False)
    
    # *text_48* updates
    if text_48.status == NOT_STARTED and tThisFlip >= 692.9-frameTolerance:
        # keep track of start time/frame for later
        text_48.frameNStart = frameN  # exact frame index
        text_48.tStart = t  # local t and not account for scr refresh
        text_48.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_48, 'tStartRefresh')  # time at next scr refresh
        text_48.setAutoDraw(True)
    if text_48.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_48.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_48.tStop = t  # not accounting for scr refresh
            text_48.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_48, 'tStopRefresh')  # time at next scr refresh
            text_48.setAutoDraw(False)
    
    # *image_16* updates
    if image_16.status == NOT_STARTED and tThisFlip >= 694.2-frameTolerance:
        # keep track of start time/frame for later
        image_16.frameNStart = frameN  # exact frame index
        image_16.tStart = t  # local t and not account for scr refresh
        image_16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_16, 'tStartRefresh')  # time at next scr refresh
        image_16.setAutoDraw(True)
    if image_16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_16.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_16.tStop = t  # not accounting for scr refresh
            image_16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_16, 'tStopRefresh')  # time at next scr refresh
            image_16.setAutoDraw(False)
    
    # *image_17* updates
    if image_17.status == NOT_STARTED and tThisFlip >= 694.5-frameTolerance:
        # keep track of start time/frame for later
        image_17.frameNStart = frameN  # exact frame index
        image_17.tStart = t  # local t and not account for scr refresh
        image_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_17, 'tStartRefresh')  # time at next scr refresh
        image_17.setAutoDraw(True)
    if image_17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_17.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_17.tStop = t  # not accounting for scr refresh
            image_17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_17, 'tStopRefresh')  # time at next scr refresh
            image_17.setAutoDraw(False)
    
    # *image_18* updates
    if image_18.status == NOT_STARTED and tThisFlip >= 694.9-frameTolerance:
        # keep track of start time/frame for later
        image_18.frameNStart = frameN  # exact frame index
        image_18.tStart = t  # local t and not account for scr refresh
        image_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_18, 'tStartRefresh')  # time at next scr refresh
        image_18.setAutoDraw(True)
    if image_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_18.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_18.tStop = t  # not accounting for scr refresh
            image_18.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_18, 'tStopRefresh')  # time at next scr refresh
            image_18.setAutoDraw(False)
    
    # *image_19* updates
    if image_19.status == NOT_STARTED and tThisFlip >= 695.3-frameTolerance:
        # keep track of start time/frame for later
        image_19.frameNStart = frameN  # exact frame index
        image_19.tStart = t  # local t and not account for scr refresh
        image_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
        image_19.setAutoDraw(True)
    if image_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_19.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_19.tStop = t  # not accounting for scr refresh
            image_19.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_19, 'tStopRefresh')  # time at next scr refresh
            image_19.setAutoDraw(False)
    
    # *image_20* updates
    if image_20.status == NOT_STARTED and tThisFlip >= 695.8-frameTolerance:
        # keep track of start time/frame for later
        image_20.frameNStart = frameN  # exact frame index
        image_20.tStart = t  # local t and not account for scr refresh
        image_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_20, 'tStartRefresh')  # time at next scr refresh
        image_20.setAutoDraw(True)
    if image_20.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_20.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_20.tStop = t  # not accounting for scr refresh
            image_20.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_20, 'tStopRefresh')  # time at next scr refresh
            image_20.setAutoDraw(False)
    
    # *image_21* updates
    if image_21.status == NOT_STARTED and tThisFlip >= 696.2-frameTolerance:
        # keep track of start time/frame for later
        image_21.frameNStart = frameN  # exact frame index
        image_21.tStart = t  # local t and not account for scr refresh
        image_21.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_21, 'tStartRefresh')  # time at next scr refresh
        image_21.setAutoDraw(True)
    if image_21.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_21.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_21.tStop = t  # not accounting for scr refresh
            image_21.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_21, 'tStopRefresh')  # time at next scr refresh
            image_21.setAutoDraw(False)
    
    # *image_22* updates
    if image_22.status == NOT_STARTED and tThisFlip >= 696.4-frameTolerance:
        # keep track of start time/frame for later
        image_22.frameNStart = frameN  # exact frame index
        image_22.tStart = t  # local t and not account for scr refresh
        image_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_22, 'tStartRefresh')  # time at next scr refresh
        image_22.setAutoDraw(True)
    if image_22.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_22.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_22.tStop = t  # not accounting for scr refresh
            image_22.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_22, 'tStopRefresh')  # time at next scr refresh
            image_22.setAutoDraw(False)
    
    # *image_23* updates
    if image_23.status == NOT_STARTED and tThisFlip >= 696.7-frameTolerance:
        # keep track of start time/frame for later
        image_23.frameNStart = frameN  # exact frame index
        image_23.tStart = t  # local t and not account for scr refresh
        image_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_23, 'tStartRefresh')  # time at next scr refresh
        image_23.setAutoDraw(True)
    if image_23.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_23.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_23.tStop = t  # not accounting for scr refresh
            image_23.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_23, 'tStopRefresh')  # time at next scr refresh
            image_23.setAutoDraw(False)
    
    # *image_24* updates
    if image_24.status == NOT_STARTED and tThisFlip >= 697-frameTolerance:
        # keep track of start time/frame for later
        image_24.frameNStart = frameN  # exact frame index
        image_24.tStart = t  # local t and not account for scr refresh
        image_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_24, 'tStartRefresh')  # time at next scr refresh
        image_24.setAutoDraw(True)
    if image_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_24.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_24.tStop = t  # not accounting for scr refresh
            image_24.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_24, 'tStopRefresh')  # time at next scr refresh
            image_24.setAutoDraw(False)
    
    # *slider_3* updates
    if slider_3.status == NOT_STARTED and tThisFlip >= 697.3-frameTolerance:
        # keep track of start time/frame for later
        slider_3.frameNStart = frameN  # exact frame index
        slider_3.tStart = t  # local t and not account for scr refresh
        slider_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_3, 'tStartRefresh')  # time at next scr refresh
        slider_3.setAutoDraw(True)
    if slider_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_3.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_3.tStop = t  # not accounting for scr refresh
            slider_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_3, 'tStopRefresh')  # time at next scr refresh
            slider_3.setAutoDraw(False)
    
    # *C5* updates
    if C5.status == NOT_STARTED and tThisFlip >= 699.2-frameTolerance:
        # keep track of start time/frame for later
        C5.frameNStart = frameN  # exact frame index
        C5.tStart = t  # local t and not account for scr refresh
        C5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C5, 'tStartRefresh')  # time at next scr refresh
        C5.setAutoDraw(True)
    if C5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C5.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C5.tStop = t  # not accounting for scr refresh
            C5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C5, 'tStopRefresh')  # time at next scr refresh
            C5.setAutoDraw(False)
    
    # *text_49* updates
    if text_49.status == NOT_STARTED and tThisFlip >= 699.2-frameTolerance:
        # keep track of start time/frame for later
        text_49.frameNStart = frameN  # exact frame index
        text_49.tStart = t  # local t and not account for scr refresh
        text_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        text_49.setAutoDraw(True)
    if text_49.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_49.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_49.tStop = t  # not accounting for scr refresh
            text_49.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_49, 'tStopRefresh')  # time at next scr refresh
            text_49.setAutoDraw(False)
    
    # *image_26* updates
    if image_26.status == NOT_STARTED and tThisFlip >= 700.5-frameTolerance:
        # keep track of start time/frame for later
        image_26.frameNStart = frameN  # exact frame index
        image_26.tStart = t  # local t and not account for scr refresh
        image_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_26, 'tStartRefresh')  # time at next scr refresh
        image_26.setAutoDraw(True)
    if image_26.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_26.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_26.tStop = t  # not accounting for scr refresh
            image_26.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_26, 'tStopRefresh')  # time at next scr refresh
            image_26.setAutoDraw(False)
    
    # *image_27* updates
    if image_27.status == NOT_STARTED and tThisFlip >= 700.8-frameTolerance:
        # keep track of start time/frame for later
        image_27.frameNStart = frameN  # exact frame index
        image_27.tStart = t  # local t and not account for scr refresh
        image_27.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_27, 'tStartRefresh')  # time at next scr refresh
        image_27.setAutoDraw(True)
    if image_27.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_27.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_27.tStop = t  # not accounting for scr refresh
            image_27.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_27, 'tStopRefresh')  # time at next scr refresh
            image_27.setAutoDraw(False)
    
    # *image_28* updates
    if image_28.status == NOT_STARTED and tThisFlip >= 701-frameTolerance:
        # keep track of start time/frame for later
        image_28.frameNStart = frameN  # exact frame index
        image_28.tStart = t  # local t and not account for scr refresh
        image_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_28, 'tStartRefresh')  # time at next scr refresh
        image_28.setAutoDraw(True)
    if image_28.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_28.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_28.tStop = t  # not accounting for scr refresh
            image_28.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_28, 'tStopRefresh')  # time at next scr refresh
            image_28.setAutoDraw(False)
    
    # *image_29* updates
    if image_29.status == NOT_STARTED and tThisFlip >= 701.4-frameTolerance:
        # keep track of start time/frame for later
        image_29.frameNStart = frameN  # exact frame index
        image_29.tStart = t  # local t and not account for scr refresh
        image_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_29, 'tStartRefresh')  # time at next scr refresh
        image_29.setAutoDraw(True)
    if image_29.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_29.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_29.tStop = t  # not accounting for scr refresh
            image_29.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_29, 'tStopRefresh')  # time at next scr refresh
            image_29.setAutoDraw(False)
    
    # *image_30* updates
    if image_30.status == NOT_STARTED and tThisFlip >= 701.8-frameTolerance:
        # keep track of start time/frame for later
        image_30.frameNStart = frameN  # exact frame index
        image_30.tStart = t  # local t and not account for scr refresh
        image_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_30, 'tStartRefresh')  # time at next scr refresh
        image_30.setAutoDraw(True)
    if image_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_30.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_30.tStop = t  # not accounting for scr refresh
            image_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_30, 'tStopRefresh')  # time at next scr refresh
            image_30.setAutoDraw(False)
    
    # *image_31* updates
    if image_31.status == NOT_STARTED and tThisFlip >= 702.3-frameTolerance:
        # keep track of start time/frame for later
        image_31.frameNStart = frameN  # exact frame index
        image_31.tStart = t  # local t and not account for scr refresh
        image_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_31, 'tStartRefresh')  # time at next scr refresh
        image_31.setAutoDraw(True)
    if image_31.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_31.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_31.tStop = t  # not accounting for scr refresh
            image_31.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_31, 'tStopRefresh')  # time at next scr refresh
            image_31.setAutoDraw(False)
    
    # *image_32* updates
    if image_32.status == NOT_STARTED and tThisFlip >= 702.5-frameTolerance:
        # keep track of start time/frame for later
        image_32.frameNStart = frameN  # exact frame index
        image_32.tStart = t  # local t and not account for scr refresh
        image_32.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_32, 'tStartRefresh')  # time at next scr refresh
        image_32.setAutoDraw(True)
    if image_32.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_32.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_32.tStop = t  # not accounting for scr refresh
            image_32.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_32, 'tStopRefresh')  # time at next scr refresh
            image_32.setAutoDraw(False)
    
    # *image_33* updates
    if image_33.status == NOT_STARTED and tThisFlip >= 702.9-frameTolerance:
        # keep track of start time/frame for later
        image_33.frameNStart = frameN  # exact frame index
        image_33.tStart = t  # local t and not account for scr refresh
        image_33.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_33, 'tStartRefresh')  # time at next scr refresh
        image_33.setAutoDraw(True)
    if image_33.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_33.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_33.tStop = t  # not accounting for scr refresh
            image_33.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_33, 'tStopRefresh')  # time at next scr refresh
            image_33.setAutoDraw(False)
    
    # *image_34* updates
    if image_34.status == NOT_STARTED and tThisFlip >= 703.4-frameTolerance:
        # keep track of start time/frame for later
        image_34.frameNStart = frameN  # exact frame index
        image_34.tStart = t  # local t and not account for scr refresh
        image_34.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_34, 'tStartRefresh')  # time at next scr refresh
        image_34.setAutoDraw(True)
    if image_34.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_34.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_34.tStop = t  # not accounting for scr refresh
            image_34.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_34, 'tStopRefresh')  # time at next scr refresh
            image_34.setAutoDraw(False)
    
    # *slider_4* updates
    if slider_4.status == NOT_STARTED and tThisFlip >= 703.6-frameTolerance:
        # keep track of start time/frame for later
        slider_4.frameNStart = frameN  # exact frame index
        slider_4.tStart = t  # local t and not account for scr refresh
        slider_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_4, 'tStartRefresh')  # time at next scr refresh
        slider_4.setAutoDraw(True)
    if slider_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_4.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_4.tStop = t  # not accounting for scr refresh
            slider_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_4, 'tStopRefresh')  # time at next scr refresh
            slider_4.setAutoDraw(False)
    
    # *C6* updates
    if C6.status == NOT_STARTED and tThisFlip >= 705.5-frameTolerance:
        # keep track of start time/frame for later
        C6.frameNStart = frameN  # exact frame index
        C6.tStart = t  # local t and not account for scr refresh
        C6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C6, 'tStartRefresh')  # time at next scr refresh
        C6.setAutoDraw(True)
    if C6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C6.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C6.tStop = t  # not accounting for scr refresh
            C6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C6, 'tStopRefresh')  # time at next scr refresh
            C6.setAutoDraw(False)
    
    # *text_50* updates
    if text_50.status == NOT_STARTED and tThisFlip >= 705.5-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        text_50.setAutoDraw(True)
    if text_50.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_50.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_50.tStop = t  # not accounting for scr refresh
            text_50.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_50, 'tStopRefresh')  # time at next scr refresh
            text_50.setAutoDraw(False)
    
    # *image_36* updates
    if image_36.status == NOT_STARTED and tThisFlip >= 706.8-frameTolerance:
        # keep track of start time/frame for later
        image_36.frameNStart = frameN  # exact frame index
        image_36.tStart = t  # local t and not account for scr refresh
        image_36.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_36, 'tStartRefresh')  # time at next scr refresh
        image_36.setAutoDraw(True)
    if image_36.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_36.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            image_36.tStop = t  # not accounting for scr refresh
            image_36.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_36, 'tStopRefresh')  # time at next scr refresh
            image_36.setAutoDraw(False)
    
    # *image_37* updates
    if image_37.status == NOT_STARTED and tThisFlip >= 707.4-frameTolerance:
        # keep track of start time/frame for later
        image_37.frameNStart = frameN  # exact frame index
        image_37.tStart = t  # local t and not account for scr refresh
        image_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_37, 'tStartRefresh')  # time at next scr refresh
        image_37.setAutoDraw(True)
    if image_37.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_37.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_37.tStop = t  # not accounting for scr refresh
            image_37.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_37, 'tStopRefresh')  # time at next scr refresh
            image_37.setAutoDraw(False)
    
    # *image_25* updates
    if image_25.status == NOT_STARTED and tThisFlip >= 707.8-frameTolerance:
        # keep track of start time/frame for later
        image_25.frameNStart = frameN  # exact frame index
        image_25.tStart = t  # local t and not account for scr refresh
        image_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_25, 'tStartRefresh')  # time at next scr refresh
        image_25.setAutoDraw(True)
    if image_25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_25.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_25.tStop = t  # not accounting for scr refresh
            image_25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_25, 'tStopRefresh')  # time at next scr refresh
            image_25.setAutoDraw(False)
    
    # *image_35* updates
    if image_35.status == NOT_STARTED and tThisFlip >= 708.1-frameTolerance:
        # keep track of start time/frame for later
        image_35.frameNStart = frameN  # exact frame index
        image_35.tStart = t  # local t and not account for scr refresh
        image_35.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_35, 'tStartRefresh')  # time at next scr refresh
        image_35.setAutoDraw(True)
    if image_35.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_35.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_35.tStop = t  # not accounting for scr refresh
            image_35.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_35, 'tStopRefresh')  # time at next scr refresh
            image_35.setAutoDraw(False)
    
    # *image_38* updates
    if image_38.status == NOT_STARTED and tThisFlip >= 708.4-frameTolerance:
        # keep track of start time/frame for later
        image_38.frameNStart = frameN  # exact frame index
        image_38.tStart = t  # local t and not account for scr refresh
        image_38.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_38, 'tStartRefresh')  # time at next scr refresh
        image_38.setAutoDraw(True)
    if image_38.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_38.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            image_38.tStop = t  # not accounting for scr refresh
            image_38.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_38, 'tStopRefresh')  # time at next scr refresh
            image_38.setAutoDraw(False)
    
    # *image_39* updates
    if image_39.status == NOT_STARTED and tThisFlip >= 709-frameTolerance:
        # keep track of start time/frame for later
        image_39.frameNStart = frameN  # exact frame index
        image_39.tStart = t  # local t and not account for scr refresh
        image_39.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_39, 'tStartRefresh')  # time at next scr refresh
        image_39.setAutoDraw(True)
    if image_39.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_39.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_39.tStop = t  # not accounting for scr refresh
            image_39.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_39, 'tStopRefresh')  # time at next scr refresh
            image_39.setAutoDraw(False)
    
    # *image_40* updates
    if image_40.status == NOT_STARTED and tThisFlip >= 709.5-frameTolerance:
        # keep track of start time/frame for later
        image_40.frameNStart = frameN  # exact frame index
        image_40.tStart = t  # local t and not account for scr refresh
        image_40.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_40, 'tStartRefresh')  # time at next scr refresh
        image_40.setAutoDraw(True)
    if image_40.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_40.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_40.tStop = t  # not accounting for scr refresh
            image_40.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_40, 'tStopRefresh')  # time at next scr refresh
            image_40.setAutoDraw(False)
    
    # *slider_5* updates
    if slider_5.status == NOT_STARTED and tThisFlip >= 709.9-frameTolerance:
        # keep track of start time/frame for later
        slider_5.frameNStart = frameN  # exact frame index
        slider_5.tStart = t  # local t and not account for scr refresh
        slider_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_5, 'tStartRefresh')  # time at next scr refresh
        slider_5.setAutoDraw(True)
    if slider_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_5.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_5.tStop = t  # not accounting for scr refresh
            slider_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_5, 'tStopRefresh')  # time at next scr refresh
            slider_5.setAutoDraw(False)
    
    # *C7* updates
    if C7.status == NOT_STARTED and tThisFlip >= 711.8-frameTolerance:
        # keep track of start time/frame for later
        C7.frameNStart = frameN  # exact frame index
        C7.tStart = t  # local t and not account for scr refresh
        C7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C7, 'tStartRefresh')  # time at next scr refresh
        C7.setAutoDraw(True)
    if C7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C7.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C7.tStop = t  # not accounting for scr refresh
            C7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C7, 'tStopRefresh')  # time at next scr refresh
            C7.setAutoDraw(False)
    
    # *text_51* updates
    if text_51.status == NOT_STARTED and tThisFlip >= 711.8-frameTolerance:
        # keep track of start time/frame for later
        text_51.frameNStart = frameN  # exact frame index
        text_51.tStart = t  # local t and not account for scr refresh
        text_51.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_51, 'tStartRefresh')  # time at next scr refresh
        text_51.setAutoDraw(True)
    if text_51.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_51.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_51.tStop = t  # not accounting for scr refresh
            text_51.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_51, 'tStopRefresh')  # time at next scr refresh
            text_51.setAutoDraw(False)
    
    # *image_41* updates
    if image_41.status == NOT_STARTED and tThisFlip >= 713.1-frameTolerance:
        # keep track of start time/frame for later
        image_41.frameNStart = frameN  # exact frame index
        image_41.tStart = t  # local t and not account for scr refresh
        image_41.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_41, 'tStartRefresh')  # time at next scr refresh
        image_41.setAutoDraw(True)
    if image_41.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_41.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_41.tStop = t  # not accounting for scr refresh
            image_41.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_41, 'tStopRefresh')  # time at next scr refresh
            image_41.setAutoDraw(False)
    
    # *image_42* updates
    if image_42.status == NOT_STARTED and tThisFlip >= 713.3-frameTolerance:
        # keep track of start time/frame for later
        image_42.frameNStart = frameN  # exact frame index
        image_42.tStart = t  # local t and not account for scr refresh
        image_42.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_42, 'tStartRefresh')  # time at next scr refresh
        image_42.setAutoDraw(True)
    if image_42.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_42.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_42.tStop = t  # not accounting for scr refresh
            image_42.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_42, 'tStopRefresh')  # time at next scr refresh
            image_42.setAutoDraw(False)
    
    # *image_43* updates
    if image_43.status == NOT_STARTED and tThisFlip >= 713.6-frameTolerance:
        # keep track of start time/frame for later
        image_43.frameNStart = frameN  # exact frame index
        image_43.tStart = t  # local t and not account for scr refresh
        image_43.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_43, 'tStartRefresh')  # time at next scr refresh
        image_43.setAutoDraw(True)
    if image_43.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_43.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_43.tStop = t  # not accounting for scr refresh
            image_43.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_43, 'tStopRefresh')  # time at next scr refresh
            image_43.setAutoDraw(False)
    
    # *image_44* updates
    if image_44.status == NOT_STARTED and tThisFlip >= 713.8-frameTolerance:
        # keep track of start time/frame for later
        image_44.frameNStart = frameN  # exact frame index
        image_44.tStart = t  # local t and not account for scr refresh
        image_44.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_44, 'tStartRefresh')  # time at next scr refresh
        image_44.setAutoDraw(True)
    if image_44.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_44.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            image_44.tStop = t  # not accounting for scr refresh
            image_44.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_44, 'tStopRefresh')  # time at next scr refresh
            image_44.setAutoDraw(False)
    
    # *image_45* updates
    if image_45.status == NOT_STARTED and tThisFlip >= 714.4-frameTolerance:
        # keep track of start time/frame for later
        image_45.frameNStart = frameN  # exact frame index
        image_45.tStart = t  # local t and not account for scr refresh
        image_45.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_45, 'tStartRefresh')  # time at next scr refresh
        image_45.setAutoDraw(True)
    if image_45.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_45.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_45.tStop = t  # not accounting for scr refresh
            image_45.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_45, 'tStopRefresh')  # time at next scr refresh
            image_45.setAutoDraw(False)
    
    # *image_46* updates
    if image_46.status == NOT_STARTED and tThisFlip >= 714.7-frameTolerance:
        # keep track of start time/frame for later
        image_46.frameNStart = frameN  # exact frame index
        image_46.tStart = t  # local t and not account for scr refresh
        image_46.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_46, 'tStartRefresh')  # time at next scr refresh
        image_46.setAutoDraw(True)
    if image_46.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_46.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_46.tStop = t  # not accounting for scr refresh
            image_46.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_46, 'tStopRefresh')  # time at next scr refresh
            image_46.setAutoDraw(False)
    
    # *image_47* updates
    if image_47.status == NOT_STARTED and tThisFlip >= 715.1-frameTolerance:
        # keep track of start time/frame for later
        image_47.frameNStart = frameN  # exact frame index
        image_47.tStart = t  # local t and not account for scr refresh
        image_47.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_47, 'tStartRefresh')  # time at next scr refresh
        image_47.setAutoDraw(True)
    if image_47.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_47.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_47.tStop = t  # not accounting for scr refresh
            image_47.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_47, 'tStopRefresh')  # time at next scr refresh
            image_47.setAutoDraw(False)
    
    # *image_48* updates
    if image_48.status == NOT_STARTED and tThisFlip >= 715.5-frameTolerance:
        # keep track of start time/frame for later
        image_48.frameNStart = frameN  # exact frame index
        image_48.tStart = t  # local t and not account for scr refresh
        image_48.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_48, 'tStartRefresh')  # time at next scr refresh
        image_48.setAutoDraw(True)
    if image_48.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_48.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_48.tStop = t  # not accounting for scr refresh
            image_48.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_48, 'tStopRefresh')  # time at next scr refresh
            image_48.setAutoDraw(False)
    
    # *image_49* updates
    if image_49.status == NOT_STARTED and tThisFlip >= 715.8-frameTolerance:
        # keep track of start time/frame for later
        image_49.frameNStart = frameN  # exact frame index
        image_49.tStart = t  # local t and not account for scr refresh
        image_49.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_49, 'tStartRefresh')  # time at next scr refresh
        image_49.setAutoDraw(True)
    if image_49.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_49.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_49.tStop = t  # not accounting for scr refresh
            image_49.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_49, 'tStopRefresh')  # time at next scr refresh
            image_49.setAutoDraw(False)
    
    # *slider_6* updates
    if slider_6.status == NOT_STARTED and tThisFlip >= 716.2-frameTolerance:
        # keep track of start time/frame for later
        slider_6.frameNStart = frameN  # exact frame index
        slider_6.tStart = t  # local t and not account for scr refresh
        slider_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_6, 'tStartRefresh')  # time at next scr refresh
        slider_6.setAutoDraw(True)
    if slider_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_6.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_6.tStop = t  # not accounting for scr refresh
            slider_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_6, 'tStopRefresh')  # time at next scr refresh
            slider_6.setAutoDraw(False)
    
    # *C8* updates
    if C8.status == NOT_STARTED and tThisFlip >= 718.1-frameTolerance:
        # keep track of start time/frame for later
        C8.frameNStart = frameN  # exact frame index
        C8.tStart = t  # local t and not account for scr refresh
        C8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C8, 'tStartRefresh')  # time at next scr refresh
        C8.setAutoDraw(True)
    if C8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C8.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C8.tStop = t  # not accounting for scr refresh
            C8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C8, 'tStopRefresh')  # time at next scr refresh
            C8.setAutoDraw(False)
    
    # *text_52* updates
    if text_52.status == NOT_STARTED and tThisFlip >= 718.1-frameTolerance:
        # keep track of start time/frame for later
        text_52.frameNStart = frameN  # exact frame index
        text_52.tStart = t  # local t and not account for scr refresh
        text_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        text_52.setAutoDraw(True)
    if text_52.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_52.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_52.tStop = t  # not accounting for scr refresh
            text_52.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_52, 'tStopRefresh')  # time at next scr refresh
            text_52.setAutoDraw(False)
    
    # *image_50* updates
    if image_50.status == NOT_STARTED and tThisFlip >= 719.4-frameTolerance:
        # keep track of start time/frame for later
        image_50.frameNStart = frameN  # exact frame index
        image_50.tStart = t  # local t and not account for scr refresh
        image_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_50, 'tStartRefresh')  # time at next scr refresh
        image_50.setAutoDraw(True)
    if image_50.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_50.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            image_50.tStop = t  # not accounting for scr refresh
            image_50.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_50, 'tStopRefresh')  # time at next scr refresh
            image_50.setAutoDraw(False)
    
    # *image_51* updates
    if image_51.status == NOT_STARTED and tThisFlip >= 720-frameTolerance:
        # keep track of start time/frame for later
        image_51.frameNStart = frameN  # exact frame index
        image_51.tStart = t  # local t and not account for scr refresh
        image_51.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_51, 'tStartRefresh')  # time at next scr refresh
        image_51.setAutoDraw(True)
    if image_51.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_51.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_51.tStop = t  # not accounting for scr refresh
            image_51.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_51, 'tStopRefresh')  # time at next scr refresh
            image_51.setAutoDraw(False)
    
    # *image_52* updates
    if image_52.status == NOT_STARTED and tThisFlip >= 720.4-frameTolerance:
        # keep track of start time/frame for later
        image_52.frameNStart = frameN  # exact frame index
        image_52.tStart = t  # local t and not account for scr refresh
        image_52.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_52, 'tStartRefresh')  # time at next scr refresh
        image_52.setAutoDraw(True)
    if image_52.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_52.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            image_52.tStop = t  # not accounting for scr refresh
            image_52.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_52, 'tStopRefresh')  # time at next scr refresh
            image_52.setAutoDraw(False)
    
    # *image_53* updates
    if image_53.status == NOT_STARTED and tThisFlip >= 721-frameTolerance:
        # keep track of start time/frame for later
        image_53.frameNStart = frameN  # exact frame index
        image_53.tStart = t  # local t and not account for scr refresh
        image_53.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_53, 'tStartRefresh')  # time at next scr refresh
        image_53.setAutoDraw(True)
    if image_53.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_53.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_53.tStop = t  # not accounting for scr refresh
            image_53.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_53, 'tStopRefresh')  # time at next scr refresh
            image_53.setAutoDraw(False)
    
    # *image_54* updates
    if image_54.status == NOT_STARTED and tThisFlip >= 721.3-frameTolerance:
        # keep track of start time/frame for later
        image_54.frameNStart = frameN  # exact frame index
        image_54.tStart = t  # local t and not account for scr refresh
        image_54.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_54, 'tStartRefresh')  # time at next scr refresh
        image_54.setAutoDraw(True)
    if image_54.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_54.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_54.tStop = t  # not accounting for scr refresh
            image_54.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_54, 'tStopRefresh')  # time at next scr refresh
            image_54.setAutoDraw(False)
    
    # *image_55* updates
    if image_55.status == NOT_STARTED and tThisFlip >= 721.8-frameTolerance:
        # keep track of start time/frame for later
        image_55.frameNStart = frameN  # exact frame index
        image_55.tStart = t  # local t and not account for scr refresh
        image_55.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_55, 'tStartRefresh')  # time at next scr refresh
        image_55.setAutoDraw(True)
    if image_55.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_55.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_55.tStop = t  # not accounting for scr refresh
            image_55.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_55, 'tStopRefresh')  # time at next scr refresh
            image_55.setAutoDraw(False)
    
    # *image_56* updates
    if image_56.status == NOT_STARTED and tThisFlip >= 722.3-frameTolerance:
        # keep track of start time/frame for later
        image_56.frameNStart = frameN  # exact frame index
        image_56.tStart = t  # local t and not account for scr refresh
        image_56.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_56, 'tStartRefresh')  # time at next scr refresh
        image_56.setAutoDraw(True)
    if image_56.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_56.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_56.tStop = t  # not accounting for scr refresh
            image_56.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_56, 'tStopRefresh')  # time at next scr refresh
            image_56.setAutoDraw(False)
    
    # *slider_7* updates
    if slider_7.status == NOT_STARTED and tThisFlip >= 722.5-frameTolerance:
        # keep track of start time/frame for later
        slider_7.frameNStart = frameN  # exact frame index
        slider_7.tStart = t  # local t and not account for scr refresh
        slider_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_7, 'tStartRefresh')  # time at next scr refresh
        slider_7.setAutoDraw(True)
    if slider_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_7.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_7.tStop = t  # not accounting for scr refresh
            slider_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_7, 'tStopRefresh')  # time at next scr refresh
            slider_7.setAutoDraw(False)
    
    # *C9* updates
    if C9.status == NOT_STARTED and tThisFlip >= 724.4-frameTolerance:
        # keep track of start time/frame for later
        C9.frameNStart = frameN  # exact frame index
        C9.tStart = t  # local t and not account for scr refresh
        C9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C9, 'tStartRefresh')  # time at next scr refresh
        C9.setAutoDraw(True)
    if C9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C9.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C9.tStop = t  # not accounting for scr refresh
            C9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C9, 'tStopRefresh')  # time at next scr refresh
            C9.setAutoDraw(False)
    
    # *text_53* updates
    if text_53.status == NOT_STARTED and tThisFlip >= 724.4-frameTolerance:
        # keep track of start time/frame for later
        text_53.frameNStart = frameN  # exact frame index
        text_53.tStart = t  # local t and not account for scr refresh
        text_53.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_53, 'tStartRefresh')  # time at next scr refresh
        text_53.setAutoDraw(True)
    if text_53.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_53.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_53.tStop = t  # not accounting for scr refresh
            text_53.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_53, 'tStopRefresh')  # time at next scr refresh
            text_53.setAutoDraw(False)
    
    # *image_57* updates
    if image_57.status == NOT_STARTED and tThisFlip >= 725.7-frameTolerance:
        # keep track of start time/frame for later
        image_57.frameNStart = frameN  # exact frame index
        image_57.tStart = t  # local t and not account for scr refresh
        image_57.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_57, 'tStartRefresh')  # time at next scr refresh
        image_57.setAutoDraw(True)
    if image_57.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_57.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_57.tStop = t  # not accounting for scr refresh
            image_57.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_57, 'tStopRefresh')  # time at next scr refresh
            image_57.setAutoDraw(False)
    
    # *image_58* updates
    if image_58.status == NOT_STARTED and tThisFlip >= 726.1-frameTolerance:
        # keep track of start time/frame for later
        image_58.frameNStart = frameN  # exact frame index
        image_58.tStart = t  # local t and not account for scr refresh
        image_58.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_58, 'tStartRefresh')  # time at next scr refresh
        image_58.setAutoDraw(True)
    if image_58.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_58.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_58.tStop = t  # not accounting for scr refresh
            image_58.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_58, 'tStopRefresh')  # time at next scr refresh
            image_58.setAutoDraw(False)
    
    # *image_59* updates
    if image_59.status == NOT_STARTED and tThisFlip >= 726.3-frameTolerance:
        # keep track of start time/frame for later
        image_59.frameNStart = frameN  # exact frame index
        image_59.tStart = t  # local t and not account for scr refresh
        image_59.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_59, 'tStartRefresh')  # time at next scr refresh
        image_59.setAutoDraw(True)
    if image_59.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_59.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_59.tStop = t  # not accounting for scr refresh
            image_59.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_59, 'tStopRefresh')  # time at next scr refresh
            image_59.setAutoDraw(False)
    
    # *image_60* updates
    if image_60.status == NOT_STARTED and tThisFlip >= 726.5-frameTolerance:
        # keep track of start time/frame for later
        image_60.frameNStart = frameN  # exact frame index
        image_60.tStart = t  # local t and not account for scr refresh
        image_60.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_60, 'tStartRefresh')  # time at next scr refresh
        image_60.setAutoDraw(True)
    if image_60.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_60.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_60.tStop = t  # not accounting for scr refresh
            image_60.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_60, 'tStopRefresh')  # time at next scr refresh
            image_60.setAutoDraw(False)
    
    # *image_61* updates
    if image_61.status == NOT_STARTED and tThisFlip >= 726.8-frameTolerance:
        # keep track of start time/frame for later
        image_61.frameNStart = frameN  # exact frame index
        image_61.tStart = t  # local t and not account for scr refresh
        image_61.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_61, 'tStartRefresh')  # time at next scr refresh
        image_61.setAutoDraw(True)
    if image_61.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_61.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_61.tStop = t  # not accounting for scr refresh
            image_61.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_61, 'tStopRefresh')  # time at next scr refresh
            image_61.setAutoDraw(False)
    
    # *image_62* updates
    if image_62.status == NOT_STARTED and tThisFlip >= 727.1-frameTolerance:
        # keep track of start time/frame for later
        image_62.frameNStart = frameN  # exact frame index
        image_62.tStart = t  # local t and not account for scr refresh
        image_62.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_62, 'tStartRefresh')  # time at next scr refresh
        image_62.setAutoDraw(True)
    if image_62.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_62.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_62.tStop = t  # not accounting for scr refresh
            image_62.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_62, 'tStopRefresh')  # time at next scr refresh
            image_62.setAutoDraw(False)
    
    # *image_63* updates
    if image_63.status == NOT_STARTED and tThisFlip >= 727.4-frameTolerance:
        # keep track of start time/frame for later
        image_63.frameNStart = frameN  # exact frame index
        image_63.tStart = t  # local t and not account for scr refresh
        image_63.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_63, 'tStartRefresh')  # time at next scr refresh
        image_63.setAutoDraw(True)
    if image_63.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_63.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_63.tStop = t  # not accounting for scr refresh
            image_63.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_63, 'tStopRefresh')  # time at next scr refresh
            image_63.setAutoDraw(False)
    
    # *image_64* updates
    if image_64.status == NOT_STARTED and tThisFlip >= 727.8-frameTolerance:
        # keep track of start time/frame for later
        image_64.frameNStart = frameN  # exact frame index
        image_64.tStart = t  # local t and not account for scr refresh
        image_64.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_64, 'tStartRefresh')  # time at next scr refresh
        image_64.setAutoDraw(True)
    if image_64.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_64.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_64.tStop = t  # not accounting for scr refresh
            image_64.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_64, 'tStopRefresh')  # time at next scr refresh
            image_64.setAutoDraw(False)
    
    # *image_65* updates
    if image_65.status == NOT_STARTED and tThisFlip >= 728.1-frameTolerance:
        # keep track of start time/frame for later
        image_65.frameNStart = frameN  # exact frame index
        image_65.tStart = t  # local t and not account for scr refresh
        image_65.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_65, 'tStartRefresh')  # time at next scr refresh
        image_65.setAutoDraw(True)
    if image_65.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_65.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_65.tStop = t  # not accounting for scr refresh
            image_65.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_65, 'tStopRefresh')  # time at next scr refresh
            image_65.setAutoDraw(False)
    
    # *image_66* updates
    if image_66.status == NOT_STARTED and tThisFlip >= 728.4-frameTolerance:
        # keep track of start time/frame for later
        image_66.frameNStart = frameN  # exact frame index
        image_66.tStart = t  # local t and not account for scr refresh
        image_66.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_66, 'tStartRefresh')  # time at next scr refresh
        image_66.setAutoDraw(True)
    if image_66.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_66.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_66.tStop = t  # not accounting for scr refresh
            image_66.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_66, 'tStopRefresh')  # time at next scr refresh
            image_66.setAutoDraw(False)
    
    # *image_67* updates
    if image_67.status == NOT_STARTED and tThisFlip >= 728.6-frameTolerance:
        # keep track of start time/frame for later
        image_67.frameNStart = frameN  # exact frame index
        image_67.tStart = t  # local t and not account for scr refresh
        image_67.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_67, 'tStartRefresh')  # time at next scr refresh
        image_67.setAutoDraw(True)
    if image_67.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_67.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_67.tStop = t  # not accounting for scr refresh
            image_67.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_67, 'tStopRefresh')  # time at next scr refresh
            image_67.setAutoDraw(False)
    
    # *slider_8* updates
    if slider_8.status == NOT_STARTED and tThisFlip >= 728.8-frameTolerance:
        # keep track of start time/frame for later
        slider_8.frameNStart = frameN  # exact frame index
        slider_8.tStart = t  # local t and not account for scr refresh
        slider_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_8, 'tStartRefresh')  # time at next scr refresh
        slider_8.setAutoDraw(True)
    if slider_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_8.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_8.tStop = t  # not accounting for scr refresh
            slider_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_8, 'tStopRefresh')  # time at next scr refresh
            slider_8.setAutoDraw(False)
    
    # *C10* updates
    if C10.status == NOT_STARTED and tThisFlip >= 730.7-frameTolerance:
        # keep track of start time/frame for later
        C10.frameNStart = frameN  # exact frame index
        C10.tStart = t  # local t and not account for scr refresh
        C10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C10, 'tStartRefresh')  # time at next scr refresh
        C10.setAutoDraw(True)
    if C10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C10.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C10.tStop = t  # not accounting for scr refresh
            C10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C10, 'tStopRefresh')  # time at next scr refresh
            C10.setAutoDraw(False)
    
    # *text_54* updates
    if text_54.status == NOT_STARTED and tThisFlip >= 730.7-frameTolerance:
        # keep track of start time/frame for later
        text_54.frameNStart = frameN  # exact frame index
        text_54.tStart = t  # local t and not account for scr refresh
        text_54.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_54, 'tStartRefresh')  # time at next scr refresh
        text_54.setAutoDraw(True)
    if text_54.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_54.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_54.tStop = t  # not accounting for scr refresh
            text_54.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_54, 'tStopRefresh')  # time at next scr refresh
            text_54.setAutoDraw(False)
    
    # *image_68* updates
    if image_68.status == NOT_STARTED and tThisFlip >= 732-frameTolerance:
        # keep track of start time/frame for later
        image_68.frameNStart = frameN  # exact frame index
        image_68.tStart = t  # local t and not account for scr refresh
        image_68.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_68, 'tStartRefresh')  # time at next scr refresh
        image_68.setAutoDraw(True)
    if image_68.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_68.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_68.tStop = t  # not accounting for scr refresh
            image_68.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_68, 'tStopRefresh')  # time at next scr refresh
            image_68.setAutoDraw(False)
    
    # *image_69* updates
    if image_69.status == NOT_STARTED and tThisFlip >= 732.4-frameTolerance:
        # keep track of start time/frame for later
        image_69.frameNStart = frameN  # exact frame index
        image_69.tStart = t  # local t and not account for scr refresh
        image_69.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_69, 'tStartRefresh')  # time at next scr refresh
        image_69.setAutoDraw(True)
    if image_69.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_69.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_69.tStop = t  # not accounting for scr refresh
            image_69.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_69, 'tStopRefresh')  # time at next scr refresh
            image_69.setAutoDraw(False)
    
    # *image_70* updates
    if image_70.status == NOT_STARTED and tThisFlip >= 732.9-frameTolerance:
        # keep track of start time/frame for later
        image_70.frameNStart = frameN  # exact frame index
        image_70.tStart = t  # local t and not account for scr refresh
        image_70.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_70, 'tStartRefresh')  # time at next scr refresh
        image_70.setAutoDraw(True)
    if image_70.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_70.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_70.tStop = t  # not accounting for scr refresh
            image_70.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_70, 'tStopRefresh')  # time at next scr refresh
            image_70.setAutoDraw(False)
    
    # *image_71* updates
    if image_71.status == NOT_STARTED and tThisFlip >= 733.4-frameTolerance:
        # keep track of start time/frame for later
        image_71.frameNStart = frameN  # exact frame index
        image_71.tStart = t  # local t and not account for scr refresh
        image_71.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_71, 'tStartRefresh')  # time at next scr refresh
        image_71.setAutoDraw(True)
    if image_71.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_71.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            image_71.tStop = t  # not accounting for scr refresh
            image_71.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_71, 'tStopRefresh')  # time at next scr refresh
            image_71.setAutoDraw(False)
    
    # *image_72* updates
    if image_72.status == NOT_STARTED and tThisFlip >= 734-frameTolerance:
        # keep track of start time/frame for later
        image_72.frameNStart = frameN  # exact frame index
        image_72.tStart = t  # local t and not account for scr refresh
        image_72.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_72, 'tStartRefresh')  # time at next scr refresh
        image_72.setAutoDraw(True)
    if image_72.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_72.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_72.tStop = t  # not accounting for scr refresh
            image_72.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_72, 'tStopRefresh')  # time at next scr refresh
            image_72.setAutoDraw(False)
    
    # *image_73* updates
    if image_73.status == NOT_STARTED and tThisFlip >= 734.5-frameTolerance:
        # keep track of start time/frame for later
        image_73.frameNStart = frameN  # exact frame index
        image_73.tStart = t  # local t and not account for scr refresh
        image_73.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_73, 'tStartRefresh')  # time at next scr refresh
        image_73.setAutoDraw(True)
    if image_73.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_73.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            image_73.tStop = t  # not accounting for scr refresh
            image_73.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_73, 'tStopRefresh')  # time at next scr refresh
            image_73.setAutoDraw(False)
    
    # *slider_9* updates
    if slider_9.status == NOT_STARTED and tThisFlip >= 735.1-frameTolerance:
        # keep track of start time/frame for later
        slider_9.frameNStart = frameN  # exact frame index
        slider_9.tStart = t  # local t and not account for scr refresh
        slider_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_9, 'tStartRefresh')  # time at next scr refresh
        slider_9.setAutoDraw(True)
    if slider_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_9.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_9.tStop = t  # not accounting for scr refresh
            slider_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_9, 'tStopRefresh')  # time at next scr refresh
            slider_9.setAutoDraw(False)
    
    # *C11* updates
    if C11.status == NOT_STARTED and tThisFlip >= 737-frameTolerance:
        # keep track of start time/frame for later
        C11.frameNStart = frameN  # exact frame index
        C11.tStart = t  # local t and not account for scr refresh
        C11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C11, 'tStartRefresh')  # time at next scr refresh
        C11.setAutoDraw(True)
    if C11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C11.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C11.tStop = t  # not accounting for scr refresh
            C11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C11, 'tStopRefresh')  # time at next scr refresh
            C11.setAutoDraw(False)
    
    # *text_55* updates
    if text_55.status == NOT_STARTED and tThisFlip >= 737-frameTolerance:
        # keep track of start time/frame for later
        text_55.frameNStart = frameN  # exact frame index
        text_55.tStart = t  # local t and not account for scr refresh
        text_55.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_55, 'tStartRefresh')  # time at next scr refresh
        text_55.setAutoDraw(True)
    if text_55.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_55.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_55.tStop = t  # not accounting for scr refresh
            text_55.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_55, 'tStopRefresh')  # time at next scr refresh
            text_55.setAutoDraw(False)
    
    # *image_74* updates
    if image_74.status == NOT_STARTED and tThisFlip >= 738.3-frameTolerance:
        # keep track of start time/frame for later
        image_74.frameNStart = frameN  # exact frame index
        image_74.tStart = t  # local t and not account for scr refresh
        image_74.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_74, 'tStartRefresh')  # time at next scr refresh
        image_74.setAutoDraw(True)
    if image_74.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_74.tStartRefresh + .7-frameTolerance:
            # keep track of stop time/frame for later
            image_74.tStop = t  # not accounting for scr refresh
            image_74.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_74, 'tStopRefresh')  # time at next scr refresh
            image_74.setAutoDraw(False)
    
    # *image_75* updates
    if image_75.status == NOT_STARTED and tThisFlip >= 739.1-frameTolerance:
        # keep track of start time/frame for later
        image_75.frameNStart = frameN  # exact frame index
        image_75.tStart = t  # local t and not account for scr refresh
        image_75.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_75, 'tStartRefresh')  # time at next scr refresh
        image_75.setAutoDraw(True)
    if image_75.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_75.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_75.tStop = t  # not accounting for scr refresh
            image_75.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_75, 'tStopRefresh')  # time at next scr refresh
            image_75.setAutoDraw(False)
    
    # *image_76* updates
    if image_76.status == NOT_STARTED and tThisFlip >= 739.6-frameTolerance:
        # keep track of start time/frame for later
        image_76.frameNStart = frameN  # exact frame index
        image_76.tStart = t  # local t and not account for scr refresh
        image_76.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_76, 'tStartRefresh')  # time at next scr refresh
        image_76.setAutoDraw(True)
    if image_76.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_76.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_76.tStop = t  # not accounting for scr refresh
            image_76.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_76, 'tStopRefresh')  # time at next scr refresh
            image_76.setAutoDraw(False)
    
    # *image_77* updates
    if image_77.status == NOT_STARTED and tThisFlip >= 740.1-frameTolerance:
        # keep track of start time/frame for later
        image_77.frameNStart = frameN  # exact frame index
        image_77.tStart = t  # local t and not account for scr refresh
        image_77.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_77, 'tStartRefresh')  # time at next scr refresh
        image_77.setAutoDraw(True)
    if image_77.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_77.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_77.tStop = t  # not accounting for scr refresh
            image_77.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_77, 'tStopRefresh')  # time at next scr refresh
            image_77.setAutoDraw(False)
    
    # *image_78* updates
    if image_78.status == NOT_STARTED and tThisFlip >= 740.6-frameTolerance:
        # keep track of start time/frame for later
        image_78.frameNStart = frameN  # exact frame index
        image_78.tStart = t  # local t and not account for scr refresh
        image_78.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_78, 'tStartRefresh')  # time at next scr refresh
        image_78.setAutoDraw(True)
    if image_78.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_78.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_78.tStop = t  # not accounting for scr refresh
            image_78.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_78, 'tStopRefresh')  # time at next scr refresh
            image_78.setAutoDraw(False)
    
    # *image_79* updates
    if image_79.status == NOT_STARTED and tThisFlip >= 741.1-frameTolerance:
        # keep track of start time/frame for later
        image_79.frameNStart = frameN  # exact frame index
        image_79.tStart = t  # local t and not account for scr refresh
        image_79.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_79, 'tStartRefresh')  # time at next scr refresh
        image_79.setAutoDraw(True)
    if image_79.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_79.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_79.tStop = t  # not accounting for scr refresh
            image_79.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_79, 'tStopRefresh')  # time at next scr refresh
            image_79.setAutoDraw(False)
    
    # *slider_10* updates
    if slider_10.status == NOT_STARTED and tThisFlip >= 741.4-frameTolerance:
        # keep track of start time/frame for later
        slider_10.frameNStart = frameN  # exact frame index
        slider_10.tStart = t  # local t and not account for scr refresh
        slider_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_10, 'tStartRefresh')  # time at next scr refresh
        slider_10.setAutoDraw(True)
    if slider_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_10.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_10.tStop = t  # not accounting for scr refresh
            slider_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_10, 'tStopRefresh')  # time at next scr refresh
            slider_10.setAutoDraw(False)
    
    # *C12* updates
    if C12.status == NOT_STARTED and tThisFlip >= 743.3-frameTolerance:
        # keep track of start time/frame for later
        C12.frameNStart = frameN  # exact frame index
        C12.tStart = t  # local t and not account for scr refresh
        C12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C12, 'tStartRefresh')  # time at next scr refresh
        C12.setAutoDraw(True)
    if C12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C12.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C12.tStop = t  # not accounting for scr refresh
            C12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C12, 'tStopRefresh')  # time at next scr refresh
            C12.setAutoDraw(False)
    
    # *text_56* updates
    if text_56.status == NOT_STARTED and tThisFlip >= 743.3-frameTolerance:
        # keep track of start time/frame for later
        text_56.frameNStart = frameN  # exact frame index
        text_56.tStart = t  # local t and not account for scr refresh
        text_56.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_56, 'tStartRefresh')  # time at next scr refresh
        text_56.setAutoDraw(True)
    if text_56.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_56.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_56.tStop = t  # not accounting for scr refresh
            text_56.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_56, 'tStopRefresh')  # time at next scr refresh
            text_56.setAutoDraw(False)
    
    # *image_80* updates
    if image_80.status == NOT_STARTED and tThisFlip >= 744.6-frameTolerance:
        # keep track of start time/frame for later
        image_80.frameNStart = frameN  # exact frame index
        image_80.tStart = t  # local t and not account for scr refresh
        image_80.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_80, 'tStartRefresh')  # time at next scr refresh
        image_80.setAutoDraw(True)
    if image_80.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_80.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_80.tStop = t  # not accounting for scr refresh
            image_80.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_80, 'tStopRefresh')  # time at next scr refresh
            image_80.setAutoDraw(False)
    
    # *image_81* updates
    if image_81.status == NOT_STARTED and tThisFlip >= 745.1-frameTolerance:
        # keep track of start time/frame for later
        image_81.frameNStart = frameN  # exact frame index
        image_81.tStart = t  # local t and not account for scr refresh
        image_81.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_81, 'tStartRefresh')  # time at next scr refresh
        image_81.setAutoDraw(True)
    if image_81.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_81.tStartRefresh + .7-frameTolerance:
            # keep track of stop time/frame for later
            image_81.tStop = t  # not accounting for scr refresh
            image_81.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_81, 'tStopRefresh')  # time at next scr refresh
            image_81.setAutoDraw(False)
    
    # *image_82* updates
    if image_82.status == NOT_STARTED and tThisFlip >= 745.9-frameTolerance:
        # keep track of start time/frame for later
        image_82.frameNStart = frameN  # exact frame index
        image_82.tStart = t  # local t and not account for scr refresh
        image_82.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_82, 'tStartRefresh')  # time at next scr refresh
        image_82.setAutoDraw(True)
    if image_82.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_82.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_82.tStop = t  # not accounting for scr refresh
            image_82.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_82, 'tStopRefresh')  # time at next scr refresh
            image_82.setAutoDraw(False)
    
    # *image_83* updates
    if image_83.status == NOT_STARTED and tThisFlip >= 746.4-frameTolerance:
        # keep track of start time/frame for later
        image_83.frameNStart = frameN  # exact frame index
        image_83.tStart = t  # local t and not account for scr refresh
        image_83.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_83, 'tStartRefresh')  # time at next scr refresh
        image_83.setAutoDraw(True)
    if image_83.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_83.tStartRefresh + .6-frameTolerance:
            # keep track of stop time/frame for later
            image_83.tStop = t  # not accounting for scr refresh
            image_83.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_83, 'tStopRefresh')  # time at next scr refresh
            image_83.setAutoDraw(False)
    
    # *image_84* updates
    if image_84.status == NOT_STARTED and tThisFlip >= 747.1-frameTolerance:
        # keep track of start time/frame for later
        image_84.frameNStart = frameN  # exact frame index
        image_84.tStart = t  # local t and not account for scr refresh
        image_84.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_84, 'tStartRefresh')  # time at next scr refresh
        image_84.setAutoDraw(True)
    if image_84.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_84.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_84.tStop = t  # not accounting for scr refresh
            image_84.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_84, 'tStopRefresh')  # time at next scr refresh
            image_84.setAutoDraw(False)
    
    # *image_85* updates
    if image_85.status == NOT_STARTED and tThisFlip >= 747.4-frameTolerance:
        # keep track of start time/frame for later
        image_85.frameNStart = frameN  # exact frame index
        image_85.tStart = t  # local t and not account for scr refresh
        image_85.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_85, 'tStartRefresh')  # time at next scr refresh
        image_85.setAutoDraw(True)
    if image_85.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_85.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_85.tStop = t  # not accounting for scr refresh
            image_85.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_85, 'tStopRefresh')  # time at next scr refresh
            image_85.setAutoDraw(False)
    
    # *slider_11* updates
    if slider_11.status == NOT_STARTED and tThisFlip >= 747.7-frameTolerance:
        # keep track of start time/frame for later
        slider_11.frameNStart = frameN  # exact frame index
        slider_11.tStart = t  # local t and not account for scr refresh
        slider_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_11, 'tStartRefresh')  # time at next scr refresh
        slider_11.setAutoDraw(True)
    if slider_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_11.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_11.tStop = t  # not accounting for scr refresh
            slider_11.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_11, 'tStopRefresh')  # time at next scr refresh
            slider_11.setAutoDraw(False)
    
    # *C13* updates
    if C13.status == NOT_STARTED and tThisFlip >= 749.6-frameTolerance:
        # keep track of start time/frame for later
        C13.frameNStart = frameN  # exact frame index
        C13.tStart = t  # local t and not account for scr refresh
        C13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C13, 'tStartRefresh')  # time at next scr refresh
        C13.setAutoDraw(True)
    if C13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C13.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C13.tStop = t  # not accounting for scr refresh
            C13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C13, 'tStopRefresh')  # time at next scr refresh
            C13.setAutoDraw(False)
    
    # *text_57* updates
    if text_57.status == NOT_STARTED and tThisFlip >= 749.6-frameTolerance:
        # keep track of start time/frame for later
        text_57.frameNStart = frameN  # exact frame index
        text_57.tStart = t  # local t and not account for scr refresh
        text_57.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_57, 'tStartRefresh')  # time at next scr refresh
        text_57.setAutoDraw(True)
    if text_57.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_57.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_57.tStop = t  # not accounting for scr refresh
            text_57.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_57, 'tStopRefresh')  # time at next scr refresh
            text_57.setAutoDraw(False)
    
    # *image_86* updates
    if image_86.status == NOT_STARTED and tThisFlip >= 750.9-frameTolerance:
        # keep track of start time/frame for later
        image_86.frameNStart = frameN  # exact frame index
        image_86.tStart = t  # local t and not account for scr refresh
        image_86.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_86, 'tStartRefresh')  # time at next scr refresh
        image_86.setAutoDraw(True)
    if image_86.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_86.tStartRefresh + .7-frameTolerance:
            # keep track of stop time/frame for later
            image_86.tStop = t  # not accounting for scr refresh
            image_86.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_86, 'tStopRefresh')  # time at next scr refresh
            image_86.setAutoDraw(False)
    
    # *image_87* updates
    if image_87.status == NOT_STARTED and tThisFlip >= 751.7-frameTolerance:
        # keep track of start time/frame for later
        image_87.frameNStart = frameN  # exact frame index
        image_87.tStart = t  # local t and not account for scr refresh
        image_87.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_87, 'tStartRefresh')  # time at next scr refresh
        image_87.setAutoDraw(True)
    if image_87.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_87.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_87.tStop = t  # not accounting for scr refresh
            image_87.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_87, 'tStopRefresh')  # time at next scr refresh
            image_87.setAutoDraw(False)
    
    # *image_88* updates
    if image_88.status == NOT_STARTED and tThisFlip >= 752.1-frameTolerance:
        # keep track of start time/frame for later
        image_88.frameNStart = frameN  # exact frame index
        image_88.tStart = t  # local t and not account for scr refresh
        image_88.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_88, 'tStartRefresh')  # time at next scr refresh
        image_88.setAutoDraw(True)
    if image_88.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_88.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_88.tStop = t  # not accounting for scr refresh
            image_88.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_88, 'tStopRefresh')  # time at next scr refresh
            image_88.setAutoDraw(False)
    
    # *image_89* updates
    if image_89.status == NOT_STARTED and tThisFlip >= 752.3-frameTolerance:
        # keep track of start time/frame for later
        image_89.frameNStart = frameN  # exact frame index
        image_89.tStart = t  # local t and not account for scr refresh
        image_89.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_89, 'tStartRefresh')  # time at next scr refresh
        image_89.setAutoDraw(True)
    if image_89.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_89.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_89.tStop = t  # not accounting for scr refresh
            image_89.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_89, 'tStopRefresh')  # time at next scr refresh
            image_89.setAutoDraw(False)
    
    # *image_90* updates
    if image_90.status == NOT_STARTED and tThisFlip >= 752.6-frameTolerance:
        # keep track of start time/frame for later
        image_90.frameNStart = frameN  # exact frame index
        image_90.tStart = t  # local t and not account for scr refresh
        image_90.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_90, 'tStartRefresh')  # time at next scr refresh
        image_90.setAutoDraw(True)
    if image_90.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_90.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_90.tStop = t  # not accounting for scr refresh
            image_90.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_90, 'tStopRefresh')  # time at next scr refresh
            image_90.setAutoDraw(False)
    
    # *image_91* updates
    if image_91.status == NOT_STARTED and tThisFlip >= 753.1-frameTolerance:
        # keep track of start time/frame for later
        image_91.frameNStart = frameN  # exact frame index
        image_91.tStart = t  # local t and not account for scr refresh
        image_91.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_91, 'tStartRefresh')  # time at next scr refresh
        image_91.setAutoDraw(True)
    if image_91.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_91.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_91.tStop = t  # not accounting for scr refresh
            image_91.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_91, 'tStopRefresh')  # time at next scr refresh
            image_91.setAutoDraw(False)
    
    # *image_92* updates
    if image_92.status == NOT_STARTED and tThisFlip >= 753.5-frameTolerance:
        # keep track of start time/frame for later
        image_92.frameNStart = frameN  # exact frame index
        image_92.tStart = t  # local t and not account for scr refresh
        image_92.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_92, 'tStartRefresh')  # time at next scr refresh
        image_92.setAutoDraw(True)
    if image_92.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_92.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_92.tStop = t  # not accounting for scr refresh
            image_92.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_92, 'tStopRefresh')  # time at next scr refresh
            image_92.setAutoDraw(False)
    
    # *slider_12* updates
    if slider_12.status == NOT_STARTED and tThisFlip >= 754-frameTolerance:
        # keep track of start time/frame for later
        slider_12.frameNStart = frameN  # exact frame index
        slider_12.tStart = t  # local t and not account for scr refresh
        slider_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_12, 'tStartRefresh')  # time at next scr refresh
        slider_12.setAutoDraw(True)
    if slider_12.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_12.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_12.tStop = t  # not accounting for scr refresh
            slider_12.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_12, 'tStopRefresh')  # time at next scr refresh
            slider_12.setAutoDraw(False)
    
    # *C14* updates
    if C14.status == NOT_STARTED and tThisFlip >= 755.9-frameTolerance:
        # keep track of start time/frame for later
        C14.frameNStart = frameN  # exact frame index
        C14.tStart = t  # local t and not account for scr refresh
        C14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(C14, 'tStartRefresh')  # time at next scr refresh
        C14.setAutoDraw(True)
    if C14.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > C14.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            C14.tStop = t  # not accounting for scr refresh
            C14.frameNStop = frameN  # exact frame index
            win.timeOnFlip(C14, 'tStopRefresh')  # time at next scr refresh
            C14.setAutoDraw(False)
    
    # *text_58* updates
    if text_58.status == NOT_STARTED and tThisFlip >= 755.9-frameTolerance:
        # keep track of start time/frame for later
        text_58.frameNStart = frameN  # exact frame index
        text_58.tStart = t  # local t and not account for scr refresh
        text_58.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_58, 'tStartRefresh')  # time at next scr refresh
        text_58.setAutoDraw(True)
    if text_58.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_58.tStartRefresh + 1.2-frameTolerance:
            # keep track of stop time/frame for later
            text_58.tStop = t  # not accounting for scr refresh
            text_58.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_58, 'tStopRefresh')  # time at next scr refresh
            text_58.setAutoDraw(False)
    
    # *image_93* updates
    if image_93.status == NOT_STARTED and tThisFlip >= 757.2-frameTolerance:
        # keep track of start time/frame for later
        image_93.frameNStart = frameN  # exact frame index
        image_93.tStart = t  # local t and not account for scr refresh
        image_93.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_93, 'tStartRefresh')  # time at next scr refresh
        image_93.setAutoDraw(True)
    if image_93.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_93.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_93.tStop = t  # not accounting for scr refresh
            image_93.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_93, 'tStopRefresh')  # time at next scr refresh
            image_93.setAutoDraw(False)
    
    # *image_94* updates
    if image_94.status == NOT_STARTED and tThisFlip >= 757.4-frameTolerance:
        # keep track of start time/frame for later
        image_94.frameNStart = frameN  # exact frame index
        image_94.tStart = t  # local t and not account for scr refresh
        image_94.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_94, 'tStartRefresh')  # time at next scr refresh
        image_94.setAutoDraw(True)
    if image_94.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_94.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_94.tStop = t  # not accounting for scr refresh
            image_94.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_94, 'tStopRefresh')  # time at next scr refresh
            image_94.setAutoDraw(False)
    
    # *image_95* updates
    if image_95.status == NOT_STARTED and tThisFlip >= 757.7-frameTolerance:
        # keep track of start time/frame for later
        image_95.frameNStart = frameN  # exact frame index
        image_95.tStart = t  # local t and not account for scr refresh
        image_95.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_95, 'tStartRefresh')  # time at next scr refresh
        image_95.setAutoDraw(True)
    if image_95.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_95.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_95.tStop = t  # not accounting for scr refresh
            image_95.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_95, 'tStopRefresh')  # time at next scr refresh
            image_95.setAutoDraw(False)
    
    # *image_96* updates
    if image_96.status == NOT_STARTED and tThisFlip >= 757.9-frameTolerance:
        # keep track of start time/frame for later
        image_96.frameNStart = frameN  # exact frame index
        image_96.tStart = t  # local t and not account for scr refresh
        image_96.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_96, 'tStartRefresh')  # time at next scr refresh
        image_96.setAutoDraw(True)
    if image_96.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_96.tStartRefresh + .1-frameTolerance:
            # keep track of stop time/frame for later
            image_96.tStop = t  # not accounting for scr refresh
            image_96.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_96, 'tStopRefresh')  # time at next scr refresh
            image_96.setAutoDraw(False)
    
    # *image_97* updates
    if image_97.status == NOT_STARTED and tThisFlip >= 758.1-frameTolerance:
        # keep track of start time/frame for later
        image_97.frameNStart = frameN  # exact frame index
        image_97.tStart = t  # local t and not account for scr refresh
        image_97.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_97, 'tStartRefresh')  # time at next scr refresh
        image_97.setAutoDraw(True)
    if image_97.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_97.tStartRefresh + .2-frameTolerance:
            # keep track of stop time/frame for later
            image_97.tStop = t  # not accounting for scr refresh
            image_97.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_97, 'tStopRefresh')  # time at next scr refresh
            image_97.setAutoDraw(False)
    
    # *image_98* updates
    if image_98.status == NOT_STARTED and tThisFlip >= 758.4-frameTolerance:
        # keep track of start time/frame for later
        image_98.frameNStart = frameN  # exact frame index
        image_98.tStart = t  # local t and not account for scr refresh
        image_98.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_98, 'tStartRefresh')  # time at next scr refresh
        image_98.setAutoDraw(True)
    if image_98.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_98.tStartRefresh + .5-frameTolerance:
            # keep track of stop time/frame for later
            image_98.tStop = t  # not accounting for scr refresh
            image_98.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_98, 'tStopRefresh')  # time at next scr refresh
            image_98.setAutoDraw(False)
    
    # *image_99* updates
    if image_99.status == NOT_STARTED and tThisFlip >= 759-frameTolerance:
        # keep track of start time/frame for later
        image_99.frameNStart = frameN  # exact frame index
        image_99.tStart = t  # local t and not account for scr refresh
        image_99.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_99, 'tStartRefresh')  # time at next scr refresh
        image_99.setAutoDraw(True)
    if image_99.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_99.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_99.tStop = t  # not accounting for scr refresh
            image_99.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_99, 'tStopRefresh')  # time at next scr refresh
            image_99.setAutoDraw(False)
    
    # *image_100* updates
    if image_100.status == NOT_STARTED and tThisFlip >= 759.4-frameTolerance:
        # keep track of start time/frame for later
        image_100.frameNStart = frameN  # exact frame index
        image_100.tStart = t  # local t and not account for scr refresh
        image_100.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_100, 'tStartRefresh')  # time at next scr refresh
        image_100.setAutoDraw(True)
    if image_100.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_100.tStartRefresh + .4-frameTolerance:
            # keep track of stop time/frame for later
            image_100.tStop = t  # not accounting for scr refresh
            image_100.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_100, 'tStopRefresh')  # time at next scr refresh
            image_100.setAutoDraw(False)
    
    # *image_101* updates
    if image_101.status == NOT_STARTED and tThisFlip >= 759.9-frameTolerance:
        # keep track of start time/frame for later
        image_101.frameNStart = frameN  # exact frame index
        image_101.tStart = t  # local t and not account for scr refresh
        image_101.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_101, 'tStartRefresh')  # time at next scr refresh
        image_101.setAutoDraw(True)
    if image_101.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_101.tStartRefresh + .3-frameTolerance:
            # keep track of stop time/frame for later
            image_101.tStop = t  # not accounting for scr refresh
            image_101.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_101, 'tStopRefresh')  # time at next scr refresh
            image_101.setAutoDraw(False)
    
    # *slider_13* updates
    if slider_13.status == NOT_STARTED and tThisFlip >= 760.3-frameTolerance:
        # keep track of start time/frame for later
        slider_13.frameNStart = frameN  # exact frame index
        slider_13.tStart = t  # local t and not account for scr refresh
        slider_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(slider_13, 'tStartRefresh')  # time at next scr refresh
        slider_13.setAutoDraw(True)
    if slider_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > slider_13.tStartRefresh + 1.8-frameTolerance:
            # keep track of stop time/frame for later
            slider_13.tStop = t  # not accounting for scr refresh
            slider_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(slider_13, 'tStopRefresh')  # time at next scr refresh
            slider_13.setAutoDraw(False)
    
    # *text_59* updates
    if text_59.status == NOT_STARTED and tThisFlip >= 762.2-frameTolerance:
        # keep track of start time/frame for later
        text_59.frameNStart = frameN  # exact frame index
        text_59.tStart = t  # local t and not account for scr refresh
        text_59.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_59, 'tStartRefresh')  # time at next scr refresh
        text_59.setAutoDraw(True)
    if text_59.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_59.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_59.tStop = t  # not accounting for scr refresh
            text_59.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_59, 'tStopRefresh')  # time at next scr refresh
            text_59.setAutoDraw(False)
    
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
thisExp.addData('text_43.started', text_43.tStartRefresh)
thisExp.addData('text_43.stopped', text_43.tStopRefresh)
sound_2.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_2.started', sound_2.tStartRefresh)
thisExp.addData('sound_2.stopped', sound_2.tStopRefresh)
sound_3.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_3.started', sound_3.tStartRefresh)
thisExp.addData('sound_3.stopped', sound_3.tStopRefresh)
thisExp.addData('VEP1I9.started', VEP1I9.tStartRefresh)
thisExp.addData('VEP1I9.stopped', VEP1I9.tStopRefresh)
thisExp.addData('S9.response', S9.getRating())
thisExp.addData('S9.rt', S9.getRT())
thisExp.addData('S9.started', S9.tStartRefresh)
thisExp.addData('S9.stopped', S9.tStopRefresh)
thisExp.addData('vep1I18.started', vep1I18.tStartRefresh)
thisExp.addData('vep1I18.stopped', vep1I18.tStopRefresh)
thisExp.addData('S18.response', S18.getRating())
thisExp.addData('S18.rt', S18.getRT())
thisExp.addData('S18.started', S18.tStartRefresh)
thisExp.addData('S18.stopped', S18.tStopRefresh)
thisExp.addData('VEP1I31.started', VEP1I31.tStartRefresh)
thisExp.addData('VEP1I31.stopped', VEP1I31.tStopRefresh)
thisExp.addData('S31.response', S31.getRating())
thisExp.addData('S31.rt', S31.getRT())
thisExp.addData('S31.started', S31.tStartRefresh)
thisExp.addData('S31.stopped', S31.tStopRefresh)
thisExp.addData('VEP1I24.started', VEP1I24.tStartRefresh)
thisExp.addData('VEP1I24.stopped', VEP1I24.tStopRefresh)
thisExp.addData('S24.response', S24.getRating())
thisExp.addData('S24.rt', S24.getRT())
thisExp.addData('S24.started', S24.tStartRefresh)
thisExp.addData('S24.stopped', S24.tStopRefresh)
thisExp.addData('VEP1I30.started', VEP1I30.tStartRefresh)
thisExp.addData('VEP1I30.stopped', VEP1I30.tStopRefresh)
thisExp.addData('S30.response', S30.getRating())
thisExp.addData('S30.rt', S30.getRT())
thisExp.addData('S30.started', S30.tStartRefresh)
thisExp.addData('S30.stopped', S30.tStopRefresh)
thisExp.addData('VEp1I12.started', VEp1I12.tStartRefresh)
thisExp.addData('VEp1I12.stopped', VEp1I12.tStopRefresh)
thisExp.addData('S12.response', S12.getRating())
thisExp.addData('S12.rt', S12.getRT())
thisExp.addData('S12.started', S12.tStartRefresh)
thisExp.addData('S12.stopped', S12.tStopRefresh)
thisExp.addData('VEP1I27.started', VEP1I27.tStartRefresh)
thisExp.addData('VEP1I27.stopped', VEP1I27.tStopRefresh)
thisExp.addData('S27.response', S27.getRating())
thisExp.addData('S27.rt', S27.getRT())
thisExp.addData('S27.started', S27.tStartRefresh)
thisExp.addData('S27.stopped', S27.tStopRefresh)
thisExp.addData('VEP1I28.started', VEP1I28.tStartRefresh)
thisExp.addData('VEP1I28.stopped', VEP1I28.tStopRefresh)
thisExp.addData('S28.response', S28.getRating())
thisExp.addData('S28.rt', S28.getRT())
thisExp.addData('S28.started', S28.tStartRefresh)
thisExp.addData('S28.stopped', S28.tStopRefresh)
thisExp.addData('VEP1I16.started', VEP1I16.tStartRefresh)
thisExp.addData('VEP1I16.stopped', VEP1I16.tStopRefresh)
thisExp.addData('S16.response', S16.getRating())
thisExp.addData('S16.rt', S16.getRT())
thisExp.addData('S16.started', S16.tStartRefresh)
thisExp.addData('S16.stopped', S16.tStopRefresh)
thisExp.addData('VEP1I29.started', VEP1I29.tStartRefresh)
thisExp.addData('VEP1I29.stopped', VEP1I29.tStopRefresh)
thisExp.addData('S29.response', S29.getRating())
thisExp.addData('S29.rt', S29.getRT())
thisExp.addData('S29.started', S29.tStartRefresh)
thisExp.addData('S29.stopped', S29.tStopRefresh)
thisExp.addData('VEP1I32.started', VEP1I32.tStartRefresh)
thisExp.addData('VEP1I32.stopped', VEP1I32.tStopRefresh)
thisExp.addData('S32.response', S32.getRating())
thisExp.addData('S32.rt', S32.getRT())
thisExp.addData('S32.started', S32.tStartRefresh)
thisExp.addData('S32.stopped', S32.tStopRefresh)
thisExp.addData('VEP1I5.started', VEP1I5.tStartRefresh)
thisExp.addData('VEP1I5.stopped', VEP1I5.tStopRefresh)
thisExp.addData('S5.response', S5.getRating())
thisExp.addData('S5.rt', S5.getRT())
thisExp.addData('S5.started', S5.tStartRefresh)
thisExp.addData('S5.stopped', S5.tStopRefresh)
thisExp.addData('VEP1I23.started', VEP1I23.tStartRefresh)
thisExp.addData('VEP1I23.stopped', VEP1I23.tStopRefresh)
thisExp.addData('S23.response', S23.getRating())
thisExp.addData('S23.rt', S23.getRT())
thisExp.addData('S23.started', S23.tStartRefresh)
thisExp.addData('S23.stopped', S23.tStopRefresh)
thisExp.addData('VEP1I26.started', VEP1I26.tStartRefresh)
thisExp.addData('VEP1I26.stopped', VEP1I26.tStopRefresh)
thisExp.addData('S26.response', S26.getRating())
thisExp.addData('S26.rt', S26.getRT())
thisExp.addData('S26.started', S26.tStartRefresh)
thisExp.addData('S26.stopped', S26.tStopRefresh)
thisExp.addData('vep1I8.started', vep1I8.tStartRefresh)
thisExp.addData('vep1I8.stopped', vep1I8.tStopRefresh)
thisExp.addData('S8.response', S8.getRating())
thisExp.addData('S8.rt', S8.getRT())
thisExp.addData('S8.started', S8.tStartRefresh)
thisExp.addData('S8.stopped', S8.tStopRefresh)
thisExp.addData('VEp1I17.started', VEp1I17.tStartRefresh)
thisExp.addData('VEp1I17.stopped', VEp1I17.tStopRefresh)
thisExp.addData('S17.response', S17.getRating())
thisExp.addData('S17.rt', S17.getRT())
thisExp.addData('S17.started', S17.tStartRefresh)
thisExp.addData('S17.stopped', S17.tStopRefresh)
thisExp.addData('VEP1I3.started', VEP1I3.tStartRefresh)
thisExp.addData('VEP1I3.stopped', VEP1I3.tStopRefresh)
thisExp.addData('S3.response', S3.getRating())
thisExp.addData('S3.rt', S3.getRT())
thisExp.addData('S3.started', S3.tStartRefresh)
thisExp.addData('S3.stopped', S3.tStopRefresh)
thisExp.addData('VEP1I11.started', VEP1I11.tStartRefresh)
thisExp.addData('VEP1I11.stopped', VEP1I11.tStopRefresh)
thisExp.addData('S11.response', S11.getRating())
thisExp.addData('S11.rt', S11.getRT())
thisExp.addData('S11.started', S11.tStartRefresh)
thisExp.addData('S11.stopped', S11.tStopRefresh)
thisExp.addData('VEP1I21.started', VEP1I21.tStartRefresh)
thisExp.addData('VEP1I21.stopped', VEP1I21.tStopRefresh)
thisExp.addData('S21.response', S21.getRating())
thisExp.addData('S21.rt', S21.getRT())
thisExp.addData('S21.started', S21.tStartRefresh)
thisExp.addData('S21.stopped', S21.tStopRefresh)
thisExp.addData('VEP1I25.started', VEP1I25.tStartRefresh)
thisExp.addData('VEP1I25.stopped', VEP1I25.tStopRefresh)
thisExp.addData('s25.response', s25.getRating())
thisExp.addData('s25.rt', s25.getRT())
thisExp.addData('s25.started', s25.tStartRefresh)
thisExp.addData('s25.stopped', s25.tStopRefresh)
thisExp.addData('VEP1I20.started', VEP1I20.tStartRefresh)
thisExp.addData('VEP1I20.stopped', VEP1I20.tStopRefresh)
thisExp.addData('S20.response', S20.getRating())
thisExp.addData('S20.rt', S20.getRT())
thisExp.addData('S20.started', S20.tStartRefresh)
thisExp.addData('S20.stopped', S20.tStopRefresh)
thisExp.addData('VEP1I13.started', VEP1I13.tStartRefresh)
thisExp.addData('VEP1I13.stopped', VEP1I13.tStopRefresh)
thisExp.addData('S13.response', S13.getRating())
thisExp.addData('S13.rt', S13.getRT())
thisExp.addData('S13.started', S13.tStartRefresh)
thisExp.addData('S13.stopped', S13.tStopRefresh)
thisExp.addData('VEP1I19.started', VEP1I19.tStartRefresh)
thisExp.addData('VEP1I19.stopped', VEP1I19.tStopRefresh)
thisExp.addData('S19.response', S19.getRating())
thisExp.addData('S19.rt', S19.getRT())
thisExp.addData('S19.started', S19.tStartRefresh)
thisExp.addData('S19.stopped', S19.tStopRefresh)
thisExp.addData('VEP1I1.started', VEP1I1.tStartRefresh)
thisExp.addData('VEP1I1.stopped', VEP1I1.tStopRefresh)
thisExp.addData('S1.response', S1.getRating())
thisExp.addData('S1.rt', S1.getRT())
thisExp.addData('S1.started', S1.tStartRefresh)
thisExp.addData('S1.stopped', S1.tStopRefresh)
thisExp.addData('VEP1I7.started', VEP1I7.tStartRefresh)
thisExp.addData('VEP1I7.stopped', VEP1I7.tStopRefresh)
thisExp.addData('S7.response', S7.getRating())
thisExp.addData('S7.rt', S7.getRT())
thisExp.addData('S7.started', S7.tStartRefresh)
thisExp.addData('S7.stopped', S7.tStopRefresh)
thisExp.addData('VEP1I4.started', VEP1I4.tStartRefresh)
thisExp.addData('VEP1I4.stopped', VEP1I4.tStopRefresh)
thisExp.addData('S4.response', S4.getRating())
thisExp.addData('S4.rt', S4.getRT())
thisExp.addData('S4.started', S4.tStartRefresh)
thisExp.addData('S4.stopped', S4.tStopRefresh)
thisExp.addData('VEP1I6.started', VEP1I6.tStartRefresh)
thisExp.addData('VEP1I6.stopped', VEP1I6.tStopRefresh)
thisExp.addData('S6.response', S6.getRating())
thisExp.addData('S6.rt', S6.getRT())
thisExp.addData('S6.started', S6.tStartRefresh)
thisExp.addData('S6.stopped', S6.tStopRefresh)
thisExp.addData('VEP1I22.started', VEP1I22.tStartRefresh)
thisExp.addData('VEP1I22.stopped', VEP1I22.tStopRefresh)
thisExp.addData('S22.response', S22.getRating())
thisExp.addData('S22.rt', S22.getRT())
thisExp.addData('S22.started', S22.tStartRefresh)
thisExp.addData('S22.stopped', S22.tStopRefresh)
thisExp.addData('VEP1I2.started', VEP1I2.tStartRefresh)
thisExp.addData('VEP1I2.stopped', VEP1I2.tStopRefresh)
thisExp.addData('S2.response', S2.getRating())
thisExp.addData('S2.rt', S2.getRT())
thisExp.addData('S2.started', S2.tStartRefresh)
thisExp.addData('S2.stopped', S2.tStopRefresh)
thisExp.addData('VEP1I10.started', VEP1I10.tStartRefresh)
thisExp.addData('VEP1I10.stopped', VEP1I10.tStopRefresh)
thisExp.addData('S10.response', S10.getRating())
thisExp.addData('S10.rt', S10.getRT())
thisExp.addData('S10.started', S10.tStartRefresh)
thisExp.addData('S10.stopped', S10.tStopRefresh)
thisExp.addData('VEP1I15.started', VEP1I15.tStartRefresh)
thisExp.addData('VEP1I15.stopped', VEP1I15.tStopRefresh)
thisExp.addData('S15.response', S15.getRating())
thisExp.addData('S15.rt', S15.getRT())
thisExp.addData('S15.started', S15.tStartRefresh)
thisExp.addData('S15.stopped', S15.tStopRefresh)
thisExp.addData('VEP1I14.started', VEP1I14.tStartRefresh)
thisExp.addData('VEP1I14.stopped', VEP1I14.tStopRefresh)
thisExp.addData('S14.response', S14.getRating())
thisExp.addData('S14.rt', S14.getRT())
thisExp.addData('S14.started', S14.tStartRefresh)
thisExp.addData('S14.stopped', S14.tStopRefresh)
thisExp.addData('text_44.started', text_44.tStartRefresh)
thisExp.addData('text_44.stopped', text_44.tStopRefresh)
thisExp.addData('VEP2C1.started', VEP2C1.tStartRefresh)
thisExp.addData('VEP2C1.stopped', VEP2C1.tStopRefresh)
thisExp.addData('text_45.started', text_45.tStartRefresh)
thisExp.addData('text_45.stopped', text_45.tStopRefresh)
thisExp.addData('d1.started', d1.tStartRefresh)
thisExp.addData('d1.stopped', d1.tStopRefresh)
thisExp.addData('d2.started', d2.tStartRefresh)
thisExp.addData('d2.stopped', d2.tStopRefresh)
thisExp.addData('s1.started', s1.tStartRefresh)
thisExp.addData('s1.stopped', s1.tStopRefresh)
thisExp.addData('b1.started', b1.tStartRefresh)
thisExp.addData('b1.stopped', b1.tStopRefresh)
thisExp.addData('d4.started', d4.tStartRefresh)
thisExp.addData('d4.stopped', d4.tStopRefresh)
thisExp.addData('s2.started', s2.tStartRefresh)
thisExp.addData('s2.stopped', s2.tStopRefresh)
thisExp.addData('VS1.response', VS1.getRating())
thisExp.addData('VS1.rt', VS1.getRT())
thisExp.addData('VS1.started', VS1.tStartRefresh)
thisExp.addData('VS1.stopped', VS1.tStopRefresh)
thisExp.addData('VEP2C2.started', VEP2C2.tStartRefresh)
thisExp.addData('VEP2C2.stopped', VEP2C2.tStopRefresh)
thisExp.addData('text_46.started', text_46.tStartRefresh)
thisExp.addData('text_46.stopped', text_46.tStopRefresh)
thisExp.addData('b2.started', b2.tStartRefresh)
thisExp.addData('b2.stopped', b2.tStopRefresh)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
thisExp.addData('image_3.started', image_3.tStartRefresh)
thisExp.addData('image_3.stopped', image_3.tStopRefresh)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)
thisExp.addData('image_7.started', image_7.tStartRefresh)
thisExp.addData('image_7.stopped', image_7.tStopRefresh)
thisExp.addData('slider.response', slider.getRating())
thisExp.addData('slider.rt', slider.getRT())
thisExp.addData('slider.started', slider.tStartRefresh)
thisExp.addData('slider.stopped', slider.tStopRefresh)
thisExp.addData('VEP2C3.started', VEP2C3.tStartRefresh)
thisExp.addData('VEP2C3.stopped', VEP2C3.tStopRefresh)
thisExp.addData('text_47.started', text_47.tStartRefresh)
thisExp.addData('text_47.stopped', text_47.tStopRefresh)
thisExp.addData('image_8.started', image_8.tStartRefresh)
thisExp.addData('image_8.stopped', image_8.tStopRefresh)
thisExp.addData('image_9.started', image_9.tStartRefresh)
thisExp.addData('image_9.stopped', image_9.tStopRefresh)
thisExp.addData('image_10.started', image_10.tStartRefresh)
thisExp.addData('image_10.stopped', image_10.tStopRefresh)
thisExp.addData('image_11.started', image_11.tStartRefresh)
thisExp.addData('image_11.stopped', image_11.tStopRefresh)
thisExp.addData('image_12.started', image_12.tStartRefresh)
thisExp.addData('image_12.stopped', image_12.tStopRefresh)
thisExp.addData('image_13.started', image_13.tStartRefresh)
thisExp.addData('image_13.stopped', image_13.tStopRefresh)
thisExp.addData('image_14.started', image_14.tStartRefresh)
thisExp.addData('image_14.stopped', image_14.tStopRefresh)
thisExp.addData('image_15.started', image_15.tStartRefresh)
thisExp.addData('image_15.stopped', image_15.tStopRefresh)
thisExp.addData('slider_2.response', slider_2.getRating())
thisExp.addData('slider_2.rt', slider_2.getRT())
thisExp.addData('slider_2.started', slider_2.tStartRefresh)
thisExp.addData('slider_2.stopped', slider_2.tStopRefresh)
thisExp.addData('VEP2C4.started', VEP2C4.tStartRefresh)
thisExp.addData('VEP2C4.stopped', VEP2C4.tStopRefresh)
thisExp.addData('text_48.started', text_48.tStartRefresh)
thisExp.addData('text_48.stopped', text_48.tStopRefresh)
thisExp.addData('image_16.started', image_16.tStartRefresh)
thisExp.addData('image_16.stopped', image_16.tStopRefresh)
thisExp.addData('image_17.started', image_17.tStartRefresh)
thisExp.addData('image_17.stopped', image_17.tStopRefresh)
thisExp.addData('image_18.started', image_18.tStartRefresh)
thisExp.addData('image_18.stopped', image_18.tStopRefresh)
thisExp.addData('image_19.started', image_19.tStartRefresh)
thisExp.addData('image_19.stopped', image_19.tStopRefresh)
thisExp.addData('image_20.started', image_20.tStartRefresh)
thisExp.addData('image_20.stopped', image_20.tStopRefresh)
thisExp.addData('image_21.started', image_21.tStartRefresh)
thisExp.addData('image_21.stopped', image_21.tStopRefresh)
thisExp.addData('image_22.started', image_22.tStartRefresh)
thisExp.addData('image_22.stopped', image_22.tStopRefresh)
thisExp.addData('image_23.started', image_23.tStartRefresh)
thisExp.addData('image_23.stopped', image_23.tStopRefresh)
thisExp.addData('image_24.started', image_24.tStartRefresh)
thisExp.addData('image_24.stopped', image_24.tStopRefresh)
thisExp.addData('slider_3.response', slider_3.getRating())
thisExp.addData('slider_3.rt', slider_3.getRT())
thisExp.addData('slider_3.started', slider_3.tStartRefresh)
thisExp.addData('slider_3.stopped', slider_3.tStopRefresh)
thisExp.addData('C5.started', C5.tStartRefresh)
thisExp.addData('C5.stopped', C5.tStopRefresh)
thisExp.addData('text_49.started', text_49.tStartRefresh)
thisExp.addData('text_49.stopped', text_49.tStopRefresh)
thisExp.addData('image_26.started', image_26.tStartRefresh)
thisExp.addData('image_26.stopped', image_26.tStopRefresh)
thisExp.addData('image_27.started', image_27.tStartRefresh)
thisExp.addData('image_27.stopped', image_27.tStopRefresh)
thisExp.addData('image_28.started', image_28.tStartRefresh)
thisExp.addData('image_28.stopped', image_28.tStopRefresh)
thisExp.addData('image_29.started', image_29.tStartRefresh)
thisExp.addData('image_29.stopped', image_29.tStopRefresh)
thisExp.addData('image_30.started', image_30.tStartRefresh)
thisExp.addData('image_30.stopped', image_30.tStopRefresh)
thisExp.addData('image_31.started', image_31.tStartRefresh)
thisExp.addData('image_31.stopped', image_31.tStopRefresh)
thisExp.addData('image_32.started', image_32.tStartRefresh)
thisExp.addData('image_32.stopped', image_32.tStopRefresh)
thisExp.addData('image_33.started', image_33.tStartRefresh)
thisExp.addData('image_33.stopped', image_33.tStopRefresh)
thisExp.addData('image_34.started', image_34.tStartRefresh)
thisExp.addData('image_34.stopped', image_34.tStopRefresh)
thisExp.addData('slider_4.response', slider_4.getRating())
thisExp.addData('slider_4.rt', slider_4.getRT())
thisExp.addData('slider_4.started', slider_4.tStartRefresh)
thisExp.addData('slider_4.stopped', slider_4.tStopRefresh)
thisExp.addData('C6.started', C6.tStartRefresh)
thisExp.addData('C6.stopped', C6.tStopRefresh)
thisExp.addData('text_50.started', text_50.tStartRefresh)
thisExp.addData('text_50.stopped', text_50.tStopRefresh)
thisExp.addData('image_36.started', image_36.tStartRefresh)
thisExp.addData('image_36.stopped', image_36.tStopRefresh)
thisExp.addData('image_37.started', image_37.tStartRefresh)
thisExp.addData('image_37.stopped', image_37.tStopRefresh)
thisExp.addData('image_25.started', image_25.tStartRefresh)
thisExp.addData('image_25.stopped', image_25.tStopRefresh)
thisExp.addData('image_35.started', image_35.tStartRefresh)
thisExp.addData('image_35.stopped', image_35.tStopRefresh)
thisExp.addData('image_38.started', image_38.tStartRefresh)
thisExp.addData('image_38.stopped', image_38.tStopRefresh)
thisExp.addData('image_39.started', image_39.tStartRefresh)
thisExp.addData('image_39.stopped', image_39.tStopRefresh)
thisExp.addData('image_40.started', image_40.tStartRefresh)
thisExp.addData('image_40.stopped', image_40.tStopRefresh)
thisExp.addData('slider_5.response', slider_5.getRating())
thisExp.addData('slider_5.rt', slider_5.getRT())
thisExp.addData('slider_5.started', slider_5.tStartRefresh)
thisExp.addData('slider_5.stopped', slider_5.tStopRefresh)
thisExp.addData('C7.started', C7.tStartRefresh)
thisExp.addData('C7.stopped', C7.tStopRefresh)
thisExp.addData('text_51.started', text_51.tStartRefresh)
thisExp.addData('text_51.stopped', text_51.tStopRefresh)
thisExp.addData('image_41.started', image_41.tStartRefresh)
thisExp.addData('image_41.stopped', image_41.tStopRefresh)
thisExp.addData('image_42.started', image_42.tStartRefresh)
thisExp.addData('image_42.stopped', image_42.tStopRefresh)
thisExp.addData('image_43.started', image_43.tStartRefresh)
thisExp.addData('image_43.stopped', image_43.tStopRefresh)
thisExp.addData('image_44.started', image_44.tStartRefresh)
thisExp.addData('image_44.stopped', image_44.tStopRefresh)
thisExp.addData('image_45.started', image_45.tStartRefresh)
thisExp.addData('image_45.stopped', image_45.tStopRefresh)
thisExp.addData('image_46.started', image_46.tStartRefresh)
thisExp.addData('image_46.stopped', image_46.tStopRefresh)
thisExp.addData('image_47.started', image_47.tStartRefresh)
thisExp.addData('image_47.stopped', image_47.tStopRefresh)
thisExp.addData('image_48.started', image_48.tStartRefresh)
thisExp.addData('image_48.stopped', image_48.tStopRefresh)
thisExp.addData('image_49.started', image_49.tStartRefresh)
thisExp.addData('image_49.stopped', image_49.tStopRefresh)
thisExp.addData('slider_6.response', slider_6.getRating())
thisExp.addData('slider_6.rt', slider_6.getRT())
thisExp.addData('slider_6.started', slider_6.tStartRefresh)
thisExp.addData('slider_6.stopped', slider_6.tStopRefresh)
thisExp.addData('C8.started', C8.tStartRefresh)
thisExp.addData('C8.stopped', C8.tStopRefresh)
thisExp.addData('text_52.started', text_52.tStartRefresh)
thisExp.addData('text_52.stopped', text_52.tStopRefresh)
thisExp.addData('image_50.started', image_50.tStartRefresh)
thisExp.addData('image_50.stopped', image_50.tStopRefresh)
thisExp.addData('image_51.started', image_51.tStartRefresh)
thisExp.addData('image_51.stopped', image_51.tStopRefresh)
thisExp.addData('image_52.started', image_52.tStartRefresh)
thisExp.addData('image_52.stopped', image_52.tStopRefresh)
thisExp.addData('image_53.started', image_53.tStartRefresh)
thisExp.addData('image_53.stopped', image_53.tStopRefresh)
thisExp.addData('image_54.started', image_54.tStartRefresh)
thisExp.addData('image_54.stopped', image_54.tStopRefresh)
thisExp.addData('image_55.started', image_55.tStartRefresh)
thisExp.addData('image_55.stopped', image_55.tStopRefresh)
thisExp.addData('image_56.started', image_56.tStartRefresh)
thisExp.addData('image_56.stopped', image_56.tStopRefresh)
thisExp.addData('slider_7.response', slider_7.getRating())
thisExp.addData('slider_7.rt', slider_7.getRT())
thisExp.addData('slider_7.started', slider_7.tStartRefresh)
thisExp.addData('slider_7.stopped', slider_7.tStopRefresh)
thisExp.addData('C9.started', C9.tStartRefresh)
thisExp.addData('C9.stopped', C9.tStopRefresh)
thisExp.addData('text_53.started', text_53.tStartRefresh)
thisExp.addData('text_53.stopped', text_53.tStopRefresh)
thisExp.addData('image_57.started', image_57.tStartRefresh)
thisExp.addData('image_57.stopped', image_57.tStopRefresh)
thisExp.addData('image_58.started', image_58.tStartRefresh)
thisExp.addData('image_58.stopped', image_58.tStopRefresh)
thisExp.addData('image_59.started', image_59.tStartRefresh)
thisExp.addData('image_59.stopped', image_59.tStopRefresh)
thisExp.addData('image_60.started', image_60.tStartRefresh)
thisExp.addData('image_60.stopped', image_60.tStopRefresh)
thisExp.addData('image_61.started', image_61.tStartRefresh)
thisExp.addData('image_61.stopped', image_61.tStopRefresh)
thisExp.addData('image_62.started', image_62.tStartRefresh)
thisExp.addData('image_62.stopped', image_62.tStopRefresh)
thisExp.addData('image_63.started', image_63.tStartRefresh)
thisExp.addData('image_63.stopped', image_63.tStopRefresh)
thisExp.addData('image_64.started', image_64.tStartRefresh)
thisExp.addData('image_64.stopped', image_64.tStopRefresh)
thisExp.addData('image_65.started', image_65.tStartRefresh)
thisExp.addData('image_65.stopped', image_65.tStopRefresh)
thisExp.addData('image_66.started', image_66.tStartRefresh)
thisExp.addData('image_66.stopped', image_66.tStopRefresh)
thisExp.addData('image_67.started', image_67.tStartRefresh)
thisExp.addData('image_67.stopped', image_67.tStopRefresh)
thisExp.addData('slider_8.response', slider_8.getRating())
thisExp.addData('slider_8.rt', slider_8.getRT())
thisExp.addData('slider_8.started', slider_8.tStartRefresh)
thisExp.addData('slider_8.stopped', slider_8.tStopRefresh)
thisExp.addData('C10.started', C10.tStartRefresh)
thisExp.addData('C10.stopped', C10.tStopRefresh)
thisExp.addData('text_54.started', text_54.tStartRefresh)
thisExp.addData('text_54.stopped', text_54.tStopRefresh)
thisExp.addData('image_68.started', image_68.tStartRefresh)
thisExp.addData('image_68.stopped', image_68.tStopRefresh)
thisExp.addData('image_69.started', image_69.tStartRefresh)
thisExp.addData('image_69.stopped', image_69.tStopRefresh)
thisExp.addData('image_70.started', image_70.tStartRefresh)
thisExp.addData('image_70.stopped', image_70.tStopRefresh)
thisExp.addData('image_71.started', image_71.tStartRefresh)
thisExp.addData('image_71.stopped', image_71.tStopRefresh)
thisExp.addData('image_72.started', image_72.tStartRefresh)
thisExp.addData('image_72.stopped', image_72.tStopRefresh)
thisExp.addData('image_73.started', image_73.tStartRefresh)
thisExp.addData('image_73.stopped', image_73.tStopRefresh)
thisExp.addData('slider_9.response', slider_9.getRating())
thisExp.addData('slider_9.rt', slider_9.getRT())
thisExp.addData('slider_9.started', slider_9.tStartRefresh)
thisExp.addData('slider_9.stopped', slider_9.tStopRefresh)
thisExp.addData('C11.started', C11.tStartRefresh)
thisExp.addData('C11.stopped', C11.tStopRefresh)
thisExp.addData('text_55.started', text_55.tStartRefresh)
thisExp.addData('text_55.stopped', text_55.tStopRefresh)
thisExp.addData('image_74.started', image_74.tStartRefresh)
thisExp.addData('image_74.stopped', image_74.tStopRefresh)
thisExp.addData('image_75.started', image_75.tStartRefresh)
thisExp.addData('image_75.stopped', image_75.tStopRefresh)
thisExp.addData('image_76.started', image_76.tStartRefresh)
thisExp.addData('image_76.stopped', image_76.tStopRefresh)
thisExp.addData('image_77.started', image_77.tStartRefresh)
thisExp.addData('image_77.stopped', image_77.tStopRefresh)
thisExp.addData('image_78.started', image_78.tStartRefresh)
thisExp.addData('image_78.stopped', image_78.tStopRefresh)
thisExp.addData('image_79.started', image_79.tStartRefresh)
thisExp.addData('image_79.stopped', image_79.tStopRefresh)
thisExp.addData('slider_10.response', slider_10.getRating())
thisExp.addData('slider_10.rt', slider_10.getRT())
thisExp.addData('slider_10.started', slider_10.tStartRefresh)
thisExp.addData('slider_10.stopped', slider_10.tStopRefresh)
thisExp.addData('C12.started', C12.tStartRefresh)
thisExp.addData('C12.stopped', C12.tStopRefresh)
thisExp.addData('text_56.started', text_56.tStartRefresh)
thisExp.addData('text_56.stopped', text_56.tStopRefresh)
thisExp.addData('image_80.started', image_80.tStartRefresh)
thisExp.addData('image_80.stopped', image_80.tStopRefresh)
thisExp.addData('image_81.started', image_81.tStartRefresh)
thisExp.addData('image_81.stopped', image_81.tStopRefresh)
thisExp.addData('image_82.started', image_82.tStartRefresh)
thisExp.addData('image_82.stopped', image_82.tStopRefresh)
thisExp.addData('image_83.started', image_83.tStartRefresh)
thisExp.addData('image_83.stopped', image_83.tStopRefresh)
thisExp.addData('image_84.started', image_84.tStartRefresh)
thisExp.addData('image_84.stopped', image_84.tStopRefresh)
thisExp.addData('image_85.started', image_85.tStartRefresh)
thisExp.addData('image_85.stopped', image_85.tStopRefresh)
thisExp.addData('slider_11.response', slider_11.getRating())
thisExp.addData('slider_11.rt', slider_11.getRT())
thisExp.addData('slider_11.started', slider_11.tStartRefresh)
thisExp.addData('slider_11.stopped', slider_11.tStopRefresh)
thisExp.addData('C13.started', C13.tStartRefresh)
thisExp.addData('C13.stopped', C13.tStopRefresh)
thisExp.addData('text_57.started', text_57.tStartRefresh)
thisExp.addData('text_57.stopped', text_57.tStopRefresh)
thisExp.addData('image_86.started', image_86.tStartRefresh)
thisExp.addData('image_86.stopped', image_86.tStopRefresh)
thisExp.addData('image_87.started', image_87.tStartRefresh)
thisExp.addData('image_87.stopped', image_87.tStopRefresh)
thisExp.addData('image_88.started', image_88.tStartRefresh)
thisExp.addData('image_88.stopped', image_88.tStopRefresh)
thisExp.addData('image_89.started', image_89.tStartRefresh)
thisExp.addData('image_89.stopped', image_89.tStopRefresh)
thisExp.addData('image_90.started', image_90.tStartRefresh)
thisExp.addData('image_90.stopped', image_90.tStopRefresh)
thisExp.addData('image_91.started', image_91.tStartRefresh)
thisExp.addData('image_91.stopped', image_91.tStopRefresh)
thisExp.addData('image_92.started', image_92.tStartRefresh)
thisExp.addData('image_92.stopped', image_92.tStopRefresh)
thisExp.addData('slider_12.response', slider_12.getRating())
thisExp.addData('slider_12.rt', slider_12.getRT())
thisExp.addData('slider_12.started', slider_12.tStartRefresh)
thisExp.addData('slider_12.stopped', slider_12.tStopRefresh)
thisExp.addData('C14.started', C14.tStartRefresh)
thisExp.addData('C14.stopped', C14.tStopRefresh)
thisExp.addData('text_58.started', text_58.tStartRefresh)
thisExp.addData('text_58.stopped', text_58.tStopRefresh)
thisExp.addData('image_93.started', image_93.tStartRefresh)
thisExp.addData('image_93.stopped', image_93.tStopRefresh)
thisExp.addData('image_94.started', image_94.tStartRefresh)
thisExp.addData('image_94.stopped', image_94.tStopRefresh)
thisExp.addData('image_95.started', image_95.tStartRefresh)
thisExp.addData('image_95.stopped', image_95.tStopRefresh)
thisExp.addData('image_96.started', image_96.tStartRefresh)
thisExp.addData('image_96.stopped', image_96.tStopRefresh)
thisExp.addData('image_97.started', image_97.tStartRefresh)
thisExp.addData('image_97.stopped', image_97.tStopRefresh)
thisExp.addData('image_98.started', image_98.tStartRefresh)
thisExp.addData('image_98.stopped', image_98.tStopRefresh)
thisExp.addData('image_99.started', image_99.tStartRefresh)
thisExp.addData('image_99.stopped', image_99.tStopRefresh)
thisExp.addData('image_100.started', image_100.tStartRefresh)
thisExp.addData('image_100.stopped', image_100.tStopRefresh)
thisExp.addData('image_101.started', image_101.tStartRefresh)
thisExp.addData('image_101.stopped', image_101.tStopRefresh)
thisExp.addData('slider_13.response', slider_13.getRating())
thisExp.addData('slider_13.rt', slider_13.getRT())
thisExp.addData('slider_13.started', slider_13.tStartRefresh)
thisExp.addData('slider_13.stopped', slider_13.tStopRefresh)
thisExp.addData('text_59.started', text_59.tStartRefresh)
thisExp.addData('text_59.stopped', text_59.tStopRefresh)

# ------Prepare to start Routine "Checker_circle"-------
continueRoutine = True
# update component parameters for each repeat
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.0,-1.0,-1.0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "message"
messageClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='',
    font='Arial',
    units='deg', pos=(0, -5.0), height=0.5, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
fixation_cross_pre = visual.TextStim(win=win, name='fixation_cross_pre',
    text='+',
    font='Arial',
    units='deg', pos=(0, 0.1), height=1.0, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
grating_inverse = visual.GratingStim(
    win=win, name='grating_inverse',units='deg', 
    tex='sqrXsqr', mask='circle',
    ori=0, pos=[0.0, 0.0], size=[15.0, 15.0], sf=[2,2], phase=[0.75,0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=256, interpolate=True, depth=0.0)
grating = visual.GratingStim(
    win=win, name='grating',units='deg', 
    tex='sqrXsqr', mask='circle',
    ori=0, pos=[0.0, 0], size=[15.0, 15.0], sf=[2,2], phase=[0.25,0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=256, interpolate=True, depth=-1.0)
fixation_cross_main = visual.TextStim(win=win, name='fixation_cross_main',
    text='+',
    font='Arial',
    units='deg', pos=[0, 0.1], height=1.0, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
p_port = parallel.ParallelPort(address='0xD010')

# custom function
def trigger():
 p_port.setData(int(255))
 core.wait(0.0002) # 0.2 ms
 p_port.setData(int(0))

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "message"-------
t = 0
messageClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
messageComponents = [instruction, fixation_cross_pre]
for thisComponent in messageComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "message"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = messageClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if t >= 0.0 and instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction.tStart = t
        instruction.frameNStart = frameN  # exact frame index
        instruction.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instruction.status == STARTED and t >= frameRemains:
        instruction.setAutoDraw(False)
    
    # *fixation_cross_pre* updates
    if t >= 0.0 and fixation_cross_pre.status == NOT_STARTED:
        # keep track of start time/frame for later
        fixation_cross_pre.tStart = t
        fixation_cross_pre.frameNStart = frameN  # exact frame index
        fixation_cross_pre.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fixation_cross_pre.status == STARTED and t >= frameRemains:
        fixation_cross_pre.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in messageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
            
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "message"-------
for thisComponent in messageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=61, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = [grating_inverse, grating, fixation_cross_main, p_port]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *grating_inverse* updates
        if t >= 0.0 and grating_inverse.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating_inverse.tStart = t
            grating_inverse.frameNStart = frameN  # exact frame index
            grating_inverse.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if grating_inverse.status == STARTED and t >= frameRemains:
            grating_inverse.setAutoDraw(False)
        
        # *grating* updates
        if t >= 0.5 and grating.status == NOT_STARTED:
            # keep track of start time/frame for later
            grating.tStart = t
            grating.frameNStart = frameN  # exact frame index
            grating.setAutoDraw(True)
        frameRemains = 0.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if grating.status == STARTED and t >= frameRemains:
            grating.setAutoDraw(False)
        
        # *fixation_cross_main* updates
        if t >= 0.0 and fixation_cross_main.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross_main.tStart = t
            fixation_cross_main.frameNStart = frameN  # exact frame index
            fixation_cross_main.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross_main.status == STARTED and t >= frameRemains:
            fixation_cross_main.setAutoDraw(False)
        # *p_port* updates
        if t >= 0.5 and p_port.status == NOT_STARTED:
            # keep track of start time/frame for later
            p_port.tStart = t
            p_port.frameNStart = frameN  # exact frame index
            p_port.status = STARTED
            # win.callOnFlip(p_port.setData, int(255))
            win.callOnFlip(trigger) # custom
        frameRemains = 0.5 + 0.05- win.monitorFramePeriod * 0.75  # most of one frame period left
        if p_port.status == STARTED and t >= frameRemains:
            p_port.status = STOPPED
            # win.callOnFlip(p_port.setData, int(0))
        
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
    if p_port.status == STARTED:
        win.callOnFlip(p_port.setData, int(0))
    thisExp.nextEntry()
    


# keep track of which components have finished
Checker_circleComponents = []
for thisComponent in Checker_circleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Checker_circleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Checker_circle"-------
while continueRoutine:
    # get current time
    t = Checker_circleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Checker_circleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Checker_circleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Checker_circle"-------
for thisComponent in Checker_circleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Checker_circle" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "rest"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
restComponents = [text_60]
for thisComponent in restComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rest"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = restClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=restClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_60* updates
    if text_60.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_60.frameNStart = frameN  # exact frame index
        text_60.tStart = t  # local t and not account for scr refresh
        text_60.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_60, 'tStartRefresh')  # time at next scr refresh
        text_60.setAutoDraw(True)
    if text_60.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_60.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_60.tStop = t  # not accounting for scr refresh
            text_60.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_60, 'tStopRefresh')  # time at next scr refresh
            text_60.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in restComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rest"-------
for thisComponent in restComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_60.started', text_60.tStartRefresh)
thisExp.addData('text_60.stopped', text_60.tStopRefresh)

# ------Prepare to start Routine "flashing_Wedge"-------
continueRoutine = True
# update component parameters for each repeat
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

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
    

# Make two wedges (in opposite contrast) and alternate them for flashing
wedge1 = visual.RadialStim(win, tex='sqrXsqr', color=1, size=1,
    visibleWedge=[0, 45], radialCycles=4, angularCycles=8, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful
wedge2 = visual.RadialStim(win, tex='sqrXsqr', color=-1, size=1,
    visibleWedge=[0, 45], radialCycles=4, angularCycles=8, interpolate=False,
    autoLog=False)  # this stim changes too much for autologging to be useful

t = 0
rotationRate = 0.1  # revs per sec
flashPeriod = 0.1  # seconds for one B-W cycle (ie 1/Hz)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(60.00000)

# update component parameters for each repeat

# reset timers
trialClock = core.Clock()
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    if t % flashPeriod < flashPeriod / 2.0:  # more accurate to count frames
        stim = wedge1
    else:
        stim = wedge2
    stim.ori = t * rotationRate * 360.0  # set new rotation
    stim.draw()
    win.flip()

win.close()
core.quit()
# keep track of which components have finished
flashing_WedgeComponents = []
for thisComponent in flashing_WedgeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
flashing_WedgeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "flashing_Wedge"-------
while continueRoutine:
    # get current time
    t = flashing_WedgeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=flashing_WedgeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in flashing_WedgeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "flashing_Wedge"-------
for thisComponent in flashing_WedgeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "flashing_Wedge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
