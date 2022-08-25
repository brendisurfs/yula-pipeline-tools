# this module attempts to mimic the houdini ROP network,
# with the ability to output multiple cameras sequentially,
# named in an organized manner.
from typing import Any
import bpy
import os
from enum import Enum

from bpy.types import Object
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
    def __init__(self, log_type: LogType, value: Any) -> None:
        print({"type": log_type.value, "value": value})


class SCENE_OT_CameraHandler:
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
        self.__render_path__ = bpy.path.abspath(path)
        Log(LogType.INFO, "camera path set to " + self.__render_path__)

    def __get_camera_collection__(self):
        camera_collection = self.scene.collection.children["Cameras"].all_objects
        return camera_collection

    def get_camera_names(self):
        # cameras
        cams = bpy.data.cameras
        cam_names = [cam.name for cam in cams]
        for name in cam_names:
            Log(LogType.INFO, name)

    def __format_camera_name__(self, obj: Object):
        format_splitter = "_"
        split_name = [char for char in obj.name.strip(" ").split(" ")]
        formatted_name = format_splitter.join(split_name)
        return formatted_name

    def render_preview_pixel(self):
        camera_collection = self.__get_camera_collection__()

        # important render params
        self.scene.render.fps = 30
        self.scene.render.resolution_x = 640
        self.scene.render.resolution_y = 480

        x_resolution = self.scene.render.resolution_x
        y_resolution = self.scene.render.resolution_y

        for cam in camera_collection:
            formatted_name = self.__format_camera_name__(cam)

            if self.__render_path__ is not None:
                # if subdir not found,
                # make subdir
                # else, use that subdir.

                render_subdir = (
                    self.__render_path__.rstrip("/")
                    + ("/")
                    + "Finals"
                    + ("/")
                    + formatted_name
                    + ("/")
                )
                file_name = "{0}_{1}x{2}".format(
                    formatted_name, str(x_resolution), str(y_resolution)
                )
                print(file_name)
                # render each frame
                self.scene.camera = cam
                self.scene.render.filepath = render_subdir
                print("filepath: ", self.scene.render.filepath)
                # set + use preview settings before rendering
                # bpy.ops.render.render()

    def render_final_pixel(self):
        camera_collection = self.__get_camera_collection__()

        # important render params
        self.scene.render.fps = 30
        self.scene.render.resolution_x = 1920
        self.scene.render.resolution_y = 1080

        x_resolution = self.scene.render.resolution_x
        y_resolution = self.scene.render.resolution_y

        for cam in camera_collection:
            formatted_name = self.__format_camera_name__(cam)

            if self.__render_path__ is not None:
                # if subdir not found,
                # make subdir
                # else, use that subdir.

                render_subdir = (
                    self.__render_path__.rstrip("/")
                    + ("/")
                    + "Finals"
                    + ("/")
                    + formatted_name
                    + ("/")
                )

                file_name = "{0}_{1}x{2}".format(
                    formatted_name, str(x_resolution), str(y_resolution)
                )
                print(file_name)
                # render each frame
                self.scene.camera = cam
                self.scene.render.filepath = render_subdir

                print("filepath: ", self.scene.render.filepath)
                # set + use final render settings before rendering
                # bpy.ops.render.render()
            else:
                return


handler = SCENE_OT_CameraHandler()
handler.set_camera_path("../../renders")
handler.get_camera_names()
handler.render_preview_pixel()
