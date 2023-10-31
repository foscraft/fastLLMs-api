set -e;

# build docker image
docker build -t fastllms-api .;

# stop and remove container if it exists
{
    docker stop fastllms-api;
    docker rm fastllms-api;
}||{
    echo "No container to stop";
};

# run api
docker run -d \
-p 8000:8000 \
--name fastllms-api \
--restart=always \
-v /opt/models:/tmp/models \
-v /opt/fastllms-api-data/db:/tmp/db \
-v /opt/fastllms-api-data/source:/tmp/source \
-e "PERSIST_DIRECTORY=/tmp/db" \
-e "MODEL_TYPE=GPT4All" \
-e "MODEL_PATH=/tmp/models/llama-2-7b-chat.ggmlv3.q2_K.bin" \
-e "EMBEDDINGS_MODEL_NAME=all-MiniLM-L6-v2" \
-e "MODEL_N_CTX=1000" \
-e "MODEL_N_BATCH=8" \
-e "TARGET_SOURCE_CHUNKS=4" \
-e "SOURCE_DIRECTORY=/tmp/source" \
fastllms-api;

# check if the container is running
echo "******************** Checking if the container is running ********************";
docker ps | grep fastllms-api;