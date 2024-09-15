from setuptools import setup
import pathlib

from phulize.version.progsettings import get_version

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

version = get_version()

setup(
    name="phulize",
    version=version,
    description="A python CLI tool to resize images while conserving folder hierarchy and preserving original ones in a different folder.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaytiri/photos-bulk-resize",
    project_urls={
        'GitHub': 'https://github.com/zaytiri/photos-bulk-resize',
        'Changelog': 'https://github.com/zaytiri/photos-bulk-resize/blob/main/CHANGELOG.md',
    },
    author="zaytiri",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    keywords="photos, image, processing, resize, reduce, cli, folder, hierarchy, bulk",
    package_data={'phulize': ['version/progsettings.yaml']},
    packages=["phulize", "phulize.settings", "phulize.version", "phulize.utils"],
    python_requires=">=3.10.6",
    install_requires=[
        "setuptools>=65.5.1",
        "margument~=1.1.4",
        "Pillow~=10.2.0",
        "PySimpleGUI~=4.60.5",
        "piexif~=1.1.3",
        "pyyaml~=6.0"
    ],
    setup_requires=[
        "setuptools>=65.5.1",
        "pyyaml~=6.0"
    ],
    entry_points={
        "console_scripts": [
            "phulize=phulize:app.main",
        ],
    }
)
