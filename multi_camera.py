# this module attempts to mimic the houdini ROP network,
# with the ability to output multiple cameras sequentially,
# named in an organized manner.
import bpy
from print_console import print

# get scene for top ref
scene = bpy.context.scene

# cameras
cams = bpy.data.cameras


class CameraHandler:
    def __init__(self) -> None:
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
        print(self._render_path)

    def get_camera_names(self):
        cam_names = [cam.name for cam in cams]
        for name in cam_names:
            print("camera: " + name)

    def render_preview_pixel(self):
        print("not implemented")

    def render_final_pixel(self):
        cam_ops = bpy.ops
        ctx = bpy.context


handler = CameraHandler()
handler.set_camera_path("../../renders")
handler.render_final_pixel()
