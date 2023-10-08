# Path-Genius

A simple Python script that converts links from Mac to Windows and vice versa. The script uses the pyperclip library to read from and write to the clipboard. You can also use it as a Mac executable (see instructions below).

- *smb* links will be converted to *file* links (and vice versa)
- *backslashes* will be converted to *forward slashes* (and vice versa)

## Usage - Mac Executable

To use Path-Genius as an application, simply run the provided Mac executable (app). The script will check the contents of the clipboard and determine whether it contains a Windows or Mac link. If a link is detected, the script will convert it to the other format and write the converted link back to the clipboard. After each conversion the application will quit.

It is strongly suggested to **add the application to your dock for easy access.**

## Usage - Command Line

To use the script from command-line, simply run:

```bash
python path_genius_app.py
```

The script will check the contents of the clipboard and determine whether it contains a Windows or Mac link. If a link is detected, the script will convert it to the other format and write the converted link back to the clipboard.

## Dependencies

Please check the requirements.txt file for a list of dependencies. You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Build from Source

You can use the script as a Mac executable (app). To build the executable yourself, just run the following command:

```bash
python setup.py py2app
```

This will create a folder called "dist" that contains the executable (app) - you can move the app to your Applications folder.

## Test cases

The script uses *pytest* test cases to ensure a minimum quality. To run the tests, simply run the following command:

```bash
pytest test_path_genius_app.py
```

## Authorship and License

This script was written by Thomas Glanzer in October 2023. Please see the LICENSE file for further details regarding the license.
