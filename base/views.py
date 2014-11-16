import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from base.models import Report
from functions import *
from db_wrapper import *


def index(request):
    tables = get_tables()
    x_axis = tables[2]
    y_axis = tables[1]
    fixed = get_third_table_func(x_axis, y_axis)
    context = {'x_axis': x_axis,
               'y_axis': y_axis,
               'tables': tables,
               'fixed': get_third_table_func(x_axis, y_axis),
                'tablice': get_tablice_func(x_axis, y_axis, fixed['name'], fixed_values={"values": "[2, 3]"}),
                'reports': Report.objects.all()}
                #'tablice': get_tablice_func(x_axis, y_axis, fixed['name'], fixed_start=1, fixed_end=5)}
    return render(request, 'main.html', context)


@csrf_exempt
def get_third_table(request):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'status': 'error'}), content_type='application/json', status=400)
    params = request.POST
    x_axis = params.get('x_axis')
    y_axis = params.get('y_axis')
    context = {'fixed': get_third_table_func(x_axis, y_axis)}
    return render(request, 'fixed_values.html', context)


@csrf_exempt
def get_tablice_html(request):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'status': 'error'}), content_type='application/json', status=400)
    params = request.POST
    tablice = get_tablice_from_params(params)
    return render(request, 'tablice.html', {'tablice': tablice})


def get_tablice_json(request):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'status': 'error'}), content_type='application/json', status=400)
    params = request.POST
    tablice = get_tablice_from_params(params)
    return HttpResponse(json.dumps({'tablice': tablice}), content_type="application/json", status=200)

# reports api
def reports_list(request):
    reports = Report.objects.all()
    context = {'reports': reports}
    return render(request, 'reports_list.html', context)


@csrf_exempt
def save_report(request, report_name):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'status': 'error'}), content_type='application/json', status=400)
    params = request.POST
    x_axis = params.get('x_axis')
    y_axis = params.get('y_axis')
    fixed = get_third_table_func(x_axis, y_axis)
    fixed_name = fixed["name"]
    fixed_type = fixed["type"]
    if "fixed[values]" in params:
        fixed_str = params["fixed[values]"]
    else:
        fixed_str = "%s %s" % (params['fixed[start]'], params['fixed[end]'])

    report = Report(name=report_name, x_axis=x_axis, y_axis=y_axis, fixed=fixed_name, fixed_type=fixed_type, fixed_str=fixed_str)

    report.save()

    return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json', status=200)

@csrf_exempt
def update_report(request, report_id):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'status': 'error'}), content_type='application/json', status=400)
    params = request.POST
    x_axis = params.get('x_axis')
    y_axis = params.get('y_axis')
    fixed = get_third_table_func(x_axis, y_axis)
    fixed_name = fixed["name"]
    fixed_type = fixed["type"]
    report_name = params["name"]
    if "fixed[values]" in params:
        fixed_str = params["fixed[values]"]
    else:
        fixed_str = "%s %s" % (params['fixed[start]'], params['fixed[end]'])

    report = get_object_or_404(Report, id=report_id)
    if report_name:
        report.name = report_name
    report.x_axis = x_axis
    report.y_axis = y_axis
    report.fixed = fixed_name
    report.fixed_type = fixed_type
    report.fixed_str = fixed_str

    report.save()

    return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json', status=200)


@csrf_exempt
def delete_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    report.delete()
    return HttpResponse({"status": "ok"}, status=200)

def load_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    params = {"x_axis": report.x_axis,
              "y_axis": report.y_axis}
    if report.fixed_type == "String":
        params["fixed[values]"] = report.fixed_str
    elif report.fixed_type == "Date":
        fixed_dates = report.fixed_str.split(" ")
        params["fixed[start]"] = fixed_dates[0]
        params["fixed[end]"] = fixed_dates[1]
    tablice = get_tablice_from_params(params)
    return render(request, 'tablice.html', {'tablice': tablice})


def download_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return HttpResponse(json.dumps(report.to_dict()), content_type='application/json', status=200)