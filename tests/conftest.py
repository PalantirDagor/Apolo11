import pytest
import time
from src.utilities.files import FileUtils
from src.utilities.config import Util_Config
from src.utilities.generic import Utils as Util
from src.dashboard.process import Report
from src.simulator.simulator import Simulator_Apolo11 as Apolo11


@pytest.fixture(scope="session")
def app(request):

    class App:
        pass

    app = App()
    Util_Config()
    app.files = FileUtils
    app.util = Util
    app.simulator = Apolo11(20)
    time.sleep(40)
    app.report = Report(20)
    return app
