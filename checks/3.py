from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

res = v1.read_node_status('kind-worker2', pretty=True)

working = False

for condition in res.status.conditions:
    if condition.type == 'Ready' and condition.status == 'True':
        working = True

if working:
    print("Well done!")
else:
    print("Try again!")