from typing import List

def test_modulo_process(app):

    assert app.report.consolidate_files().get("state") == True
    assert app.report.start_process().get("state") == True
