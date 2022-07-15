#!/bin/bash

BACKUP_SUFFIX="${BACKUP_SUFFIX:-$(date +%s)}"
BACKUP_DIR=${BACKUP_DIR:-/tmp}

### backup odoo database
db_temp_file=/tmp/odoo.pgdump

docker compose exec db \
  pg_dump -U odoo -Fc -d odoo -f $db_temp_file

docker compose cp db:$db_temp_file $BACKUP_DIR/odoo-db-$BACKUP_SUFFIX.pgdump

docker compose exec db \
  rm $db_temp_file

### backup odoo file store
fs_temp_file=/tmp/odoo-filestore.tar.gz

docker compose exec -w /var/lib/odoo odoo \
  tar -czf $fs_temp_file filestore

docker compose cp odoo:$fs_temp_file $BACKUP_DIR/odoo-fs-$BACKUP_SUFFIX.tar.gz

docker compose exec odoo \
  rm $fs_temp_file
