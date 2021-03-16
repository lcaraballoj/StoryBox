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
* [Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/)

## Hardware 
1. Raspberry Pi
2. Speakers
3. Microphone
4. Button

To setup the Raspberry Pi look at the Fritzing layout...

## Installation



## Basic Commands
* One button press will allow the user to say a key word and have the story read to them
    Once story is being read:
      * One button press will pause the story
      * Two button presses will cancel the story
* Two button presses will allow a person to record a story, set a key word, and story name
* Three button presses will allow for anothe key word to be set for a story title that already exists

## Recording a Story and Setting Story Name and Key Words
To record a story simply press the button twice. You will then be prompted to say a key word and then a story name. After that you can read the story and when done reading the story press the button to stop. Your recording will then be played back to you and you can choose to keep it or discard it. 

    Alternatively: You can do this from the Python command prompt on your computer with the code StoryBoxKeyboard.py

## Listening to a Story
To listen to a story simply press the button once, wait for the beep, and then say a key word. The story will then be played and can be pause with one button press or canceled with two button presses. 

## Team Members
- Linnea Caraballo
- Chelsea Coelho
- Katherine Durkin
