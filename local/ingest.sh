set -e;

# run ingest script
docker run --rm \
-v /opt/fastllms-api-data/db:/tmp/db \
-v /opt/fastllms-api-data/source:/tmp/source \
-e "PERSIST_DIRECTORY=/tmp/db" \
-e "EMBEDDINGS_MODEL_NAME=all-MiniLM-L6-v2" \
-e "MODEL_N_CTX=1000" \
-e "MODEL_N_BATCH=8" \
-e "TARGET_SOURCE_CHUNKS=4" \
-e "SOURCE_DIRECTORY=/tmp/source" \
-e "RUN_INGEST=true" \
--entrypoint /bin/bash \
fastllms-api -c "python3 ingest.py"

