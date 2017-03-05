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

from collections import namedtuple

"""
Parse GWT (Google Web Toolkit) ".symbolMap" files to extract compilation/debug
symbols. Used to infer the relationship between the compiled JavaScript and
the original Java Source code.
"""

# maps actual header names to our field names
gwt_headers = (
    'jsName',
    'jsniIdent',
    'className',
    'memberName',
    'sourceUri',
    'sourceLine',
)

GwtSymbol = namedtuple('GwtSymbol', gwt_headers)


def is_symbol_map(location):
    return location.lower().endswith('.symbolmap')


def parse(location):
    """
    Yield tuples of symbols extracted for a .symbolmap location. Symbol maps
    are produced by GWT compilation. 

    See:
    http://code.google.com/p/google-web-toolkit/wiki/WebModeExceptions#Resymbolization_/_Deobfuscation

    "Symbol maps can be generated at compile time using the -extra GWT
    compiler argument, e.g. -extra war/WEB-INF/classes/"

    These files are like a CSV location with # python like comment lines.

    See as a good base to understand the format:
    http://code.google.com/p/speedtracer/source/browse/trunk/src/client/ui/src/com/google/speedtracer/client/GwtSymbolMapParser.java?r=84 

    Another format is compressed: this is not handled here yet:
    http://code.google.com/p/speedtracer/source/browse/trunk/src/client/ui/src/com/google/speedtracer/client/CompactGwtSymbolMapParser.java?spec=svn84&r=84 

    See also for general JS map parsing: https://github.com/pombredanne/python-sourcemap-1/blob/master/smap.py 
    """
    if is_symbol_map(location):
        with open(location, 'rU') as symap_file:
            for line in symap_file:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('#'):
                    # header line
                    if any(x in line for x in gwt_headers):
                        pass
                    else:
                        # ignore other comment lines
                        pass
                    continue

                gwts = GwtSymbol(*line.split(','))
                # remove possible jar:file: prefix
                clean_path = gwts.sourceUri.replace('jar:file:', '')
                # remove possible c: or drive name from windows paths. they
                # are useless
                clean_path = '/'.join([x for x in clean_path.split('/')
                                             if ':' not in x])
                yield (gwts.jsName, gwts.jsniIdent, gwts.className,
                       gwts.memberName, clean_path, gwts.sourceLine)
