# Jupyter Notebook DSC 400 Stack

Building cross-platform:

[Building Multi-Arch Images for Arm and x86 with Docker Desktop](https://www.docker.com/blog/multi-arch-images/)

```shell
docker buildx create --name mybuilder
docker buildx use mybuilder
docker buildx inspect --bootstrap
```

Build locally: 

```shell
docker buildx build --platform linux/amd64,linux/arm64 -t bellevueuniversity/dsc400-notebook:latest .
```

Build and Push to DockerHub:

```shell
docker build -t bellevueuniversity/dsc400-notebook:latest .
docker push bellevueuniversity/dsc400-notebook:latest
```

```shell
docker buildx build --platform linux/amd64,linux/arm64 -t bellevueuniversity/dsc400-notebook:latest --push .
```
