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
import logging

from commoncode.fileutils import file_name
from compiledcode import dwarf
from compiledcode import dwarf2
from typecode import contenttype


logger = logging.getLogger(__name__)


"""
Combine different techniques to extract Elf files DWARF references to source code
files.
"""

# some file names are plugs injected by the GNU compiler or similar and are not worth
# keeping
ignores = {
    'crtstuff.c',
}

def get_source_file_path_references(location):
    """
    Yield unique references to source file paths extracted from DWARF debug symbols
    from the Elf file at `location`.

    If there are errors when processing Elfs, these are returned as well as paths
    prefixed with 'ERROR: '.
    """
    if not os.path.exists(location):
        return
    T = contenttype.get_type(location)
    if not T.is_elf:
        return
    unique_files = set()
    unique_paths = set()
    errors = []
    try:
        with_libdwarf = dwarf.Dwarf(location)
        for path in with_libdwarf.included_source_files:
            if '/' not in path:
                # bare file name
                unique_files.add(path)
            else:
                unique_paths.add(path)

        for path in with_libdwarf.original_source_files:
            if '/' not in path:
                # bare file name
                unique_files.add(path)
            else:
                unique_paths.add(path)

    except Exception as lde:
        msg = str(lde)
        _, m1, m2 = msg.partition('dwarfdump')
        errors.append(''.join([m1, m2]))

    try:
        with_binutils_nm = dwarf2.get_dwarfs(location)
        for entry in with_binutils_nm:
            path = entry.path
            if '/' not in path:
                # bare file name
                unique_files.add(path)
            else:
                unique_paths.add(path)
    except Exception as lde:
        msg = str(lde)
        errors.append(msg)

    seen_file_names = set(file_name(p) for p in unique_paths)
    for fn in unique_files:
        if fn not in seen_file_names and fn not in ignores:
            unique_paths.add(fn)

    for error in errors:
        yield 'ERROR: ' + error

    for path in sorted(unique_paths):
        yield path
