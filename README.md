# deluge-cmd


[![pypi](https://img.shields.io/pypi/v/deluge-cmd.svg)](https://pypi.org/project/deluge-cmd/)
[![python](https://img.shields.io/pypi/pyversions/deluge-cmd.svg)](https://pypi.org/project/deluge-cmd/)
[![Build Status](https://github.com/mupaduw/deluge-cmd/actions/workflows/dev.yml/badge.svg)](https://github.com/mupaduw/deluge-cmd/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/mupaduw/deluge-cmd/branch/main/graphs/badge.svg)](https://codecov.io/github/mupaduw/deluge-cmd)


Some cli tools to manage Synthstrom Deluge SD card contents.

* Documentation: <https://mupaduw.github.io/deluge-cmd>
* GitHub: <https://github.com/mupaduw/deluge-cmd>
* PyPI: <https://pypi.org/project/deluge-cmd/>
* Free software: MIT


## Features

- verify Deluge Filesytem structure
- list songs 
- list song attributes bpm, key, samples
- list samples (used/unused)

### Planned features
- move songs, samples 
- delete songs, samples
- posix-like glob filtering for list, move & delete
- list instruments and types
- anything helpful for backward/forward migration of deluge SD cards having fw3.15 and 4.0 content.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
