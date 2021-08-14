import constant                                                                       #Calling constants from constant.py to use

from gpiozero import Button                                                           #Importing button functionality from gpiozero
from Record_Play import RecordSoundFile, PlaySound                                    #Calling function to record and play sound from Record_play.py
from Find_Story_Keyword import FindKeyWord, story_name, define_keyword_storyname      #Calling all functions/classes from Find_Story_Keyword.py

#Function that takes in button input and then runs code to ask for a keyword and then searches for it to play the matching story
def button_story_record(btn):
    keyWord = FindKeyWord()                     #Run class that asks for keyword
    story_name = keyWord.recognize()            #Run function that takes speech and converts it to text and then searches

    #If the string is empty then the keyword was not found
    if (story_name == ''):
        print("Not Found")
        notFound = PlaySound("key_word_not_found.mp3")
        notFound.play()

    #If keyword found then play the matching story
    else:
        story = PlaySound(story_name)
        story.play()

#Main function
def main():
    print ("Press the button and say a key word to listen")
    instruction = PlaySound("buttonCommand.mp3")
    instruction.play()
    btn = Button(2)                                 #Initializing the button with correction GPIO pin

    #Wait for button press
    while True:
        btn.when_pressed = button_story_record      #When button press indicated run function

#Call main function
main()
