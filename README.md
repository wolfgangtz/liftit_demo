LIFTIT DEMO

V1:

To complete this test, I believe that we need to analyze the problem, after that define the database struct. The database will have two tables invoces and files, the relation between invoces and files is one to many, the objective of this is save the info about the uploade file (name, total amount of invoices ... ) and obviously the info about the invoce that we CAN SAVE in the database, after this intro, I think in how develop this test, and think in three steps:


- The first step is define how we will comunicate the backend with the frontend, to do that, we will use Channels of Django, therefore, we will stablish a websocket connection with the backend from the frontend. 

- the second step to solve is the data processing, to solve that I'm veirfying if the best choice is use celery, add a task to the backend and thought the workers, process the CSV file, once the processing finished, we will contact the frontend using the channels and send the processed result.

- the third step to solve is the processing of the CSV file and all the validations that we need to do before to save in database, I will search a library to help me to perform the iteration over the CSV file and finally, do the related validations.


the objetive of this document is say the way that I think is the best way to solve this problem, I will update this file among the development of this test.



V2:

The implementation of channels will need to you run redis locally, please, before run the project run this command:

docker run -p 6379:6379 -d redis:2.8

make usre that you have docker installed.