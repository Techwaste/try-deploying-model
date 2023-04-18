# Boiler plate for Fast API

Experimenting with deployments on the model

Contains:

- hello world, located at [hello_world.py](hello_world.py)
- restful api, located at [restful_api.py](restful_api.py)
- main (predict model api), located at [main.py](main.py)

## How to run

1. Install the necessary libraries located at [requirements.txt](requirements.txt) by using `pip install -r requirements.txt`
2. Run the file with `uvicorn [filename]:app --reload`
3. Experiment with it or open the docs

Examples:

### 1. To run the [hello world app](hello_world.py)

```bash
uvicorn hello_world:app --reload
```

### 2. To run the [restful api app](restful_api.py)

```bash
uvicorn restful_api:app --reload
```

You will obtain an output similar to this in the console:

```text
INFO:     Will watch for changes in these directories: ['E:\\Projects\\try-deploying-model']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7640] using WatchFiles
INFO:     Started server process [16504]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Then you can open the browser and receive an output:

```json
{
  "items": {
    "0": {
      "name": "Apple",
      "price": 9.99,
      "count": 20,
      "id": 0,
      "category": "fruits"
    },
    "1": {
      "name": "Kale",
      "price": 5.99,
      "count": 20,
      "id": 1,
      "category": "vegetables"
    },
    "2": {
      "name": "Orange",
      "price": 1.99,
      "count": 100,
      "id": 2,
      "category": "fruits"
    }
  }
}
```

### 3. To run the [main.py](main.py) sky classification model

To access the model, go to this [link](https://drive.google.com/file/d/1U5B9TSl6RXTBzL6mXsMwE2sbpeMMVnZI/view?usp=sharing), note that you should put your model under the `model/sky_classification.h5` path

```bash
uvicorn main:app --reload
```

You will obtain an output similar to this in the console:

```text
INFO:     Will watch for changes in these directories: ['E:\\Projects\\try-deploying-model']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [5428] using WatchFiles
2023-04-18 13:40:53.408262: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-18 13:40:53.658282: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-18 13:40:53.701145: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-18 13:40:54.383965: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-18 13:40:54.418867: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
Model loaded
INFO:     Started server process [8428]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Then you can open the url in the browser and receive an output:

```json
"go to /docs to try the api"
```

To try the API, simply follow these steps:

1. `http://127.0.0.1:8000/docs`, you will get to the documentation page
2. Find the `POST` method and click `Try it out`
3. Input the file which is an image and execute it
4. (Optional) you can use the example input in the [input](input) directory
