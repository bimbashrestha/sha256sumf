# sha256sumf

A simple command line utility for producing recursive SHA 256 checksums of folders using:

* Inner file contents
* Inner file paths 
* Inner folder paths

Produces the same output as sha256sum when used with a single file.

# Installation and Usage

```
$ pip install sha256sumf
$ sha256sumf folder
92f49e486823dbfbb514097761f8dbeebb997f6a5552180e057e454964224b15  folder
```