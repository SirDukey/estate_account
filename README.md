# Odoo: estate_account
An Odoo addon ***link module*** for a Real Estate module and the Account module.  Its purpose is to generate invoices 
from the Real Estate module using the Account module.

This is a module from the official Odoo [tutorial](https://www.odoo.com/documentation/18.0/developer/tutorials/server_framework_101/13_other_module.html) 
chapter 13: Interact With Other Modules.

It relies on the Real Estate module which can be found [here](https://github.com/SirDukey/real-estate) and the standard 
**account** (Invoice) module provided by Odoo

## Using the module
I create a folder called `addons` near my forked Odoo repository which contains this repo as well as the Real-Estate 
repo, I use a `odoo.conf` file like this:

    [options]
    db_host = localhost
    db_port = 5432
    db_user = ****
    db_password = ****
    addons_path = <PATH TO YOUR ODOO REPO>/odoo/addons, <PATH TO YOUR ODOO REPO>/addons

then I run Odoo `./odoo/odoo-bin -c odoo.conf`

When developing the module I use the `-u` flag to auto upgrade the module when restarting and
the `--dev` flag to allow browser refresh when working on the views

I run a Pycharm configuration and use the following flags (adjust as needed), this allows edits to xml files only
requiring a browser refresh to see the changes and a module upgrade each time the configuration is restart, handy for 
developing :grin:

`-c odoo.conf -u real-estate -u estate_account --dev xml`