import os
import sys

# Garante que a pasta raiz do projeto (onde estão main.py, tasks.py, storage.py)
# está no sys.path, para que os testes em tests/ consigam importar estes módulos.
sys.path.insert(0, os.path.dirname(__file__))