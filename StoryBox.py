import speech_recognition as sr     #Spech Recognition
import os                           #Operating system for speech-to-text
import keyboard                     #Keyboard Library
# import pyaudio                    #Pyaudio to record sound
# import wave                       #Ability to play and save wave files
import csv                          #csv files and functions
import time


from csv import DictReader                              #Used to add values and read values from a csv file
# from pygame import mixer                              #Used to play, pause, and stop sound
from Record_Play import RecordSoundFile, PlaySound      #File that has classes to record and play

# CHUNK = 1024
# P = pyaudio.PyAudio() #Create interface to PortAudio

#Global Constants
STORY_KEYWORD_CSV = "stories_keywords.csv"  # csv file that holds the key words and story names
JSON_FILE = "GCPKey.json"                   #json file that is needed for GCP (Google Cloud Platform)
MIC = 1                                     #Set mic index
SLEEPTIME = 2

#Class to find if word spoken is a keyword
class FindKeyWord():
    #Function to convert speech-to-text and search for keyword
    def recognize(self):

        #Setting up the Google Speech-to-Text Cloud
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = JSON_FILE

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


#Function to define a storyname
def story_name():

    #Setup Google Speech-to-Text evironment
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = JSON_FILE

    r = sr.Recognizer()
    file = sr.Microphone(device_index = MIC)

    with file as source:
        print("What is the story name for the key word?")
        command = PlaySound("story_name_set.mp3")
        command.play()
        audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        story = r.recognize_google_cloud(audio, language = 'en-US')
        print("You said: " + story)
        print (story.strip())
        return story.strip() #Get rid of spaces at beginning and end of string

    #Exceptions/Error Catching
    except sr.UnknownValueError:
        print("Google Cloud Speech Recognition could not understand audio")
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(SLEEPTIME)
        return story_name()

    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech Recognition service")
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(SLEEPTIME)
        return story_name()

#Function to define a keyword
def define_keyword_storyname():
    #global variables
    global temp_story_keyword
    global story_title

    #Setup temporary dictionary to hold key and values
    temp_story_keyword = {}

    #Setup Google Speech-to-Text evironment
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = JSON_FILE

    r = sr.Recognizer()
    file = sr.Microphone(device_index = MIC)

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
        story_title = story_name()
        print (story_title)
        story_title = remove(story_title)
        #Call story_name function and set that to pair with the keyword
        temp_story_keyword[recog.strip()] = story_title
        print("Recorded in CSV File") #Debug

        #Append data to csv file to save
        with open(STORY_KEYWORD_CSV, 'a') as f:
            writer = csv.writer(f)
            for k, v in temp_story_keyword.items():
                writer.writerow([k, v])

        return story_title

    #Exceptions/Error Catching
    except sr.UnknownValueError:
        print("Google Cloud Speech Recognition could not understand audio")
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(SLEEPTIME)
        return define_keyword_storyname()

    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech Recognition service; {0}".format(e))
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(SLEEPTIME)
        return define_keyword_storyname()

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

#Main function
def main():
    instruction = PlaySound("instructionCommand.mp3")
    instruction.play()

    while True:
        choice = input("Press 1 to record and 2 to listen: ")

        if choice == '1':
            #storyname = ''
            storyname = define_keyword_storyname()          #Call function to set keyword and story name and set story_title to story_name
            recordStory = RecordSoundFile(storyname+'.wav') #Set file name and call RecordSoundFile class (add .wav to make it a wav file)
            recordStory.record()                            #Call record functionn in RecordSoundFile class


        if choice == '2':
            keyWord = FindKeyWord()
            story_name = keyWord.recognize()

            #If the string is empty then the keyword was not found
            if (story_name == ''):
                print("Not Found")
                notFound = PlaySound("key_word_not_found.mp3")
                notFound.play()

            else:
                story = PlaySound(story_name)
                story.play_pause()

#Call main function
main()
