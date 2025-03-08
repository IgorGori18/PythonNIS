FROM postgres:13
ENV POSTGRES_USER=youruser
ENV POSTGRES_PASSWORD=yourpassword
ENV POSTGRES_DB=comments_db
COPY init.sql /docker-entrypoint-initdb.d/
