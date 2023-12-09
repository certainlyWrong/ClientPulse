
# About ClientPulse
This is a simple API for project [StockMingle](https://github.com/certainlyWrong/StockMingle). It is written in Python and uses the FastAPI framework to serve the API and MySQL as the database.

## How to run
To run this project separately, you need to have Docker installed on your machine. After that, you can run the following command to start the database:
```bash
docker run -p 3306:3306 --name clientpulse-bd -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=clientpulse 
-d mysql:latest
```

After that, you can run the following command to start the API:
```bash
poetry run server
```

## Routes
You can see the routes in the following link: [http://localhost:8000/docs](http://localhost:8000/docs)


