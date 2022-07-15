#!/bin/bash

COMPOSE_ENV_FILE="${COMPOSE_ENV_FILE:-.env}"

docker compose --env-file $COMPOSE_ENV_FILE up -d

docker compose exec odoo ./restore-odoo-fs-if-empty.sh
