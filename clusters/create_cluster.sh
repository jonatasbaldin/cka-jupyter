#/bin/bash

kind create cluster --config clusters/two_nodes.yaml

# Jojo's hackiest move in 2020 so far
# This adds a new option to kube-controller-manager, by editing the file in place after the line 24
# which is the middle of the `command:` section of the manifest
# Used to caught generated failures in nodes with less time
docker exec kind-control-plane sed -i '24i \ \ \ \ - --node-monitor-grace-period=10s' /etc/kubernetes/manifests/kube-controller-manager.yaml