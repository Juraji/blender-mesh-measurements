from .edit_mode_mesh_measurements_panel import EditModeMeshMeasurementsPanel


def register():
    from bpy.utils import register_class

    register_class(EditModeMeshMeasurementsPanel)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(EditModeMeshMeasurementsPanel)
