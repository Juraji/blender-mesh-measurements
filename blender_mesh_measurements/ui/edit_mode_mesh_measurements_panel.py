from bpy.types import Panel

from ..operators import MeasureTotalSelectedEdgeLengthOperator


class EditModeMeshMeasurementsPanel(Panel):
    bl_category = "Juraji's Tools"
    bl_space_type = 'VIEW_3D'
    bl_context = "mesh_edit"
    bl_idname = "VIEW3D_PT_edit_mode_mesh_measurements_panel"
    bl_region_type = 'UI'
    bl_label = "Mesh Measurements"

    def draw(self, context):
        layout = self.layout

        layout.operator(MeasureTotalSelectedEdgeLengthOperator.bl_idname)
