from setuptools import setup
import pathlib

from version.progsettings import get_version

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

version = get_version()

setup(
    name="python-template",
    version=version,
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaytiri/python-template",
    project_urls={
        'GitHub': 'https://github.com/zaytiri/python-template',
        'Changelog': 'https://github.com/zaytiri/python-template/blob/main/CHANGELOG.md',
    },
    author="zaytiri",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    keywords="keywords, separated, by, commas",
    package_data={'python-template': ['progsettings.yaml']},
    packages=["python-template", "python-template.subfolder1", "python-template.subfolder2"],
    python_requires=">=3.10.6",
    install_requires=[
      "PyYAML~=6.0",
    ],
    entry_points={
        "console_scripts": [
            "python-template=python-template:app.main",
        ],
    }
)