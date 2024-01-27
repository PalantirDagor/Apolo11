def test_modulo_process(app):

    #assert app.report.consolidate_files().message.get("state") == True
    assert app.report.start_process().message.get("state") == True
