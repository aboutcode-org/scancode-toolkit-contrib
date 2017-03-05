
# Copyright (c) 2006 Jason Petrone <jp_py@demonseed.net>
# All Rights Reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#
#     * Neither the name of this product nor the names of its contributors may
#     be used to endorse or promote products derived from this software without
#     specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import absolute_import
import sys
from copy import copy

from .javaclass import _canonicalize
from .javaclass import ACCESS_MASK
from .javaclass import fmtAccessFlags
from .javaclass import Class
from .javaclass import ACC_FINAL
from .javaclass import ACC_STATIC
from .javaclass import ACC_NATIVE
from .javaclass import ACC_INTERFACE
from .javaclass import ACC_ABSTRACT
from .javaclass import ACC_SUPER_OR_SYNCHRONIZED
from .javaclass import getAccessFromFlags
from .javaclass import getJavacVersion

"""
Compares API differences between 2 class files

(C)opyright 2006 Jason Petrone <jp_py@demonseed.net>
All Rights Reserved

"""

__author__ = 'Jason Petrone <jp_py@demonseed.net>'
__version__ = '1.0'



USAGE = '''
Usage: %s [options] <file0.class> <file1.class>

Supported Options:
  --access=v0[,v1,...]   Filter by access level(package, private, protected,
                         public, all) [default=protected,public].
  --noadded              Suppress display of new fields, classes, and methods.
  --bincompat            Only show changes that will break binary compatibility
''' % (sys.argv[0])



# TODO:
#   * when "suppress_add" is enabled, won't catch new abstract fields
#     and methods
#   * check for changes in static final constants


def checkAccess(obj, opts):
    try:
        levels = opts['access_level']
    except KeyError:
        levels = ['all']

    if 'all' in levels:
        return 1

    isClass = type(obj) == Class
    # print '%s: %i' % (obj.name, obj.access)
    access = fmtAccessFlags(obj.access & ACCESS_MASK, isClass)
    if not access:
        access = 'package'
    try:
        return access in levels
    except KeyError:
        return 1


def parseCmdline(argv):
    files = []
    opts = {
        'access_level': ['protected', 'public'],
        'suppress_added': False,
        'bincompat': False,
    }
    for a in argv[1:]:
        if a.startswith('--access='):
            if '--bincompat' in argv:
                print 'Only one of --bincompat, or --access are allowed'
                sys.exit();
            opts['access_level'] = a.split('=')[-1].split(',')
        elif a == '--bincompat':
            opts['bincompat'] = True
            opts['access_level'] = ['public', 'protected']
            opts['suppress_added'] = True
        elif a == '--noadded':
            opts['suppress_added'] = True
        else:
            files.append(a)
    return opts, files


def compareModifiers(obj0, obj1, opts={}):
    a0 = obj0.access
    a1 = obj1.access

    if a0 == a1:
        return True

    if (a0 & ACC_FINAL) != (a1 & ACC_FINAL): return False
    if (a0 & ACC_STATIC) != (a1 & ACC_STATIC): return False
    if (a0 & ACC_NATIVE) != (a1 & ACC_NATIVE): return False
    if (a0 & ACC_INTERFACE) != (a1 & ACC_INTERFACE): return False
    if (a0 & ACC_ABSTRACT) != (a1 & ACC_ABSTRACT): return False


    # can ignore synchronization changes in bincompat mode
    if ((a0 & ACC_SUPER_OR_SYNCHRONIZED) != (a1 & ACC_SUPER_OR_SYNCHRONIZED)
        and not isinstance(obj0, Class) and not opts['bincompat']):
        return False

    p0 = getAccessFromFlags(a0)
    p1 = getAccessFromFlags(a1)
    # ignore access relaxation for binary compatibility
    if opts['bincompat']:
        if p0 == 'public' and p1 != 'public':
            return False
        elif p0 == 'protected' and p1 not in ['protected', 'public']:
            return False
        elif p0 == 'default' and p1 not in ['default', 'public']:
            return False
    else:
        if p0 != p1:
            return False

    return True


