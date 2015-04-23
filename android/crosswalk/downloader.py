#!/usr/bin/env pypy

import os
import sys
import subprocess
from pprint import pprint


def downloadArchive(deps):
    for directory, url in deps.iteritems():
        if directory.startswith('v8'):
            directory = 'src/' + directory
        try:
            os.makedirs(directory)
        except OSError:
            pass

        if url is None: continue
        if '@' in url and (
             url.startswith('https://chromium.googlesource.com/') or
             url.startswith('http://src.chromium.org/') or
             url.startswith('https://pdfium.googlesource.com/') or
             url.startswith('https://boringssl.googlesource.com/')):

            source, filename = url.rsplit('@')
            filename += '.tar.gz'
            url = '%s/+archive/%s' % (source, filename)

            print 'Downloading: %s -> %s -> %s' % (directory, filename, url)
            if os.path.exists(os.path.join(directory, filename)):
                continue
            os.system('cd %s && wget -q %s' % (directory, url))
        else:
            print 'NOT Downloading: %s -> %s' % (directory, url)

depsFiles = reduce(lambda x, y: x + y, [ filter(lambda filename: 'DEPS' in filename, map(lambda k_: os.path.join(i, k_), k)) for i, j, k in os.walk('src') ])
for depsFile in depsFiles:
#   if '.DEPS' not in depsFile:
#       continue
    l = {}
    def Var(key): return l['vars'][key]
    g = {
        'Var': Var
    }
    execfile(depsFile, g, l)
    builtins = '__builtins__'
    if builtins in g:
        del g['__builtins__']
    if builtins in l:
        del l['__builtins__']

    deps = {}
    if 'solutions' in l.keys():
        for solution in l['solutions']:
            if 'custom_deps' in solution:
                deps.update(solution['custom_deps'])
    if 'deps' in l.keys():
        deps.update(l['deps'])
    if 'deps_os' in l.keys():
        if 'android' in l['deps_os']:
            deps.update(l['deps_os']['android'])

    if len(deps) <= 0:
        continue

#   pprint((os.path.join(os.path.dirname(depsFile), os.path.pardir), deps))

    downloadArchive(deps)
