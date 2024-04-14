from playwright.sync_api import Page
from path import OUTPOOT_PATH
import os


def test_screen1(page: Page):
    page.locator(".desktop-impact-item-eeQO3:nth-child(2)").screenshot(path=os.path.join(OUTPOOT_PATH, "TK1.png"))


def test_screen2(page: Page):
    page.locator(".desktop-impact-item-eeQO3:nth-child(4)").screenshot(path=os.path.join(OUTPOOT_PATH, "TK2.png"))


def test_screen3(page: Page):
    page.locator(".desktop-impact-item-eeQO3:nth-child(6)").screenshot(path=os.path.join(OUTPOOT_PATH, "TK3.png"))
