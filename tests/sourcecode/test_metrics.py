#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/aboutcode-org/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/aboutcode-org/scancode-toolkit/ for support and download.

from __future__ import absolute_import, print_function

import os

from commoncode.testcase import FileBasedTesting
from sourcecode import metrics


class TestLineCount(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_file_lines_count_file(self):
        test_file = self.get_test_loc('metrics/lines/amrr.c')
        code, comments = metrics.file_lines_count(test_file)
        assert code == 390
        assert comments == 151

    def test_file_lines_count_file_not_source(self):
        test_file = self.get_test_loc('metrics/lines/a.txt')
        code, comments = metrics.file_lines_count(test_file)
        assert code == 0
        assert comments == 0

    def test_file_lines_count_file_on_dir(self):
        test_file = self.get_test_loc('metrics/lines')
        code, comments = metrics.file_lines_count(test_file)
        assert code == 0
        assert comments == 0

    def test_lines_count_file(self):
        test_file = self.get_test_loc('metrics/lines/amrr.c')
        code = metrics.code_lines_count(test_file)
        comments = metrics.comment_lines_count(test_file)
        assert code == 390
        assert comments == 151

    def test_get_lines_count_file(self):
        test_file = self.get_test_loc('metrics/lines/amrr.c')
        code = metrics.get_code_lines_count(test_file)
        comments = metrics.get_comment_lines_count(test_file)
        assert code == 390
        assert comments == 151

    def test_code_lines_count_dir(self):
        test_dir = self.get_test_loc('metrics/lines')
        code = metrics.get_code_lines_count(test_dir)
        comments = metrics.get_comment_lines_count(test_dir)
        assert code == 7398
        assert comments == 2884
