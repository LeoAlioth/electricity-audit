FROM alpine:3.14

# Install requirements for add-on
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache sqlite

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
# COPY db /app/db
# COPY __init__.py /app/main

# set enfiroment variable for flask aplication

ENV FLASK_APP=/app/web/__init__

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

CMD [ "-m" , "flask", "run", "--host=0.0.0.0"]
