#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import keyring
import argparse

from credentials import BOT_KEY_NAMESPACE, BOT_TOKEN


def main():
    parser = argparse.ArgumentParser(description='Tools for working with keychain in GasGuard.')
    parser.add_argument('-t', '--token', help='Set token value into keychain.')

    args = parser.parse_args()

    keyring.set_password(BOT_KEY_NAMESPACE, BOT_TOKEN, args.token)

    parser.print_help()


if __name__ == '__main__':
    main()
