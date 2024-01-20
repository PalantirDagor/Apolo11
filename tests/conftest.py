import pytest
from src.utilities.files import FileUtils
from src.dashboard.process import Report

@pytest.fixture(scope="session")
def app(request):
    
    class App:
        pass
    
    app = App()
    app.files = FileUtils
    app.report = Report("Name_report")
    return app
