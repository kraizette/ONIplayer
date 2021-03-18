from openni import openni2

def getVideo(filename: str):
    openni2.initialize()

    framesColor = []
    framesDepth = []

    file = openni2.Device.open_file(filename.encode('utf-8'))
    cStream = openni2.VideoStream(file, openni2.SENSOR_COLOR)
    dStream = openni2.VideoStream(file, openni2.SENSOR_DEPTH)

    cStream.start()
    dStream.start()
    for i in range(cStream.get_number_of_frames()):
        framesColor.append(cStream.read_frame())
        framesDepth.append(dStream.read_frame())
    cStream.stop()
    dStream.stop()
    return framesColor, framesDepth