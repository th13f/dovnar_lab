from random import WichmannHill

from db_wrapper import *


def get_third_table_func(x_axis, y_axis):
    tables = get_tables()
    tables.remove(x_axis)
    tables.remove(y_axis)
    info = get_table_info(tables[0])
    info['values'] = get_values(tables[0])
    if info['type'] == 'Date':
        info['start'], info['end'] = info['values'][0][1], info['values'][-1][1]
    return info


def get_tablice_func(x_axis, y_axis, fixed, fixed_values):
    tablice = get_tablice(x_axis, y_axis, fixed, fixed_values)
    return tablice


def get_fixed_type_func(fixed):
    return get_type(fixed)


def get_tablice_from_params(params):
    x_axis = params.get('x_axis')
    y_axis = params.get('y_axis')
    fixed = get_third_table_func(x_axis, y_axis)

    if "fixed[values]" in params:
        fixed_param = {"values": params["fixed[values]"]}
    elif "fixed[value]" in params:
        fixed_param = {"value": params.get("fixed[value]")}
    else:
        fixed_param = {"start": params.get('fixed[start]'), "end": params.get('fixed[end]')}
    tablice = get_tablice_func(x_axis, y_axis, fixed['name'], fixed_param)
    return tablice