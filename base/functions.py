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


def get_tablice_func(x_axis, y_axis, fixed, fixed_values=None, fixed_start=None, fixed_end=None):
    tablice = get_tablice(x_axis, y_axis, fixed, fixed_values, fixed_start, fixed_end)
    return tablice


def get_fixed_type_func(fixed):
    return get_type(fixed)


def get_tablice_from_params(params):
    x_axis = params.get('x_axis')
    y_axis = params.get('y_axis')
    fixed = get_third_table_func(x_axis, y_axis)
    tablice = None
    if fixed['type'] == 'String':
        tablice = get_tablice_func(x_axis, y_axis, fixed['name'], fixed_values=params.get('fixed_values'))
    elif fixed['type'] == 'Date':
        tablice = get_tablice_func(x_axis, y_axis, fixed['name'],
                                   fixed_start=params.get('fixed_start'),
                                   fixed_end=params.get('fixed_end'))
    return tablice