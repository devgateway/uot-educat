#!/bin/bash

PGDUMP=/backup/odoo-db.pgdump
DB_NAME=odoo
PG_CONN_ARGS="-U $POSTGRES_USER"

if [ -f "$PGDUMP" ]; then
    createdb $PG_CONN_ARGS $DB_NAME
    pg_restore $PG_CONN_ARGS -d $DB_NAME $PGDUMP
fi
