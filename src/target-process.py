#!/usr/bin/env python
# encoding: utf-8

import sys
import argparse
import subprocess
from workflow import Workflow3

DEFAULT_SETTINGS = {
    'instance_url': 'https://<my-tp-instance>.tpondemand.com',
}

UPDATE_SETTINGS = {'github_slug': 'lukewaite/alfred-target-process'}

# GitHub Issues
HELP_URL = 'https://github.com/lukewaite/alfred-target-process/issues'

ICON_UPDATE_AVAILABLE = 'icons/update-available.png'


# Populated later - setting scope
log = None

def show_update():
    """Add an 'update available!' item."""
    if wf.update_available:
        wf.add_item('Workflow Update Available!',
                    u'↩ or ⇥ to install update',
                    autocomplete='workflow:update',
                    valid=False,
                    icon=ICON_UPDATE_AVAILABLE)
        return True

    return False


def do_settings():
    """Open ``settings.json`` in default editor.
    Returns:
        int: Exit status.
    """
    subprocess.call(['open', wf.settings_path])
    return 0

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--settings', action='store_true')
    parser.add_argument('query', nargs='?', default=None)
    # parse the script's arguments
    args = parser.parse_args(wf.args)
    log.debug('args=%r', args)
    return args

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def do_query(query):
    if RepresentsInt(query):
        query = int(query)
        wf.add_item(
            'Open TargetProcess #{}'.format(query),
            arg=wf.settings['instance_url'] + '/entity/' + str(query),
            valid=True
        )
    else:
        wf.add_item(
            'Search TargetProcess for \'{}\''.format(query),
            arg=wf.settings['instance_url'] + '/RestUI/Board.aspx#searchPopup=query/' + query,
            valid=True
        )

    wf.send_feedback()
    return 0


def main(wf):
    """Run workflow script."""
    args=parse_args()

    show_update()

    # First, check for a query to keep that quick.
    if args.query:
        return do_query(args.query)

    if args.settings:
        return do_settings()

    raise ValueError('unknown action')


if __name__ == '__main__':
    wf = Workflow3(
        default_settings=DEFAULT_SETTINGS,
        update_settings=UPDATE_SETTINGS,
        help_url=HELP_URL,
    )
    log = wf.logger
    sys.exit(wf.run(main))