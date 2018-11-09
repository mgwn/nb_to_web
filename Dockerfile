FROM python:3

WORKDIR /opt/notebook
COPY . .

# Install dependencies 
RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "make", "clean", "html", "serve" ]