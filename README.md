
# iTunesU credential generator app for mac.

Creates a headless py2app mac app that will create an iTunesU login
once you've edited the variables in genitu.py. When run it will generate a
web page with a time-stamped hash that will automatically open and
attempt to login to the iTunesU site specified in the genitu.py file.

The reason for doing this is that you can distribute this app to people
who are responsible for updating the iTunesU site so they can login without
distributing your entire site's shared secret. 

**NOTE:** Because of the way iTunesU works (authentication via token), this app
is the same as setting up ssh keys, except it's usable anywhere, so it may be advisable to 
not distribute an app that contains your entire site login, but rather sub-section logins only.

Regardless, using this app instead of a webapp with authentication should only be a stopgap until you have a more secure system in place. 

## 
The file declared in setup.py (launch-itu.py) will/must be included
in the app, but other .py files are compiled and source is not
included (that's why launch-itu.py is like that, so you're not
distributing your shared secret).

You will need to know the following information for this to work:

> The iTunesU url for your institution, like: "https://deimos.apple.com/WebObjects/Core.woa/Browse/example.edu"

> Your shared secret, like: "STRINGOFTHIRTYTWOLETTERSORDIGITS"

> The administrator credential, like: "Administrator@urn:mace:itunesu.com:sites:example.edu"

> Your debug suffix, like: "/abc123"


See the [iTunesU Administration Guide](http://deimos.apple.com/rsrc/doc/iTunesUAdministrationGuide/) for more information.

## Configuration

While configuring genitu.py to match your credentials, it is advisable to 

1. uncomment the line that will generate a debug page instead of logging you in:

   site_url = site_url + debugsuffix

1. run genitu.py from the command line so you don't have to keep rebuilding the 

## Building the mac.app 

To build the mac app from this directory:

    python setup.py py2app

### collophon 

This repo is based off of sample code previously distributed by Apple, Inc. at [Apple's iTunes U Support page](http://www.apple.com/support/itunes-u/) which seems to have [mysteriously disappeared](https://discussions.apple.com/thread/3766430?start=0&tstart=0) and further inspired by the article [Fixing Apple’s iTunes U Python Sample Code](http://www.maclearning.org/articles/40/fixing-apple-s-i-tunes-u-python-s)