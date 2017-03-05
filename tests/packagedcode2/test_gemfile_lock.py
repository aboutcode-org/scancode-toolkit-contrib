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

from packagedcode2 import gemfile_lock
from commoncode.testcase import FileBasedTesting


class TestGemfileLock(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_get_options(self):
        test = '''GIT
  remote: git://github.com/amatsuda/kaminari.git
  revision: cb5539e0e81188ccadc0e703b32ae7b5dec13cb1
  specs:
    kaminari (0.15.0)
      actionpack (>= 3.0.0)
      activesupport (>= 3.0.0)
  ref: 4e286bf
  ref: 81e5e4d6
  ref: 92d6dac
  remote: .
  remote: ..
  remote: ../
  remote: ../../
  remote: ../gems/encryptor
  remote: /Users/hector/dev/gems/factory
  remote: git://github.com/ahoward/mongoid-grid_fs.git
  remote: git://github.com/amatsuda/kaminari.git
  remote: http://rubygems.org/
  remote: http://www.rubygems.org/
  revision: 059012a2c2a9e0a5d6e67137752c3e918689c88a
  foo: bar'''.splitlines()

        expected = [
        (None, None),
        ('remote', 'git://github.com/amatsuda/kaminari.git'),
        ('revision', 'cb5539e0e81188ccadc0e703b32ae7b5dec13cb1'),
        (None, None),
        (None, None),
        (None, None),
        (None, None),
        ('ref', '4e286bf'),
        ('ref', '81e5e4d6'),
        ('ref', '92d6dac'),
        ('remote', '.'),
        ('remote', '..'),
        ('remote', '../'),
        ('remote', '../../'),
        ('remote', '../gems/encryptor'),
        ('remote', '/Users/hector/dev/gems/factory'),
        ('remote', 'git://github.com/ahoward/mongoid-grid_fs.git'),
        ('remote', 'git://github.com/amatsuda/kaminari.git'),
        ('remote', 'http://rubygems.org/'),
        ('remote', 'http://www.rubygems.org/'),
        ('revision', '059012a2c2a9e0a5d6e67137752c3e918689c88a'),
        (None, None)]
        results = [gemfile_lock.get_option(t) for t in test]
        self.assertEqual(expected, results)

    def test_NAME_VERSION_re(self):
        import re
        nv = re.compile(gemfile_lock.NAME_VERSION).match
        test = ['brakeman (2.3.1)',
                'erubis (~> 2.6)',
                'fastercsv (~> 1.5)',
                'haml (>= 3.0, < 5.0)',
                'highline (~> 1.6.20)',
                'multi_json (~> 1.2)',
                'ruby2ruby (~> 2.0.5)',
                'ruby_parser (~> 3.2.2)',
                'sass (~> 3.0)',
                'slim (>= 1.3.6, < 3.0)',
                'terminal-table (~> 1.4)',
                'json (1.8.0-java)',
                'json',
                'alpha (1.9.0-x86-mingw32)']

        expected = [('brakeman', '2.3.1'),
                    ('erubis', '~> 2.6'),
                    ('fastercsv', '~> 1.5'),
                    ('haml', '>= 3.0, < 5.0'),
                    ('highline', '~> 1.6.20'),
                    ('multi_json', '~> 1.2'),
                    ('ruby2ruby', '~> 2.0.5'),
                    ('ruby_parser', '~> 3.2.2'),
                    ('sass', '~> 3.0'),
                    ('slim', '>= 1.3.6, < 3.0'),
                    ('terminal-table', '~> 1.4'),
                    ('json', '1.8.0'),
                    ('json', None),
                    ('alpha', '1.9.0')]

        results = [(nv(x).group('name'),
                    nv(x).group('version'),) for x in test]

        self.assertEqual(expected, results)

    def test_DEPS_re(self):
        test = '''DEPENDENCIES
  activesupport (~> 3.0)
  addressable
  bcrypt-ruby!
  activemodel (= 3.2.13.rc1)
  activemodel (= 4.0.0.beta)!
  activerecord (~> 3.1.12)
  activerecord (= 2.0.0)
  activerecord (>= 3.0.0)
  activesupport (= 2.3.11)
  msgpack (>= 0.4.4, < 0.6.0, != 0.5.3, != 0.5.2, != 0.5.1, != 0.5.0)
  msgpack (>= 0.4.4, < 0.6.0, != 0.5.3, != 0.5.2, != 0.5.1, != 0.5.0)!
  tilt (~> 1.1, != 1.3.0)!'''.splitlines()
        expected = [None,
                    ('activesupport', '~> 3.0', False),
                    ('addressable', None, False),
                    ('bcrypt-ruby', None, True),
                    ('activemodel', '= 3.2.13.rc1', False),
                    ('activemodel', '= 4.0.0.beta', True),
                    ('activerecord', '~> 3.1.12', False),
                    ('activerecord', '= 2.0.0', False),
                    ('activerecord', '>= 3.0.0', False),
                    ('activesupport', '= 2.3.11', False),
                    ('msgpack', '>= 0.4.4, < 0.6.0, != 0.5.3, != 0.5.2, != 0.5.1, != 0.5.0', False),
                    ('msgpack', '>= 0.4.4, < 0.6.0, != 0.5.3, != 0.5.2, != 0.5.1, != 0.5.0', True),
                    ('tilt', '~> 1.1, != 1.3.0', True),
                    ]
        results = []
        for t in test:
            dep = gemfile_lock.DEPS(t)
            if dep:
                version = dep.group('version')
                name = dep.group('name')
                pinned = True if dep.group('pinned') else False
                results.append((name, version, pinned,))
            else:
                results.append(None)
        self.assertEqual(expected, results)

    def test_SPEC_DEPS_re(self):
        test = '''    specs:
    actionmailer (4.0.0.rc1)
    actionpack (4.0.0.beta1)
    airbrake (3.1.16)
    akami (1.2.1)
    allowy (0.4.0)
    arel (5.0.1.20140414130214)
    bson (1.4.0-java)
    active_attr (0.8.4)'''.splitlines()
        expected = [
            ('actionmailer', '4.0.0.rc1'),
            ('actionpack', '4.0.0.beta1'),
            ('airbrake', '3.1.16'),
            ('akami', '1.2.1'),
            ('allowy', '0.4.0'),
            ('arel', '5.0.1.20140414130214'),
            ('bson', '1.4.0'),
            ('active_attr', '0.8.4')
                    ]
        nv = gemfile_lock.SPEC_DEPS
        results = [(nv(x).group('name'),
                    nv(x).group('version'),) for x in test if nv(x)]
        self.assertEqual(expected, results)

    def test_SPEC_SUB_DEPS_re(self):
        test = '''  specs:
    akami (1.2.1)
      actionmailer (= 4.0.0)
      actionmailer (= 4.0.0.rc1)
      actionmailer (>= 3, < 5)
      actionpack (~> 3.0)
      active_utils (~> 2.0, >= 2.0.1)
      activemodel (~> 3.0)
      activemodel (~> 3.0.0)
      beefcake (~> 1.2366.0)
      msgpack (>= 0.4.4, < 0.6.0, != 0.5.3, != 0.5.2, != 0.5.1, != 0.5.0)
      tilt (~> 1.1, != 1.3.0)'''.splitlines()
        expected = [
            ('actionmailer', '= 4.0.0'),
            ('actionmailer', '= 4.0.0.rc1'),
            ('actionmailer', '>= 3, < 5'),
            ('actionpack', '~> 3.0'),
            ('active_utils', '~> 2.0, >= 2.0.1'),
            ('activemodel', '~> 3.0'),
            ('activemodel', '~> 3.0.0'),
            ('beefcake', '~> 1.2366.0'),
            ('msgpack', '>= 0.4.4, < 0.6.0, != 0.5.3, != 0.5.2, != 0.5.1, != 0.5.0'),
            ('tilt', '~> 1.1, != 1.3.0'),
            ]
        nv = gemfile_lock.SPEC_SUB_DEPS
        results = [(nv(x).group('name'),
                    nv(x).group('version'),) for x in test if nv(x)]
        self.assertEqual(expected, results)

    def test_parse_dependency(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_dependency/Gemfile.lock')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock, print_errors=False)
        expected_names = [
            u'activesupport',
            u'addressable',
            u'debugger',
            u'eventmachine',
            u'machinist',
            u'mysql2',
            u'nokogiri',
            u'rspec-instafail',
            u'sequel',
            u'yajl-ruby',
                          ]
        self.assertEqual(expected_names, gfl.all_gems.keys())
        self.assertEqual(expected_names, gfl.dependencies.keys())
        self.assertEqual(gfl.all_gems, gfl.dependencies)

        expected_gems = [
            (u'activesupport', None, ['~> 3.0'], False,),
            (u'addressable', None, [], False,),
            (u'debugger', None, [], True,),
            (u'eventmachine', None, ['~> 1.0.0'], True,),
            (u'machinist', None, ['~> 1.0.6'], False,),
            (u'mysql2', None, [], False,),
            (u'nokogiri', None, ['~> 1.6.2'], False,),
            (u'rspec-instafail', None, [], False,),
            (u'sequel', None, ['~> 3.48'], False,),
            (u'yajl-ruby', None, [], True,),
                          ]

        for name, version, vercon, pinned in expected_gems:
            g = gfl.dependencies[name]
            self.assertEqual(version, g.version)
            self.assertEqual(vercon, g.version_constraints)
            self.assertEqual(pinned, g.pinned)

    def test_parse_platform(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_platform/Gemfile.lock')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        expected = [u'ruby', u'java', ]
        self.assertEqual(expected, gfl.platforms)

    def test_Gem_urn(self):
        a = gemfile_lock.Gem('a', '1')
        self.assertEqual('urn:dje:component:a:1', a.urn)

    def test_Gem_as_nv_tree(self):
        Gem = gemfile_lock.Gem
        a = Gem('a', '1')
        b = Gem('b', '2')
        c = Gem('c', '2')
        d = Gem('d', '2')
        e = Gem('e', '2')
        f = Gem('f', '2')

        a.dependencies['b'] = b
        a.dependencies['c'] = c

        b.dependencies['d'] = d
        b.dependencies['e'] = e
        b.dependencies['f'] = f

        c.dependencies['e'] = e
        c.dependencies['f'] = f

        expected = {('a', '1'): {('b', '2'): {('d', '2'): {},
                                             ('e', '2'): {},
                                             ('f', '2'): {}},
                                ('c', '2'): {('e', '2'): {},
                                             ('f', '2'): {}}}}
        self.assertEqual(expected, a.as_nv_tree())

    def test_Gem_flatten_urn(self):
        Gem = gemfile_lock.Gem
        a = Gem('a', 'v1')
        b = Gem('b', 'v2')
        c = Gem('c', 'v3')
        d = Gem('d', 'v4')
        e = Gem('e', 'v5')
        f = Gem('f', 'v6')
        g = Gem('g', 'v7')

        a.dependencies['b'] = b
        a.dependencies['c'] = c

        b.dependencies['d'] = d
        b.dependencies['e'] = e
        b.dependencies['f'] = f

        c.dependencies['e'] = e
        c.dependencies['f'] = f
        c.dependencies['g'] = g

        g.dependencies['b'] = b

        expected = sorted([
            (u'urn:dje:component:a:v1', 'a-v1.gem', u'urn:dje:component:b:v2', 'b-v2.gem'),
            (u'urn:dje:component:a:v1', 'a-v1.gem', u'urn:dje:component:c:v3', 'c-v3.gem'),
            (u'urn:dje:component:b:v2', 'b-v2.gem', u'urn:dje:component:d:v4', 'd-v4.gem'),
            (u'urn:dje:component:b:v2', 'b-v2.gem', u'urn:dje:component:e:v5', 'e-v5.gem'),
            (u'urn:dje:component:b:v2', 'b-v2.gem', u'urn:dje:component:f:v6', 'f-v6.gem'),
            (u'urn:dje:component:c:v3', 'c-v3.gem', u'urn:dje:component:e:v5', 'e-v5.gem'),
            (u'urn:dje:component:c:v3', 'c-v3.gem', u'urn:dje:component:f:v6', 'f-v6.gem'),
            (u'urn:dje:component:c:v3', 'c-v3.gem', u'urn:dje:component:g:v7', 'g-v7.gem'),
            (u'urn:dje:component:g:v7', 'g-v7.gem', u'urn:dje:component:b:v2', 'b-v2.gem'),
            ])
        results = sorted(a.flatten_urn())
        self.assertEqual(expected, results)

    def test_Gem_flatten(self):
        Gem = gemfile_lock.Gem
        a = Gem('a', 'v1')
        b = Gem('b', 'v2')
        c = Gem('c', 'v3')
        d = Gem('d', 'v4')
        e = Gem('e', 'v5')
        f = Gem('f', 'v6')
        g = Gem('g', 'v7')

        a.dependencies['b'] = b
        a.dependencies['c'] = c

        b.dependencies['d'] = d
        b.dependencies['e'] = e
        b.dependencies['f'] = f

        c.dependencies['e'] = e
        c.dependencies['f'] = f
        c.dependencies['g'] = g

        g.dependencies['b'] = b

        expected = sorted([
            (a, c),
            (a, b),
            (b, d),
            (b, e),
            (b, f),
            (c, e),
            (c, f),
            (c, g),
            (g, b),
            ])
        results = sorted(a.flatten())
        self.assertEqual(expected, results)

    def test_Gem_as_nv_tree_with_no_deps(self):
        Gem = gemfile_lock.Gem
        a = Gem('a', '1')
        expected = {('a', '1'): {}}
        self.assertEqual(expected, a.as_nv_tree())

    def test_Gem_pformat(self):
        Gem = gemfile_lock.Gem
        a = Gem('a', '1')
        b = Gem('b', '2')
        a.dependencies['b'] = b
        expected = '''Gem(name='a',
    version='1',
    platform=None,
    pinned=False,
    remote=None,
    type=None,
    path=None,
    location=None,
    revision=None,
    ref=None,
    branch=None,
    submodules=None,
    tag=None,
    version_constraints=
        [],
    dependencies=
        {('a', '1'): {('b', '2'): {}}},
    )'''
        self.assertEqual(expected, a.pformat())

    def test_parse_spec_single_level(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_spec/Gemfile.lock1')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        expected_names = ['user-lib']
        self.assertEqual(expected_names, gfl.all_gems.keys())
        expected_tree = {(u'user-lib', u'2.1.0'): {}}
        result = gfl.all_gems['user-lib'].as_nv_tree()
        self.assertEqual(expected_tree, result)

    def test_parse_spec_two_levels(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_spec/Gemfile.lock2')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        expected_names = ['user-lib', 'multi_json']
        self.assertEqual(expected_names, gfl.all_gems.keys())
        expected_tree = {(u'user-lib', u'2.1.0'): {('multi_json', None):{}}}
        result = gfl.all_gems['user-lib'].as_nv_tree()
        self.assertEqual(expected_tree, result)
        result = gfl.all_gems['multi_json'].as_nv_tree()
        self.assertEqual({('multi_json', None):{}}, result)

    def test_parse_spec_multi_levels(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_spec/Gemfile.lock3')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        expected_tree = {
            u'activesupport': {(u'activesupport', u'3.2.17'): {(u'i18n', '0.6.9'): {},
                                                               (u'multi_json', '1.9.2'): {}}},
            u'addressable': {(u'addressable', u'2.3.6'): {}},
            u'allowy': {(u'allowy', u'0.4.0'): {(u'activesupport', u'3.2.17'): {(u'i18n', '0.6.9'): {},
                                                                                (u'multi_json', '1.9.2'): {}},
                                                (u'i18n', '0.6.9'): {}}},
            u'i18n': {(u'i18n', '0.6.9'): {}},
            u'multi_json': {(u'multi_json', '1.9.2'): {}}
            }

        result = dict((n, g.as_nv_tree(),) for n, g in gfl.all_gems.items())
        self.assertEqual(expected_tree, result)

    def test_parse_spec_multi_levels_complex(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_spec/Gemfile.lock4')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        expected_tree = {
            u'activesupport':
                {(u'activesupport', u'3.2.17'):
                    {(u'i18n', u'0.6.9'):
                        {(u'clockwork', u'0.4.1'):
                            {(u'fluent-logger', u'0.4.7'):
                                {(u'msgpack', u'0.5.8'): {},
                                 (u'yajl-ruby', u'1.2.0'): {}}}},
                     (u'multi_json', u'1.9.2'): {}}},

            u'addressable': {(u'addressable', u'2.3.6'): {}},

            u'allowy':
                {(u'allowy', u'0.4.0'):
                    {(u'activesupport', u'3.2.17'):
                        {(u'i18n', u'0.6.9'):
                            {(u'clockwork', u'0.4.1'):
                                {(u'fluent-logger', u'0.4.7'):
                                    {(u'msgpack', u'0.5.8'): {},
                                    (u'yajl-ruby', u'1.2.0'): {}}}},
                         (u'multi_json', u'1.9.2'): {}},
                     (u'i18n', u'0.6.9'):
                        {(u'clockwork', u'0.4.1'):
                            {(u'fluent-logger', u'0.4.7'):
                                {(u'msgpack', u'0.5.8'): {},
                                 (u'yajl-ruby', u'1.2.0'): {}}}}}},

            u'clockwork':
                {(u'clockwork', u'0.4.1'):
                    {(u'fluent-logger', u'0.4.7'):
                        {(u'msgpack', u'0.5.8'): {},
                         (u'yajl-ruby', u'1.2.0'): {}}}},

            u'delayed_job':
                {(u'delayed_job', u'4.0.0'):
                    {(u'activesupport', u'3.2.17'):
                        {(u'i18n', u'0.6.9'):
                            {(u'clockwork', u'0.4.1'):
                                {(u'fluent-logger', u'0.4.7'):
                                    {(u'msgpack', u'0.5.8'): {},
                                     (u'yajl-ruby', u'1.2.0'): {}}}},
                         (u'multi_json', u'1.9.2'): {}}}},

            u'fluent-logger': {(u'fluent-logger', u'0.4.7'):
                                    {(u'msgpack', u'0.5.8'): {},
                                     (u'yajl-ruby', u'1.2.0'): {}}},

            u'i18n': {(u'i18n', u'0.6.9'):
                            {(u'clockwork', u'0.4.1'):
                                {(u'fluent-logger', u'0.4.7'):
                                    {(u'msgpack', u'0.5.8'): {},
                                     (u'yajl-ruby', u'1.2.0'): {}}}}},

            u'msgpack': {(u'msgpack', u'0.5.8'): {}},
            u'multi_json': {(u'multi_json', u'1.9.2'): {}},
            u'yajl-ruby': {(u'yajl-ruby', u'1.2.0'): {}}
        }

        result = dict((n, g.as_nv_tree(),) for n, g in gfl.all_gems.items())
        self.assertEqual(expected_tree, result)

    def test_parse_gem(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_gem/Gemfile.lock1')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual('https://rubygems.org/', gfl.current_options['remote'])

    def test_parse_gem_with_two_remotes(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_gem/Gemfile.lock3')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual({u'remote': u'https://rubygems.org/'}, gfl.current_options)

    def test_parse_gem_with_path_before(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_gem/Gemfile.lock2')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual({u'remote': u'http://rubygems.org/'}, gfl.current_options)

    def test_parse_source_one_path(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_source/Gemfile.lock_path1')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual({u'remote': u'.'}, gfl.current_options)
        self.assertEqual('PATH', gfl.current_type)

    def test_parse_source_two_path(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_source/Gemfile.lock_path2')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual({u'remote': u'/'}, gfl.current_options)
        self.assertEqual('PATH', gfl.current_type)

    def test_parse_source_mixed_step1(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_source/Gemfile.lock_mixed1')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual({u'tag': u'that', u'remote': u'.'}, gfl.current_options)

    def test_parse_source_mixed_step2(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_source/Gemfile.lock_mixed2')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual({u'remote': u'http://rubygems.org/'}, gfl.current_options)

    def test_parse_source_mixed_step3(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_source/Gemfile.lock_mixed3')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual({u'branch': u'tree',
                          u'ref': u'this',
                          u'remote': u'https://github.com/mypath/registrar.git',
                          u'revision': u'49850ee876652a59dbd2233dad726b3b808bb8f9',
                          u'tag': u'that'},
                         gfl.current_options)

    def test_parse_source_mixed_step4(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_source/Gemfile.lock_mixed4')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        expected = {u'branch': u'treebranch',
                    u'ref': u'81e5e4d6',
                    u'remote': u'https://github.com/mylib/lib.git',
                    u'revision': u'81e5e4d622338b3332ab24840e6b40d47b161849',
                    u'tag': u'thistag'}
        self.assertEqual(expected, gfl.current_options)

    def test_parse_source_mixed_step5(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_source/Gemfile.lock_mixed5')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        self.assertEqual({u'remote': u'/asdasda'}, gfl.current_options)

    def test_parse_source_with_multi_paths_in_git(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_git/Gemfile.lock')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        result_deps = '\n'.join(repr(i) for i in gfl.all_gems.items())
        expected_deps = (
'''(u'barden-client', Gem(name=u'barden-client', version=u'517d065bfbbbad82e7165639d32adf298b48471a', type=u'GIT'))
(u'eventmachine', Gem(name=u'eventmachine', version=None, type=u'GEM'))
(u'barden-server', Gem(name=u'barden-server', version=u'517d065bfbbbad82e7165639d32adf298b48471a', type=u'GIT'))
(u'barden-network', Gem(name=u'barden-network', version=u'517d065bfbbbad82e7165639d32adf298b48471a', type=u'GIT'))
(u'beefcake', Gem(name=u'beefcake', version=None, type=u'GEM'))''')
        self.assertEqual(expected_deps, result_deps)

        expected = [
        dict(name=u'barden-client',
            version=u'517d065bfbbbad82e7165639d32adf298b48471a',
            platform='ruby',
            pinned=False,
            remote=u'https://github.com/bitops/barden.git',
            type=u'GIT',
            path=None,
            location=None,
            revision=u'517d065bfbbbad82e7165639d32adf298b48471a',
            ref=None,
            branch=None,
            submodules=None,
            tag=None,
            ),
        dict(name=u'eventmachine',
            version=None,
            platform=None,
            pinned=False,
            remote=None,
            type=u'GEM',
            path=None,
            location=None,
            revision=None,
            ref=None,
            branch=None,
            submodules=None,
            tag=None,
            ),
        dict(name=u'barden-server',
            version=u'517d065bfbbbad82e7165639d32adf298b48471a',
            platform='ruby',
            pinned=False,
            remote=u'https://github.com/bitops/barden.git',
            type=u'GIT',
            path=None,
            location=None,
            revision=u'517d065bfbbbad82e7165639d32adf298b48471a',
            ref=None,
            branch=None,
            submodules=None,
            tag=None,
            ),
        dict(name=u'barden-network',
            version=u'517d065bfbbbad82e7165639d32adf298b48471a',
            platform='ruby',
            pinned=False,
            remote=u'https://github.com/bitops/barden.git',
            type=u'GIT',
            path=None,
            location=None,
            revision=u'517d065bfbbbad82e7165639d32adf298b48471a',
            ref=None,
            branch=None,
            submodules=None,
            tag=None,),
        dict(name=u'beefcake',
            remote=None,
            type=u'GEM',
            path=None,
            location=None,
            revision=None,
            ref=None,
            branch=None,
            submodules=None,
            tag=None)]
        for ex in expected:
            res = gfl.all_gems[ex['name']]
            for k, v in ex.items():
                self.assertEqual(v, getattr(res, k))

    def test_parse_source_git_no_deps(self):
        gemfilelock = self.get_test_loc('gemfile_lock/parse_git/Gemfile.lock_single')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        result_deps = '\n'.join(repr(i) for i in gfl.all_gems.items())
        expected_deps = "(u'concurrency', Gem(name=u'concurrency', version=u'2a5b0179842cb3d3e7f912a6453ec5731979d115', type=u'GIT'))"
        self.assertEqual(expected_deps, result_deps)

        expected = [
        dict(name=u'concurrency',
            version=u'2a5b0179842cb3d3e7f912a6453ec5731979d115',
            pinned=False,
            remote=u'https://github.com/pombredanne/concurrency.git',
            type=u'GIT',
            revision=u'2a5b0179842cb3d3e7f912a6453ec5731979d115',
            ref='2a5b01798',
            branch=None,),
                ]
        for ex in expected:
            res = gfl.all_gems[ex['name']]
            for k, v in ex.items():
                self.assertEqual(v, getattr(res, k))

    def test_GemfileLockParser_can_parse_simple_files(self):
        gemfilelock = self.get_test_loc('gemfile_lock/complete/Gemfile.lock_simple')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        result = '\n\n'.join(g.pformat() for g in gfl.all_gems.values())
        exf = self.get_test_loc('gemfile_lock/complete/expected_Gemfile.lock_simple')
        expected = open(exf).read()
        self.assertEqual(expected, result)

        result_deps = '\n'.join(repr(i) for i in gfl.dependencies.items())
        expected_deps = (
'''(u'activerecord', Gem(name=u'activerecord', version=u'4.0.0', type=u'GEM'))
(u'appraisal', Gem(name=u'appraisal', version=u'0.5.2', type=u'GEM'))
(u'aruba', Gem(name=u'aruba', version=u'0.5.3', type=u'GEM'))
(u'bourne', Gem(name=u'bourne', version=u'1.5.0', type=u'GEM'))
(u'cucumber', Gem(name=u'cucumber', version=u'1.2.5', type=u'GEM'))
(u'factory_girl', Gem(name=u'factory_girl', version=u'4.3.0', type=u'PATH'))
(u'mocha', Gem(name=u'mocha', version=u'0.14.0', type=u'GEM'))
(u'rspec', Gem(name=u'rspec', version=u'2.12.0', type=u'GEM'))
(u'simplecov', Gem(name=u'simplecov', version=u'0.7.1', type=u'GEM'))
(u'sqlite3', Gem(name=u'sqlite3', version=u'1.3.8', type=u'GEM'))
(u'timecop', Gem(name=u'timecop', version=u'0.6.2.2', type=u'GEM'))
(u'yard', Gem(name=u'yard', version=u'0.8.7', type=u'GEM'))''')
        self.assertEqual(expected_deps, result_deps)
        self.assertEqual(True, gfl.dependencies['factory_girl'].pinned)

    def test_GemfileLockParser_can_yield_a_flat_list_of_deps(self):
        gemfilelock = self.get_test_loc('gemfile_lock/as_deps/Gemfile.lock')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        result = sorted(repr(fd) for fd in gfl.flatten())
        expected = sorted([
            "(Gem(name=u'activemodel', version=u'4.0.0', type=u'GEM'), Gem(name=u'activesupport', version=u'4.0.0', type=u'GEM'))",
            "(Gem(name=u'activemodel', version=u'4.0.0', type=u'GEM'), Gem(name=u'builder', version=u'3.1.4', type=u'GEM'))",
            "(Gem(name=u'activerecord', version=u'4.0.0', type=u'GEM'), Gem(name=u'activemodel', version=u'4.0.0', type=u'GEM'))",
            "(Gem(name=u'activerecord', version=u'4.0.0', type=u'GEM'), Gem(name=u'activerecord-deprecated_finders', version=u'1.0.3', type=u'GEM'))",
            "(Gem(name=u'activerecord', version=u'4.0.0', type=u'GEM'), Gem(name=u'activesupport', version=u'4.0.0', type=u'GEM'))",
            "(Gem(name=u'activerecord', version=u'4.0.0', type=u'GEM'), Gem(name=u'arel', version=u'4.0.0', type=u'GEM'))",
            "(Gem(name=u'activesupport', version=u'4.0.0', type=u'GEM'), Gem(name=u'i18n', version=u'0.6.4', type=u'GEM'))",
            "(Gem(name=u'activesupport', version=u'4.0.0', type=u'GEM'), Gem(name=u'minitest', version=u'4.7.5', type=u'GEM'))",
            "(Gem(name=u'activesupport', version=u'4.0.0', type=u'GEM'), Gem(name=u'multi_json', version=u'1.7.7', type=u'GEM'))",
            "(Gem(name=u'activesupport', version=u'4.0.0', type=u'GEM'), Gem(name=u'thread_safe', version=u'0.1.2', type=u'GEM'))",
            "(Gem(name=u'activesupport', version=u'4.0.0', type=u'GEM'), Gem(name=u'tzinfo', version=u'0.3.37', type=u'GEM'))",
            "(Gem(name=u'appraisal', version=u'0.5.2', type=u'GEM'), Gem(name=u'rake', version=u'10.1.0', type=u'GEM'))",
            "(Gem(name=u'aruba', version=u'0.5.3', type=u'GEM'), Gem(name=u'childprocess', version=u'0.3.9', type=u'GEM'))",
            "(Gem(name=u'aruba', version=u'0.5.3', type=u'GEM'), Gem(name=u'cucumber', version=u'1.2.5', type=u'GEM'))",
            "(Gem(name=u'aruba', version=u'0.5.3', type=u'GEM'), Gem(name=u'rspec-expectations', version=u'2.12.1', type=u'GEM'))",
            "(Gem(name=u'bourne', version=u'1.5.0', type=u'GEM'), Gem(name=u'mocha', version=u'0.14.0', type=u'GEM'))",
            "(Gem(name=u'childprocess', version=u'0.3.9', type=u'GEM'), Gem(name=u'ffi', version=u'1.9.0', type=u'GEM'))",
            "(Gem(name=u'cucumber', version=u'1.2.5', type=u'GEM'), Gem(name=u'builder', version=u'3.1.4', type=u'GEM'))",
            "(Gem(name=u'cucumber', version=u'1.2.5', type=u'GEM'), Gem(name=u'diff-lcs', version=u'1.1.3', type=u'GEM'))",
            "(Gem(name=u'cucumber', version=u'1.2.5', type=u'GEM'), Gem(name=u'gherkin', version=u'2.11.8', type=u'GEM'))",
            "(Gem(name=u'cucumber', version=u'1.2.5', type=u'GEM'), Gem(name=u'multi_json', version=u'1.7.7', type=u'GEM'))",
            "(Gem(name=u'factory_girl', version=u'4.3.0', type=u'PATH'), Gem(name=u'activesupport', version=u'4.0.0', type=u'GEM'))",
            "(Gem(name=u'gherkin', version=u'2.11.8', type=u'GEM'), Gem(name=u'multi_json', version=u'1.7.7', type=u'GEM'))",
            "(Gem(name=u'mocha', version=u'0.14.0', type=u'GEM'), Gem(name=u'metaclass', version=u'0.0.1', type=u'GEM'))",
            "(Gem(name=u'rspec', version=u'2.12.0', type=u'GEM'), Gem(name=u'rspec-core', version=u'2.12.2', type=u'GEM'))",
            "(Gem(name=u'rspec', version=u'2.12.0', type=u'GEM'), Gem(name=u'rspec-expectations', version=u'2.12.1', type=u'GEM'))",
            "(Gem(name=u'rspec', version=u'2.12.0', type=u'GEM'), Gem(name=u'rspec-mocks', version=u'2.12.2', type=u'GEM'))",
            "(Gem(name=u'rspec-expectations', version=u'2.12.1', type=u'GEM'), Gem(name=u'diff-lcs', version=u'1.1.3', type=u'GEM'))",
            "(Gem(name=u'simplecov', version=u'0.7.1', type=u'GEM'), Gem(name=u'multi_json', version=u'1.7.7', type=u'GEM'))",
            "(Gem(name=u'simplecov', version=u'0.7.1', type=u'GEM'), Gem(name=u'simplecov-html', version=u'0.7.1', type=u'GEM'))",
            "(Gem(name=u'thread_safe', version=u'0.1.2', type=u'GEM'), Gem(name=u'atomic', version=u'1.1.10', type=u'GEM'))",
            "(None, Gem(name=u'activerecord', version=u'4.0.0', type=u'GEM'))",
            "(None, Gem(name=u'appraisal', version=u'0.5.2', type=u'GEM'))",
            "(None, Gem(name=u'aruba', version=u'0.5.3', type=u'GEM'))",
            "(None, Gem(name=u'bourne', version=u'1.5.0', type=u'GEM'))",
            "(None, Gem(name=u'cucumber', version=u'1.2.5', type=u'GEM'))",
            "(None, Gem(name=u'factory_girl', version=u'4.3.0', type=u'PATH'))",
            "(None, Gem(name=u'mocha', version=u'0.14.0', type=u'GEM'))",
            "(None, Gem(name=u'rspec', version=u'2.12.0', type=u'GEM'))",
            "(None, Gem(name=u'simplecov', version=u'0.7.1', type=u'GEM'))",
            "(None, Gem(name=u'sqlite3', version=u'1.3.8', type=u'GEM'))",
            "(None, Gem(name=u'timecop', version=u'0.6.2.2', type=u'GEM'))",
            "(None, Gem(name=u'yard', version=u'0.8.7', type=u'GEM'))",
        ])
        self.assertEqual(expected, result)

    def test_GemfileLockParser_can_parse_complex_files(self):
        gemfilelock = self.get_test_loc('gemfile_lock/complete/Gemfile.lock_complex')
        gfl = gemfile_lock.GemfileLockParser(gemfilelock)
        result = '\n\n'.join(g.pformat() for g in gfl.all_gems.values())
        exf = self.get_test_loc('gemfile_lock/complete/expected_Gemfile.lock_complex')
        regen = False
        if regen:
            with open(exf, 'wb') as outf:
                outf.write(result)
        expected = open(exf).read()
        self.assertEqual(expected.splitlines(), result.splitlines())

#         result_deps = '\n'.join(repr(i) for i in gfl.dependencies.items())
#         expected_deps = (
# '''(u'activerecord', Gem(name=u'activerecord', version=u'4.0.0', type=u'GEM'))
# (u'appraisal', Gem(name=u'appraisal', version=u'0.5.2', type=u'GEM'))
# (u'aruba', Gem(name=u'aruba', version=u'0.5.3', type=u'GEM'))
# (u'bourne', Gem(name=u'bourne', version=u'1.5.0', type=u'GEM'))
# (u'cucumber', Gem(name=u'cucumber', version=u'1.2.5', type=u'GEM'))
# (u'factory_girl', Gem(name=u'factory_girl', version=u'4.3.0', type=u'PATH'))
# (u'mocha', Gem(name=u'mocha', version=u'0.14.0', type=u'GEM'))
# (u'rspec', Gem(name=u'rspec', version=u'2.12.0', type=u'GEM'))
# (u'simplecov', Gem(name=u'simplecov', version=u'0.7.1', type=u'GEM'))
# (u'sqlite3', Gem(name=u'sqlite3', version=u'1.3.8', type=u'GEM'))
# (u'timecop', Gem(name=u'timecop', version=u'0.6.2.2', type=u'GEM'))
# (u'yard', Gem(name=u'yard', version=u'0.8.7', type=u'GEM'))''')
#         self.assertEqual(expected_deps, result_deps)
#         self.assertEqual(True, gfl.dependencies['factory_girl'].pinned)
