import os

import pytest
from datetime import datetime

from utils.api_client import *
from utils.config import *
import random




@pytest.fixture(scope="session")
def api_client():
    return APIClient(Config.baseUrl)

@pytest.fixture
def unique_id():
    return random.randint(100000, 999999)


def pytest_html_report_title(report):
    report.title = "Petstore API Automation Report"

@pytest.hookimpl(optionalhook = True)
def pytest_metadata(metadata):
    metadata.clear()
    metadata["Project"] = "Petstore API"
    metadata["Type"] = "API Automation"
    metadata["Environment"] = "QA"
    metadata["Executed On"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

