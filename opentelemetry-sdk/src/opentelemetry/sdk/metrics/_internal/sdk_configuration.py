# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint =unused-import

from typing import Sequence

# This kind of import is needed to avoid Sphinx errors.
import opentelemetry.sdk.metrics
import opentelemetry.sdk.resources


class SdkConfiguration(object):

    def __init__(self, exemplar_filter=None, resource=None, metric_readers=None, views=None):
        self.exemplar_filter = exemplar_filter
        self.resource = resource
        self.metric_readers = metric_readers
        self.views = views

    def __eq__(self, other):
        if not isinstance(other, SdkConfiguration):
            return NotImplemented
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "SdkConfiguration(exemplar_filter={}, resource={}, metric_readers={}, views={})".format(
            self.exemplar_filter, self.resource, self.metric_readers, self.views)
