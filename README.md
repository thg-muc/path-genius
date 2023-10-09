# Path-Genius

A simple Python script that **converts links from Windows to Mac and vice versa**.

Path-Genius uses the pyperclip library to read from and write to the clipboard. It will check the contents of the clipboard and determine whether it contains a Windows or Mac link and convert it.

- *smb* links will be converted to *file* links (and vice versa)
- *backslashes* will be converted to *forward slashes* (and vice versa)

 The app is not supposed to run in the background, but only on request. After each conversion the application will quit.

## Usage - Mac Executable

You can also use Path-Genius as a Mac executable. To do this, download the latest binary from the release page and move the app to your Applications folder (or any other folder). Next, simply run the provided Mac executable (app).

In case the application is blocked by MacOS Security settings, be sure to obtain admin privileges and run the following command in the terminal to **remove the quarantine flag**:

```bash
xattr -d com.apple.quarantine /path/to/Path-Genius.app
```

It is suggested to **add the application to your dock for easy access.**

## Usage - Command Line

Before running from command line, be sure to install the dependencies from the requirements file. Once this is done, simply run:

```bash
python3 path_genius_app.py
```

The script will check the contents of the clipboard and convert the link to the other format. The script will quit after each conversion.

## Dependencies

Please check the requirements.txt file for a list of dependencies. You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Build from Source

You can use the script as a Mac executable (app). Before performing this step, be sure to install the listed dependencies in the requirements file to ad the required libraries to you Python 3.10/3.11 installation. Afterwards, just run the following command:

```bash
python3 setup.py py2app
```

This will create a folder called "dist" which contains the executable (app) - you can then move the app to your Applications folder.

## Test cases

The script uses *pytest* test cases to ensure a minimum quality. To run the tests, simply run the following command:

```bash
pytest test_path_genius_app.py
```

## Authorship and License

This script was written by Thomas Glanzer in October 2023. Please see the LICENSE file for further details regarding the license.
