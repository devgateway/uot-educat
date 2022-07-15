#!/bin/bash

set -e

# set the project name, BUILD_TAG is specified by Jenkins
PRJ_NAME="${BUILD_TAG:-uot-educat-test}"

# comma separated list of modules to test
MODULES=openeducat_core

# cleanup even in case of failure
trap "docker compose -p $PRJ_NAME down -v" EXIT

# run tests
docker compose -p $PRJ_NAME run --rm odoo \
  odoo -i $MODULES -d odoo --test-enable --stop-after-init
