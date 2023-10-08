"""Simple script to convert links from Mac to Windows and vice versa (CMD)."""

# * Author(s): Thomas Glanzer
# * Creation : Oct 2023
# * License  : MIT

# %% ----------------------------------
# * Import libraries

import pyperclip

# %% ----------------------------------
# * Define functions

APP_TITLE = "Path-Genius"


def check_string(possible_link: str) -> tuple[int, str]:
    """Check if a string is a Windows link, a Mac link, or no link at all.

    This is done by checking the string for certain prefixes that are
    indicative of a link. (e.g. "file" or "smb").

    Parameters
    ----------
    possible_link : str
        The string to check for a link.

    Returns
    -------
    int
        1 if the string is a Windows link, -1 if it is a Mac link,
        and 0 if it is not a link (but a normal string)
    str
        returns the input string with trailing and leading whitespace removed

    """
    # Remove trailing and leading whitespace from the string
    cleaned_link = possible_link.strip()

    # If there are both forward and backslashes, it is not a link
    if r"/" in cleaned_link and r"\\" in cleaned_link:
        return 0, possible_link
    # Detect the link type
    if cleaned_link.startswith(r"file:") or cleaned_link.startswith(r"\\"):
        return 1, cleaned_link
    if cleaned_link.startswith(r"smb:") or cleaned_link.startswith(r"//"):
        return -1, cleaned_link

    # Return 0 if no link is detected (and keep the original string)
    return 0, possible_link


def mac_to_windows_path(mac_path: str) -> str:
    """Convert a Mac path to a Windows path.

    This is done by replacing all forward slashes with backslashes and
    by converting "smb" to "file".

    Parameters
    ----------
    mac_path : str
        The Mac path to be converted.

    Returns
    -------
    str
        The converted Windows path.

    """
    # Convert smb:// to file:\\
    mac_path = mac_path.replace(r"smb://", r"file:\\")
    mac_path = mac_path.replace(r"//", r"file:\\")
    # Split the path into components
    components = mac_path.split('/')
    # Combine the components with the Windows path separator
    windows_path = '\\'.join(components)

    return windows_path


def windows_to_mac_path(windows_path: str) -> str:
    """Convert a Windows path to a Mac path.

    This is done by replacing all backslashes with forward slashes and
    by converting "file" to "smb".

    Parameters
    ----------
    windows_path : str
        The Windows path to be converted.

    Returns
    -------
    str
        The converted Mac path.

    """
    # Convert all forward slashes to backslashes
    windows_path = windows_path.replace('/', '\\')
    # Convert file:// to smb://
    windows_path = windows_path.replace(r"file:\\", r"smb://")
    windows_path = windows_path.replace(r"\\", r"smb://")
    # Split the path into components
    components = windows_path.split('\\')
    # Combine the components with the Mac path separator
    mac_path = '/'.join(components)

    return mac_path


def display_notification(title: str, message: str) -> None:
    """Display a notification with the specified title and message.

    Uses NSUserNotification from the `Foundation` framework to display
    notifications on Mac. If the classes are not available (e.g., command-line
    or on non-Mac OS systems), the function will silently fail and do nothing.

    Parameters
    ----------
    title : str
        The title of the notification.
    message : str
        The message to display in the notification.

    Returns
    -------
    None

    """
    try:
        # pylint: disable=import-outside-toplevel
        from Foundation import NSUserNotification, NSUserNotificationCenter

        # Try to display a notification
        notification = NSUserNotification.alloc().init()
        notification.setTitle_(title)
        notification.setInformativeText_(message)
        NSUserNotificationCenter.defaultUserNotificationCenter(
        ).scheduleNotification_(notification)
    except AttributeError:
        # If the notification classes are not available, fail silently
        pass


def convert_clipboard() -> None:
    """Convert any clipboard links between Mac <-> Windows.

    This function first checks the contents of the clipboard to see if it
    contains a Windows or Mac path. If this is the case, it converts the path
    to the other and copies the converted path to the clipboard format while
    printing the path to the command-line (and displaying a notification).

    """
    # Get the contents of the clipboard
    clipboard_contents = pyperclip.paste()
    # Check if the clipboard contains a link
    link_type, possible_link = check_string(clipboard_contents)

    if link_type == 1:
        # Convert Windows link to Mac link
        converted_link = windows_to_mac_path(possible_link)
        # Store the converted link in the clipboard
        pyperclip.copy(converted_link)

        # Set the feedback message
        feedback_msg = f"Converted Windows to Mac Path: \n{converted_link}"
        # Print the converted link to the command line
        print(feedback_msg)
        # Try to display a notification
        display_notification(APP_TITLE, feedback_msg)

    elif link_type == -1:
        # Convert Mac link to Windows link
        converted_link = mac_to_windows_path(possible_link)
        # Store the converted link in the clipboard
        pyperclip.copy(converted_link)

        # Set the feedback message
        feedback_msg = f"Converted Mac to Windows Path: \n{converted_link}"
        # Print the converted link to the command line
        print(feedback_msg)
        # Try to display a notification
        display_notification(APP_TITLE, feedback_msg)

    else:
        # Set the feedback message
        feedback_msg = "No link detected!"
        # Print the converted link to the command line
        print(feedback_msg)
        # Try to display a notification
        display_notification(APP_TITLE, feedback_msg)


# On script execution, read the clipboard and convert any links
if __name__ == "__main__":

    convert_clipboard()
