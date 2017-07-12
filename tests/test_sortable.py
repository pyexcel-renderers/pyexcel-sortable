import uuid

import pyexcel as p
from nose.tools import raises

from pyexcel_sortable.sortable import Sortable


def test_render_sheet():
    test_header = uuid.uuid4().hex
    sheet = p.Sheet([[test_header], [1]])
    sortable = Sortable('sortable.html')
    stream = sortable.get_io()
    sortable.set_output_stream(stream)
    sortable.render_sheet(sheet)
    assert test_header in stream.getvalue()


@raises(Exception)
def test_render_book():
    sortable = Sortable('sortable.html')
    sortable.render_book("not supported yet")
