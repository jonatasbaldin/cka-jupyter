from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

res = v1.list_pod_for_all_namespaces(watch=False, field_selector='metadata.name=nginx')

if len(res.items) > 0 and res.items[0].metadata.name == 'nginx' and res.items[0].spec.containers[0].image == 'nginx:alpine':
    print("Well done!")
else:
    print("Try again!")