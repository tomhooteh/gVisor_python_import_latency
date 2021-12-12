import time

start = time.perf_counter()
from utils import requests
end = time.perf_counter() - start

print('{:.3f}s for external importing requests'.format(end))

