from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True, 'includes': ['sip']}},
    windows = [{
        'script': "pyqtwebkit.py", 
        'icon_resources': [(0, "pyQt.ico")], 
        'dest_base': 'pyqtwebkit'}],
    zipfile = None,
    version = '2014.11.18.1',
)