import speech_recognition as sr     #Spech Recognition
import os                           #Operating system for speech-to-text
import keyboard                     #Keyboard Library
import pyaudio                      #Pyaudio to record sound
import wave                         #Ability to play and save wave files
import csv                          #csv files and functions


from csv import DictReader          #Used to add values and read values from a csv file
from pygame import mixer            #Used to play, pause, and stop sound

CHUNK = 1024
P = pyaudio.PyAudio() #Create interface to PortAudio

#Set a global variables
global key_words
global story_name
global mic
global story_keyword_csv

# csv file that holds the key words and story names
story_keyword_csv = "stories_keywords.csv"

#json file that is needed for GCP (Google Cloud Platform)
json_file = "GCPKey.json"

#Set mic index
mic = 1

#Class to record a wav file
class RecordSoundFile():
    #Function that is always initiated
    def __init__(self, filename):
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.fs = 44100
        self.chunk = CHUNK
        self.filename = filename

    #Function to record sound and save to a wav file
    def record(self):
        p = P #Create interface to PortAudio

        #open stream
        stream = p.open(format = self.audio_format, channels = self.channels, rate = self.fs,
                        frames_per_buffer = self.chunk, input = True)

        recordData = [] #Initialize array for frames

        #Instructions to User
        print("Press ctr+C to stop recording")

        #Record sound
        try:
            while True:
                print("Recording...")           #Debugging line to make sure it is running

                # Record data audio data
                data = stream.read(self.chunk)

                # Add the data to a buffer (a list of chunks)
                recordData.append(data)

        #Stop when keyboard interrupts (ctr+C is pressed)
        except KeyboardInterrupt:
            print("Done Recording")

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
    #Function that is always initiated
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        mixer.init()
        mixer.music.load(self.filename)         #Load file
        mixer.music.set_volume(0.5)             #Set volume
        mixer.music.play()                      #Play sound volume at desired volume

    #Function to play, pause, resume, and stop an audio file
    def play_pause(self):
        mixer.init()
        mixer.music.load(self.filename)
        mixer.music.set_volume(0.5)
        mixer.music.play()

        while True:
            #Pause, resume, exit
            print("Press 'p' to pause, 'r' to resume")
            print("Press 'e' to exit the program")
            query = input("  ")

            if query == 'p':

                # Pausing the music
                mixer.music.pause()
            elif query == 'r':

                # Resuming the music
                mixer.music.unpause()
            elif query == 'e':

                # Stop the mixer
                mixer.music.stop()
                break

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

            recog = recog.strip()

            #Search dictionary for key
            for key in story_keyword:
                #If the key matches the spoken word
                if key['key'] == recog.strip():
                    res = key
                    story_name = res.get('story')
                    print(story_name) #Print story name
                    story_name = story_name + '.wav' #Add .wav to storyname to match it with the wav sound files
                    return story_name

                else:
                    print("Not Found") #Debugging (need to find way to just say not found if keyword is not found in any list)
                    story_name = ''
                    return story_name    #Returns empty string for exception handeling

                # found = recog.find(key['key'])
                #
                # if (found == -1):                    #If keyword not found
                #     print ("Not found")
                #
                # else:                                #If key word is found
                #     print ("Found")
                #     res = key
                #     story_name = res.get('story')       #Get story name from key
                #     print(story_name)                   #Debug
                #     story_name = story_name + '.wav'    #Add .wav to storyname to get correct sound file
                #     return story_name


        #Exceptions/Error Catching
        except sr.UnknownValueError:
            print("Google Cloud Speech Recognition could not understand audio")
            story_name = ''
            return story_name

        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech Recognition service")
            story_name = ''
            return story_name


#Function to define a storyname
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
            story_name()

        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech Recognition service")
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

        # print(temp_story_keyword)
        # return temp_story_keyword

    #Exceptions/Error Catching
    except sr.UnknownValueError:
        print("Google Cloud Speech Recognition could not understand audio")
        define_keyword_storyname()

    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech Recognition service; {0}".format(e))
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

#Main function
def main():
    while True:
        choice = input("Press 1 to record and 2 to listen: ")

        if choice == '1':
            newChoice = input("Press 1 to record story and 2 to record key word: ")
            if newChoice == '1':
                storyname = define_keyword_storyname()          #Call function to set keyword and story name and set story_title to story_name
                recordStory = RecordSoundFile(storyname+'.wav') #Set file name and call RecordSoundFile class (add .wav to make it a wav file)
                recordStory.record()                            #Call record functionn in RecordSoundFile class


            if newChoice == '2':
                define_keyword_storyname()


        if choice == '2':
            keyWord = FindKeyWord()
            story_name = keyWord.recognize()

            #If the string is empty then the keyword was not found
            if (story_name == ''):
                print("Not Found")

            else:
                story = PlaySound(story_name)
                story.play_pause()



#Call main function
main()
