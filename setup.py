"""Creates a Mac OS X application bundle for Path-Genius."""

# * Author(s): Thomas Glanzer
# * Creation : Oct 2023
# * License  : MIT

# %% ----------------------------------
# * Import libraries

from setuptools import setup

# %% ----------------------------------
# * Define py2app options

APP = ['path_genius_app.py']
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'assets/AppIcon.icns',
    'plist': {
        'CFBundleName': 'Path-Genius',
        'CFBundleDisplayName': 'Path-Genius',
        'CFBundleGetInfoString': 'Converts Windows and Mac file paths',
        'CFBundleIdentifier': 'com.thg.path-genius',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleExecutable': 'Path-Genius',
    },
    'packages': ['pyperclip'],
    'frameworks': ['assets/libffi.8.dylib'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
