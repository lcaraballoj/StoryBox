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
8. [Team Members](#team-members)

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

## Installation
1. `Git clone https://github.com/confuzzled-equation/StoryBox.git`
2. Install: `sudo apt-get install portaudio19-dev` **May not need (check)**
3. Install: `sudo apt-get install python-rpi.gpio python3-rpi.gpio` **Only for Raspberry Pi**
4. Open command prompt and cd into folder
5. Run: `pip install -r requirements.txt`
      **Note:** on Windows you cannot install PyAudio through pip, use this link: [PyAudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
      **Note:** if you get `pygame.error: Failed loading libmpg123.dll` then try uninstalling Pygame and [reinstalling it]
 ()
6. Make a project in Google Cloud ![Make New Project](https://user-images.githubusercontent.com/71469786/111881416-af069800-8986-11eb-9903-bd5cb28b31a1.gif)

7. Add Google Speech-to-Text and Google Text-to-Speech APIs ![Get APIs](https://user-images.githubusercontent.com/71469786/111881568-5388da00-8987-11eb-888e-9f2e762ee281.gif)

8. Make a service account and save json key to same file location that the code is in ![Service Account and JSON Key](https://user-images.githubusercontent.com/71469786/111881838-d52d3780-8988-11eb-95d6-68a31a8f0b4d.gif)

9. Run: **`SpeakCommand.py`** first to get all the command audio files needed

10. Open **`StoryBox.py`** and make sure your json key is in the right location and change `json_file = ` to your json key file name

## Basic Commands
* One button press will allow the user to say a key word and have the story assoicated with that key word, read to them
    * Once story is playing:
        * One button press will pause the story
        * Two button presses will cancel the story
* Two button presses will allow a person to record a story, set a key word and story title that will be associated with it
* Three button presses will allow for another key word to be set for an already existing story title

## Recording a Story and Setting Story Name and Key Words
To record a story simply press the button twice. You will then be prompted to say a key word and then a story name. After that you can read the story and when done reading the story press the button to stop. Your recording will then be played back to you and you can choose to keep it or discard it. 

    Alternatively: You can do this from the Python command prompt on your computer with the code StoryBoxKeyboard.py

## Listening to a Story
To listen to a story simply press the button once, wait for the beep, and then say a key word. The story will then be played and can be pause with one button press or canceled with two button presses. 

## Team Members
- [Linnea Caraballo](https://github.com/confuzzled-equation)
- [Chelsea Coelho](https://github.com/chelseacoelho)
- [Katherine Durkin](https://github.com/StrawberryKat)
