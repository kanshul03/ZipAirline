# ZipHr

### Problem Statement - 
The assignment is to create and submit a working digital version of the aircraft passenger capacity issue, ZipAirlines, along with instructions to run the code. Solution should be in Python. More detailed requirements are listed below.

### Requirements -
##### We are creating a new software for a airline company called “ZipAirlines”.
    * The company is assessing 10 different airplanes.
    * Each airplane has a fuel tank of (200 liters * id of the airplane) capacity. For example, if the airplane id = 2, the fuel tank capacity is 2*200 = 400 liters.
    * The airplane fuel consumption per minute is the logarithm of the airplane id multiplied by 0.80 liters.
    * Each passenger will increase fuel consumption for additional 0.002 liters per minute.

##### Write a RESTful API using Django Rest Framework to:
    * Allow for input of 10 airplanes with user defined id and passenger assumptions
    * Print total airplane fuel consumption per minute and maximum minutes able to fly



## Running RESTful API - 
1. Download/clone the porject/repository.
2. Open command prompt(cmd) in the project folder directory.
3. run the following commands - 
    +  __pip install -r requirements.txt__
    + __python manage.py makemigrations__
    +  __python manage.py migrate__
    +  __python manage.py runserver__
4. Open - __http://127.0.0.1:8000/airplanes/__  in browser/insomnia/postman to get/post/put/delete data on the rest api.



## Running Unittests - 
1. Open command prompt in project directory.
2. run following command - 
      + __python manage.py test__
 
 
 ## Checking unittest coverage - 
1. Open command prompt in project directory.
2. run following command - 
      + __coverage run --source='.' manage.py test__
