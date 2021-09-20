# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
#
# Copyright 2021 The NiPreps Developers <nipreps@gmail.com>
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
#
# We support and encourage derived works from this project, please read
# about our expectations at
#
#     https://www.nipreps.org/community/licensing/
#
"""MRIQC."""
from mriqc._version import get_versions

__version__ = get_versions()["version"]
del get_versions

__copyright__ = (
    "Copyright 2020, Center for Reproducible Neuroscience, Stanford University"
)
__credits__ = "Oscar Esteban"
__download__ = f"https://github.com/poldracklab/mriqc/archive/{__version__}.tar.gz"
__all__ = ["__version__", "__copyright__", "__credits__", "__download__"]
