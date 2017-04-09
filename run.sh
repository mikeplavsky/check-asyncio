docker build -t test .
docker rm -f test

docker run --name=test \
    -v $(pwd):/tets \
    -p 8080:8080 \
    test \
    bash


