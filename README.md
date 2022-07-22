# University of Tikrit Open EduCat

## Prerequisites

The only prerequisite is to have Docker installed.

## Running the app

Launch the app from the terminal with `./up.sh`.

If you want to run the app with a specific database/filestore backup then you'll need to create `odoo-db.pgdump` and `odoo-fs.tar.gz` files in the `./backup` directory before launching the app.

If you already launched the app then in order to restore from the backup you'll have to delete the exsting app with `docker compose down`.
