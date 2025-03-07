source .env

# docker image ls | awk "match($$1, /${TAG_NAME}/) { print $$1 }" | grep . > /dev/null
docker build . --tag "${TAG_NAME}"
docker run --rm --detach --name "${CONTAINER_NAME}" --publish "${PORT}:${PORT}" --volume "${VOLUME_NAME}:/data/db" "${TAG_NAME}"
