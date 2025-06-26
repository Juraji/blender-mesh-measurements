from .measure_total_selected_edge_length import MeasureTotalSelectedEdgeLengthOperator


def register():
    from bpy.utils import register_class

    register_class(MeasureTotalSelectedEdgeLengthOperator)


def unregister():
    from bpy.utils import unregister_class

    unregister_class(MeasureTotalSelectedEdgeLengthOperator)
