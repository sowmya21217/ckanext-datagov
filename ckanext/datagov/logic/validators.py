import ckan.plugins.toolkit as tk


def datagov_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "datagov_required": datagov_required,
    }
