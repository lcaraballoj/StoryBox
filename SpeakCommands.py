#Code to take text and implement the Google Text-to-Speech API to create audio files for the commands
import os

from google.cloud import texttospeech

global json

json_file = "GCPKey.json"

class Speak():
    def __init__(self, text, filename):
        self.text = text
        self.filename = filename

    def talk(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_file

        # Instantiates a client
        client = texttospeech.TextToSpeechClient()

        # Set the text input to be synthesized
        synthesis_input = texttospeech.SynthesisInput(text=self.text)

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
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
