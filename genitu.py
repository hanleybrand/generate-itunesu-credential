#!/usr/bin/python

# do not distribute this file ; contains sensitive information
# edit the variables in engage() to match your institution and needs

import urllib
import urllib2
import time
import hashlib
import hmac

def engage():

# Define the user information. Replace the credentials with the
# credentials you want to grant to that user, and the optional
# identity information with the identity of the current user.
# For initial testing and site setup, use the singe administrator
# credential defined when your iTunes U site was created. Once
# you have access to your iTunes U site, you will be able to define
# additional credentials and the iTunes U access they provide.

    user_credential = "Administrator@urn:mace:itunesu.com:sites:example.edu"
    credential_array = [user_credential]
    display_name = "Jane Doe"
    email_address = "janedoe@example.edu"
    user_name = "jdoe"
    user_identifier = "42"

    # Define your site's information. Replace these
    # values with ones appropriate for your site.

    site_url = "https://deimos.apple.com/WebObjects/Core.woa/Browse/example.edu"
    debugsuffix = "/abc123"
    shared_secret = "STRINGOFTHIRTYTWOLETTERSORDIGITS"

    # uncomment the line below to access debug information from the
    # iTunes U server.

    # site_url = site_url + debugsuffix

    identity = get_identity_string(display_name, email_address, user_name, user_identifier)
    credentials = get_credentials_string(credential_array)
    # time.time() returns a float, so we cast to an int
    currenttime = int(time.time())
    token = get_authorization_token(identity, credentials, currenttime, shared_secret)

    invoke_action(site_url, token, user_name)


def get_identity_string(displayname, emailaddress, username, useridentifier):
    # Combine user identity information into an appropriately formatted string.
    # take the arguments passed into the function copy them to variables
    return '"%s" <%s> (%s) [%s]' % (displayname, emailaddress, username, useridentifier)

def get_credentials_string(credentialarray):
    # Combine individual credentials into a semicolon delimited string
    credentialString = ""
    i = 0
    while(i < len(credentialarray)):
        if (i == 0):
            credentialString = credentialarray[i]
        else:
            credentialString =   "%s;%s" %  (credentialString,credentialarray[i])
        i += 1
    return credentialString


def get_authorization_token(identity, credentials, currenttime, sharedsecret):
    # create the token that contains the necessary elements to authorize the user
    # signature = "";
    # buffer = ""

    dict = {"credentials" : credentials,
            "identity" : identity,
            "time" : currenttime
    }

    encoded_parms = urllib.urlencode(dict)

    h = hmac.new(sharedsecret, encoded_parms, hashlib.sha256)

    dict['signature'] = h.hexdigest()
    return urllib.urlencode(dict)

def invoke_action(siteurl, token, username):
    # create the request and pass it to the iTunes U server.
    req = urllib2.Request(siteurl, token)
    req.add_data(token)
    handle = urllib2.urlopen(req)
    the_page = handle.read()
    filename = 'openITU-' + username + '.html'
    f = open( filename , 'w' )

    f.write("Content-type: text/html\n\n")
    f.write(the_page)

    f.close()
    #print "Content-type: text/html\n\n"
    #print the_page

