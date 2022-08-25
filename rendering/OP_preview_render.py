import bpy
from bpy.types import Context

# custom print script on load
from print_console import print


class YULA_OT_YTrender(bpy.types.Operator):
    """
    Renders out a final frame preview animation for the given scene.
    This will render every camera in the selected camera collection.
    """

    bl_idname: str = "yrt.render_preview"
    bl_label: str = "Set Preview Render"
    # prop
    res_x: bpy.props.IntProperty(
        name="X Resolution",
        description="resolution of X in pixels",
        default=1920,
        min=256,
        soft_max=4096,
    )
    # prop
    res_y: bpy.props.IntProperty(
        name="Y Resolution",
        description="resolution of Y in pixels",
        default=1080,
        min=256,
        soft_max=4096,
    )

    # prop
    send_email: bpy.props.BoolProperty(
        name="Send Email",
        description="send an email over smtp server once render is done",
        default=False,
    )

    @classmethod
    def poll(cls, context: Context):
        return context.area.type == "VIEW_3D"

    def set_path(self, context: Context):
        context.scene.render.filepath = "/tmp/"
        pass

    def send_to_email(self, context: Context):
        """Sends an email after the render is done"""
        if context.scene.yrt_tool.send_email:
            print("sending email")

    def execute(self, context: Context):
        render_settings = context.scene.render

        # always 30fps
        render_settings.fps = 30

        render_settings.resolution_x = self.res_x
        render_settings.resolution_y = self.res_y

        print(
            "rendering info: {} {}".format(
                render_settings.resolution_x, render_settings.resolution_y
            )
        )
        print(context.scene.yrt_tool.my_bool)
        return {"FINISHED"}
