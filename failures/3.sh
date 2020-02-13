#/bin/bash

echo "Breaking something..."
docker exec kind-worker2 service kubelet stop
sleep 10
echo "Done!"