{% extends "BASIC-README.rst.jj2" %}

{%block constraint%}
{%endblock%}

{%block features %}
**{{name}}** is inspired by `csvtotable <https://github.com/vividvilla/csvtotable>`_ and
provides csvtotable functionality to pyexcel family.

Quick evaluation::

    $ pyexcel transcode --sheet-index 0 goog.ods google.sortable.html

Here's what you will get:


.. image:: https://github.com/pyexcel/csvtotable/raw/master/sample/table.gif

{%endblock%}
