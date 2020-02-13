# The CKA Jupyter Lab 🤓
An interactive Jupyter Lab to study for the Certified Kubernetes Administrator exam.

> This is only a PoC, don't mind the ugly code 😉

## Requirements
You'll need to have locally in your machine:
- Python 3.7+
- kubectl
- docker
- kind

## Installing
```bash
git clone git@github.com:jonatasbaldin/cka-jupyter.git
cd cka-jupyter

python -m venv venv
source venv/bin/activate

pip install jupyterlab==1.2.6 bash-kernel==0.7.2 kubernetes==10.0.1
python -m bash_kernel.install
```

## Running
**Be sure to not have any kind cluster running**.
```bash
jupyter lab
```

## Ideas
So far, this is using [Kind](https://kind.sigs.k8s.io/) as a Kubernetes cluster and Jupyter Lab as the exercises interface. I had ideas for other methods, any feedback is appreciated:

- Run [Coder](https://coder.com/) interface, using simple Markdown files for the labs.
- Create a local K8S cluster with Vagrant. Isolates the environment better, allows SSH into Nodes (with kind one can use `docker exec`) and dynamic clusters (more nodes can be added) or even create a cluster from scratch to test `kubeadm`.