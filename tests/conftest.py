import pytest
from src.utilities.files import FileUtils
from src.utilities.config import Util_Config
from src.utilities.generic import Utils as Util
from src.dashboard.process import Report
from src.Simulator.simulator import Simulator_Apolo11 as apolo11


@pytest.fixture(scope="session")
def app(request):

    class App:
        pass

    app = App()
    app.files = FileUtils()
    app.generic = util()
    app.report = Report("Name_report")
    app.simulator = apolo11()

    config = Util_Config()

    Util_Config()

    app.files = FileUtils
    app.util = Util
    app.report = Report(20)
    app.simulator = apolo11(20)

    return app
