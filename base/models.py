from django.db import models
from django.utils import timezone

from base.functions import *


class Report(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    x_axis = models.CharField(max_length=255)
    y_axis = models.CharField(max_length=255)
    fixed = models.CharField(max_length=255)
    fixed_type = models.CharField(max_length=255)
    fixed_str = models.CharField(max_length=255)

    def to_dict(self):
        result = {'x_axis': self.x_axis,
                  'y_axis': self.y_axis,
                  'fixed': {'name': self.fixed,
                            'type': self.fixed_type},
                  'created_at': str(self.created_at),
                  'updated_at': str(self.updated_at), }

        if self.fixed_type == 'String':
            result['fixed[values]'] = self.fixed_str
        elif self.fixed_type == 'Date':
            dates = self.fixed_str.split(" ")
            result['fixed[start]'] = dates[0]
            result['fixed[end]'] = dates[1]

        tablice = get_tablice_func(self.x_axis, self.y_axis, self.fixed, self.fixed_str)
        result['tablice'] = tablice

        return result