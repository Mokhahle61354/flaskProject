# Documentation

- Run the app.
  1) Using pipenv
    ```
    # first time use, or if virtualenv is not exit
    pipenv install
    
    # the activate pipenv and run flask app
    pipenv shell 
    sh run.sh
    ```
  2) Docker
    ```
    docker build .
    ```
    
    
- Accessing function over http.
  
  url has form of:
    ``http://localhost:port/{commands}/{address}```
  
  list of commands:
    - description 
    - +description 
    - distance
    - enclosed
