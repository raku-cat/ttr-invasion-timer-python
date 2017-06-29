ttr-invasion-timer-python
===========
An invasion timer app for ToonTown Rewritten made in python.

## Dependencies
 - Gtk3
 - Zenity
 - Python3

## Running
 __Linux__
 - Clone the repository
 - Run `ttrinvtimer.py`

 __Windows__
 - [Download](https://github.com/raku-cat/ttr-invasion-timer-python/releases/download/0.1/ttrinvtimer.exe) the precompiled executable
 - Install [zenity-windows](https://github.com/kvaps/zenity-windows/releases/download/v3.20.0-1/zenity-3.20.0_win32-1.exe)
 - Run the executable

## Compilation (for windows)
 __Linux__
 1. Clone the repository
 2. Edit the `ttrinvtimer.spec` file and set `pathex=['']` to the wine formatted path where you cloned the repository.
 3. In wine, with [PyInstaller](https://pypi.python.org/pypi/PyInstaller/) installed, run `pyinstaller -F ttrinvtimer.spec`
 The exe should be in `$PATH_OF_REPO/dist/ttrinvtimer.exe`

 __Windows__
 - None yet