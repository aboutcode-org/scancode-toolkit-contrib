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


"""
Known packaging and package metadata formats.
https://en.wikipedia.org/wiki/Package_manager
https://en.wikipedia.org/wiki/Package_format
"""
package_formats = {

    # mainline distros
    'rpm': ('RPM (Linux)', ''),
    # 'rpm_spec': ('RPM spec file (Linux)', ''),
    'deb': ('Debian (Linux)', ''),
    # 'deb_control': ('Debian control file (Linux)', ''),


    # java
    'pom': ('Maven POM (Java)', ''),
    'ivy': ('IVY (Java)', ''),
    'gradle': ('gradle (Groovy/Java)', 'https://gradle.org/'),
    'jboss': ('JBoss (Java)', ''),
    'buildr': ('buildr (Ruby)', 'https://buildr.apache.org/'),
    'osgi': ('OSGi (Eclipse/Java)', ''),
    'sbt': ('sbt (Scala/Java)', 'http://www.scala-sbt.org/'),

    'clojars': ('Clojars (Clojure)', ''),
    'eclipse': ('Eclipse plugin (Eclipse)', ''),
    'netbeans': ('NetBeans plugin (NetBeans)', ''),
    'jenkins': ('Jenkins plugin (Jenkins)', ''),

    # linux
    'lkm': ('Loadable Kernel Module (Linux)', ''),

    # Perl
    'cpan': ('CPAN (Perl)', ''),

    # ruby
    'gem': ('RubyGems (Ruby)', ''),
    'gemfile': ('Bundler Gemfile/Gemfile.lock (Ruby)', ''),
    'gemspec': ('RubyGem gemspec file (Ruby)', ''),

    # JS
    'npm': ('npm (JavaScript)', ''),
    'jspm': ('jspm (JavaScript)', ''),
    'bower': ('Bower (JavaScript)', ''),

    # php
    'pear': ('PEAR (PHP)', ''),
    'composer': ('Composer (PHP)', ''),

    # python
    'setup.py': ('Python package (Python)', ''),
    'sdist': ('PyPI (Python)', ''),
    'bdist': ('PyPI (Python)', ''),
    'pypi': ('PyPI (Python)', ''),
    'py': ('Python metadata', ''),  # __version__, __copyright__
    'egg': ('Egg (Python)', ''),
    'wheel': ('Wheel (Python)', ''),

    # windows
    'nuget': ('NuGet (.NET)', ''),

    # exes
    'winpe': ('PE Binary (Windows)', ''),
    'elf': ('ELF binaries (POSIX)', ''),
    'macho': ('Mach-O binaries (MacOSX)', ''),

    # installers
    'mpkg': ('Apple m/package (MacOSX)', ''),
    'msi': ('Windows installer (Windows)', ''),


    # mobile
    'ipa': ('.ipa (iOS)', ''),
    'apk': ('.apk (Android)', ''),
    'modlic': ('MODULE_LICENSE (Android)', ''),

    # Go
    'godoc': ('GoDoc (Go)', ''),
    'godep': ('Godep (Go)', 'https://github.com/tools/godep'),
    # less common
    'gom': ('Gom (Go)', ''),
    'gondler': ('Gondler (Go)', ''),
    'goop': ('Goop (Go)', ''),
    'dondur': ('dondur (Go)', 'https://github.com/oguzbilgic/dondur'),

    # less common
    'buildout': ('buildout (Python)', ''),
    'about': ('AboutCode', 'http://aboutcode.org'),
    'freebsd': ('FreeBSD ports (Unix)', ''),
    'openbsd': ('OpenBSD ports (Unix)', ''),
    'podfile': ('CocoaPods Podfile (Objective-C/Swift)', 'https://cocoapods.org/'),
    'vmdk': ('VMware disk image', ''),
    'vdi': ('VirtualBox disk image', ''),
    'spdx': ('SPDX', ''),
    'doap': ('DOAP', ''),
    'docker': ('Docker Image', ''),
    'bosh': ('BOSH (CloudFoundry)', ''),

    'ebuild': ('Gentoo ebuild(Linux)', ''),
    'nix': ('NixOS (Linux)', ''),
    'conary': ('conary rPath (Linux)', ''),
    'opkg': ('Yocto opkg (Linux)', ''),
    'pacman': ('ArchLinux pacman (Linux)', ''),
    'pkgsrc': ('NetBSD pkgsrc (Unix)', ''),
    'brew': ('Homebrew (MacOSX)', ''),
    'slack': ('Slackware (Linux)', ''),
    'solaris': ('Solaris (Unix)', ''),

    'cran': ('CRAN (R)', ''),
    'mix': ('Mix (Elixir/Erlang)', 'http://Hex.pm',),
    'melpa': ('MELPA (Emacs)', ''),
    'cabal': ('Cabal (Haskell)', ''),
    'cargo': ('cargo (Rust)', ''),
    'conda': ('Conda (Python)', ''),
    'pypm': ('PyPM (Python)', ''),
    'rocks': ('LuaRocks (Lua)', ''),
    'appdata': ('AppStream (Linux)', 'https://github.com/ximion/appstream'),
    'asdf': ('ASDF (Common Lisp)', ''),
    'ctan': ('CTAN (TeX)', ''),
    'appx': ('.appx (Windows 8)', ''),

    'sublime': ('Sublime plugin (Sublime)', ''),

    'rebar': ('Rebar (Erlang)', ''),
    'cean': ('CEAN (Erlang)', ''),
    'beam': ('Beam (Erlang)', ''),
}
