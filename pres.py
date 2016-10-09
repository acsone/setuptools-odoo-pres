#!/home/sbi-local/.virtualenvs/prysenter/bin/python
from prysenter import Prysentation

slides = [
    'import odoo.addons\n'
    '\n'
    '{s_bright}stephane.bidoul@acs{f_yellow}on{f_reset}e.eu',

    'The basics\n'
    '\n'
    'virtualenv, pip install',

    'Let\'s create a project',

    'Release time\n'
    '\n'
    'pip freeze, git tag, pip wheel',

    'Package your own addons\n'
    '\n'
    'setuptools-odoo in a nutshell',

    'Thank you!\n'
    '\n'
    '{s_bright}stephane.bidoul@acs{f_yellow}on{f_reset}e.eu',
]

Prysentation(slides=slides).start()
