#!/usr/bin/env python26
#Description: Constants definitions

#   Copyright 2013 Zynga Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

SYSLOG_TAG = 'zbasebackup'
MBRESTORE_PID_FILE = '/var/run/mbrestore.pid'
MBBACKUP_PID_FILE = '/var/run/zbbackup.pid'
SCHEDULER_PID_FILE = '/var/run/backup_merge.pid'
BLOBRESTORED_PID_FILE = '/var/run/blobrestored.pid'
MEMCACHED_PID_FILE = '/var/run/memcached/memcached.pid'
CONFIG_FILE = '/etc/zbase-backup/default.ini'
MEMCACHED_SYSCONFIG_FILE = '/etc/sysconfig/memcached'
LAST_CHECKPOINT_FILE = '/var/tmp/last_closed_checkpoint'
BACKUP_TAPNAME = 'backup'
REPLICATION_TAPNAME = 'replication'
PATH_MBBACKUP_EXEC = '/opt/zbase/lib/python/mbbackup-incremental'
PATH_S3CMD_EXEC = '/opt/zbase/zbase-backup/zstore_cmd_helper'
PATH_S3CMD_ZYNGA_EXEC = '/usr/bin/s3cmd'
INCR_DIRNAME = 'incremental'
MASTER_DIRNAME = 'master'
PERIODIC_DIRNAME = 'daily'
MAX_BACKUP_SEARCH_TRIES = 15
PATH_MBRESTORE_EXEC = '/opt/zbase/lib/python/mbadm-online-restore'
PATH_MBTAP_REGISTER_EXEC = '/opt/zbase/lib/python/mbadm-tap-registration'
PATH_COUNTKEYS_EXEC = '/opt/zbase/zbase-backup/count_backup_keys.sh'
PATH_MBMERGE_EXEC = '/opt/zbase/zbase-backup/merge-incremental'
DEFAULT_LOGLEVEL = 'INFO'
MERGE_CMD = "/opt/zbase/zbase-backup/merge.py"
BACKUP_ROOT = "/dev/shm"
SPLIT_UPLOAD_CMD = "/opt/zbase/zbase-backup/misc/split_backup.py"
SPLIT_SIZE = 1024
DEL_COMMAND = "del"
BLOBRESTORE_JOBS_DIR = '/home/storageserver/jobs/'
BLOBRESTORE_PROCESSED_JOBS_DIR = '/home/storageserver/processed_jobs/'
SYSLOG_TAG_BLOBRESTORE = 'blobrestore'
BLOBRESTORE_DAEMON_LOG = '/var/log/blobrestore_daemon.log'
STORAGE_SERVER_ROOT = '/var/www/html/'
MAX_BACKUP_LOOKUP_DAYS = 21
LAST_MASTER_BACKUP_TIME = '/db/last_master_backup'
NAGIOS_BACKUP_TIME = '/tmp/nagios_state/mb_backup_time'
CKSUM_VERSION = 2
DB_PATHS = ['/db/zbase/']
MIN_INCR_BACKUPS_COUNT = 15
BAD_DISK_FILE = '/var/tmp/disk_mapper/bad_disk'
DIRTY_DISK_FILE = 'dirty'
TO_BE_DELETED_FILE = 'to_be_deleted'
PATH_DAILY_MERGE = '/opt/zbase/zbase-backup/daily-merge'
PATH_MASTER_MERGE = '/opt/zbase/zbase-backup/master-merge'
MAX_MASTERJOBS = 1
MAX_DAILYJOBS = 5
DAILYJOB_MEM_THRESHOLD = 10240
MASTERJOB_MEM_THRESHOLD = 15360
ZRT_URL = 'https://api.runtime.zynga.com:8994'
BLOBRESTORE_API_PATH = 'api?action=get_vb_mapping'
PADDING_ZEROS = 3
ZRT_MAPPER_KEY = 'ACTIVE_MCS'
ZRT_RETRIES = 300
LOCAL_BACKUP_PATH = '/db_localbackup/'
LOCAL_BACKUP_COUNT = 5
DISKMAPPER_HOSTCONFIG = '/var/tmp/diskmapper_hostconfig'
DEL_MANIFEST = 'manifest.del'
PROMOTE_MANIFEST = '.promoting'
CONNECT_RETRIES = 20
PATH_MBFLUSHCTL = "/opt/zbase/lib/python/mbflushctl"
VBS_API_PATH = 'vbucketMap'
SS_API_PATH = 'api?action=get_ss_mapping&storage_server=%s'
PATH_MBVBUCKET_CTL = '/opt/zbase/lib/python/mbvbucketctl'
BACKUP_RETRIES = 10
BACKUP_INTERVAL = 3600
LAST_CHECKPOINT_FILE = 'last_cpoint'
SS_PORT = 22122
RESTORE_CMD = "zbase-restore"
RESTORE_CMD_ABS = "/opt/zbase/zbase-backup/zbase-restore"
TAP_REGISTERATION = '/opt/zbase/zbase-backup/mbadm-tap-registration'
