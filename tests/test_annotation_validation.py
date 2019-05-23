#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `annotation_validation` package."""

import pytest


from annotation_validation import annotation_validation

import pytest
from annotation_validation import validate_types
from typing import Union, Iterable, Dict, List


class TestAnnotation:

    @validate_types
    def addition(self, number: int, other_number: int) -> int:
        return number + other_number


    @validate_types
    def name(self, first: Union[str, int]) -> str:
        return "hi {first}!".format(first=first)


    @validate_types
    def name2(self, first: Union[str, int]) -> int:
        return "hi {first}!".format(first=first)


    @validate_types
    def name3(self, first: Union[str, int]) -> Union[int, str]:
        return "hi {first}!".format(first=first)    \


    @validate_types
    def name_iterable(self, first: Iterable) -> str:
        names = ', '.join(first)
        return "hi {names}!".format(names=names)


    @validate_types
    def name_dict(self, dict_name: Dict) -> str:
        return "hi {first} {last}!".format_map(dict_name)


    @validate_types
    def name_list(self, first: List) -> str:
        names = ', '.join(first)
        return "hi {names}!".format(names=names)


    def test_decorator_fail_basic_int(self):
        with pytest.raises(TypeError):
            self.addition("1", 1)


    def test_decorator_basic_int(self):
        assert self.addition(1, 1) == 2


    def test_fail_decorator_basic_Union(self):
        with pytest.raises(TypeError):
            self.name(["sam"])


    def test_decorator_basic_Union(self):
        assert self.name("sam") == "hi sam!"


    def test_fail_decorator_basic_Iterable(self):
        with pytest.raises(TypeError):
            self.name_iterable(1)


    def test_decorator_basic_Iterable(self):
        assert self.name_iterable(["sam", "mike"]) == "hi sam, mike!"


    def test_decorator_basic_Iterable2(self):
        assert self.name_iterable(("sam", "mike")) == "hi sam, mike!"


    def test_fail_return(self):
        with pytest.raises(TypeError):
            self.name2("sam")


    def test_return_Union(self):
        assert self.name3("sam") == "hi sam!"


    def test_return_Union_int(self):
        assert self.name3(1) == "hi 1!"


    def test_Dict(self):
        my_dict = {'first': 'sam', 'last': 'zuckerman'}
        assert self.name_dict(dict_name=my_dict) == "hi sam zuckerman!"


    def test_List(self):
        assert self.name_list(first=['sam', 'mike']) == "hi sam, mike!"


    def test_List_fail(self):
        with pytest.raises(TypeError):
            assert self.name_list(first=('sam', 'mike'))

