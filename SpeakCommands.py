#Code to take text and implement the Google Text-to-Speech API to create audio files for the commands

#Import os and texttospeech from the Google cloud
import os
from google.cloud import texttospeech

#Set json key as a global variable and set value
global json_file

json_file = "GCPKey.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

#Class to take text and synthesize a voice
class Speak():
    def __init__(self, text, filename):
        self.text = text
        self.filename = filename

    def talk(self):
        # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=self.text)

        # Build the voice request, select the language code ("en-US") and the ssml
        #Name can be changed
        # voice gender ("neutral") [THIS CAN BE CHANGED]
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name = "en-US-Wavenet-H",
            ssml_gender = texttospeech.SsmlVoiceGender.FEMALE
        )

        # Select the type of audio file you want returned
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # The response's audio_content is binary.
        with open(self.filename, "wb") as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written')

def list_voices():
    #Lists the available voices.
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print(f"Name: {voice.name}")

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            print(f"Supported language: {language_code}")

        ssml_gender = texttospeech.SsmlVoiceGender(voice.ssml_gender)

        # Display the SSML Voice Gender
        print(f"SSML Voice Gender: {ssml_gender.name}")

        # Display the natural sample rate hertz for this voice. Example: 24000
        print(f"Natural Sample Rate Hertz: {voice.natural_sample_rate_hertz}\n")


#Call to get list of all the voices available, simply uncomment this and comment out call to the Speak class
#list_voices()

#Command to say key word
keyWordCommand = Speak("Say a key word", "key_word_command.mp3")
keyWordCommand.talk()

#Command to set key word
keyWordSet = Speak("Say a key word to set it", "key_word_Set.mp3")
keyWordSet.talk()

#Command to set story title
storyNameSet = Speak("Say the name of the story", "story_name_set.mp3")
storyNameSet.talk()

keyWordNotFound = Speak("The key word was not found. Try again.", "key_word_not_found.mp3")
keyWordNotFound.talk()

instructionCommand = Speak("Press 1 to set a key word, story name, and record the story. Press 2 and say a key word to listen",
"instructionCommand.mp3")
instructionCommand.talk()

buttonCommand = Speak("Press the button and say a key word to listen", "buttonCommand.mp3")
buttonCommand.talk()

couldNotUnderstand = Speak("Could not understand.", "couldNotUnderstand.mp3")
couldNotUnderstand.talk()
