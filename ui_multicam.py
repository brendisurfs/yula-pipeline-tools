import typing
import bpy
from bpy.ops import scene
from bpy.props import BoolProperty, PointerProperty
from bpy.types import Context

# import Operators
from rendering import OP_preview_render


# Settings class
class YulaUISettings(bpy.types.PropertyGroup):
    send_email: BoolProperty(
        name="Test enable or disable", description="bool prop", default=False
    )


# --------------------
# MAIN UI
# --------------------
class VIEW_3D_PT_yrt_panel(bpy.types.Panel):
    bl_space_type: typing.Union[str, int] = "VIEW_3D"
    bl_region_type: typing.Union[str, int] = "UI"
    bl_category: str = "Yula Render Tools"
    bl_label: str = "Render"

    def draw(self, context: Context):
        layout = self.layout
        # render column
        col = self.layout.column(align=True)
        # RENDER BUTTON PROPS
        props = col.operator(
            "yrt.render_preview", text="Render Small Preview", icon="RENDER_ANIMATION"
        )

        props.res_x = 640
        props.res_y = 480

        # render 1:1 large render
        props = col.operator(
            "yrt.render_preview", text="Render Square Preview", icon="RENDER_ANIMATION"
        )
        props.res_x = 512
        props.res_y = 512

        # Add render samples
        # col = self.layout.column(align=True)
        # col.prop(context.scene.eevee, "taa_render_samples")

        # SEND EMAIL PROP
        layout.prop(context.scene.yrt_tool, "send_email", text="Send email on finish?")
        pass


# Register
ui_classes = (
    YulaUISettings,
    VIEW_3D_PT_yrt_panel,
)


def register():

    bpy.utils.register_class(YulaUISettings)
    bpy.utils.register_class(OP_preview_render.YULA_OT_YTrender)
    bpy.utils.register_class(VIEW_3D_PT_yrt_panel)

    bpy.types.Scene.yrt_tool = PointerProperty(type=YulaUISettings)


def unregister():
    bpy.utils.unregister_class(YulaUISettings)
    bpy.utils.unregister_class(OP_preview_render.YULA_OT_YTrender)
    bpy.utils.unregister_class(VIEW_3D_PT_yrt_panel)

    # del bpy.types.Scene.yrt_tool


if __name__ == "__main__":
    register()
