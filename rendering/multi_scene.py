import bpy
from bpy.props import StringProperty

from print_console import print

scenes = bpy.data.scenes

scene_store = []

# filter out scenes
for scene in scenes:
    scene_name: str = scene.name_full
    camera_name = scene.camera.name_full
    scene.render.use_stamp = False

    # settings for output
    render_settings = scene.render.image_settings
    render_settings.file_format = "JPEG"
    render_settings.quality = 100
    output_path = scene.render.filepath

    if "YU-" in scene_name:
        print(scene_name, camera_name, output_path)
        scene_store.append(scene)
        # bpy.ops.render.render(animation=True)

for sc in scene_store:
    print(sc.name)


class MultiScene_Render(bpy.types.Operator):
    bl_idname: str = "render.every_scene"
    bl_label: str = "Render Every Scene"

    base_path: StringProperty(name="Path")

    # -------------------
    # internal variables

    cancel_render = None
    is_rendering = None
    render_queue = []
    timer_event = None

    def pre_render(self, ctx):
        self.is_rendering = True

    def post_render(self, ctx):
        self.render_queue.pop(0)
        self.is_rendering = False

    def on_render_cancel(self, ctx):
        self.cancel_render = True

    def execute(self, ctx):
        self.cancel_render = False
        self.is_rendering = False
