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


from __future__ import print_function, absolute_import

from commoncode import fileutils


"""
Parse generated make depend files to find sources corresponding binaries.
"""


def is_make_depend(location):
    return location.endswith('.d')


def parse(location):
    """
    Return path of the .o location and the list of the source location paths
    that were built in the .o given the location of the .d location generated
    by makedepend
    """
    obj_path = ''
    src_paths = []

    if is_make_depend(location):
        file_name = fileutils.resource_name(fileutils.as_posixpath(location))

        with open(location, 'rU') as dfile:
            for line in dfile:
                line = line.strip()

                if not line or line == "\\":
                    continue

                if ":" in line and obj_path:
                    break

                if ":" in line:
                    left, right = line.split(":")
                    left = left.strip()
                    # Assuming there is no space in the filename and that
                    # several files may exist on the left side, space
                    # separated FIXME: we should use a proper makefile parser
                    if " " in left:
                        left_files = []
                        for f in left.split():
                            if (f not in left_files
                                and f != file_name
                                and not f.endswith(file_name)
                                    and not f.endswith('.d')):
                                left_files.append(f)

                        lenf = len(left_files)

                        if lenf >= 1:
                            obj_path = left_files[0]
                    else:
                        obj_path = left

                    right = right.strip()
                    right = right.rstrip("\\")
                    right = right.strip()

                    if right:
                        for r in right.split():
                            src_paths.append(r)

                else:
                    line = line.strip()
                    line = line.rstrip("\\")
                    line = line.strip()
                    if line and not line.endswith('.d'):
                        # FIXME: we assume no spaces in filenames: use a make
                        # parser
                        for p in line.split():
                            src_paths.append(p)

    return obj_path, src_paths
