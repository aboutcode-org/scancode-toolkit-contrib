#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
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
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import, print_function

import os

from commoncode.testcase import FileBasedTesting
from compiledcode import gwt


class TestGWT(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_parse_basic(self):
        test_file = self.get_test_loc('gwt/gwt.symbolMap')
        expected = [
         ('GXT', '',
          'com.extjs.gxt.ui.client.GXT', '',
          '/Views/zoro/lib/lib/gxt/gxt-2.2.6-gwt22.jar!/com/extjs/gxt/ui/client/GXT.java',
          '33'),
         ('qc', 'com.extjs.gxt.ui.client.GXT::$clinit()V',
          'com.extjs.gxt.ui.client.GXT', '$clinit',
          '/Views/zoro/lib/lib/gxt/gxt-2.2.6-gwt22.jar!/com/extjs/gxt/ui/client/GXT.java',
          '33'),
         ('Nb', 'com.extjs.gxt.ui.client.GXT::BLANK_IMAGE_URL',
          'com.extjs.gxt.ui.client.GXT', 'BLANK_IMAGE_URL',
          '/Views/zoro/lib/lib/gxt/gxt-2.2.6-gwt22.jar!/com/extjs/gxt/ui/client/GXT.java',
          '39'),
         ('Ob', 'com.extjs.gxt.ui.client.GXT::IMAGES',
          'com.extjs.gxt.ui.client.GXT', 'IMAGES',
          '/Views/zoro/lib/lib/gxt/gxt-2.2.6-gwt22.jar!/com/extjs/gxt/ui/client/GXT.java',
          '44'),
         ('Pb', 'com.extjs.gxt.ui.client.GXT::SSL_SECURE_URL',
          'com.extjs.gxt.ui.client.GXT', 'SSL_SECURE_URL',
          '/Views/zoro/lib/lib/gxt/gxt-2.2.6-gwt22.jar!/com/extjs/gxt/ui/client/GXT.java',
          '180'),
         ('Qb', 'com.extjs.gxt.ui.client.GXT::ariaEnabled',
          'com.extjs.gxt.ui.client.GXT', 'ariaEnabled',
          '/Views/zoro/lib/lib/gxt/gxt-2.2.6-gwt22.jar!/com/extjs/gxt/ui/client/GXT.java',
          '186'),
         ('Rb', 'com.extjs.gxt.ui.client.GXT::defaultTheme',
          'com.extjs.gxt.ui.client.GXT', 'defaultTheme',
          '/Views/zoro/lib/lib/gxt/gxt-2.2.6-gwt22.jar!/com/extjs/gxt/ui/client/GXT.java',
          '187')
        ]

        result = list(gwt.parse(test_file))
        assert expected == result
