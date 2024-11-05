# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).


## [Unreleased]


### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security


## [0.3.7] - 2024-11-05

### Added

- Add Python 3.13 to classifiers list


## [0.3.6] - 2024-11-04

### Removed

- Drop Python 3.5 support

### Fixed

- Fix false positive with class attribute string value and docstring



## [0.3.5] - 2023-10-22

### Added

- Add Python 3.12 support

### Removed

- Drop support for Python 3.3 & 3.4

### Fixed

- Fix check for f-strings on Python 3.12
  - Prior to this version, this plugin cannot find implicit concats
    when using Python 3.12 and f-strings are involved


## [0.3.4] - 2022-10-31

### Added

- Add Python 3.11 to classifier list


## [0.3.3] - 2021-12-15

### Fixed

- Remove more-itertools version constraint
  - Because more-itertools 8.11.0 has been yanked


## [0.3.2] - 2021-11-16

### Fixed

- Fix error code for bytes literals prefixed with 'rb'


## [0.3.1] - 2021-10-15

### Added

- Add Python 3.3 and 3.4 support


## [0.3.0] - 2021-10-11

### Changed

- Separate error codes for bytes literal concatenations


## [0.2.1] - 2021-10-07

### Added

- Add Python 3.10 support


## [0.2.0] - 2021-10-01

### changed

- Remove attrs from dependency list
- Separate error code for concat over multiple lines


## [0.1.5] - 2021-09-20

### Added

- Add Python 3.9 support


## [0.1.4] - 2020-08-19

### Added

- Update documents

### changed

- Changed package structure


## [0.1.3] - 2020-05-25

### Added

- Update documents and metadata

## [0.1.2] - 2020-05-21

### Fixed

- Fix License in setup.cfg


## [0.1.1] - 2020-05-20

### Added

- Update README

### Fixed

- Fix License classifier


## [0.1.0] - 2020-05-18

### Added

- Update README


## 0.0.1 - 2020-05-17

- First release


[unreleased]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.3.7...HEAD
[0.3.7]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.3.6...v0.3.7
[0.3.6]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.3.5...v0.3.6
[0.3.5]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.3.4...v0.3.5
[0.3.4]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.3.3...v0.3.4
[0.3.3]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.3.2...v0.3.3
[0.3.2]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.1.5...v0.2.0
[0.1.5]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/10sr/flake8-no-implicit-concat/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/10sr/flake8-no-implicit-concat/releases/tag/v0.1.0
