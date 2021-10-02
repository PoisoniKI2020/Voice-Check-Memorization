from gtts import gTTS
import pyglet

tts = gTTS('Hello my dear friend', lang='ru')
tts.save('tts_output.mp3')
mus = pyglet.resource.media("tts_output.mp3")
mus.play()

pyglet.app.run()