# Specify base image
FROM python:3.10

WORKDIR /usr/app/qdpb

# add the required files
ADD bot.py .
ADD requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# run the bot
CMD [ "python3", "./bot.py" ]
