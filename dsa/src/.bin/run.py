import importlib
import sys


try:
    module = importlib.import_module(f"algorithms.{sys.argv[1]}")
    module.main()
except ImportError:
    print("module not found" + sys.argv[1])
