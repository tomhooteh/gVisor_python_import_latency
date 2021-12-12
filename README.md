# gVisor python import modules from external and internal latency

## Prerequire
- OS: linux kernel 3.17+
- Docker
- python3

## Environment Setup

- install gvisor: [click here](https://gvisor.dev/docs/user_guide/install/)
> note: if your machine is using kubernetes, you need to change cgroup-systemd to cgroup-cgroupfs because gvisor doesn't support systemd cgroup
- install numpy by pip:
```
python3 -m pip install numpy
```

## Experiment
1. pull the same python version image. [offical website](https://hub.docker.com/_/python) (In this experiment we use python 3.6.9)
  ```
  sudo docker pull python:3.6.9
  ```
2. check the path of python modules by following python code(use requests for example)
  ```
  import requests
  print(requests.__file__)
  ```
  - result: you need to remember this path for later volume's path 
  ![](https://i.imgur.com/kChNEsg.png)

3. build container with Dockerfile:
  ```
  sudo docker build -t python_import_test
  ```
  > if you want to import non python standard library. you need to change dockerfile to install module first.
  > adding belowing instruction before CMD python
  ```
  RUN pip install "modulename"
  ```
  
  
4. run container and use volume to mount python modules
  - run container by default runc
  ```
  sudo docker run --rm -v /usr/lib/python3/dist-packages/:/app/utils python_import
  ```
  
  - run container by runsc(gVisor)
  ```
  sudo docker run --rm --runtime=runsc -v /usr/lib/python3/dist-packages/:/app/utils python_import
  ```
  
  
  
 
 
## REFERENCES
- [The True Cost of Containing: A gVisor Case Study](https://www.usenix.org/system/files/hotcloud19-paper-young.pdf)
