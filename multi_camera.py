# this module attempts to mimic the houdini ROP network,
# with the ability to output multiple cameras sequentially,
# named in an organized manner.
import bpy
import print_console

# get scene for top ref
scene = bpy.context.scene

# cameras
cams = bpy.data.cameras


class CameraHandler:
    def __init__(self) -> None:
        pass

    def get_camera_names():
        cam_names = [cam.name for cam in cams]
        for name in cam_names:
            print_console.print("camera: " + name)


CameraHandler.get_camera_names()
