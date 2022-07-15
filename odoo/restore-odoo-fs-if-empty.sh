#!/bin/bash

odoo_fs_backup=/backup/odoo-fs.tar.gz
odoo_data_dir=/var/lib/odoo
odoo_fs_dir=$odoo_data_dir/filestore

if [ -f "$odoo_fs_backup" ] && [ ! -d "$odoo_fs_dir" ]; then
    cd $odoo_data_dir
    tar xfz $odoo_fs_backup
fi
