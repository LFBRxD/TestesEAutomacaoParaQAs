FROM postman/newman:alpine

WORKDIR /etc/newman

COPY . /etc/newman

ENTRYPOINT ["newman", "run", "API_Flask_for_QA.postman_collection.json"]
