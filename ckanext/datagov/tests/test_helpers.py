"""Tests for helpers.py."""

import ckanext.datagov.helpers as helpers


def test_datagov_hello():
    assert helpers.datagov_hello() == "Hello, datagov!"
