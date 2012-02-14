#!/usr/bin/env python
# -*- coding: utf-8 -*-
#date: 14.02.12
import glob
import sys

from cx_Freeze import setup, Executable


#sys.argv.append('install_exe')
sys.argv.append('build_exe')

install_exe_options = {'install_dir': './Autocad tools'}
build_exe_options = {'excludes': ['bz2', '_hashlib', 'unittest']}  # TODO Experimental

exclude_scripts = ['cx_setup.py']
scripts_to_build = [name for name in glob.glob('*.py') if
                    name not in exclude_scripts]

setup(name="Autocad tools",
      version="0.1",
      description="Generate cable list, get drawing names etc.",

      options=dict(install_exe=install_exe_options,
                   build_exe=build_exe_options),

      executables=[Executable(script=script) for script in scripts_to_build])