docker rm -f test

docker run --name=test \
    -v $(pwd):/test \
    -p 8080:8080 \
    -ti -w /test mikeplavsky/aiohttp \
    bash


