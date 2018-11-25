# -*- coding: utf-8 -*-


def delete_file(sender, **kwargs):
    instance = kwargs.get('instance')
    instance.image.delete(save=False)
