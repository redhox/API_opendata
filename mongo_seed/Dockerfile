FROM mongo:5.0
ARG DATABASE_URI
ARG USERNAME
ARG PASSWORD

ENV DATABASE_URI ${DATABASE_URI}
ENV USERNAME ${USERNAME}
ENV PASSWORD ${PASSWORD}

COPY conso_departement.json /conso_departement.json



CMD mongoimport --jsonArray --db=consommations --collection=consommation_departements --file=conso_departement.json -u root -p example --host=mongo --port=27017 --authenticationDatabase admin