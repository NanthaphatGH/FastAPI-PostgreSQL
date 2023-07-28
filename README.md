# FastAPI-PostgreSQL
Use FastAPI framework to connect with postgreSQL to access database by using pipenv 

1. Install pipenv using command --> "pip install pipenv"
2. Use command "pipenv shell" to start virtual environment.
3. To get all necessary packages using pipenv "pipenv install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn python-dotenv"
4. Create a database in PostgreSQL and replace that name with my DATABASE_URL in file .env
5. Run command "alembic init alembic" to create a folder named alembic, inside that folder search for env.py and replace file with the given code.
6. Generates a new migration file based on the detected changes in the models, Using " alembic revision --autogenerate -m "New Migration" "
8. Applies migrations to the database --> "alembic upgrade head"
9. Uses Uvicorn to start the FastAPI application --> "uvicorn app.main:app --reload"
10. Entry this link "http://127.0.0.1:8000/docs" or use Postman to use CRUD operations. 
