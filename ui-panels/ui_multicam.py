import typing
import bpy
from bpy.types import Context

# import Operators


# MAIN UI
class VIEW_3D_PT_yrt_panel(bpy.types.Panel):
    bl_space_type: typing.Union[str, int] = "VIEW_3D"
    bl_region_type: typing.Union[str, int] = "UI"
    bl_category: str = "Yula Render Tools"
    bl_label: str = "Render"

    def draw(self, context: Context):

        # render column
        col = self.layout.column(align=True)

        # RENDER BUTTON PROPS
        props = col.operator(
            "yrt.render_preview", text="Render Small Preview", icon="RENDER_ANIMATION"
        )
        props.res_x = 640
        props.res_y = 480

        col = self.layout.column(align=True)
        col.prop(context.scene.eevee, "taa_render_samples")
        # SEND EMAIL PROP
        # props = col.operator("yrt.render_preview", text="send email on finish?")
        # props.send_email = col.activate_init
        pass


def register():
    bpy.utils.register_class(VIEW_3D_PT_yrt_panel)


def unregister():
    bpy.utils.unregister_class(VIEW_3D_PT_yrt_panel)


if __name__ == "__main__":
    register()
