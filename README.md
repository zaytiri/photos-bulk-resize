[![Downloads](https://pepy.tech/badge/phulize)](https://pepy.tech/project/phulize)

# Photo Resizer

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [License](#license)
- [Status](#status)

<a name="description"></a>

## Description

Photo Resizer is a CLI (command-line interface) tool which takes a folder full of photos and resizes each photo
recursively depending on the extensions chosen. It does this while conserving folder hierarchy without having to
organize each photo again.

All photos are checked if they are valid or corrupted before the resizing as well as after, to make sure any photos are
resized correctly.

A filter is also available for searching for photos, meaning it's possible to only resize photos which the size is
higher or below the specified. More details below.

All original photos are copied to a different folder which can be configured, also cloning the existent folder
hierarchy. If any image fails to resize, this photo will remain in the original folder.

At the start, a safety question is displayed to make sure the path inserted is the correct one as it will be permanently
modified. This safety question can be disabled.

An option to shut down the device is also available as it can be useful to leave the process running for a long time
without worrying.

When all is finished, an output file will be created with statistics and relevant information, such as:

- list of images resized;
- display original size and resized size of each image;
- display all photos' original size and resized size;
- display how much size was resized between all photos;
- total number of photos resized, increased, unsuccessful and found;
- warning if the photo size increased instead of decreased;

### Output file example

```txt
    ... (hidden)

[2023-04-05 17:44:13.979793]
The following photo was resized: C:\Users\<username>\Desktop\example\1subfolder\anothersubfolder\1680170906941
	-The original photo size was: 1.98 MB
	-The resized photo size is: 2.04 MB
        [WARNING] Size increased!

[2023-04-05 17:44:14.209180]
The following photo was resized: C:\Users\<username>\Desktop\example\1subfolder\anothersubfolder\1680170908790
	-The original photo size was: 699.66 KB
	-The resized photo size is: 258.03 KB


[2023-04-05 17:44:14.211177]
Final Statistics:
	Size of all original photos: 9.29 MB
	Size of all resized photos: 4.67 MB
	Space in disk saved: 4.63 MB

	- Total number of photos with reduced size: 6
	- Total number of photos with increased size: 1
	- Total number of photos unsuccessfully reduced: 0
	- Total number of photos found: 7
```

### Folder example

The original folder full of images to be resized:<br>
![1](https://github.com/zaytiri/photos-bulk-resize/blob/main/readme_imgs/1.png)

Content of original folder before resize with pictures' original size:<br>
![5](https://github.com/zaytiri/photos-bulk-resize/blob/main/readme_imgs/5.png)

Both the original folder and the folder created after all is finished, which contains all original images:<br>
![2](https://github.com/zaytiri/photos-bulk-resize/blob/main/readme_imgs/2.png)

Display of both folders containing exactly the same hierarchy:<br>
![3](https://github.com/zaytiri/photos-bulk-resize/blob/main/readme_imgs/3.png)

Content of original folder after resize with pictures' reduced size at 55% quality and the output file:<br>
![4](https://github.com/zaytiri/photos-bulk-resize/blob/main/readme_imgs/4.png)

<a name="features"></a>

## Features

| Feature                                                                              |
|:-------------------------------------------------------------------------------------|
| resize photos in bulk conserving folder hierarchy                                    |
| resize photos depending on specific extension                                        |
| resize photos recursively  within folders                                            |
| checking of invalid or corrupted photos                                              |
| filter photos to resize depending on their size                                      |
| all original photos are preserved in another folder in case of something going wrong |
| creation of a final output file containing relevant information about the process    |
| existence of a safety question                                                       |
| option of shutting down the device when the resizing process is finished             |
| configurations provided will be save for easier usage of the command                 |

Any new features are **_very_** welcomed.

### Future features

Nothing at the moment.

<a name="prerequisites"></a>

## Prerequisites

[Python 3](https://www.python.org/downloads/) must be installed.

<a name="installation"></a>

## Installation

```bash
pip --no-cache-dir install phulize
```

or,

```bash
pip3 --no-cache-dir install phulize
```

## Usage

| Command (shortcut) | Command (full)                         | Required                             | Default value | Description                                                                                                                                      |
|:-------------------|----------------------------------------|--------------------------------------|---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| -r                 | --run                                  | ***REQUIRED*** to start the resizing | ---           | If specified, the resizing will start running using user-defined configurations.                                                                 |
| -p                 | --path                                 | ***REQUIRED*** to resize photos      | empty         | Absolute path of the folder containing images to be resized.                                                                                     |
| -e                 | --extensions                           | ***REQUIRED*** to resize photos      | empty         | Insert the extensions of all the images that should be resized.                                                                                  |
| -q                 | --quality                              | ***OPTIONAL***                       | 55            | The desired quality of the image. An original image has 100% quality, meaning that anything below this value will reduce the size of the images. |
| -f                 | --folder                               | ***OPTIONAL***                       | _ORIGINAL     | The name or path of the folder which will contain all original photos resized.                                                                   |
| -hi                | --higher                               | ***OPTIONAL***                       | 0             | The size in ***Bytes*** of any image that should be resized. Any images' size higher than this value will be resized.                            |
| -b                 | --below                                | ***OPTIONAL***                       | 0             | The size in ***Bytes*** of any image that should be resized. Any images' size below this value will be resized.                                  |
| ---                | --safety-question/--no-safety-question | ***OPTIONAL***                       | True          | Enable or disable the safety question                                                                                                            |
| ---                | --shutdown/--no-shutdown               | ***OPTIONAL***                       | False         | Enable or disable the shutting down device when process is finished.                                                                             |

<a name="before"></a>

### Before
- If possible, **make a backup of the folder to be resized**, in case anything goes wrong. This will ensure no data is lost.
- It's recommended that a trial is made first (with dummy images), to check the best quality to use.

<a name="after"></a>

### After
- **Make sure to check the output file for any unexpected outcomes**, regarding if it resized correctly, as expected, or not.
- **Make sure to check the images resized**, to make sure there is no loss. The program itself checks if an image is or becomes corrupted after resizing, but make sure 

<a name="important"></a>

---
### Important 
- The quality of the image to be resized, by default, is 50%, meaning all images to resize will have, approximately, 50% less quality than the original image. This can be change, adding the '--quality' argument with a number between 0 and 100.
---

Any additional help can be provided if the following command is run:
```bash
phulize --help
```

or,
```bash
phulize -h
```
Running the previous command is also useful to make sure the package was downloaded correctly.

Example of an initial command, could be:
```bash
phulize -p "C:\Users\<username>\Desktop\example" -q 60 -e jpg png
```
This will configure the path of the folder containing images to resize, the quality those images should have and the extensions to search for and resize.

Any configuration can also be individually inserted:
```bash
phulize -q 50
```
```bash
phulize -f "CONVERTED" 
```

The following command corresponds to only resizing images that have a size higher than 1MB:
```bash
phulize -hi 1048576
```
The opposite is also true (resizing images that have a size lower than 1MB):
```bash
phulize -b 1048576
```
To disable the previous filters ('--hi' or '--b'), one can simply set them to 0 (zero):
```bash
phulize -b 0
```

The previous configuration can be seen in a file, with the content just like the following:
```txt
below: 0
extensions:
- .jpg
- .png
folder: CONVERTED
higher: 1048576
path: C:\Users\<username>\Desktop\example
quality: 50
```


Usage of boolean arguments:
```bash
phulize --safety-question
phulize --no-safety-question
```
```bash
phulize --shutdown
phulize --no-shutdown
```

To run the resizing after all configurations are done:
```
phulize --run
```

<a name="support"></a>

## Support

If any problems occurs, feel free to open an issue.

<a name="license"></a>

## License

[MIT](https://choosealicense.com/licenses/mit/)

<a name="status"></a>

## Status

Currently maintaining it.