"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.datagov.logic import validators


def test_datagov_reauired_with_valid_value():
    assert validators.datagov_required("value") == "value"


def test_datagov_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.datagov_required(None)
