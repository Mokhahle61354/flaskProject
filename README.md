# Documentation

- Run the app.
  1: Using pipenv

    ```
      # first time use, or if virtualenv is not exit
      pipenv install
      
      # the activate pipenv and run flask app
      pipenv shell 
      sh run.sh
    ```
  2: Docker
    ```
    docker build .
    ```
    
    
- Accessing function over http.
  
  - url has form of:
  
    ``http://localhost:port/{commands}/{address}```

    eg: http://127.0.0.1:5000/distance%20enclosed/CBD%20CAPE%20town

      - city/address: CBD CAPE town
      - Parameters/commands: distance and enclosed

  - Results:
      ```
        {
          "distance": {
            "distance": 8731.817414524074, 
            "lower_envelope": 8731.66016465223, 
            "unit": "km", 
            "upper_envelope": 8730.249148970079
          }, 
          "enclosed": false
        }
        ```
  
- list of commands:

  - description 
  - +description 
  - distance
  - enclosed


- Generate Sphinx docs

```
sphinx-build -b html source ./docs
```