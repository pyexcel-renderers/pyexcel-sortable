"""
    pyexcel_sortable
    ~~~~~~~~~~~~~~~~~~~~~~~

    Transform pyexcel sheet into a sortable html

    :copyright: (c) 2016-2017 by Onni Software Ltd.
    :license: New BSD License, see LICENSE for further details
"""
from pyexcel.renderer import Renderer
from pyexcel._compact import PY2


from excel2table.convert import render_template, freeze_js


class Sortable(Renderer):
    def render_sheet_to_stream(self, file_stream, sheet,
                               write_title=True, caption="",
                               display_length=None,
                               **keywords):
        self.set_write_title(write_title)
        self.set_output_stream(file_stream)

        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(0)

        html = render_template(
            sheet.colnames, sheet.array[1:],
            notebook=True,
            caption=caption, display_length=display_length)
        self._stream.write(html)

    def render_sheet(self, sheet, caption="", display_length=None,
                     **keywords):
        if len(sheet.colnames) == 0:
            sheet.name_columns_by_row(0)

        html = render_template(
            sheet.colnames, sheet.array[1:],
            caption=caption, pagination=True, export=False,
            virtual_scroll=-1,
            display_length=display_length)

        js_freezed_html = freeze_js(html)
        if PY2:
            js_freezed_html = js_freezed_html.encode('utf-8')
        self._stream.write(js_freezed_html)

    def render_book(self, book, **keywords):
        raise Exception("Please select a sheet for transformation")
