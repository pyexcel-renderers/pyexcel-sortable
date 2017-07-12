{% extends "BASIC-README.rst.jj2" %}

{%block constraint%}
{%endblock%}

{%block features %}
**{{name}}** is inspired by `csvtotable <https://github.com/vividvilla/csvtotable>`_ and
provides csvtotable functionality to pyexcel family.

.. image:: https://github.com/pyexcel/pyexcel-sortable/raw/master/sortable.gif


Quick evaluation::

    $ pyexcel transcode --sheet-index 0 goog.ods google.sortable.html


{%endblock%}

{%block documentation_link%}
{%endblock %}
