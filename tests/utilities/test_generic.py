
def test_modulo_generic(app):
    assert app.util.generate_random(["1", "2", "3", "4"]) in ["1", "2", "3", "4"]
    assert app.util.generate_random(["a", "b", "c", "d"]) in ["a", "b", "c", "d"]
