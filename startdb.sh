TAG_NAME=agendum-database
CONTAINER_NAME=agendum-database
VOLUME_NAME="agendum-database-volume"

if docker images | grep "$TAG_NAME" > /dev/null ; then
    echo 'image already built, skipping.'
else
    docker build . --tag "$TAG_NAME"
fi

docker run --rm --detach --name "$CONTAINER_NAME" --publish 27017:27017 --volume "$VOLUME_NAME:/data/db" agendum-database
