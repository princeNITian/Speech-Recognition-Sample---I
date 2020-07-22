import pyglet

file = pyglet.resource.media('test.mp3')

file.play()

pyglet.app.run()