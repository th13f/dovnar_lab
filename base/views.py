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
                'tablice': get_tablice_func(x_axis, y_axis, fixed['name'], fixed_values={"values": "[2, 3]"})}
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
    response_data = {'reports': reports}
    return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)


@csrf_exempt
def save_report(request):
    if request.method != 'POST':
        return HttpResponse(json.dumps({'status': 'error'}), content_type='application/json', status=400)
    params = request.POST
    x_axis = params.get('x_axis')
    y_axis = params.get('y_axis')
    fixed = params.get('fixed')
    fixed_type = get_fixed_type_func(fixed)

    report = Report(x_axis=x_axis, y_axis=y_axis, fixed=fixed, fixed_type=fixed_type)
    if fixed_type == 'date':
        report.fixed_start = params.get('fixed_start')
        report.fixed_end = params.get('fixed_end')
    elif fixed_type == 'int':
        report.fixed_values = str(params.get('fixed_values'))

    report.save()

    return HttpResponse(json.dumps({'status': 'ok'}), content_type='application/json', status=200)


def load_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'main.html', report.to_dict())


def download_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return HttpResponse(json.dumps(report.to_dict()), content_type='application/json', status=200)