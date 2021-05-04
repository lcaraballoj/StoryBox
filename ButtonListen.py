import speech_recognition as sr
import csv
import pyaudio
import os
import time
import wave

from csv import DictReader
from pygame import mixer
from gpiozero import Button
from datetime import datetime, timedelta

CHUNK = 1024
P = pyaudio.PyAudio() #Create interface to PortAudio
SLEEP_TIME = 2

# csv file that holds the key words and story names
story_keyword_csv = "stories_keywords.csv"

#json file that is needed for GCP (Google Cloud Platform)
json_file = "GCPKey.json"

#Set mic index
MIC = 1

# #Set story
# STORY = ''

#Set sleep time
SLEEPTIME = 2

#Class to play wav file
class PlaySound():
    #Function that is always initiated
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        mixer.init()
        mixer.music.load(self.filename)         #Load file
        mixer.music.set_volume(0.5)             #Set volume
        mixer.music.play()                      #Play sound volume at desired volume

    def button_pause_play(btn):
        global HOLD_TIME

        pause = False
        start_time = time.time()
        diff = 0

        while btn.is_active and (diff < HOLD_TIME):
            current_time = time.time()
            diff = current_time - start_time

            if diff < HOLD_TIME:
                print("Paused")
                mixer.music.pause()
                pause = True

            if (diff < HOLD_TIME and pause == True):
                print("Play")
                mixer.music.play()

            else:
                print("Stop")
                mixer.stop()

#Class to find if word spoken is a keyword
class FindKeyWord():
    #Function to convert speech-to-text and search for keyword
    def recognize(self):
        global story_name

        #Setting up the Google Speech-to-Text Cloud
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

        r = sr.Recognizer()
        file = sr.Microphone(device_index = MIC)

        #Using the microphone as the source of audio listen for words
        with file as source:
            print("say something!!.....")
            command = PlaySound("key_word_command.mp3")
            command.play()
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        #Try to convert speech to text
        try:
            recog = r.recognize_google_cloud(audio, language = 'en-US')
            print("You said: " + recog)                 #Debugger (prints what you said)

            #Convert CSV file to dictionary
            csv_to_dictionary_list()

            res = None

            recog = recog.strip()

            story_name = ''                             #Set story_name as an empty string

            #Search dictionary for key
            for key in story_keyword:
                #If the key matches the spoken word
                if key['key'] == recog.strip():
                    res = key
                    story_name = res.get('story')
                    print(story_name)                   #Print story name (debug)
                    story_name = story_name + '.wav'    #Add .wav to storyname to match it with the wav sound files


            if story_name == '':
                print("Not Found")

            return story_name

        #Exceptions/Error Catching
        except sr.UnknownValueError:
            print("Google Cloud Speech Recognition could not understand audio")
            story_name = ''
            notRecognized = PlaySound("couldNotUnderstand.mp3")
            notRecognized.play()
            time.sleep(SLEEPTIME)
            return story_name

        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech Recognition service")
            story_name = ''
            notRecognized = PlaySound("couldNotUnderstand.mp3")
            notRecognized.play()
            time.sleep(SLEEPTIME)
            return story_name

        except TimeOUt

#Function to take CSV and make a list of dictionaries
def csv_to_dictionary_list():
    global story_keyword

    with open('stories_keywords.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        story_keyword = list(dict_reader)
        # print list of dict i.e. rows
        print(story_keyword)

        #Returns list of dictionaries
        return story_keyword

def button_story_record(btn):
    keyWord = FindKeyWord()
    storyName = keyWord.recognize()

    #If the string is empty then the keyword was not found
    if (story_name == ''):
        print("Not Found")
        notFound = PlaySound("key_word_not_found.mp3")
        notFound.play()

    else:
        story = PlaySound(story_name)
        story.play_pause()

#Main function
def main():
    print ("Press button once to say a keyword and play a story, and press button twice to record a story and set a keyword and story")
    btn = Button(2)

    while True:
        btn.when_pressed = button_story_record

#Call main function
main()
