import typing
import bpy

from bpy.props import PointerProperty
from bpy.types import AnyType, Point

from print_console import print


class MULTICAM_PT_layout_panel(bpy.types.Panel):
    bl_label: str = "MultiCam"
    bl_category: str = "Multi Cam"
    bl_space_type: typing.Union[str, int] = "VIEW_3D"
    bl_region_type: typing.Union[str, int] = "UI"

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        col = layout.column()
        col.prop(scene, "camera_collection")


def register():
    scene_collection = bpy.types.Scene

    camera_collection = PointerProperty(
        name="Camera Collection", type=bpy.types.Collection
    )
    scene_collection.camera_collection = camera_collection

    bpy.utils.register_class(MULTICAM_PT_layout_panel)

    stored_camera_collection = bpy.context.scene.camera_collection


def unregister():
    bpy.utils.unregister_class(MULTICAM_PT_layout_panel)
    del bpy.types.Scene.camera_collection


if __name__ == "__main__":
    register()
