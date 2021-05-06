
import constant

from gpiozero import Button
from datetime import datetime, timedelta
from Record_Play import RecordSoundFile, PlaySound
from Find_Story_Keyword import FindKeyWord, story_name, define_keyword_storyname

def button_story_record(btn):
    keyWord = FindKeyWord()
    story_name = keyWord.recognize()

    #If the string is empty then the keyword was not found
    if (story_name == ''):
        print("Not Found")
        notFound = PlaySound("key_word_not_found.mp3")
        notFound.play()

    else:
        story = PlaySound(story_name)
        story.play()

#Main function
def main():
    print ("Press the button and say a key word to listen")
    instruction = PlaySound("buttonCommand.mp3")
    instruction.play()
    btn = Button(2)

    while True:
        btn.when_pressed = button_story_record

#Call main function
main()
