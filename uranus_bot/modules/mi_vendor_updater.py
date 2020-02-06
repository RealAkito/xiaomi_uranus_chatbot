#!/usr/bin/env python3.7
"""Mi Vendor updater"""

import yaml
from requests import get
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .mwt import MWT
from .extras import check_codename


@MWT(timeout=60 * 60 * 6)
def fetch_devices():
    """
    fetches devices data every 6h
    :return: devices
    """
    return yaml.load(get(
        "https://raw.githubusercontent.com/XiaomiFirmwareUpdater/" +
        "xiaomifirmwareupdater.github.io/master/data/vendor_codenames.yml").text, Loader=yaml.CLoader)


@check_codename(fetch_devices(), markup=True)
def fetch_vendor(device):
    """
    generate latest vendor links for a device
    :argument device - Xiaomi device codename
    :returns message - telegram message string
    """
    site = 'https://xiaomifirmwareupdater.com'
    message = f"*Available vendor downloads for* `{device}`\n"
    latest = InlineKeyboardButton(f"Latest Vendor", f"{site}/vendor/{device}/")
    archive = InlineKeyboardButton(f"Vendor Archive", f"{site}/archive/vendor/{device}/")
    channel = InlineKeyboardButton("MIUIVendorUpdater", url="https://t.me/MIUIVendorUpdater")
    reply_markup = InlineKeyboardMarkup([[latest, archive], [channel]])
    return message, reply_markup