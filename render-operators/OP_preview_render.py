from typing import ContextManager
import bpy
from bpy.types import Context, Event, OperatorOptions

# custom print script on load
from print_console import print


class YULA_OT_YTrender(bpy.types.Operator):
    """
    Renders out a final frame preview animation for the given scene.
    This will render every camera in the selected camera collection.
    """

    bl_idname: str = "yrt.render_preview"
    bl_label: str = "Set Preview Render"

    @classmethod
    def poll(cls, context: Context):
        return context.area.type == "VIEW_3D"

    def set_path(self, context: Context):
        context.scene.render.filepath = "/tmp/"
        pass

    def execute(self, context: Context):
        render_settings = context.scene.render

        render_settings.fps = 30
        render_settings.resolution_x = 640
        render_settings.resolution_y = 480

        print("rendering!")
        return {"FINISHED"}


def register():
    bpy.utils.register_class(YULA_OT_YTrender)


def unregister():
    bpy.utils.unregister_class(YULA_OT_YTrender)


if __name__ == "__main__":
    register()
