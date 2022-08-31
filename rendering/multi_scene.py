import bpy
from bpy.props import CollectionProperty, StringProperty
from bpy.types import BlendDataScenes, Context, Scene, SceneObjects, bpy_prop_collection

from print_console import print

# scenes = bpy.data.scenes

# scene_store = []

# # filter out scenes
# for scene in scenes:
#     scene_name: str = scene.name_full
#     camera_name = scene.camera.name_full
#     scene.render.use_stamp = False

#     # settings for output
#     render_settings = scene.render.image_settings
#     render_settings.file_format = "JPEG"
#     render_settings.quality = 100
#     output_path = scene.render.filepath

#     if "YU-" in scene_name:
#         print(scene_name, camera_name, output_path)
#         scene_store.append(scene)
#         # bpy.ops.render.render(animation=True)

# for sc in scene_store:
#     print(sc.name)


class MultiScene_Render(bpy.types.Operator):
    bl_idname: str = "render.everything"
    bl_label: str = "Render Every Scene"

    # base_path: StringProperty(name="Path")
    scene_list: CollectionProperty(type=bpy.types.Scene, name="Scene Collection")
    # -------------------
    # internal variables

    cancel_render = None
    is_rendering = None
    render_queue = []
    timer_event = None

    def pre_render(self, ctx, _dummy):
        self.is_rendering = True

    def post_render(self, ctx, _dummy):
        self.render_queue.pop(0)
        self.is_rendering = False

    def on_render_cancel(self, ctx):
        self.cancel_render = True

    def execute(self, ctx: Context):
        self.cancel_render = False
        self.is_rendering = False

        # append to the render queue from scenes.
        self.render_queue = []
        for scene in self.scene_list:
            if "YU-" in scene.name_full:
                self.render_queue.append(scene)
                print(self.render_queue)

        # register callback handlers
        bpy.app.handlers.render_pre.append(self.pre_render)
        bpy.app.handlers.render_post.append(self.post_render)
        bpy.app.handlers.render_cancel.append(self.on_render_cancel)

        # checks if the render queue needs to be updated
        self.timer_event = ctx.window_manager.event_timer_add(1.0, window=ctx.window)

        # register this pipeline to run in the background
        ctx.window_manager.modal_handler_add(self)

    def modal(self, ctx: Context, event):
        if event.type == "TIMER":

            if not self.render_queue or self.cancel_render is True:

                # remove all callbacks
                bpy.app.handlers.render_pre.remove(self.pre_render)
                bpy.app.handlers.render_post.remove(self.post_render)
                bpy.app.handlers.render_cancel.remove(self.on_render_cancel)

                # remove timer
                ctx.window_manager.event_timer_remove(self.timer_event)
                self.report({"INFO"}, "RENDER QUEUE FINISHED")
                return {"FINISHED"}

            elif self.is_rendering is False:
                sc = bpy.context.scene
                queue_item = self.render_queue[0]
                print(queue_item)
                # bpy.ops.render.render(animation=True)

        return {"PASS_THROUGH"}


def register():
    bpy.utils.register_class(MultiScene_Render)


def unregister():
    bpy.utils.unregister_class(MultiScene_Render)


if __name__ == "__main__":
    register()
