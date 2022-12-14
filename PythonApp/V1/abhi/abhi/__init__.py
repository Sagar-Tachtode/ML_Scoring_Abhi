# Copyright 2020 Abhijit Ghosh. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://www.apache.org/licenses/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


from . import fancy
from . import metrics
from . import auto
from . import torch
from . import utils


__author__ = 'Abhijit Ghosh'
__version__ = '0.1 (beta)'

__all__ = [ "auto", "fancy", "metrics", "torch", "utils"]