# Boiler plate for Fast API

Experimenting with deployments on the model

Contains:

- hello world, located at [hello_world.py](hello_world.py)
- restful api, located at [restful_api.py](restful_api.py)
- you can get the machine learning model at [model](https://drive.google.com/file/d/1U5B9TSl6RXTBzL6mXsMwE2sbpeMMVnZI/view?usp=sharing)

## How to run

1. Install the necessary libraries located at [requirements.txt](requirements.txt)
2. Run the file with `uvicorn [filename]:app --reload`
3. Experiment with it

Examples:

1. To run the [hello world app](hello_world.py)

   ```bash
   uvicorn hello_world:app --reload
   ```

2. To run the [restful api app](restful_api.py)

   ```bash
   uvicorn restful_api:app --reload
   ```

You will obtain an output similar to this:

```bash
Will watch for changes in these directories: ['E:\\Projects\\try-deploying-model']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7640] using WatchFiles
INFO:     Started server process [16504]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Then you can open the browser and receive an output:

```javascript
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
