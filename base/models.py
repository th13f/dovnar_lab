from django.db import models
from django.utils import timezone

from base.functions import *


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    x_axis = models.CharField(max_length=255)
    y_axis = models.CharField(max_length=255)
    fixed = models.CharField(max_length=255)
    fixed_type = models.CharField(max_length=255)
    fixed_start = models.CharField(max_length=255)
    fixed_end = models.CharField(max_length=255)
    fixed_values = models.CharField(max_length=255)

    def to_dict(self):
        result = {'x_axis': self.x_axis,
                  'y_axis': self.y_axis,
                  'fixed': {'name': self.fixed,
                            'type': self.fixed_type},
                  'created_at': str(self.created_at),
                  'updated_at': str(self.updated_at), }

        tablice = None
        if self.fixed_type == 'String':
            tablice = get_tablice_func(self.x_axis, self.y_axis, self.fixed, fixed_values=self.fixed_values)
            result['fixed']['values'] = self.fixed_values
        elif self.fixed_type == 'Date':
            tablice = get_tablice_func(self.x_axis, self.y_axis, self.fixed,
                                       fixed_start=self.fixed_start,
                                       fixed_end=self.fixed_end)
            result['fixed']['start'] = self.fixed_start
            result['fixed']['end'] = self.fixed_end
        result['tablice'] = tablice

        return result