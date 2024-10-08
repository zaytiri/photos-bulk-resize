# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### Status
- Added
- Changed
- Fixed
- Removed

## [1.1.2] - 2024-09-15

### Removed
- unnecessary prints.

## [1.1.1] - 2024-09-15

### Fixed
- github action workflow on publishing package to PyPi.

## [1.1.0] - 2024-09-15

### Added
- feature to use the image's name as the original date created of the file. The image's name must have the format of "IMG_<yyyymmdd>_<hhmmss>" to be recognized as the date created of the file.

## [1.0.5] - 2024-01-25

### Fixed
- program's version and deployment.

## [1.0.4] - 2024-01-25

### Fixed
- vulnerability due to external library: Pillow. Update Pillow's version to 10.0.2.

## [1.0.3] - 2023-09-23

### Added
- GUI version.

### Fixed
- some issues and adaptions for the program to be used by the GUI as well.

## [1.0.2] - 2023-04-07

### Fixed
- fixed issue where it would give an error when trying to print '%'. It was not escaped correctly.

## [1.0.1] - 2023-04-07

### Fixed
- version's file not being found because of bad configurations on setup.py.

## [1.0.0] - 2023-04-06

### Added
- first release on PyPI