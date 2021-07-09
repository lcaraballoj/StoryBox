# StoryBox
This is a voice box that can record multiple stories and upon a key word being said will play the story connected to that key word. 

## Table of Contents
1. [Purpose](#purpose)
2. [Technologies](#technologies)
3. [Hardware](#hardware)
4. [Installation](#installation)
5. [Basic Commands](#basic-commands)
6. [Recording a Story and Setting Story Name and Key Words](#recording-a-story-and-setting-story-name-and-key-words)
7. [Listening to a Story](#listening-to-a-story)
8. [Resources](#resources)
9. [Team Members](#team-members)

## Purpose
This project is a voice box that is triggered by a button and relies on voice commands and key words to play a story. It is similar to Alexa, Siri, and the Google Assistant,  however it is not triggered by saying a keyword like “hey Siri”, instead it will only start to listen once a button is pressed. This is because the voice box is not meant to be as advanced as those softwares, it is instead meant to be an aid for kids and those with special needs. Many times people with special needs repeat themselves and request the same song or story to be read multiple times in a row. The goal of this project is to create a voice box that allows someone with special needs to trigger and request something. The voice box will be individualized and will have the ability to adapt as well as have the ability to be placed in a stuffed animal. So, if for example, a child requests _The Very Hungry Caterpillar_ to be read to them all the time, instead the voice box can be placed inside a stuffed animal of the caterpillar, and the child can press the button and say something like “Very Hungry Caterpillar”, “Caterpillar”, “Hungry Caterpillar”, etc. The voice box will then read the book to them as the preferred person will record the story,set a key word, and story title so that when it is requested the story will be read to them.

## Technologies
* [Python 3.8.1](https://www.python.org/)
* [PyAudio](https://pypi.org/project/PyAudio/)
* [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/docs)
* [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/docs)

## Hardware 
1. Raspberry Pi
2. Speakers
3. Microphone
4. Button

To setup the Raspberry Pi look at the Fritzing layout...

<img src="https://user-images.githubusercontent.com/71469786/117373262-e7135d00-ae98-11eb-9470-646ebc92ca03.jpg" alt="Frtizing" width=40% height=40%>

<img src="https://user-images.githubusercontent.com/71469786/117373285-f2668880-ae98-11eb-8123-045cea3b7f35.jpg" alt="FrontBear" width=40% height=500>      <img src="https://user-images.githubusercontent.com/71469786/117373288-f4304c00-ae98-11eb-93eb-7ea1d3b73c04.jpg" alt="BackBear" width=40% height=500px>


## Installation
1. `Git clone https://github.com/confuzzled-equation/StoryBox.git`
2. Install: `sudo apt-get install portaudio19-dev` **May not need (check)**
3. Install: `sudo apt-get install python-rpi.gpio python3-rpi.gpio` **Only for Raspberry Pi**
4. Open command prompt and cd into folder
5. Run: `pip install -r requirements.txt` **OR** `pip install -r requirements_PC.txt`
      - **Note:** on Windows you cannot install PyAudio through pip, use this link: [PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
      - **Note:** if you get `pygame.error: Failed loading libmpg123.dll` then try uninstalling Pygame and reinstalling it with this link: [Pygame](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame)
6. Make a project in Google Cloud ![Make New Project](https://user-images.githubusercontent.com/71469786/111881416-af069800-8986-11eb-9903-bd5cb28b31a1.gif)

7. Add Google Speech-to-Text and Google Text-to-Speech APIs ![Get APIs](https://user-images.githubusercontent.com/71469786/111881568-5388da00-8987-11eb-888e-9f2e762ee281.gif)

8. Make a service account and save json key to same file location that the code is in ![Service Account and JSON Key](https://user-images.githubusercontent.com/71469786/111881838-d52d3780-8988-11eb-95d6-68a31a8f0b4d.gif)

9. Open **`constant.py`** and make sure your json key is in the right location and change `json_file = ` to your json key file name

10. Check your mic index by running **`FindMicIndex.py`** and change `MIC = ` in the code file **`constant.py`**

11. Run: **`SpeakCommand.py`** first to get all the command audio files needed

12. Run **`ButtonListe.py`** if using button or run **`StoryBox.py`** if using a keyboard

## Basic Commands
* A short button press will allow the user to say a key word and have the story assoicated with that key word, read to them
    * Once story is playing:
        * One button press will cancel the story

## Recording a Story and Setting Story Name and Key Words
To record a story simply run **`StoryBox.py`** and press 1. Users will then be instructed on when to say the keyword, story name, and record the story.
      
      Alternatively: Users can upload their own wav file and go directly into the csv to add the keyword and storyname. 
      The filename must be the same as the story name in the csv but WITHOUT the `.wav`

   * **Note** If you want to delete a story or change a keyword you must navigate to the folder in the Raspberry Pi itself

## Listening to a Story
To listen to a story simply short press the button, wait for the command, and then say a key word. The story will then be played and can be canceled with a button press

      Alternatively: Users can do this from the Python command prompt on your computer with the codeStor yBox.py

## Resources
* [Connecting Bluetooth Devices to Raspberry Pi](https://wiretuts.com/connecting-bluetooth-audio-device-to-raspberry-pi)
* [Finding the Mic Index](https://www.codespeedy.com/print-mic-name-device-id-in-python/)
* [Google Cloud Speech-to-Text Documentation](https://cloud.google.com/speech-to-text/docs/concepts)
* [Integrate Google Cloud Speech-to-Text with Python](https://www.pragnakalp.com/speech-recognition-speech-to-text-python-using-google-api-wit-ai-ibm-cmusphinx/)
* [Using the Google Speech-to-Text API with Python](https://codelabs.developers.google.com/codelabs/cloud-speech-text-python3)

## Team Members
- [Linnea Caraballo](https://github.com/lcaraballoj)
- [Chelsea Coelho](https://github.com/chelseacoelho)
- [Katherine Durkin](https://github.com/StrawberryKat)
