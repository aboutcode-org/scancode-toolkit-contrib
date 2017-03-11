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
import json
import codecs

from commoncode.testcase import FileBasedTesting

from compiledcode.elf import Elf
from compiledcode.elf import demangle_chunk
from compiledcode.elf import demangle


class TestElf(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_demangle_chunk_1(self):
        result = demangle_chunk([])
        expected = []
        assert expected == result

    def test_demangle_chunk_2(self):
        expected = ['MMT_add']
        result = demangle_chunk(['_ZZ7MMT_addP8MMmatrixS0_S0_E1m'])
        assert expected == result

    def test_demangle_chunk_3(self):
        expected = ['CContainer::ProcessChildSendNotifyInfo']
        result = demangle_chunk(['_ZN10CContainer26ProcessChildSendNotifyInfoElPcRtRlRdRS0_lPP9CCallbackPP9CTriggers'])
        assert expected == result

    def test_demangle_chunk_4(self):
        expected = ['MMT_add',
                    'CContainer::ProcessChildSendNotifyInfo',
                    'MurmurHashNeutral2',
                    'main']

        result = demangle_chunk(
            ['_ZZ7MMT_addP8MMmatrixS0_S0_E1m',
             '_ZN10CContainer26ProcessChildSendNotifyInfoElPcRtRlRdRS0_lPP9CCallbackPP9CTriggers',
             '_Z18MurmurHashNeutral2PKvij',
             'main'])

        assert sorted(expected) == sorted(result)

    def test_demangle_chunk_5(self):
        expected = []
        result = demangle_chunk([
                     '_GLOBAL__I_main',
                     '_Z41__static_initialization_and_destruction_0ii',
                     '__tcf_0'])
        assert expected == result

    def test_demangle(self):
        expected = ['CContainer::ProcessChildSendNotifyInfo']
        test = ['_ZN10CContainer26ProcessChildSendNotifyInfoElPcRtRlRdRS0_lPP9CCallbackPP9CTriggers'] * 317
        assert set(expected) == set(demangle(test))

    def test_needed_libraries_1(self):
        test_file = 'elf/libelf.so'
        expected = ['libc.so.6']
        test_loc = self.get_test_loc(test_file)
        elf = Elf(test_loc)
        assert set(expected) == set(elf.needed_libraries)

    def test_needed_libraries_2(self):
        test_file = 'dwarf/amd64_exec'
        expected = ['libacl.so.1', 'libc.so.6', 'librt.so.1']
        test_loc = self.get_test_loc(test_file)
        elf = Elf(test_loc)
        assert set(expected) == set(elf.needed_libraries)

    def test_needed_libraries_3(self):
        test_file = 'dwarf/file_stripped'
        expected = ['libc.so.6', 'libmagic.so.1', 'libz.so.1']
        test_loc = self.get_test_loc(test_file)
        elf = Elf(test_loc)
        assert set(expected) == set(elf.needed_libraries)

    def test_needed_libraries_4(self):
        test_file = 'dwarf/ia64_exec'
        expected = ['libacl.so.1', 'libc.so.6.1', 'librt.so.1']
        test_loc = self.get_test_loc(test_file)
        elf = Elf(test_loc)
        assert set(expected) == set(elf.needed_libraries)

    def test_needed_libraries_5(self):
        test_file = 'dwarf/shash.i686'
        expected = ['libc.so.6']
        test_loc = self.get_test_loc(test_file)
        elf = Elf(test_loc)
        assert set(expected) == set(elf.needed_libraries)

    def test_needed_libraries_6(self):
        test_file = 'dwarf/ssdeep.i686'
        expected = ['libc.so.6']
        test_loc = self.get_test_loc(test_file)
        elf = Elf(test_loc)
        assert set(expected) == set(elf.needed_libraries)

    def test_needed_libraries_7(self):
        test_file = 'dwarf/ssdeep.x86_64'
        expected = ['libc.so.6']
        test_loc = self.get_test_loc(test_file)
        elf = Elf(test_loc)
        assert set(expected) == set(elf.needed_libraries)

    def test_corrupted_elf_compiled_with_gcc2(self):
        test_file = self.get_test_loc('elf-corrupted/corrupt.o')
        elf = Elf(test_file)
        assert elf.symbols_section
        sections_to_tests = [
            elf.symbols_section.files,
            elf.symbols_section.standard_files,
            elf.symbols_section.local_functions,
            elf.symbols_section.local_objects,
            elf.symbols_section.global_functions,
            elf.symbols_section.global_objects,
            elf.symbols_section.external_libs_functions,
            elf.symbols_section.external_libs_objects,
            elf.symbols_section.standard_functions,
            elf.symbols_section.standard_objects
        ]
        for section in sections_to_tests:
            assert not section

    def a_test_generator(self, test_file, expected):
        """
        Use this function to generate new tests.
        """
        from commoncode.text import python_safe_name
        from pprint import pformat
        test_loc = self.get_test_loc(test_file)
        function = python_safe_name('test_elf_symbols_' + test_file)
        testf = '''
    def %(function)s(self):
        test_file = self.get_test_loc(%(test_file)r)
        expected_file = self.get_test_loc('%(test_file)s.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert v == sorted(result)[i]''' % locals()
        print(testf)
        expected_dict = {}
        expected_dict['files'] = expected[0]
        expected_dict['standard_files'] = expected[1]
        expected_dict['local_functions'] = expected[2]
        expected_dict['local_objects'] = expected[3]
        expected_dict['global_functions'] = expected[4]
        expected_dict['global_objects'] = expected[5]
        expected_dict['external_libs_functions'] = expected[6]
        expected_dict['external_libs_objects'] = expected[7]
        expected_dict['standard_functions'] = expected[8]
        expected_dict['standard_objects'] = expected[9]

        with open(test_loc + '.expected_elf_symbols', 'wb') as out:
            json.dump(expected_dict, out, indent=2)

    def run_test_gen(self):
        #  for test_file, expected in SYMBOL_TEST_DATA.items():
        #   self.a_test_generator(test_file, expected)
        pass

    def test_elf_symbols_dwarf_arm_gentoo_elf(self):
        test_file = self.get_test_loc('dwarf/arm_gentoo_elf')
        expected_file = self.get_test_loc('dwarf/arm_gentoo_elf.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert v == sorted(result)[i]

    def test_elf_symbols_misc_elfs_cpp_test_o(self):
        test_file = self.get_test_loc('misc_elfs/cpp-test.o')
        expected_file = self.get_test_loc('misc_elfs/cpp-test.o.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert v == sorted(result)[i]

    def test_elf_symbols_dwarf_ssdeep_x86_64(self):
        test_file = self.get_test_loc('dwarf/ssdeep.x86_64')
        expected_file = self.get_test_loc('dwarf/ssdeep.x86_64.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert tuple(v) == tuple(sorted(result)[i])

    def test_elf_symbols_elf_libelf_so(self):
        test_file = self.get_test_loc('elf/libelf.so')
        expected_file1 = self.get_test_loc('elf/libelf.so.expected_elf_symbols')
        expected_file2 = self.get_test_loc('elf/libelf.so.expected_elf_relocatable_symbols')
        with codecs.open(expected_file1, encoding='utf-8') as expect1:
            expected1 = json.load(expect1)
        elf = Elf(test_file)
        for section, expected_values in expected1.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert tuple(v) == tuple(sorted(result)[i])

        with codecs.open(expected_file2, encoding='utf-8') as expect2:
            expected2 = json.load(expect2)
        for section, expected_values in expected2.items():
            result = getattr(elf.relocatable_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert tuple(v) == tuple(sorted(result)[i])

    def test_elf_symbols_dwarf_ssdeep_i686(self):
        test_file = self.get_test_loc('dwarf/ssdeep.i686')
        expected_file = self.get_test_loc('dwarf/ssdeep.i686.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert tuple(v) == tuple(sorted(result)[i])

    def test_elf_symbols_dwarf_arm_object(self):
        test_file = self.get_test_loc('dwarf/arm_object')
        expected_file = self.get_test_loc('dwarf/arm_object.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert v == sorted(result)[i]

    def test_elf_symbols_dwarf_arm_scatter_load(self):
        test_file = self.get_test_loc('dwarf/arm_scatter_load')
        expected_file = self.get_test_loc('dwarf/arm_scatter_load.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert v == sorted(result)[i]

    def test_elf_symbols_dwarf_shash_i686(self):
        test_file = self.get_test_loc('dwarf/shash.i686')
        expected_file = self.get_test_loc('dwarf/shash.i686.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert tuple(v) == tuple(sorted(result)[i])

    def test_elf_symbols_dwarf_libelf_begin_o(self):
        test_file = self.get_test_loc('dwarf/libelf-begin.o')
        expected_file = self.get_test_loc('dwarf/libelf-begin.o.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert v == sorted(result)[i]

    def test_elf_symbols_dwarf_arm_exec(self):
        test_file = self.get_test_loc('dwarf/arm_exec')
        expected_file = self.get_test_loc('dwarf/arm_exec.expected_elf_symbols')
        with codecs.open(expected_file, encoding='utf-8') as expect:
            expected = json.load(expect)
        elf = Elf(test_file)
        for section, expected_values in expected.items():
            result = getattr(elf.symbols_section, section)
            for i, v in enumerate(sorted(expected_values)):
                assert v == sorted(result)[i]
