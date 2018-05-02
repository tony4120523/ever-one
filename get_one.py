#!/usr/bin/python 
# -*- coding: utf-8 -*-
#
# A simple Evernote API demo script that lists all notebooks in the user's
# account and creates a simple test note in the default notebook.
#
# Before running this sample, you must fill in your Evernote developer token.
#
# To run (Unix):
#   export PYTHONPATH=../../lib; python EDAMTest.py
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

auth_token = "S=s1:U=94930:E=16a74fe3f63:C=1631d4d1120:P=1cd:A=en-devtoken:V=2:H=bd72d309237af750c91c0d11cfa179d4"

if auth_token == "your developer token":
    print "Please fill in your developer token"
    print "To get a developer token, visit " \
        "https://sandbox.evernote.com/api/DeveloperToken.action"
    exit(1)


# To access Sandbox service, set sandbox to True 
# To access production (International) service, set both sandbox and china to False
# To access production (China) service, set sandbox to False and china to True
sandbox = True
china = False

# Initial development is performed on our sandbox server. To use the production
# service, change sandbox=False and replace your
# developer token above with a token from
# https://www.evernote.com/api/DeveloperToken.action
client = EvernoteClient(token=auth_token, sandbox=sandbox, china=china)

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

note_store = client.get_note_store()

# List all of the notebooks in the user's account
notebooks = note_store.listNotebooks()
#print "Found ", len(notebooks), " notebooks:"
#for notebook in notebooks:
#    print "  * ", notebook.name

# write the notebook_name
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
#spec.includeCreated = True
note_infos = note_store.findNotesMetadata(auth_token, filter, 0,
                        LimitConstants.EDAM_USER_NOTES_MAX, spec)
#print note_infos
note_guid = random.choice(note_infos.notes).guid
notebook = note_store.getNote(auth_token, note_guid, True, False, False, False)

print note_guid
print notebook.title
print
#print notebook.content
print PlainTextOfENML(notebook.content)



