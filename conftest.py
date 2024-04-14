import pytest
from playwright.sync_api import Page
import os
from path import OUTPOOT_PATH
import shutil


@pytest.fixture(scope="session", autouse=True)
def delete_folder():
    if os.path.exists(OUTPOOT_PATH):
        shutil.rmtree(OUTPOOT_PATH)


@pytest.fixture(scope='function', autouse=True)
def browser_open(page: Page):
    page.goto('https://www.avito.ru/avito-care/eco-impact')


@pytest.fixture(scope="function")
def create_folder():
    if not os.path.exists(OUTPOOT_PATH):
        os.mkdir(OUTPOOT_PATH)
