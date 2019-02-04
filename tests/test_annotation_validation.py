#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `annotation_validation` package."""

import pytest


from annotation_validation import annotation_validation

import pytest
from annotation_validation import validate_types
from typing import Union


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string





@validate_types
def addition(number: int, other_number: int) -> int:
    return number + other_number


@validate_types
def name(first: Union[str, int]) -> str:
    return 'hi {first}!'.format(first=first)


@validate_types
def name2(first: Union[str, int]) -> int:
    return 'hi {first}!'.format(first=first)


@validate_types
def name3(first: Union[str, int]) -> Union[int, str]:
    return 'hi {first}!'.format(first=first)


def test_decorator_fail_basic_int():
    with pytest.raises(TypeError):
        addition('1', 1)


def test_decorator_basic_int():
        assert addition(1, 1) == 2


def test_fail_decorator_basic_Union():
    with pytest.raises(TypeError):
        name(['sam'])


def test_decorator_basic_Union():
        assert name('sam') == 'hi sam!'


def test_fail_return():
    with pytest.raises(TypeError):
        name2('sam')


def test_return_Union():
    assert name3('sam') == 'hi sam!'

