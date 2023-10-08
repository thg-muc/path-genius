"""Test cases for the application."""

# * Author(s): Thomas Glanzer
# * Creation : Oct 2023
# * License  : MIT

# %% ----------------------------------
# * Import libraries

import pytest

from path_genius_app import (check_string, mac_to_windows_path,
                             windows_to_mac_path)

# %% ----------------------------------
# * Define test cases


@pytest.mark.parametrize("possible_link, expected_link_type", [
    # Test case for smb:// links
    (r"smb://example.corp/_path/folder/etc", -1),

    # Test case with leading whitespaces
    (r"  smb://example.corp/_path/folder/etc", -1),

    # Test case with trailing slash
    (r"smb://example.corp/_path/folder/etc/", -1),

    # Test case without smb://
    (r"//example.corp/_path/folder/etc", -1),

    # Test case with a file
    (r"smb://example.corp/_path/folder/etc/file.txt", -1),

    # Test case for file:// links
    (r"file:\\example.corp\_path\folder\etc", 1),

    # Test case with leading whitespace
    (r" file:\\example.corp\_path\folder\etc", 1),

    # Test case with trailing slash
    (r"file:\\example.corp\_path\folder\etc" + "\\", 1),

    # Test case without file://
    (r"\\example.corp\_path\folder\etc", 1),

    # Test case with a file
    (r"file:\\example.corp\_path\folder\etc\file.txt", 1),

    # Normal web link
    (r"https://example.com", 0),

    # Normal string
    (r"normal string", 0),

    # Empty string
    ("", 0),

    # String with both forward and backslashes
    (r"normal string/with/forward\and\backslashes", 0),

])
def test_check_string(possible_link, expected_link_type):
    """Test the identify_string function."""
    link_type, _ = check_string(possible_link)
    assert link_type == expected_link_type


@pytest.mark.parametrize("mac_path, expected_windows_path", [
    # Test case for smb:// links
    (r"smb://example.corp/_path/folder/etc",
     r"file:\\example.corp\_path\folder\etc"),

    # Test case with trailing backslash
    (r"smb://example.corp/_path/folder/etc/",
     r"file:\\example.corp\_path\folder\etc" + "\\"),

    # Test case with a file
    (r"smb://example.corp/_path/folder/etc/file.txt",
     r"file:\\example.corp\_path\folder\etc\file.txt"),

    # Test case with leading whitespace
    (r" smb://example.corp/_path/folder/etc",
     r"file:\\example.corp\_path\folder\etc"),

    # Test case with leading and trailing whitespaces
    (r"   smb://example.corp/_path/folder/etc     ",
     r"file:\\example.corp\_path\folder\etc"),

    # Test case without smb://
    (r"//example.corp/_path/folder/etc",
        r"file:\\example.corp\_path\folder\etc"),

    # Normal string with whitespace
    (r" normal string ", r" normal string "),


])
def test_mac_to_windows_path(mac_path, expected_windows_path):
    """Test the mac_to_windows_path function."""
    # Get a clean string
    _, cleaned_link = check_string(mac_path)
    windows_path = mac_to_windows_path(cleaned_link)
    assert windows_path == expected_windows_path


@pytest.mark.parametrize("windows_path, expected_mac_path", [
    # Test case for file:// links
    (r"file:\\example.corp\_path\folder\etc",
     r"smb://example.corp/_path/folder/etc"),

    # Test case with trailing backslash
    (r"file:\\example.corp\_path\folder\etc" + "\\",
     r"smb://example.corp/_path/folder/etc/"),

    # Test case with a file
    (r"file:\\example.corp\_path\folder\etc\file.txt",
     r"smb://example.corp/_path/folder/etc/file.txt"),

    # Test case with leading whitespace
    (r" file:\\example.corp\_path\folder\etc",
     r"smb://example.corp/_path/folder/etc"),

    # Test case with leading and trailing whitespaces
    (r"   file:\\example.corp\_path\folder\etc     ",
     r"smb://example.corp/_path/folder/etc"),

    # Test case without file://
    (r"\\example.corp\_path\folder\etc",
        r"smb://example.corp/_path/folder/etc"),

    # Normal string with whitespace
    (r" normal string ", r" normal string "),

    # Test case with file:// and forward slashes
    (r"file://example.corp/_path/folder/etc",
        r"smb://example.corp/_path/folder/etc"),

    # Test case with file:// and forward slashes and trailing slash
    (r"file://example.corp/_path/folder/etc/",
        r"smb://example.corp/_path/folder/etc/"),

])
def test_windows_to_mac_path(windows_path, expected_mac_path):
    """Test the windows_to_mac_path function."""
    # Get a clean string
    _, cleaned_link = check_string(windows_path)
    mac_path = windows_to_mac_path(cleaned_link)
    assert mac_path == expected_mac_path
