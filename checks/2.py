from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

res = v1.list_service_for_all_namespaces(
    watch=False,
    field_selector='metadata.name=nginx-svc',
)

if len(res.items) > 0:
    svc = res.items[0]

if svc.spec.type == 'NodePort' and svc.spec.ports[0].node_port == 30080:
    print("Well done!")
else:
    print("Try again!")