# -*- coding: utf-8 -*-

"""Main module."""


from functools import wraps
from inspect import getfullargspec
import typing


def _validate_types(obj, **kwargs):
    hints = typing.get_type_hints(obj)
    # iterate all type hints
    for attr_name, attr_type in hints.items():

        if attr_name == 'return':
            continue

        if type(attr_type) == type(typing.Union):
            if not isinstance(kwargs[attr_name], attr_type.__args__):
                raise TypeError(
                    '%r is not one of types %s' % (attr_name, attr_type)
                )

        else:
            if not isinstance(kwargs[attr_name], attr_type):
                raise TypeError(
                    '%r is not of type %s' % (attr_name, attr_type)
                )


def _validate_return(obj, result):
    hints = typing.get_type_hints(obj)
    # iterate all type hints
    # result_type = type(result)
    for attr_name, attr_type in hints.items():

        if attr_name == 'return':

            if type(attr_type) == type(typing.Union):
                if not isinstance(result, attr_type.__args__):
                    raise TypeError(
                        'return value is not one of types %s' % (attr_type.__args__)
                    )

            else:
                if not isinstance(result, attr_type):
                    raise TypeError(
                        'return value is not of type %s' % (attr_type)
                    )

        else:
            continue




def validate_types(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):

        # translate *args into **kwargs
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))

        _validate_types(decorator, **kwargs)

        result=decorator(**kwargs)

        _validate_return(decorator, result)

        return result

    return wrapped_decorator
