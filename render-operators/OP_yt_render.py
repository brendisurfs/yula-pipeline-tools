import bpy
from bpy.types import Context, Event


class YULA_OT_YTrender(bpy.types.Operator):
    """Tooltip here"""

    bl_idname: str = "yrt.render_preview"
    bl_label: str = "Set Preview Render"

    def execute(self, context: Context):
        scene = context.scene
        render_settings = scene.render
        render_settings.resolution_x = 640
        render_settings.resolution_y = 480
        return {"FINISHED"}


def register():
    bpy.utils.register_class(YULA_OT_YTrender)


def unregister():
    bpy.utils.unregister_class(YULA_OT_YTrender)


if __name__ == "__main__":
    register()
