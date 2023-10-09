"""Creates a Mac OS X application bundle for Path-Genius."""

# * Author(s): Thomas Glanzer
# * Creation : Oct 2023
# * License  : MIT

# %% ----------------------------------
# * Import libraries

from setuptools import setup

# %% ----------------------------------
# * Define py2app options

VERSION = '1.0.1'

APP = ['path_genius_app.py']
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'assets/AppIcon.icns',
    'plist': {
        'CFBundleName': 'Path-Genius',
        'CFBundleDisplayName': 'Path-Genius',
        'CFBundleGetInfoString': 'Converts Windows and Mac file paths',
        'CFBundleIdentifier': 'com.thg.path-genius',
        'CFBundleVersion': VERSION,
        'CFBundleShortVersionString': VERSION,
        'CFBundleExecutable': 'Path-Genius',
        'NSHumanReadableCopyright': '(c) 2023 Thomas Glanzer (MIT License)',
    },
    'packages': ['pyperclip', 'Foundation'],
    'frameworks': ['assets/libffi.8.dylib'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
