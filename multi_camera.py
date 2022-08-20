# this module attempts to mimic the houdini ROP network,
# with the ability to output multiple cameras sequentially,
# named in an organized manner.
import bpy
from enum import Enum
from print_console import print


class LogType(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERR = "ERR"
    OK = "OK"


"""
Log - utility class to keep logs consistent.
"""


class Log:
    def __init__(self, log_type: LogType, value) -> None:
        print({"type": log_type.value, "value": value})


class CameraHandler:
    def __init__(self) -> None:
        # get scene for top ref
        scene = bpy.context.scene
        self.scene = scene
        pass

    """
    set_consistent_cameras - sets consistent naming convention
    for each camera in the scene, referencing the project name given.
     """

    def set_consistent_cameras(self):
        print("not implemented")

    """
    set_camera_path - sets the path for each camera to render frames to. 
    """

    def set_camera_path(self, path: str):
        # set the path for all the camera outputs.
        self._render_path = bpy.path.abspath(path)
        print(Log(LogType.INFO, "camera path set to " + self._render_path))

    def get_camera_names(self):
        # cameras
        cams = bpy.data.cameras
        cam_names = [cam.name for cam in cams]
        for name in cam_names:
            print(Log(LogType.INFO, name))

    def render_preview_pixel(self):

        print("not implemented")

    def render_final_pixel(self):
        cam_ops = bpy.ops
        ctx = bpy.context


handler = CameraHandler()
handler.set_camera_path("../../renders")
handler.render_final_pixel()
