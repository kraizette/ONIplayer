from openni import openni2

# https://github.com/thelotusflower/openni-file-player/blob/master/oni_func.py


def getVideo():
    OPENNI_FOLDER_PATH = r"C:\Program Files (x86)\OpenNI2\Redist"
    ONI_VIDEO_PATH = 'D:\Projects\Python\ONI\oni_for_player\cap1.oni'

    openni2.initialize(OPENNI_FOLDER_PATH)

    framesColor = []
    framesDepth = []

    file = openni2.Device.open_file(ONI_VIDEO_PATH.encode('utf-8'))
    file.set_depth_color_sync_enabled
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