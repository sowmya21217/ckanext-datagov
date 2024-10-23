import ckan.plugins.toolkit as tk
import ckanext.datagov.logic.schema as schema


@tk.side_effect_free
def datagov_get_sum(context, data_dict):
    tk.check_access(
        "datagov_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.datagov_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'datagov_get_sum': datagov_get_sum,
    }
