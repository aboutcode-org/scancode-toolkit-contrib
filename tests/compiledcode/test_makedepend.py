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
from compiledcode import makedepend


class TestMakeDepend(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_parse_simple(self):
        test_file = self.get_test_loc('makedepend/simple/addrutil.d')
        obj_path, src_paths = makedepend.parse(test_file)
        assert 'addrutil.o' == obj_path
        expected_paths = [
            '/test/ram/../../Common/Src/addrutil.c',
            '/test/ram/../../Common/Inc/buildmode.h',
            '/test/ram/../../Common/Inc/dct_types.h',
            '/test/ram/../../Common/Inc/mostypes.h',
            '/test/ram/../../Common/Inc/memutil.h',
            '/test/ram/../../Common/Inc/addrutil.h',
            '/test/ram/../../Common/Inc/hwdevices.h',
            '/test/ram/../../Common/Inc/tsic.h',
            '/test/ram/../../Common/Inc/pltcfg.h',
            '/test/ram/../../Common/Inc/dct_debug.h'
        ]
        assert expected_paths == src_paths

    def test_parse_d_file(self):
        test_file = self.get_test_loc('makedepend/d_dep_files/string2key.d')
        obj_path, src_paths = makedepend.parse(test_file)

        expected = '/home/code/app/base/obj/os/fulcrum/src/string2key.o'
        assert expected, obj_path

        expected = self.get_test_loc(
            'makedepend/d_dep_files/string2key.expected')
        expected_paths = open(expected).read().splitlines(False)
        assert expected_paths == src_paths

    def test_parse_d_file2(self):
        test_file = self.get_test_loc('makedepend/d_dep_files2/XmlHelper.d')
        obj_path, src_paths = makedepend.parse(test_file)

        assert 'XmlHelper.o' == obj_path
        expected = self.get_test_loc(
            'makedepend/d_dep_files2/XmlHelper.expected')
        #         with open(expected, 'wb') as out:
        #             out.write('\n'.join(src_paths))
        expected_paths = open(expected).read().splitlines(False)
        assert expected_paths == src_paths

    def test_parse_makedepend_alternate_style(self):
        test_file = self.get_test_loc('makedepend/alternate/makedep.d')
        obj_path, src_paths = makedepend.parse(test_file)

        expected = '/mycode/base/core/qcom/modules/char/drv/src1/drv/objs/qcomdrv.elf'
        assert expected == obj_path

        expected = '/mycode/base/modules/qcom/include/../net/enet/shared/qcomenet.h'
        assert expected in src_paths

        expected = '/mycode/base/linux-2.6.x/arch/arm/include/asm/mach-chipset-snmp/superh_intr.h'
        assert expected not in src_paths
