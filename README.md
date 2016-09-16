# Try before buy

## Plone evaluation build

* `Source code @ GitHub <https://github.com/a25kk/tbb>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/ade25/tbb>`_


## Installation

This buildout is intended to be used via the development profile to provide
a ready to work on setup. To get started with a new development environment
clone the buildout to your local machine and initialize the buildout:

``` bash
$ git clone git@github.com:username/tbb.git
$ cd ./tbb
$ virtualenv-2.7 .
$ ./bin/pip install zc.buildout
$ bin/buildout -Nc development.cfg
```

## Configuration

The generated buildout asumes that the developer has setup a local egg cache and therefore provides a buildout 'default.cfg' containing:

``` ini
[buildout]
eggs-directory      = /home/yourusername/.buildout/eggs
download-cache      = /home/yourusername/.buildout/downloads
extends-cache       = /home/yourusername/.buildout/extends

socket-timeout      = 3

[fabric]
username            = yourusername
```
