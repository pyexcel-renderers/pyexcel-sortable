"""
    pyexcel_sortable
    ~~~~~~~~~~~~~~~~~~~~~~~

    Transform pyexcel sheet into a sortable html

    :copyright: (c) 2016-2017 by Onni Software Ltd.
    :license: New BSD License, see LICENSE for further details
"""
from lml.plugin import PluginInfoChain, PluginInfo


class MyPluginInfo(PluginInfo):

    def tags(self):
        file_types = self.file_types
        for file_type in file_types:
            yield file_type


PluginInfoChain(__name__).add_a_plugin_instance(
    MyPluginInfo(
        'renderer',
        '%s.sortable.Sortable' % __name__,
        file_types=['sortable.html'],
        stream_type='string'
    )
)
