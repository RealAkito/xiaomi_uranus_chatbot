"""Data Provider class"""
import asyncio

from uranus_bot import LOGGER
from uranus_bot.providers.custom_recovery.pitchblack.pitchblack import load_pitchblack_data
from uranus_bot.providers.custom_recovery.twrp.twrp import load_twrp_data
from uranus_bot.providers.devices_info.info import load_firmware_codenames,\
    load_vendor_codenames, load_devices_names, load_miui_codenames, load_models
from uranus_bot.providers.firmware.firmware import load_firmware_data
from uranus_bot.providers.misc.arb import get_arb_table
from uranus_bot.providers.miui_updates_tracker.miui_updates_tracker import load_roms_data
from uranus_bot.providers.specs.specs import load_specs_data
from uranus_bot.providers.vendor.vendor import load_vendor_data
from uranus_bot.providers.xiaomi_eu.xiaomi_eu import load_eu_codenames, load_eu_data


class Provider:
    """Provides data that needs to be refreshed"""
    # pylint: disable=too-many-instance-attributes
    def __init__(self, _loop):
        self.loop = _loop
        self.twrp_data = {}
        self.orangefox_data = {}
        self.pitchblack_data = []
        self.firmware_codenames = []
        self.firmware_data = {}
        self.bak_firmware_data = {}
        self.vendor_codenames = []
        self.vendor_data = {}
        self.bak_vendor_data = {}
        self.codenames_names = {}
        self.names_codenames = {}
        self.models_data = {}
        self.miui_codenames = []
        self.miui_updates = []
        self.bak_miui_updates = []
        self.eu_codenames = {}
        self.eu_data = []
        self.specs_data = []
        self.arb = ""
        self.loop.create_task(self.twrp_data_loop())
        self.loop.create_task(self.pitchblack_data_loop())
        self.loop.create_task(self.firmware_codenames_loop())
        self.loop.create_task(self.firmware_data_loop())
        self.loop.create_task(self.vendor_codenames_loop())
        self.loop.create_task(self.vendor_data_loop())
        self.loop.create_task(self.devices_names_loop())
        self.loop.create_task(self.models_loop())
        self.loop.create_task(self.miui_codenames_loop())
        self.loop.create_task(self.miui_data_loop())
        self.loop.create_task(self.eu_codenames_loop())
        self.loop.create_task(self.eu_data_loop())
        self.loop.create_task(self.specs_data_loop())
        self.loop.create_task(self.arb_loop())

    async def twrp_data_loop(self):
        """
        fetch devices' twrp_data info every six hours
        """
        while True:
            LOGGER.info("Refreshing twrp data")
            self.twrp_data = await load_twrp_data()
            await asyncio.sleep(60 * 60 * 6)

    async def pitchblack_data_loop(self):
        """
        fetch PitchBlack recovery data every six hours
        """
        while True:
            LOGGER.info("Refreshing PitchBlack downloads data")
            self.pitchblack_data = await load_pitchblack_data()
            await asyncio.sleep(60 * 60 * 6)

    async def firmware_codenames_loop(self):
        """
        fetch devices' firmware codenames every six hours
        """
        while True:
            LOGGER.info("Refreshing firmware codenames")
            self.firmware_codenames = await load_firmware_codenames()
            await asyncio.sleep(60 * 60 * 6)

    async def firmware_data_loop(self):
        """
        fetch devices' firmware data every hour
        """
        while True:
            LOGGER.info("Refreshing firmware data")
            self.bak_firmware_data = self.firmware_data
            self.firmware_data = await load_firmware_data()
            await asyncio.sleep(60 * 60)

    async def vendor_data_loop(self):
        """
        fetch devices' vendor data every hour
        """
        while True:
            LOGGER.info("Refreshing vendor data")
            self.bak_vendor_data = self.vendor_data
            self.vendor_data = await load_vendor_data()
            await asyncio.sleep(60 * 60)

    async def miui_codenames_loop(self):
        """
        fetch devices' miui codenames every six hours
        """
        while True:
            LOGGER.info("Refreshing miui codenames")
            self.miui_codenames = await load_miui_codenames()
            await asyncio.sleep(60 * 60 * 6)

    async def vendor_codenames_loop(self):
        """
        fetch devices' vendor codenames every six hours
        """
        while True:
            LOGGER.info("Refreshing vendor codenames")
            self.vendor_codenames = await load_vendor_codenames()
            await asyncio.sleep(60 * 60 * 6)

    async def devices_names_loop(self):
        """
        fetch devices' codenames and names every six hours
        """
        while True:
            LOGGER.info("Refreshing devices codenames and names")
            self.codenames_names, self.names_codenames = await load_devices_names()
            await asyncio.sleep(60 * 60 * 6)

    async def models_loop(self):
        """
        fetch devices' models every six hours
        """
        while True:
            LOGGER.info("Refreshing models data")
            self.models_data = await load_models()
            await asyncio.sleep(60 * 60 * 6)

    async def miui_data_loop(self):
        """
        fetch devices' miui roms data every hour
        """
        while True:
            LOGGER.info("Refreshing miui data")
            self.bak_miui_updates = self.miui_updates
            self.miui_updates = await load_roms_data()
            await asyncio.sleep(60 * 60)

    async def eu_codenames_loop(self):
        """
        fetch devices' Xiaomi.eu codenames every hour
        """
        while True:
            LOGGER.info("Refreshing eu codenames data")
            self.eu_codenames = await load_eu_codenames()
            await asyncio.sleep(60 * 60 * 6)

    async def eu_data_loop(self):
        """
        fetch devices' Xiaomi.eu data every hour
        """
        while True:
            LOGGER.info("Refreshing eu downloads data")
            self.eu_data = await load_eu_data()
            await asyncio.sleep(60 * 60)

    async def specs_data_loop(self):
        """
        fetch devices' specs every six hours
        """
        while True:
            LOGGER.info("Refreshing specs data")
            self.specs_data = await load_specs_data()
            await asyncio.sleep(60 * 60 * 6)

    async def arb_loop(self):
        """
        fetch arb data every 12 hours
        """
        while True:
            LOGGER.info("Refreshing ARB data")
            self.arb = await get_arb_table()
            await asyncio.sleep(60 * 60 * 12)
