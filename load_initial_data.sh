#!/bin/bash

PROJECT_DIR=$(dirname "${BASH_SOURCE[0]}")
ALBUM_CSV=$1

docker compose -f "$PROJECT_DIR/docker-compose.yml" cp "$ALBUM_CSV" api:/albumlist.csv
docker compose -f "$PROJECT_DIR/docker-compose.yml" exec -i api flask cli load-albums /albumlist.csv