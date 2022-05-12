
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [0.3.1] - 2022-05-12
## Added
 - fix for import error #7
 - some basic test cover

### Added
## [0.3.0] - 2022-05-12
### Added
- new **highly experimental** `dmv` command 

### Changed
- reordered `dls` args for easier auto-fill and compatability with new `dmv` and `ls`
- `-p` is now the `pattern` argument (non-optional)
- updated usage docs
- requires deluge-card 0.4.2

## [0.2.0] - 2022-05-04
### Changed
- command name changed to `dls` for *deluge ls*.
- removed cli script install.
- depends on deluge-card >= 0.3.0.
- `sdu ~/SD01 -ls` replaced by `dls ~/SD01 s` or `songs`
- `sdu ~/SD01 -la` replaced by `dls ~/SD01 a` or `samples`
- `sdu ~/SD01 -lS` replaced by `dls ~/SD01 ss` or `song_samples`
- updated README.

### Added
- `-p`, `--pattern` option for globby path filtering. eg `dls ~/SD01 song_samples -p **/kick*`
- `-D`, `--debug` option for debugging output.
- added TLDR style usage docs.

## [0.1.4] - 2022-05-02
### Fixed
- Script entry point `dsd`.

## [0.1.3] - 2022-05-02

## [0.1.2] - 2022-05-02
### Changed
- Removed dev-requirements from the published package.
- Depends on deluge-card >= 0.2.3.
- Improved the Pypi classifiers.

### Added
- New script entry point `dsd`.

## [0.1.1] - 2022-05-01
 - First release on PyPI.
### Added

 - basic list features in sdu.py module

## [0.1.0] - 2022-04-30

