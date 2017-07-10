# Restrictions PASScode Recovery

This program is licensed under the MIT License.

## How this Works

In your iTunes Backup, there is a file that holds the hashed Restrictions passcode, with the salt. The maker of http://ios7hash.derson.us created a web utility based on an original Perl script (see their website) that can take the key and salt and try all of the passcodes to recover your passcode for the Restrictions settings on iOS.

## Install

```
git clone https://github.com/juniorRubyist/rpassr.git
```

Run `rpassr.py` with `python3`

## How to Recover the Passcode

1. Backup your iPhone (or iOS device) in iTunes __without encryption__. This utility will not decrypt the backup, nor will it get a device passcode.

2. Navigate to the iTunes Backup. On Windows, they are stored in `%APPDATA%\Apple Computer\MobileSync\Backups`. On Mac, they are stored in `~/Library/Application Support/MobileSync/Backup`.

3. Determine which backup is the correct one (using the dates).

4. Navigate into the `39` folder. Open `398bc9c2aeeab4cb0c12ada0f52eea12cf14f40b` with a __text/code editor__.

5. Open a terminal and execute the script with `python3 rpassr.py`.

6. If you want verbose output, input `v`, or else input `r` and press <kbd>Enter</kbd>. If you want to test certain passcodes only, input `a` and press <kbd>Enter</kbd> (you will be asked for the range).

7. Find `RestrictionsPasswordKey`. Copy/paste the value in between `<data>` and `</data>` into the terminal and press <kbd>Enter</kbd>.

8. Find `RestrictionsPasswordSalt`. Copy/paste the value in between `<data>` and `</data>` into the terminal and press <kbd>Enter</kbd>.

9. The passcode will be found in less than a minute, depending on processor speed. You will see output if you chose verbose (`v`).

10. If the search was sucessful, it will stop and give you the passcode. If it failed, check the key and salt, then retry. If a retry doesn't work, try backing up again.

## Common Errors

> __Note:__ I will ignore/close all issues for these.

```python
binascii.Error: Incorrect padding
```
This indicates that the inputted key or salt was an incorect format. Check your entry.

__Any "This is for Unix Only" Error__

Windows users may get an error that says something about Unix. This will not be helped; I only have a Mac. Please file a PR if you have a solution.

## Credits

- http://ios7hash.derson.us
