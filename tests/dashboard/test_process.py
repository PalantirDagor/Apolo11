def test_modulo_process(app):

    assert app.report._start_process().message.get("state") == True
