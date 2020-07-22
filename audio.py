import pyglet

file = pyglet.resource.media('audio/wet.mp3')

file.play()

pyglet.app.run()