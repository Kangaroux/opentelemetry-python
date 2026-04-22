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


from typing import (
    Callable,
    Final,
    Generator,
    Iterable,
    Optional,
    Sequence,
    Union,
)

from opentelemetry.metrics import (
    CallbackOptions,
    Meter,
    ObservableGauge,
    Observation,
    UpDownCounter,
)

# pylint =invalid-name
CallbackT = Union[
    Callable,
    Generator,
]

VCS_CHANGE_COUNT = "vcs.change.count"
"""
The number of changes (pull requests/merge requests/changelists) in a repository, categorized by their state (e.g. open or merged)
Instrument
Unit: {change}
"""


def create_vcs_change_count(meter):
    """The number of changes (pull requests/merge requests/changelists) in a repository, categorized by their state (e.g. open or merged)"""
    return meter.create_up_down_counter(
        name=VCS_CHANGE_COUNT,
        description="The number of changes (pull requests/merge requests/changelists) in a repository, categorized by their state (e.g. open or merged).",
        unit="{change}",
    )


VCS_CHANGE_DURATION = "vcs.change.duration"
"""
The time duration a change (pull request/merge request/changelist) has been in a given state
Instrument
Unit
"""


def create_vcs_change_duration(
    meter, callbacks
):
    """The time duration a change (pull request/merge request/changelist) has been in a given state"""
    return meter.create_observable_gauge(
        name=VCS_CHANGE_DURATION,
        callbacks=callbacks,
        description="The time duration a change (pull request/merge request/changelist) has been in a given state.",
        unit="s",
    )


VCS_CHANGE_TIME_TO_APPROVAL = "vcs.change.time_to_approval"
"""
The amount of time since its creation it took a change (pull request/merge request/changelist) to get the first approval
Instrument
Unit
"""


def create_vcs_change_time_to_approval(
    meter, callbacks
):
    """The amount of time since its creation it took a change (pull request/merge request/changelist) to get the first approval"""
    return meter.create_observable_gauge(
        name=VCS_CHANGE_TIME_TO_APPROVAL,
        callbacks=callbacks,
        description="The amount of time since its creation it took a change (pull request/merge request/changelist) to get the first approval.",
        unit="s",
    )


VCS_CHANGE_TIME_TO_MERGE = "vcs.change.time_to_merge"
"""
The amount of time since its creation it took a change (pull request/merge request/changelist) to get merged into the target(base) ref
Instrument
Unit
"""


def create_vcs_change_time_to_merge(
    meter, callbacks
):
    """The amount of time since its creation it took a change (pull request/merge request/changelist) to get merged into the target(base) re"""
    return meter.create_observable_gauge(
        name=VCS_CHANGE_TIME_TO_MERGE,
        callbacks=callbacks,
        description="The amount of time since its creation it took a change (pull request/merge request/changelist) to get merged into the target(base) ref.",
        unit="s",
    )


VCS_CONTRIBUTOR_COUNT = "vcs.contributor.count"
"""
The number of unique contributors to a repository
Instrument
Unit: {contributor}
"""


def create_vcs_contributor_count(
    meter, callbacks
):
    """The number of unique contributors to a repository"""
    return meter.create_observable_gauge(
        name=VCS_CONTRIBUTOR_COUNT,
        callbacks=callbacks,
        description="The number of unique contributors to a repository.",
        unit="{contributor}",
    )


VCS_REF_COUNT = "vcs.ref.count"
"""
The number of refs of type branch or tag in a repository
Instrument
Unit: {ref}
"""


def create_vcs_ref_count(meter):
    """The number of refs of type branch or tag in a repository"""
    return meter.create_up_down_counter(
        name=VCS_REF_COUNT,
        description="The number of refs of type branch or tag in a repository.",
        unit="{ref}",
    )


VCS_REF_LINES_DELTA = "vcs.ref.lines_delta"
"""
The number of lines added/removed in a ref (branch) relative to the ref from the `vcs.ref.base.name` attribute
Instrument
Unit: {line}
Note: This metric should be reported for each `vcs.line_change.type` value. For example if a ref added 3 lines and removed 2 lines,
instrumentation SHOULD report two measurements: 3 and 2 (both positive numbers).
If number of lines added/removed should be calculated from the start of time, then `vcs.ref.base.name` SHOULD be set to an empty string.
"""


def create_vcs_ref_lines_delta(
    meter, callbacks
):
    """The number of lines added/removed in a ref (branch) relative to the ref from the `vcs.ref.base.name` attribute"""
    return meter.create_observable_gauge(
        name=VCS_REF_LINES_DELTA,
        callbacks=callbacks,
        description="The number of lines added/removed in a ref (branch) relative to the ref from the `vcs.ref.base.name` attribute.",
        unit="{line}",
    )


VCS_REF_REVISIONS_DELTA = "vcs.ref.revisions_delta"
"""
The number of revisions (commits) a ref (branch) is ahead/behind the branch from the `vcs.ref.base.name` attribute
Instrument
Unit: {revision}
Note: This metric should be reported for each `vcs.revision_delta.direction` value. For example if branch `a` is 3 commits behind and 2 commits ahead of `trunk`,
instrumentation SHOULD report two measurements: 3 and 2 (both positive numbers) and `vcs.ref.base.name` is set to `trunk`.
"""


def create_vcs_ref_revisions_delta(
    meter, callbacks
):
    """The number of revisions (commits) a ref (branch) is ahead/behind the branch from the `vcs.ref.base.name` attribute"""
    return meter.create_observable_gauge(
        name=VCS_REF_REVISIONS_DELTA,
        callbacks=callbacks,
        description="The number of revisions (commits) a ref (branch) is ahead/behind the branch from the `vcs.ref.base.name` attribute.",
        unit="{revision}",
    )


VCS_REF_TIME = "vcs.ref.time"
"""
Time a ref (branch) created from the default branch (trunk) has existed. The `ref.type` attribute will always be `branch`
Instrument
Unit
"""


def create_vcs_ref_time(
    meter, callbacks
):
    """Time a ref (branch) created from the default branch (trunk) has existed. The `ref.type` attribute will always be `branch`"""
    return meter.create_observable_gauge(
        name=VCS_REF_TIME,
        callbacks=callbacks,
        description="Time a ref (branch) created from the default branch (trunk) has existed. The `ref.type` attribute will always be `branch`.",
        unit="s",
    )


VCS_REPOSITORY_COUNT = "vcs.repository.count"
"""
The number of repositories in an organization
Instrument
Unit: {repository}
"""


def create_vcs_repository_count(meter):
    """The number of repositories in an organization"""
    return meter.create_up_down_counter(
        name=VCS_REPOSITORY_COUNT,
        description="The number of repositories in an organization.",
        unit="{repository}",
    )
