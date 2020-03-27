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

___

## Running RESTful API - 
1. Download or clone the repository.
2. Open command prompt(cmd) in the project folder directory.
3. run the following commands - 
    +  __pip install -r requirements.txt__
    + __python manage.py makemigrations__
    +  __python manage.py migrate__
    +  __python manage.py runserver__
4. Open - __http://127.0.0.1:8000/airplanes/__  in browser/insomnia/postman to use get/post services.
   
   **OR**
      
   __http://127.0.0.1:8000/airplanes/< int:airplane_id >__   -  in browser/insomnia/postman to use get/put/delete services for a specific airplane using its airplane_id. Click [here](http://127.0.0.1:8000/airplanes/1) to open example url.

___

## Running Unittests - 
1. Open command prompt in project directory.
2. run following command - 
      + __python manage.py test__
 
 ___
 
 ## Checking unittest coverage - 
1. Open command prompt in project directory.
2. run following command - 
      + __coverage run --source='.' manage.py test__
      
___


### Libraries required - 
   + Django
   + djangorestframework
   + coverage
   
___

### About the project - 
+ Django Rest Api
+ Supports get/post/put/delete operations.
+ get operation can be used to view all the airplanes in db or to view the details of a single airplane. To view the all the airplanes use get request on [this](http://127.0.0.1:8000/airplanes/) url, otherwise insert airplane id in the last of the same url and use get service to get details of a specific airplane.
+ Supports using post service for single as well as multiple airplanes, i.e, either we can send a single airplane's data or we can send say 10 airplane's data altogether.
+ Standard json format prefferd while sending data.
+ Partially updating a record is possible, i.e, we can use put request with airplane id in the browser with only the data details to be changed to change the data of that airplane. Eg we just want to change the passenger number for an airplane having airplane id = 6, we can easily do that by just opening [this](http://127.0.0.1:8000/airplanes/6) url and sending data {'passengers': 6}.
