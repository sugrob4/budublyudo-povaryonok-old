# -*- coding: utf-8 -*-
import os
from django.utils.deconstruct import deconstructible
import time

@deconstructible
class UploadPath:

    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        date_dirs = time.strftime('%Y/%m/%d/')
        return os.path.join(self.path, date_dirs, filename)
