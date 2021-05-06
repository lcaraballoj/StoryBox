#Code to record and play audio files

import pyaudio                      #Pyaudio to record sound
import wave                         #Ability to play and save wave files
import constant

from pygame import mixer            #Used to play, pause, and stop sound

# CHUNK = 1024
P = pyaudio.PyAudio() #Create interface to PortAudio

#Class to record a wav file
class RecordSoundFile():
    #Function that is always initiated
    def __init__(self, filename):
        self.audio_format = pyaudio.paInt16
        self.channels = 1
        self.fs = 44100
        self.chunk = constant.CHUNK
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
