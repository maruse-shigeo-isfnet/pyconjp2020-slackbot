#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import google.auth
from google.cloud import secretmanager
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

credentials, project = google.auth.default()

client = secretmanager.SecretManagerServiceClient()
name = client.secret_version_path(project, 'iriomote_cat', 'latest')
response = client.access_secret_version(name)

API_TOKEN = response.payload.data.decode('UTF-8')
DEFAULT_REPLY = 'はじめまして、西表山猫です。'
PLUGINS = ['plugins']
ERRORS_TO = 'errors'
