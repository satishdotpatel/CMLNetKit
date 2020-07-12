# -*- coding: utf-8 -*-
# (c) 2020 Piotr Wojciechowski <piotr@it-playground.pl>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import argparse


class CMLNetKitConfig:
    """
    Initializes a CMLNetKitConfig instance. This class is used to collect all parameters provided by
    argparse and in future perform some additional checkup.

    :param args: List of arguments parsed by parse_args().
    :type args: argparse.Namespace
    """

    # Connection definition
    host = None
    lab_id = None
    port = None
    username = None
    password = None
    ssl_verify = True

    # Parameters for changing the "External Connection" objects
    change_bridge = False

    def __init__(self, args):
        self.host = args.host
        self.username = args.username
        self.password = args.password
        self.port = args.port
        self.ssl_verify = args.ssl_verify

        if args.lab_id is not None:
            self.lab_id = args.lab_id