#Main code

import keyboard                     #Keyboard Library
import constant

from Record_Play import RecordSoundFile, PlaySound      #File that has classes to record and play
from Find_Story_Keyword import FindKeyWord, story_name, define_keyword_storyname

#Main function
def main():
    instruction = PlaySound("instructionCommand.mp3")
    instruction.play()

    while True:
        choice = input("Press 1 to record and 2 to listen: ")
        print(constant.JSON_FILE)

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
