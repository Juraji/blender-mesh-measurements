from bpy.types import Context


def convert_length_in_scene_units(context: Context, raw_length: float) -> tuple[float, str]:
    # Unit Settings
    unit_settings = context.scene.unit_settings
    scale_length = unit_settings.scale_length
    unit_name = unit_settings.length_unit.upper()

    scaled_length = raw_length * scale_length

    match unit_name:
        case "KILOMETERS":
            return scaled_length / 1000, "km"
        case "METERS":
            return scaled_length, "m"
        case "CENTIMETERS":
            return scaled_length * 100, "cm"
        case "MILLIMETERS":
            return scaled_length * 1000, "mm"
        case "MICROMETERS":
            return scaled_length * 1000_000, "mm"
        case "ADAPTIVE":
            return scaled_length, "scene units"
        case _:
            return raw_length, "BU (Blender Units)"
