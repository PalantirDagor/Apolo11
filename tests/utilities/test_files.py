import os
path0: str = os.path.join("tests", "utilities", "folder")
path1: str = os.path.join(path0, "patch1")
path2: str = os.path.join(path0, "patch2")
file_name: str = "text.txt"


def test_modulo_files(app):
    assert app.files.Save(file_name, path1, ["1", "2", "3", "4"]).message.get("state")  == True
    assert app.files.read_file(os.path.join(path1, file_name)).message.get("state") == True
    assert app.files.move_file(path1, path2, file_name).message.get("state")  == True
    assert app.files.move_file(path1, path2, "text_2.txt").message.get("state") == False
    assert app.files.move_file(path1, path2).message.get("state")  == True
