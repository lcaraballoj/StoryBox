import speech_recognition as sr
import csv
import keyboard
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
HOLD_TIME = 10
SLEEP_TIME = 2

#Set global variables
global count
global key_words
global mic
global story_keyword_csv
global story_name

count = 0
mic = 0
story_keyword_csv = "stories_keywords.csv"

json_file = "GCPKey.json"

#Class to record a waw file
class RecordSoundFile():
    #Function that is always initiated
    def __init__(self, filename):
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.fs = 44100
        self.chunk = CHUNK
        self.filename = filename
        self.state = 1

    #Function to record sound and save to wav file
    def record(self):
        p = P #Create interface to PortAudio

        #Open stream
        stream = p.open(format = self.audio_format, channels = self.channels, rate = self.fs,
                        frames_per_buffer = self.chunk, input = True)

        recordData = [] #Initialize array for frames


        #Record sound
        try:
            while self.state == 1:
                print ("Recording...")

                #Record data audio data
                data = stream.read(self.chunk)

                #Add the data to a buffer (a list of chunks)
                recordData.append(data)

                btn = Button(2)
                btn.waitforpress()
                self.state = 0

        #Stop when button is pressed
        except KeyboardInterrupt:
            print("Done recording")

        except Exception as e:
            print(str(e))

        #Stop and close stream and terminate PortAudio
        stream.stop_stream()
        stream.close()
        p.terminate()

        #Save recorded audio to a file
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.audio_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(recordData))
        wf.close()

#Class to play wav file
class PlaySound():
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        mixer.init()
        mixer.music.load(self.filename)
        mixer.music.set_volume(0.5)
        mixer.music.play()

    def play_pause(self):
        mixer.init()
        mixer.music.load(self.filename)
        mixer.music.set_volume(0.5)
        mixer.music.play()

#Class to find if word spoken is a keyword
class FindKeyWord():
    #Function to convert speech-to-text and search for keyword
    def recognize(self):
        global story_name

        #Setting up the Google Speech-to-Text Cloud
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

        r = sr.Recognizer()
        file = sr.Microphone(device_index = mic)

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
            print("You said: " + recog)         #Debugger (prints what you said)

            #Convert CSV file to dictionary
            csv_to_dictionary_list()

            res = None
            #Search dictionary for key
            for key in story_keyword:
                #If the key matches the spoken word
                if key['key'] == recog.strip():
                    res = key
                    story_name = res.get('story')
                    print(story_name) #Print story name
                    story_name = story_name + '.wav' #Add .wav to storyname to match it with the wav sound files
                    return story_name

                    break

                else:
                    print("Not Found") #Debugging (need to find way to just say not found if keyword is not found in any list)

        #Exceptions/Error Catching
        except sr.UnknownValueError:
            print("Google Cloud Speech Recognition could not understand audio")
            story_name = ''
            notRecognized = PlaySound("couldNotUnderstand.mp3")
            notRecognized.play()
            time.sleep(SLEEP_TIME)
            return story_name

        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech Recognition service; {0}".format(e))
            story_name = ''
            notRecognized = PlaySound("couldNotUnderstand.mp3")
            notRecognized.play()
            time.sleep(SLEEP_TIME)
            return story_name

def story_name():
        global story

        #Setup Google Speech-to-Text evironment
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

        r = sr.Recognizer()
        file = sr.Microphone(device_index = mic)

        with file as source:
            print("What is the story name for the key word?")
            command = PlaySound("story_name_set.mp3")
            command.play()
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            story = r.recognize_google_cloud(audio, language = 'en-US')
            print("You said: " + story)
            return story.strip() #Get rid of spaces at beginning and end of string

        #Exceptions/Error Catching
        except sr.UnknownValueError:
            print("Google Cloud Speech Recognition could not understand audio")
            notRecognized = PlaySound("couldNotUnderstand.mp3")
            notRecognized.play()
            time.sleep(SLEEP_TIME)
            story_name()

        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech Recognition service; {0}".format(e))
            notRecognized = PlaySound("couldNotUnderstand.mp3")
            notRecognized.play()
            time.sleep(SLEEP_TIME)
            story_name()

#Function to define a keyword
def define_keyword_storyname():
    #global variables
    global temp_story_keyword
    global story_title

    #Setup temporary dictionary to hold key and values
    temp_story_keyword = {}

    #Setup Google Speech-to-Text evironment
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

    r = sr.Recognizer()
    file = sr.Microphone(device_index = mic)

    with file as source:
        print("Say a word to set it as a key word")
        command = PlaySound("key_word_Set.mp3")
        command.play()
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        recog = r.recognize_google_cloud(audio, language = 'en-US')
        print("You said: " + recog)
        #Call "remove" function to take away spaces in story name
        story_title = remove(story_name())
        #Call story_name function and set that to pair with the keyword
        temp_story_keyword[recog.strip()] = story_title
        print("Recorded in CSV File") #Debug

        #Append data to csv file to save
        with open(story_keyword_csv, 'a') as f:
            writer = csv.writer(f)
            for k, v in temp_story_keyword.items():
                writer.writerow([k, v])

        return story_title

    #Exceptions/Error Catching
    except sr.UnknownValueError:
        print("Google Cloud Speech Recognition could not understand audio")
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(SLEEP_TIME)
        define_keyword_storyname()

    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech Recognition service; {0}".format(e))
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(SLEEP_TIME)
        define_keyword_storyname()

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

#Function to remove spaces in a string
def remove(string_input):
    return string_input.replace(" ", "")

#Function for button press once story is being read
def button_pause_play(btn):
    global HOLD_TIME

    pause = False
    start_time = time.time()
    diff = 0

    while btn.is_active and (diff < hold_time):
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

def button_story_record(btn):
        global HOLD_TIME

        start_time = time.time()
        diff = 0

        storyname = ''

        while btn.is_active and (diff < HOLD_TIME):
            current_time = time.time()
            diff = current_time - start_time

        #Short press activates listen for keyword and then play story if found
        if diff < HOLD_TIME:
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
        #Long press activates recording story and setting keyword and story name
        else:
            #storyname = ''
            storyname = define_keyword_storyname()
            recordStory = RecordSoundFile(storyname + 'wav')
            recordStory.record()

#Main function
def main():
    print ("Press button once to say a keyword and play a story, and press button twice to record a story and set a keyword and story")
    btn = Button(2)

    while True:
        btn.when_pressed = button_story_record


#Call main function
main()
