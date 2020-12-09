import gtts
from playsound import playsound

# make request to google to get synthesis
tts = gtts.gTTS("testing python text to voice conversion")

# save the audio file
tts.save("hello.mp3")
 
#play the sound file
playsound("hello.mp3")

#all available languages with their ITF tag
print(gtts.lang.tts_langs())