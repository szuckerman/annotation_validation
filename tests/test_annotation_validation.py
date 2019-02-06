#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `annotation_validation` package."""

import pytest


from annotation_validation import annotation_validation

import pytest
from annotation_validation import validate_types
from typing import Union

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
        return "hi {first}!".format(first=first)


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


    def test_fail_return(self):
        with pytest.raises(TypeError):
            self.name2("sam")


    def test_return_Union(self):
        assert self.name3("sam") == "hi sam!"
