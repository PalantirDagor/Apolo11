import pytest
from src.utilities.files import FileUtils
<<<<<<< HEAD
from src.utilities.generic import Utils as util
=======
from src.utilities.config import Util_Config
from src.utilities.generic import Utils as Util
>>>>>>> 10a85115b76a84c23658455bd0b5ad08f7a886c9
from src.dashboard.process import Report
from src.Simulator.simulator import Simulator_Apolo11 as apolo11


@pytest.fixture(scope="session")
def app(request):

    class App:
        pass

    app = App()
<<<<<<< HEAD
    app.files = FileUtils()
    app.generic = util()
    app.report = Report("Name_report")
    app.simulator = apolo11()
=======
    config = Util_Config()
    app.files = FileUtils
    app.util = Util
    app.report = Report(20)
    app.simulator = apolo11(20)
>>>>>>> 10a85115b76a84c23658455bd0b5ad08f7a886c9
    return app
