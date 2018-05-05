#!/usr/bin/python 
# -*- coding: utf-8 -*-
#
# Before running this sample, you must fill in your Evernote developer token.
#

import random
import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.limits.constants as LimitConstants
import evernote.edam.type.ttypes as Types
#import evernote.edam.notestore.NoteStore as NoteStore

from evernote.api.client import NoteStore
from evernote.api.client import EvernoteClient
from enml import PlainTextOfENML, HTMLOfENML
# Real applications authenticate with Evernote using OAuth, but for the
# purpose of exploring the API, you can get a developer token that allows
# you to access your own Evernote account. To get a developer token, visit
# https://SERVICE_HOST/api/DeveloperToken.action
#
# There are three Evernote services:
#
# Sandbox: https://sandbox.evernote.com/
# Production (International): https://www.evernote.com/
# Production (China): https://app.yinxiang.com/
#
# For more information about Sandbox and Evernote China services, please 
# refer to https://dev.evernote.com/doc/articles/testing.php 
# and https://dev.evernote.com/doc/articles/bootstrap.php

#auth_token = ""

#if auth_token == "your developer token":
#    print "Please fill in your developer token"
#    print "To get a developer token, visit " \
#        "https://sandbox.evernote.com/api/DeveloperToken.action"
#    exit(1)


# To access Sandbox service, set sandbox to True 
# To access production (International) service, set both sandbox and china to False
# To access production (China) service, set sandbox to False and china to True
#sandbox = True
#china = False

# Initial development is performed on our sandbox server. To use the production
# service, change sandbox=False and replace your
# developer token above with a token from
# https://www.evernote.com/api/DeveloperToken.action
##client = EvernoteClient(token=auth_token, sandbox=sandbox, china=china)

#user_store = client.get_user_store()

#version_ok = user_store.checkVersion(
#    "Evernote EDAMTest (Python)",
#    UserStoreConstants.EDAM_VERSION_MAJOR,
#    UserStoreConstants.EDAM_VERSION_MINOR
#)
#print "Is my Evernote API version up to date? ", str(version_ok)
#print ""
#if not version_ok:
#    exit(1)
# ==============================================================
## OAuth
#client = EvernoteClient(
#    consumer_key='',
#    consumer_secret='',
#    sandbox=True # Default: True
#)
#request_token = client.get_request_token('https://127.0.0.1:8000')
#client.get_authorize_url(request_token)
 
#To obtain the access token
#request_token['aouth_verifier'] = "547E7EFCEBC38A4D966E72CB2AAE0D01&sandbox_lnb=false"
#access_token = client.get_access_token(
#    request_token['oauth_token'],
#    request_token['oauth_token_secret'],
#    request.GET.get('oauth_verifier', '')
#    ['oauth_verifier', '547E7EFCEBC38A4D966E72CB2AAE0D01&sandbox_lnb=false']
#)

#client = EvernoteClient(token=access_token)
#note_store = client.get_note_store()
#notebooks = note_store.listNotebooks()
#===================================================================
#===================================================================

# fill the token here
auth_token = ""
client = EvernoteClient(token=auth_token)
note_store = client.get_note_store()
notebooks = note_store.listNotebooks()
#print "Found ", len(notebooks), " notebooks:"
#for notebook in notebooks:
#    print "  * ", notebook.name

# fill the notebook_name
notebook_name = "專案 1"
notebook_guid = ""
for notebook in notebooks:
    if notebook.name == notebook_name:
        notebook_guid = notebook.guid
filter = NoteStore.NoteFilter()
filter.notebookGuid = notebook_guid
spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True
spec.includeContentLength = True
note_infos = note_store.findNotesMetadata(auth_token, filter, 0,
                        LimitConstants.EDAM_USER_NOTES_MAX, spec)
#print note_infos
note_guid = random.choice(note_infos.notes).guid
note = note_store.getNote(auth_token, note_guid, True, False, False, False)

print notebook_name + "<br clear=\"none\">"
print note.title + "<br clear=\"none\">"
#print notebook.content
print HTMLOfENML(note.content)



