# Boiler plate for Fast API

Experimenting with deployments on the model

Contains:

- hello world, located at [hello_world.py](hello_world.py)
- restful api, located at [restful_api.py](restful_api.py), source from [chuck's](https://github.com/chuck1z) [**repository**](https://github.com/chuck1z/deploy-model)
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

#### Note that you need to have model.h5 to run this api

You can get it through this [link](https://drive.google.com/file/d/1U5B9TSl6RXTBzL6mXsMwE2sbpeMMVnZI/view?usp=sharing) or run the [download.py](download.py) file

Note that you should name your model with `model.h5` or simply change the model path in the script

```bash
uvicorn main:app --reload
```

You will obtain an output similar to this in the console:

```text
INFO:     Will watch for changes in these directories: ['E:\\Projects\\try-deploying-model']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [10712] using StatReload
2023-04-19 03:25:13.691430: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-19 03:25:14.177428: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-19 03:25:14.230110: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-19 03:25:15.825289: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-19 03:25:15.865302: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
INFO:     Started server process [20704]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

or you can run the code by running `py main.py` in the terminal and you will receive an output similar to this:

```text
2023-04-19 02:58:57.877659: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-19 02:58:58.345451: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-19 02:58:58.397330: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-19 02:58:59.431456: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
2023-04-19 02:58:59.467924: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 160563200 exceeds 10% of free system memory.
INFO:     Started server process [16784]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Then you can open the url in the browser and receive an output:

```json
{
  "Hello": "World"
}
```

To try the API, simply follow these steps:

1. `http://127.0.0.1:8000/docs`, you will get to the documentation page
2. Find the `POST` method and click `Try it out`
3. Input the file which is an image and execute it
4. (Optional) you can use the example input in the [input](input) directory
