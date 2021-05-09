import importlib
import sys


try:
    module_name = sys.argv[2].replace("src/", "").replace("/", ".")
    module = importlib.import_module(f"{module_name}.{sys.argv[1]}")
    module.main()
except ImportError:
    print("module not found " + sys.argv[1])
