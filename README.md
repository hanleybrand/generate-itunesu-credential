
## iTunesU credential generator app for mac.

This creates an mac app that will create an iTunesU login
once you've edited the variables in genitu.py

The file declared below (launch-itu.py) will/must be included
in the app, but other .py files are compiled and source is not
included (that's why launch-itu.py is like that, so you're not
distributing your shared secret).

You will need to know the following information for this to work:

> The iTunesU url for your institution, like: "https://deimos.apple.com/WebObjects/Core.woa/Browse/example.edu"

> Your shared secret, like: "STRINGOFTHIRTYTWOLETTERSORDIGITS"

> The administrator credential, like: "Administrator@urn:mace:itunesu.com:sites:example.edu"

> Your debug suffix, like: "/abc123"

See the [iTunesU Administration Guide](http://deimos.apple.com/rsrc/doc/iTunesUAdministrationGuide/) for more information.

To build the mac app from this directory:

    python setup.py py2app

### collophon 

This repo is based off of sample code previously distributed by Apple, Inc. at [Apple's iTunes U Support page](http://www.apple.com/support/itunes-u/) which seems to have [mysteriously disappeared](https://discussions.apple.com/thread/3766430?start=0&tstart=0) and further inspired by the article [Fixing Apple’s iTunes U Python Sample Code](http://www.maclearning.org/articles/40/fixing-apple-s-i-tunes-u-python-s)