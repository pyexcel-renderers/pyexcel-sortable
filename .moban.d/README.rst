{% extends "BASIC-README.rst.jj2" %}

{%block constraint%}
{%endblock%}

{%block features %}
**{{name}}** is inspired by `csvtotable <https://github.com/vividvilla/csvtotable>`_ and
provides the functionality to pyexcel family.

Quick evaluation::

    $ pyexcel transcode --sheet-index 0 googl.ods google.sortable.html

{%endblock%}
