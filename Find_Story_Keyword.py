#Code to set a key word, story name, and record the story

import speech_recognition as sr     #Spech Recognition
import os                           #Operating system for speech-to-text
import csv
import constant

from Record_Play import PlaySound
from csv_dictionary import csv_to_dictionary_list
from Remove import remove

#Class to find if word spoken is a keyword
class FindKeyWord():
    #Function to convert speech-to-text and search for keyword
    def recognize(self):

        #Setting up the Google Speech-to-Text Cloud
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = constant.JSON_FILE

        r = sr.Recognizer()
        file = sr.Microphone(device_index = constant.MIC)

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
            time.sleep(constant.SLEEP_TIME)
            return story_name

        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech Recognition service")
            story_name = ''
            notRecognized = PlaySound("couldNotUnderstand.mp3")
            notRecognized.play()
            time.sleep(constant.SLEEP_TIME)
            return story_name


#Function to define a storyname
def story_name():

    #Setup Google Speech-to-Text evironment
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = constant.JSON_FILE

    r = sr.Recognizer()
    file = sr.Microphone(device_index = constant.MIC)

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
        time.sleep(constant.SLEEP_TIME)
        return story_name()

    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech Recognition service")
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(constant.SLEEP_TIME)
        return story_name()

#Function to define a keyword
def define_keyword_storyname():
    # #global variables
    # global temp_story_keyword
    # global story_title

    #Setup temporary dictionary to hold key and values
    temp_story_keyword = {}

    #Setup Google Speech-to-Text evironment
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = constant.JSON_FILE

    r = sr.Recognizer()
    file = sr.Microphone(device_index = constant.MIC)

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
        story_title = remove(story_title)

        #Call story_name function and set that to pair with the keyword
        temp_story_keyword[recog.strip()] = story_title
        print("Recorded in CSV File")                   #Debug

        #Append data to csv file to save
        with open(constant.STORY_KEYWORD_CSV, 'a') as f:
            writer = csv.writer(f)
            for k, v in temp_story_keyword.items():
                writer.writerow([k, v])

        return story_title

    #Exceptions/Error Catching
    except sr.UnknownValueError:
        print("Google Cloud Speech Recognition could not understand audio")
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(constant.SLEEP_TIME)
        return define_keyword_storyname()

    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech Recognition service; {0}".format(e))
        notRecognized = PlaySound("couldNotUnderstand.mp3")
        notRecognized.play()
        time.sleep(constant.SLEEP_TIME)
        return define_keyword_storyname()
