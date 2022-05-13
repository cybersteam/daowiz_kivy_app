import kivy
import os
import random
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from kivy.uix.video import Video
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

from random import randint
import random

#For the Dragger widget (not happening yet)
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock



            # AN APP should ALWAYS BE CHILD PROOF AND IDIOT PROOF!!!!!!!!!!!!!



class SoundControl():
                        #NEXT - make a new "button/or/input" - current song fade while new song starts
    # these are the music directories:
    music_dir = "music"
    music_dir1 = "music1"
    # these are list objects of the files in those directories
    music_files = os.listdir(music_dir)
    music_files1 = os.listdir(music_dir1)
    # these are each a list of the mp3 files in those directories
    song_list = [x for x in music_files if x.endswith(('mp3'))]
    song_list1 = [i for i in music_files1 if i.endswith(('mp3'))]
    # these are just a count of the number of songs in each directory to be used in the methods below
    song_count = len(song_list)
    song_count1 = len(song_list1)

    #The following two methods (playaudio & nextaudio) play a song, each in a different directory, one after the other
        #the 'music' directory contains songs and 'music1' directory contains instrumentals.
    #PLAYs a song in the "music" directory
    def playaudio(self, next = 0):
        #creates a song_title obj randomly from the list of songs in song_list of that directory
        song_title = self.song_list[random.randrange(0,self.song_count)]
        #create sound obj from the random song_title obj
        self.sound = SoundLoader.load('{}/{}'.format(self.music_dir, song_title))
        #play the song
        self.sound.play()
        #bind the "nextaudio" method to when this current song stops.. (so when this song stops it triggers the 'nextaudio' method)
        self.sound.bind(on_stop=self.nextaudio)

    #PLAYs a song in the "music1" directory (all the same as the "playaudio" method above but with music1 directory)
    def nextaudio(self, next = 0):
        print("hello it stopped")
        song_title1 = self.song_list1[random.randrange(0,self.song_count1)]
        self.sound1 = SoundLoader.load('{}/{}'.format(self.music_dir1, song_title1))
        self.sound1.play()
        self.sound1.bind(on_stop=self.playaudio)

    #This method plays one exact song if needed - specified by a number when called in the .kv file
    # e.g. can be used on a button or on_enter screen etc.
    def playexactsong(self, song = 0):
        song_title = self.song_list[song]
        self.sound = SoundLoader.load('{}/{}'.format(self.music_dir, song_title))
        self.sound.play()

## This is not working yet - it will stop the audio that is playing or do other such things - to be continued
'''
    def stopaudio(self, song = 0):
        #NEEDS TO be able to STOP AN EXACT SONG OR ALL SOUNDs
        song_title = self.song_list[song]
        unloadsound = SoundLoader.unload('{}/{}'.format(self.music_dir, song_title))
        unloadsound.stop()
'''
#the intro screen (see .kv file)
class IntroPage(Screen):
    pass

# this creates a Screen class for our root widget
class FirstPage(Screen):
    #creates a snd object that can be called from the .kv file (see .kv file - FirstPage)
    snd = SoundControl()

# the borderlands screen
class BorderlandsPage(Screen):
    pass

# This is the screenmanager for each screen (see .kv file)
class WindowManager(ScreenManager):
    #Makes the app automatically go fullscreen on the device
    Window.fullscreen = True

# this is the main App Widget of the whole App
class DaowizApp(App):
    pass

daowiz = DaowizApp()
if __name__== "__main__":
    daowiz.run()
