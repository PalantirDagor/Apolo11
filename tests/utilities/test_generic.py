
def test_modulo_generic(app):
    assert app.Util.generate_random2(["1","2","3","4"]) == type(str)
    assert app.Util.generate_random(["a","b","c","d"]) == type(str)
    assert app.Util.generate_hash("10-02-2024", 
                                  "JUPITRAVEL", 
                                  "rover", 
                                  "warning") == type(str)
