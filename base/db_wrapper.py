from random import WichmannHill
from sqlite3 import Date
from xml.dom import minidom
from django.db import connection
import dateutil.parser as date_parser


def get_tables():
    doc = minidom.parse("tables.xml")
    tables = doc.getElementsByTagName("Table")
    names = []
    for table in tables:
        names.append(table.getAttribute("name"))
    return names


def get_table_info(table_name):
    doc = minidom.parse("tables.xml")
    tables = doc.getElementsByTagName("Table")
    info = {}
    for table in tables:
        name = table.getAttribute("name")
        if name == table_name:
            info = {
                'name': name,
                'type': table.getElementsByTagName("Type")[0].firstChild.data,
                'db_name': table.getElementsByTagName("DBName")[0].firstChild.data,
                'column': table.getElementsByTagName("Column")[0].firstChild.data,
                'fact_name': table.getElementsByTagName("FactName")[0].firstChild.data,
            }
            break
    return info


def get_values(table_name):
    info = get_table_info(table_name)

    cursor = connection.cursor()

    cursor.execute("SELECT id,%s FROM %s;" % (info['column'], info['db_name']))
    rows = cursor.fetchall()
    values = []
    for row in rows:
        values.append(row)
    return values


def get_value(table_name,id):
    info = get_table_info(table_name)
    cursor = connection.cursor()

    cursor.execute("SELECT %s FROM %s WHERE id=%s;" % (info['column'], info['db_name'], id))
    row = cursor.fetchone()
    return row[0]

def get_type(table_name):
    return get_table_info(table_name)['type']


def get_indices_mapping(table_name):
    values = get_values(table_name)
    mapping = {}
    i = 1
    for key, value in values:
        mapping[key] = i
        i+=1
    return mapping

def get_tablice(x_axis,y_axis,fixed, fixed_values=None, fixed_start=None, fixed_end=None):
    x_info = get_table_info(x_axis)
    x_values = get_values(x_axis)
    x_mapping = get_indices_mapping(x_axis)

    y_info = get_table_info(y_axis)
    y_values = get_values(y_axis)
    y_mapping = get_indices_mapping(y_axis)

    fixed_info = get_table_info(fixed)

    if not fixed_values:
        fixed_start_date = date_parser.parse(get_value(fixed, fixed_start))
        fixed_end_date = date_parser.parse(get_value(fixed, fixed_end))
        fixed_values = [x[0] if date_parser.parse(x[1])>=fixed_start_date and date_parser.parse(x[1])<=fixed_end_date
                        else 0
                        for x in get_values(fixed)]
    query = "select %s, %s, value from base_fact where %s in %s;" % (x_info['fact_name'], y_info['fact_name'],
                                                                    fixed_info['fact_name'], str(tuple(fixed_values)))
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    n, m = len(x_mapping)+1, len(y_mapping)+1
    table_values = [[0 for i in xrange(m)] for j in xrange(n)]
    table_values[0][0] = '\\'
    for i in xrange(1, n):
        table_values[i][0] = get_value(x_axis, x_values[i-1][0])
    for i in xrange(1, m):
        table_values[0][i] = get_value(y_axis, y_values[i-1][0])

    for row in rows:
        x, y, value = row
        table_values[x_mapping[x]][y_mapping[y]] += value

    return table_values