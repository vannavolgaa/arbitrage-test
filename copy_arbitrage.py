import os
import shutil

source = "/Users/marinjoublot-ferre/marquesasarbitrage/arbitrage/venv/lib/python3.12/site-packages/arbitrage.cpython-312-darwin.so"
destination = "/Users/marinjoublot-ferre/marquesasarbitrage/arbitrage-test/arbitrage.so"

if os.path.exists(source):
    shutil.copy(source, destination)
    print("File copied successfully!")
else:
    print("Source file not found!")