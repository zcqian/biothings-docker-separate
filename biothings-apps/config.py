from config_hub import *
import os
import urllib.parse

src_parsed = urllib.parse.urlparse(os.environ.get('SRC_URI'))
target_parsed = urllib.parse.urlparse(os.environ.get('TARGET_URI'))
hub_parsed = urllib.parse.urlparse(os.environ.get('HUB_URI'))

DATA_ARCHIVE_ROOT = '/data/biothings/API_NAME/datasources'
DATA_PLUGIN_FOLDER = '/data/biothings/API_NAME/plugins'
DATA_UPLOAD_FOLDER = '/data/biothings/API_NAME/dataupload'

DIFF_PATH = "/data/biothings/API_NAME/diff"
RELEASE_PATH = "/data/biothings/API_NAME/release"
CACHE_FOLDER = "/data/biothings/API_NAME/cache"

LOG_FOLDER = "/data/biothings/API_NAME/logs"
logger = setup_default_log("hub", LOG_FOLDER)

RUN_DIR = '/data/biothings/API_NAME/run'

DATA_SRC_SERVER = src_parsed.hostname or 'localhost'
DATA_SRC_PORT = src_parsed.port or 27017
DATA_SRC_DATABASE = os.environ.get('SRC_DB', 'biothings_src')
DATA_SRC_SERVER_USERNAME = urllib.parse.unquote(src_parsed.username) if src_parsed.username else ''
DATA_SRC_SERVER_PASSWORD = urllib.parse.unquote(src_parsed.password) if src_parsed.password else ''

DATA_TARGET_SERVER = target_parsed.hostname or 'localhost'
DATA_TARGET_PORT = target_parsed.port or 27017
DATA_TARGET_DATABASE = os.environ.get('TARGET_DB', 'biothings_target')
DATA_TARGET_SERVER_USERNAME = urllib.parse.unquote(target_parsed.username) if target_parsed.username else ''
DATA_TARGET_SERVER_PASSWORD = urllib.parse.unquote(target_parsed.password) if target_parsed.password else ''

# FIXME: deal with other uri later
assert hub_parsed.scheme == 'mongodb'
DATA_HUB_DB_DATABASE = os.environ.get('HUB_DB', 'biothings_hub')
HUB_DB_BACKEND = {
		"module" : "biothings.utils.mongo",
		"uri" : os.environ.get('HUB_URI', 'mongodb://localhost:27017'),
    }

CONFIG_READONLY = False

# FIXME: deal with the version issue
# At least for BIOTHINGS_VERSION, it is trying to use the git repo version
# which does not seem to make sense
BIOTHINGS_VERSION = 'fixme'

# SSH port for hub console
HUB_SSH_PORT = 7022
HUB_API_PORT = 7080

# Hub name/icon url/version, for display purpose
HUB_NAME = "Studio for API_NAME"
HUB_ICON = "http://biothings.io/static/img/API_NAME-logo-shiny.svg"
HUB_VERSION = "master"

USE_RELOADER = True # so no need to restart hub when a datasource has changed

# cleanup config namespace
del os, urllib, src_parsed, target_parsed, hub_parsed