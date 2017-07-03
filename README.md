ttr-invasion-timer-python
===========
An invasion timer app for ToonTown Rewritten made in python.

## Dependencies
 - Gtk3
 - Python3

## Running
 #### Linux
 - Clone the repository
 - Run `ttrinvtimer.py`

 #### Windows
 - [Download](https://github.com/raku-cat/ttr-invasion-timer-python/releases/download/0.1/ttrinvtimer.exe) the precompiled executable
 - Run the executable

## Compilation (to run on windows)
 #### Linux
 1. Clone the repository
 2. Edit the `ttrinvtimer.spec` file and set `pathex=['']` to the wine formatted path where you cloned the repository.
 3. Using an (ideally fresh) 32-bit wine prefix, install python and all the scripts dependencies
 4. In wine, with [PyInstaller](https://pypi.python.org/pypi/PyInstaller/) installed, run `pyinstaller -F ttrinvtimer.spec`
 
 #### Windows
 1. Clone the repository
 2. Edit the `ttrinvtimer.spec` file and set `pathex=['']` to the path where you cloned the repository.
 3. Install the dependencies for the script
 4. With [PyInstaller](https://pypi.python.org/pypi/PyInstaller/) installed, run `pyinstaller -F ttrinvtimer.spec`


 *The exe should be in `$PATH_OF_REPO/dist/ttrinvtimer.exe`*
 