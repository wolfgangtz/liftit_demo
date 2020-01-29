# LIFTIT Demo - Backend Test

---

This repository have the resolution of the backend test in liftit.

## What Need you to run this project ?

In order to run locally this project, you need to have installed in your laptop this:

- Docker
- Virtualenv
- Postgres
- python 3.6

## What I will found in this project?

in this project, also the resolution of the probe, you will found:

- Swagger documentation about the API.
- Frontend Demo, where you will probe the resolution of this project.
- A CSV example File
- A docker compose file, which will help you to run this project.

## How Work this project?

To solve the async comunication, this project use channels to stablish a websocket comunication between the frontend and the backend, aditionally, we have celery, which together with redis, will help us to queue the processing CSV task, once the process finish, using channels will notify to the frontend the result and the information, for the other hand, this project use a postgres database where we can see the information.

## What is the structure of the local models?

well, in order to have all the trasability and that not do this test so big, I use two models (please see the attached image in repo) invoices and files, where one file can have so much invoices related (one to many). The model file have the name of the CSV and total item (related on each invoice) price amount, the model invoices have all the fields that must to have a invoices and was appinted on the test papper.

aditional of the previous tables, this project was made with Django, and is available with the admin and user features, for that reason you will see more tables which can improve the project but I not work with that because is not in the test scope.

## How run this project?

well, initially tou need to clone the repo and create a virtualenv which will help the project to run, to do this run this commands:

```bash
cd project-destination-path
git clone https://github.com/wolfgangtz/liftit_demo.git
virtualenv -p python3 venv
```
until this step, we will have the virtualenv created and the repository cloned, now, we need to turn on the virtualenv and install here the requeriments of the project:

```bash
source source venv/bin/activate
cd liftit_demo
pip install -r requeriments.txt
```

finally, run the project using docker-compose:

```bash
docker-compose build
docker-compose up
```

## Stuff to see in this project

I believe that you want to tee this project in action, well, please visit this [url](http://localhost:5000/) once the project is running, here, you will see a frontend demo that work together with the backend. Please use the attached CSV file (sales.csv) to probe the logic of the backend, the validations that we do with this project is:

- The Headers names (pleas ebe carefull to use ; delimiter to the CSV file if you want to use your own CSV test file).
- The parser process of the CSV should be done.
- The uploade file must be a CSV file.
- The request must to have a session name expecificated (this session name will be used to identify the channel that will be use to notify the result of the process).

after pre previous mentinated validation, the backend will queue the process and return a celery task_id and a 200 status in the HTTP response, something like this:

```bash
{
	message: "File in process",
	task_id: "acee9649-35cd-44e0-ade0-531b2c426c0f"
}
```

the previous response say us that the task was queue correctly, once the celery workers finish the process, and using the session_name, we notify via websocket to the frontend the response, fi the response was ok you can receive something like this:
```
[ 
   true,
   [ 

   ],
   { 
      "id":"ae0e5e7b-ec83-4593-a076-95e29c8e0051",
      "filename":"sales.csv",
      "total_items_price":"570000.00000",
      "created_at":"2020-01-29T16:23:00.916768Z",
      "updated_at":"2020-01-29T16:23:00.997408Z",
      "invoices":[ 
         { 
            "id":"915f298d-0d80-4f62-9237-aa38f47f21dd",
            "invoice_number":"456",
            "client_name":"michellys",
            "client_lastname":"vargas granados",
            "client_id":"1065603249",
            "item_code":"101",
            "item_description":"camisas de fiesta",
            "item_amount":"2.00000",
            "item_price":"320000.00000",
            "item_discount_rate":"15.00000",
            "file":"ae0e5e7b-ec83-4593-a076-95e29c8e0051",
            "created_at":"2020-01-29T16:23:00.992140Z",
            "updated_at":"2020-01-29T16:23:00.992412Z"
         },
         { 
            "id":"6847a492-65d9-4e4e-a9bc-516dcb25785f",
            "invoice_number":"123",
            "client_name":"wolfgang enrique",
            "client_lastname":"gutierrez barrera",
            "client_id":"1065630838",
            "item_code":"100",
            "item_description":"zapatillas deportivas",
            "item_amount":"1.00000",
            "item_price":"250000.00000",
            "item_discount_rate":"20.00000",
            "file":"ae0e5e7b-ec83-4593-a076-95e29c8e0051",
            "created_at":"2020-01-29T16:23:00.969927Z",
            "updated_at":"2020-01-29T16:23:00.970029Z"
         }
      ]
   }
]
```
the previous response always will have the next structure [status, errors array, response] at least that the response hace a error, in this case the response will be [status, errorr] for example:

```
[false,"Wrong Headers"]
```

another posible response is that the process finished ok but we found mistakes in some line of the CSV file, in this case, we will sate which line was and what was the problem, for examle:

```
[ 
   true,
   [ 
      { 
         "error_line":2,
         "error_description":"The file sales.csv is corrupt, validate file on line 2",
         "error_capturated":{ 
            "item_discount_rate":[ 
               "A valid number is required."
            ]
         }
      }
   ],
   { 
      "id":"4e7ba80e-3d77-484e-8857-62dadf94900d",
      "filename":"sales.csv",
      "total_items_price":"320000.00000",
      "created_at":"2020-01-29T16:26:47.240342Z",
      "updated_at":"2020-01-29T16:26:47.274135Z",
      "invoices":[ 
         { 
            "id":"5ece880b-8449-45ed-b2f4-b616bdd649ae",
            "invoice_number":"456",
            "client_name":"michellys",
            "client_lastname":"vargas granados",
            "client_id":"1065603249",
            "item_code":"101",
            "item_description":"camisas de fiesta",
            "item_amount":"2.00000",
            "item_price":"320000.00000",
            "item_discount_rate":"15.00000",
            "file":"4e7ba80e-3d77-484e-8857-62dadf94900d",
            "created_at":"2020-01-29T16:26:47.270201Z",
            "updated_at":"2020-01-29T16:26:47.270262Z"
         }
      ]
   }
]
```
We can have several problem in some lines of the CSV for that reason we use a array to save the errors.
another interesting thing to see is the swagger  documentation, where you can see the API and seee interesting information, to see this docs click [here](http://localhost:5000/swagger/) (make sure to have your project run).

## Nice to have

This is a list of stuff that be cool to have in this demo, however, is not in the test scope:
- Authentication services to protect the API.
- Save the session_name on database, this name is the room name where the frontend is connected.
- Implement a changelog.
- Implement logger.
- Implement multi-lenguage
- have a better look and feel in the frontend demo page.

## Why you should hire me?

well, I'm convinced that the real important things in a employed is not the technical skill (obiously the employed need to have a minimun skills) instead of this is better to have somenone that can adapt quicly to the changes, with a positive actitude, someone who will not give you problems but solutions, someone that learn quickly, someone that can work in teamwork's, someone leader and cnad work under pressure, and I believe that I have all this aditional skills. Thanks for let me participate in this process and I hope that we can work together in liftit.

If you have any doubts about this project, or the propoused solution, please don't hesitate in contact me ! ... 