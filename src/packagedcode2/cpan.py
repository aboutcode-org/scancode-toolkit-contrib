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


"""
CPAN license list from:
http://search.cpan.org/dist/CPAN-Meta/lib/CPAN/Meta/Spec.pm#license
"""

CPAN_LICENSES = {
    'agpl_3': 'GNU Affero General Public License, Version 3',
    'apache_1_1': 'Apache Software License, Version 1.1',
    'apache_2_0': 'Apache License, Version 2.0',
    'artistic_1': 'Artistic License, (Version 1)',
    'artistic_2': 'Artistic License, Version 2.0',
    'bsd': 'BSD License (three-clause)',
    'freebsd': 'FreeBSD License (two-clause)',
    'gfdl_1_2': 'GNU Free Documentation License, Version 1.2',
    'gfdl_1_3': 'GNU Free Documentation License, Version 1.3',
    'gpl_1': 'GNU General Public License, Version 1',
    'gpl_2': 'GNU General Public License, Version 2',
    'gpl_3': 'GNU General Public License, Version 3',
    'lgpl_2_1': 'GNU Lesser General Public License, Version 2.1',
    'lgpl_3_0': 'GNU Lesser General Public License, Version 3.0',
    'mit': 'MIT (aka X11) License',
    'mozilla_1_0': 'Mozilla Public License, Version 1.0',
    'mozilla_1_1': 'Mozilla Public License, Version 1.1',
    'openssl': 'OpenSSL License',
    'perl_5': 'The Perl 5 License (Artistic 1 & GPL 1 or later)',
    'qpl_1_0': 'Q Public License, Version 1.0',
    'ssleay': 'Original SSLeay License',
    'sun': 'Sun Internet Standards Source License (SISSL)',
    'zlib': 'zlib License',

    # The following license strings are also valid and indicate other licensing not described above:',
    'open_source': 'Other Open Source Initiative (OSI) approved license',
    'restricted': 'Requires special permission from copyright holder',
    'unrestricted': 'Not an OSI approved license, but not restricted',
    'unknown': 'License not provided in metadata',
}

# map of CPAN licenses to a list of scancode license expression
LICENSE_MAPPING = {
    'agpl_3': 'agpl-3.0',
    'apache_1_1': 'apache-1.1',
    'apache_2_0': 'apache-2.0',
    'artistic_1': 'artistic-1.0',
    'artistic_2': 'artistic-2.0',
    'bsd': 'bds-new',
    'freebsd': 'bsd-simplified',
    'gfdl_1_2': 'gfdl-1.2',
    'gfdl_1_3': 'gfdl-1.2',
    'gpl_1': 'gpl-1.0',
    'gpl_2': 'gpl-2.0',
    'gpl_3': 'gpl-3.0',
    'lgpl_2_1': 'lgpl-2.1',
    'lgpl_3_0': 'lgpl-3.0',
    'mit': 'mit',
    'mozilla_1_0': 'mpl-1.0',
    'mozilla_1_1': 'mpl-1.1',
    'openssl': 'openssl',
    'perl_5': 'artistic-1.0 or gpl-1.0-plus',
    'qpl_1_0': 'qpl-1.0',
    'ssleay': 'ssleay',
    'sun': 'sissl-1.0',
    'zlib': 'zlib',

    # The following license strings are also valid and indicate other licensing not described above:
    # FIXME: find a better mapping, or create scancode keys as needed
    'open_source': 'open-source',
    'restricted': 'restricted',
    'unrestricted': 'unrestricted',
    'unknown': 'unknown',
}
