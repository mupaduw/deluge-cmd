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

This project uses [deluge-card](https://github.com/mupaduw/deluge-card) which provides a python API for the Deluge Folder System.

## Features

- list Songs Samples, and Song Samples on a Deluge Folder System (DFS).
- check Deluge Folder Systems.
- list useful attributes tempo, key, scale.
- filter on path patterns: e.g. list all "Kick" samples).

e.g.

```
>$ dls ~/Music/DELUGE/01 songs -p *001*
Deluge filesystem at /homie/Music/DELUGE/01 mounted: False
  DelugeSong(/homie/Music/DELUGE/01/SONGS/SONG001.XML) key C major tempo 96.0
  DelugeSong(/homie/Music/DELUGE/01/SONGS/SONG001A.XML) key C major tempo 96.0
  DelugeSong(/homie/Music/DELUGE/01/SONGS/SONG001B.XML) key C major tempo 108.0
  DelugeSong(/homie/Music/DELUGE/01/SONGS/SONG001C.XML) key C major tempo 108.0
  DelugeSong(/homie/Music/DELUGE/01/SONGS/SONG001D.XML) key C major tempo 96.0
```

### Planned features
- (d)cp, (d)mv and (d)rm commands.
- song groups (1, 1A, 1B, 1C).
- instruments, kits & synths.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
