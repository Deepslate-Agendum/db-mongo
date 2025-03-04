TAG_NAME=agendum-database
CONTAINER_NAME=agendum-database
VOLUME_NAME=agendum-database-volume
PORT=27017

if docker image ls | awk "match($\1, /${TAG_NAME}/) { print $\1 }" | grep . > /dev/null ; then
    echo 'image already built, skipping.'
else
    docker build . --tag "${TAG_NAME}"
fi

docker run --rm --detach --name "${CONTAINER_NAME}" --publish "${PORT}:${PORT}" --volume "${VOLUME_NAME}:/data/db" "${TAG_NAME}"
