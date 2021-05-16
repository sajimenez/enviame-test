# enviame-test

## __Local installation instructions__ 
### __Option 1: Run in a container using docker-compose:__
1. Install dependencies:
    * Docker
    * docker-compose

1. Open your terminal and clone this project:
    ```
    git clone https://github.com/sajimenez/enviame-test.git
    ```

1. Go to the project's root folder, build the images and run the containers:
    ```
    cd enviame-test
    docker-compose up
    ```

1. Open your web browser and try the API: http://localhost:5000/api/companies/

1. To execute the additional exercises:
    ```
    docker exec [CONTAINER_ID] python scripts/exercise3.py
    docker exec [CONTAINER_ID] flask create-shipping
    docker exec [CONTAINER_ID] python scripts/exercise5.py
    docker exec [CONTAINER_ID] python scripts/exercise6.py
    ```

### __Option 2: Run in a local virtual environment:__

1. Install dependencies:
    * Python3.9 (https://www.python.org/downloads/)
    * Pipenv (https://pipenv-es.readthedocs.io/es/latest/)

1. Clone this project:
    ```
    git clone https://github.com/sajimenez/enviame-test.git
    ```

1. Go to the project's root folder, create a virtual environment and install python dependencies:
    ```
    cd enviame-test
    pipenv install --dev
    ```

1. Set the enviromental variables: 
    * Duplicate the file `example.env` and rename it to `.env`
    * Edit the environment variables inside the `.env` file accordingly
    * Activate the virtual environment: `pipenv shell` (this automatically loads the `.env` file)
    * Note: If no DATABASE_URL is defined, the app creates an Sqlite file by default.

1. Run migrations, load mock data and start the server:
    ```
    flask db upgrade
    flask load-companies [QTY]
    flask run
    ```

1. Open your web browser and try the API: http://localhost:5000/api/companies/

1. To execute the additional exercises:
    ```
    python scripts/exercise3.py
    flask create-shipping
    python scripts/exercise5.py
    python scripts/exercise6.py
    ```

Note: The SQL script corresponding to the Exercise 7 is located in the `scripts` folder.