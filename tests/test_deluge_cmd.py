#!/usr/bin/env python
"""Tests for `deluge_cmd` package."""

from unittest import mock, skip
from deluge_cmd import deluge_dls, deluge_dmv
from collections import namedtuple

dls_args_tuple = namedtuple('dls_args_tuple', 'type root pattern debug')


@mock.patch('deluge_cmd.deluge_dls.list_deluge_fs', return_value=[])
def test_dls_command_line_interface(mocked):
    args = dls_args_tuple('a', '.', '*', '')
    deluge_dls.handle_args(args)
    assert mocked.call_count == 1


dmv_args_tuple = namedtuple('dmv_args_tuple', 'root pattern dest debug')


@mock.patch('deluge_cmd.deluge_dmv.list_deluge_fs', return_value=[])
def test_dmv_command_line_interface(mocked):
    args = dmv_args_tuple('.', '*', 'SAMPLE/NEW', '')
    deluge_dmv.handle_args(args)
    assert mocked.call_count == 1
