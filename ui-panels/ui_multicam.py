import typing
import bpy
import bpy
from bpy.types import Context


class VIEW_3D_PT_yrt_panel(bpy.types.Panel):
    bl_space_type: typing.Union[str, int] = "VIEW_3D"
    bl_region_type: typing.Union[str, int] = "UI"
    bl_category: str = "Yula Render Tools"
    bl_label: str = "Render"

    def draw(self, context: Context):
        pass


def register():
    bpy.utils.register_class(VIEW_3D_PT_yrt_panel)


def unregister():
    bpy.utils.unregister_class(VIEW_3D_PT_yrt_panel)


if __name__ == "__main__":
    register()
