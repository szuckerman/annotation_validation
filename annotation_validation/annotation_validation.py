# -*- coding: utf-8 -*-

"""Main module."""


from functools import wraps, lru_cache
from inspect import getfullargspec
from typing import get_type_hints, Union


@lru_cache(maxsize=128)
def getfullargspec_cache(func):
    return getfullargspec(func)


@lru_cache(maxsize=128)
def get_type_hints_cache(func):
    hints = get_type_hints(func)
    return_type_list = [(k, v) for k, v in hints.items() if k == 'return']
    return hints, return_type_list


def _validate_types(hints, **kwargs):
    # iterate all type hints
    for attr_name, attr_type in hints.items():

        if attr_name == 'return':
            continue

        if type(attr_type) == type(Union):
            if not isinstance(kwargs[attr_name], attr_type.__args__):
                raise TypeError(
                    '%r is not one of types %s' % (attr_name, attr_type)
                )

        else:
            if not isinstance(kwargs[attr_name], attr_type):
                raise TypeError(
                    '%r is not of type %s' % (attr_name, attr_type)
                )


def _validate_return(return_type, result):
    # iterate all type hints
    # result_type = type(result)
    if type(return_type) == type(Union):
        if not isinstance(result, return_type.__args__):
            raise TypeError(
                'return value is not one of types %s' % (return_type.__args__)
            )

    else:
        if not isinstance(result, return_type):
            raise TypeError(
                'return value is not of type %s' % (return_type)
            )


def validate_types(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):

        # translate *args into **kwargs
        func_args = getfullargspec_cache(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))

        hints, return_type_list = get_type_hints_cache(decorator)

        _validate_types(hints, **kwargs)

        result=decorator(**kwargs)

        if return_type_list:
            return_type = return_type_list[0][1]
            _validate_return(return_type, result)

        return result

    return wrapped_decorator


