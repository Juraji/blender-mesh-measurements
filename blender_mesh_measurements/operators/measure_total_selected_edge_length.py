from bpy.types import Operator, Context
import bmesh

from ..utils.units import convert_length_in_scene_units


class MeasureTotalSelectedEdgeLengthOperator(Operator):
    bl_idname = "object.measure_total_selected_edge_length"
    bl_label = "Measure Total Selected Edge Length"
    bl_description = "Measure the total length of all selected edges combined. (Meant for loop/line selections.)"

    @classmethod
    def poll(cls, context: Context):
        obj = context.active_object
        return (
                obj is not None and
                obj.mode == 'EDIT' and
                obj.type == 'MESH'
        )

    def execute(self, context: Context):
        # Get selected edges
        obj = context.edit_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        # Measure total selected edge length
        raw_length = sum(e.calc_length() for e in bm.edges if e.select)

        # Apply unit scale
        value, label = convert_length_in_scene_units(context, raw_length)

        # Format output based on unit type
        formatted_value = f"{value:.7f}"
        context.window_manager.clipboard = formatted_value

        self.report({'INFO'}, f"Selected Edge Length: {formatted_value} {label}")
        return {"FINISHED"}
