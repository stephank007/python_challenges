import os
import shutil as sh
import nbconvert

print(os.getcwd())

sc_exporter = nbconvert.ScriptExporter()
for r, d, f in os.walk('.'):
    if 'venv' not in r:
        for file in f:
            if '.ipynb' in file:
                full_name = os.path.join(r, file)
                root = os.path.splitext(file)
                py_name = os.path.join(r, root[0] + '.py')
                print(py_name)
                moshe = sc_exporter.from_file(full_name)
                f_handler = open(py_name, 'w')
                f_handler.write(moshe[0])
                f_handler.close()
