# Copyright 2018 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""Helpers for unittests."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import REDACTED.transformer_lingvo.lingvo.compat as tf


def test_src_dir_path(relative_path):
  return os.path.join(
      tf.flags.FLAGS.test_srcdir,
      'REDACTED/transformer_lingvo/lingvo',
      relative_path)
