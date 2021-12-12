import time

start = time.perf_counter()
import requests
end = time.perf_counter() - start
print('{:.3f}s for the importing '.format(end), end = '')
print(requests.__name__);