def classdiff(class0, class1, opts={}):
    '''
    See what has changed between the classes
    '''
    if not checkAccess(class0, opts) and not checkAccess(class1, opts):
        return

    diff = ''
    if class0.version != class1.version:
        v0 = class0.version
        v1 = class1.version
        javac0 = getJavacVersion(v0)
        javac1 = getJavacVersion(v1)
        if not opts['ignore_compiler_version']:
            diff += ('Different compiler versions: %s => %s  (%s => %s)\n' %
                     (v0, v1, javac0, javac1))

    if not compareModifiers(class0, class1, opts):
        a0 = fmtAccessFlags(class0.access, True)
        a1 = fmtAccessFlags(class1.access, True)
        diff += 'Class modifiers changed: "%s" => "%s"\n' % (a0, a1)

    if class0.superClass != class1.superClass:
        s0 = _canonicalize(class0.superClass)
        s1 = _canonicalize(class1.superClass)
        diff += 'New superclass:  %s => %s\n' % (s0, s1)

    if class0.interfaces != class1.interfaces:
        i0 = ', '.join(class0.interfaces)
        i1 = ', '.join(class1.interfaces)
        diff += 'Interfaces changes:  %s => %s\n' % (i0, i1)

    diff += '\n'
    diff += diffMethods(class0, class1, opts)
    diff += '\n'
    diff += diffFields(class0, class1, opts)

    if diff.strip():
        print 70 * '/'
        print '// Class %s' % (class0.name.replace('/', '.'))
        # print len('Class '+class0.name)*'//'
        print 70 * '/'
        print
        print diff


def diffFields(class0, class1, opts={}):
    fields = {}
    for field in class0.fields:
        fields[field.name] = field

    addedfields = []
    changedfields = []
    fields1 = copy(class1.fields)

    for newfield in fields1:
        try:
            oldfield = fields[newfield.name]
        except KeyError:
            # new field in class1
            if checkAccess(newfield, opts):
                addedfields.append(newfield)
            continue

        if not checkAccess(newfield, opts) and not checkAccess(oldfield, opts):
            continue

        if not compareModifiers(oldfield, newfield, opts):
            # field signature changed
            changedfields.append('%s => %s' % (str(oldfield), str(newfield)))

        del(fields[newfield.name])

    diff = ''

    if changedfields:
        diff += 'Changed Fields:\n'
        diff += '  ' + '\n  '.join(changedfields) + '\n'
        diff += '\n'

    if addedfields and not opts['suppress_added']:
        diff += 'Added Fields:\n'
        diff += '  ' + '\n  '.join(map(str, addedfields)) + '\n'
        diff += '\n'

    removed = [str(x) for x in fields.values() if checkAccess(x, opts)]
    if removed:
        diff += 'Removed Fields:\n'
        diff += '  ' + '\n  '.join(removed) + '\n'
        diff += '\n'

    return diff


def diffMethods(class0, class1, opts={}):
    meths = {}
    for meth in class0.methods:
        sig = '%s(%s)' % (meth.name, ', '.join(meth.args))
        meths[sig] = meth

    addedmeths = []
    changedmeths = []
    meths1 = copy(class1.methods)

    for newmeth in meths1:
        sig = '%s(%s)' % (newmeth.name, ', '.join(newmeth.args))
        try:
            oldmeth = meths[sig]
        except KeyError:
            # new method in class1
            if checkAccess(newmeth, opts):
                addedmeths.append(newmeth)
            continue

        # make sure return type or modifiers haven't changed
        if checkAccess(newmeth, opts) or checkAccess(oldmeth, opts):
            if not compareModifiers(oldmeth, newmeth, opts):
                s = '%s => %s' % (str(oldmeth), str(newmeth))
                changedmeths.append(s)

        # remove from meths so we can use whats left for added list
        del(meths[sig])

    diff = ''

    if changedmeths:
        diff += 'Changed Methods:\n'
        diff += '  ' + '\n  '.join(map(str, changedmeths)) + '\n'
        diff += '\n'


    if addedmeths and not opts['suppress_added']:
        diff += 'Added Methods:\n'
        diff += '  ' + '\n  '.join(map(str, addedmeths)) + '\n'
        diff += '\n'

    removed = [str(x) for x in meths.values() if checkAccess(x, opts)]
    if removed:
        diff += 'Removed Methods:\n'
        diff += '  ' + '\n  '.join(removed) + '\n'
        diff += '\n'

    return diff

if __name__ == '__main__':
    opts, l = parseCmdline(copy(sys.argv))

    if len(l) != 2:
        print USAGE
        sys.exit(-1)

    c0 = Class(open(l[0], 'rb'))
    c1 = Class(open(l[1], 'rb'))
    classdiff(c0, c1, opts)


