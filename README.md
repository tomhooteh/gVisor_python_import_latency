# gVisor python import modules from external and internal latency

## Prerequire
- OS: linux kernel 3.17+
- Docker
- python3

## Environment Setup
- install gvisor: [click here](https://gvisor.dev/docs/user_guide/install/)
- note: if your machine is using kubernetes, you need to change cgroup-systemd to cgroup-cgroupfs because gvisor doesn't support systemd cgroup

## Experiment
1. pull the same python version image. [offical website](https://hub.docker.com/_/python) (In this experiment we use python 3.6.9)
  ```
  sudo docker pull python:3.6.9
  ```
2. check the path of python modules by following python code(use numpy for example)
  ```
  import numpy
  print(numpy.__file__)
  ```
  - result:

  ![find_path](https://user-images.githubusercontent.com/9292747/145703315-9d845c31-b2db-44a5-b4a0-ed332afbaa2f.png)

3. write two python file to import from internal ann external(by volume)
  - import_internal.py:
  ```
  import time
  start = time.perf_counter()
  import requests
  end = time.perf_counter() - start
  print('{:.3f}s for importing requests'.format(end))
  ```
  - import_external.py:
  ```
  import time
  start = time.perf_counter()
  from utils import requests
  end = time.perf_counter() - start
  print('{:.3f}s for external importing requests'.format(end))
  ```
4. build container by Dockerfile:
  - Dockerfile
  ```
  FROM python:3.6.9
  WORKDIR /app
  COPY import_external.py /app/
  COPY import_internal.py /app/

  ENV PYTHONPATH /app/utils
  ENV PATH=$PATH:/app/utils

  CMD python import_external.py ; python import_internal.py
  ```
  - Build:
  ```
  sudo docker build -t python_import_test
  ```
  
  
 
 
## REFERENCES
- [The True Cost of Containing: A gVisor Case Study](https://www.usenix.org/system/files/hotcloud19-paper-young.pdf)
