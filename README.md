ttr-invasion-timer-python
===========
An invasion timer app for ToonTown Rewritten made in python.

## Dependencies
 - Gtk3
 - Zenity
 - Python3

## Installation
 __Linux__
 - Clone the repository and run `ttrinvtimer.py`
 __Windows__
 (add later)

## Compilation (for windows)
 __Linux__
 1. Clone the repository
 2. Edit the `ttrinvtimer.spec` file and set `pathex=['']` to the wine formatted path where you cloned the repository.
 3. In wine, with [PyInstaller](https://pypi.python.org/pypi/PyInstaller/) installed, run `pyinstaller -F ttrinvtimer.spec`
 The exe should be in `$PATH_OF_REPO/dist/ttrinvtimer.exe`
 __Windows__
 