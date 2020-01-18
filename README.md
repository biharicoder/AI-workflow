# AI Workflow: An end to end AI pipeline

* **cs-train**: Contains all the data to train the model
* **models**: Contains all pre-trained saved models for prediction
* **notebooks**: Contains all the notebooks describing solutions and depicting visualizations
* **templates**: Simple templates for rendering flask app
* **unittest**: It has logger test, API test and model test for testing all the functionalities before deploying to production and for maintenance post deployment
* **Dockerfile**: Contains all the commands a user could call on the command line to assemble the docker image.
* **app.py**: Flask app for creating a user interface /train and /predict APIs in order to train and predict respectively
* **cslib.py**: A collection of functions that will transform the data set into features you can use to train a model.
* **model.py**:  A module having functions for training, loading a model and making predictions
## Build the Docker image and run it
```bash
    ~$ cd AI-workflow
    ~$ docker build -t capstone-project .
```
Check that the image is there.
```bash
    ~$ docker image ls
```
Run the container
```bash
docker run -p 4000:8080 capstone-project
```
## Test the running app
First go to [http://0.0.0.0:4000/](http://0.0.0.0:4000/) to ensure the app is running and accessible.

For training the model: [http://0.0.0.0:4000/train](http://0.0.0.0:4000/train)

For making predictions using the model: [http://0.0.0.0:4000/predict](http://0.0.0.0:4000/predict)

## Reviewing pointers:

Unit tests for the API: unittests/ApiTests.py

Unit tests for the model: unittests/ModelTests.py

Unit tests for the logging: unittests/LoggerTests.py

Run all of the unit tests with a single script: run-tests.py

Read/write unit tests are isolated from production models and logs

APIs for training and prediction: /app.py

Data ingestion automation pipeline: /cslib.py

Multiple models comparison: notebooks/

EDA investigation with visualizations: notebooks/data_ingestion_eda_part1.ipynb

Containerization within a working Docker image: /Dockerfile

Visualization to compare the model to the baseline model: notebooks/time_series_iteration.ipynb