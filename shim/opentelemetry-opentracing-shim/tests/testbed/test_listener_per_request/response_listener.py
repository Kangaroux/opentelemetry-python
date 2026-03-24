from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import object
class ResponseListener(object):
    def __init__(self, span):
        self.span = span

    def on_response(self, res):
        del res
        self.span.finish()
