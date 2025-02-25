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

from sourcecode import kernel


class TestLoadableKernelModule(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_find_lkms1(self):
        testfile = self.get_test_loc('kernel/amrr.c')
        expected = [
            ('lkm-header-include', u'include <linux/module.h>'),
            ('lkm-license', u'Dual BSD/GPL'),
        ]
        results = list(kernel.find_lkms(testfile))
        self.assertEqual(expected, results)

    def test_find_lkms2(self):
        testfile = self.get_test_loc('kernel/if_ath.c')
        expected = [('lkm-header-include', u'include <linux/module.h>')]
        results = list(kernel.find_lkms(testfile))
        self.assertEqual(expected, results)

    def test_find_lkms3(self):
        testfile = self.get_test_loc('kernel/include-linux-module.c')
        expected = [('lkm-header-include', u'include <linux/module.h>')]
        results = list(kernel.find_lkms(testfile))
        self.assertEqual(expected, results)

    def test_find_lkms4(self):
        testfile = self.get_test_loc('kernel/Makefile')
        expected = []
        results = list(kernel.find_lkms(testfile))
        self.assertEqual(expected, results)

    def test_find_lkms5(self):
        testfile = self.get_test_loc('kernel/module-license.c')
        expected = [('lkm-license', u'Dual BSD/GPL')]
        results = list(kernel.find_lkms(testfile))
        self.assertEqual(expected, results)
