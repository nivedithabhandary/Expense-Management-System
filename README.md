# README #

Client-side sharding for the expense management application

### Files included ###
* Application instances (app.py, app2.py, app3.py) are run on ports 5001, 5002, 5003 which have their own MySQL instance (model.py, model2.py, model3.py).
* ConsistentHashRing.py file has logic to add a node, delete node and get node details.
* The router.py file is run on port 5000. It recieves all incoming POST and GET request from clients and routes it to different server instances running on ports 5001, 5002, 5003 by calling ConsistentHashRing APIs. The router.py file has **return r.text +"\n"+ r.url** as return statement for POST and GET. r.url has the hostname of the server which is sending response for request.
* Screenshots of Postman requests and DB instances are present in Screenshot folder for verification.

### GET /v1/expenses/{expense_id} outputs ###
| {expense_id}     							| RESPONSE      | 
| ------------- 							|:-------------:| 
|1|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 1, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5002/v1/expenses/1  |
|2|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 2, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5003/v1/expenses/2  |
|3|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 3, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5001/v1/expenses/3  |
|4|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 4, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5001/v1/expenses/4  |
|5|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 5, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5003/v1/expenses/5  |
|6|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 6, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5001/v1/expenses/6  |
|7|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 7, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5001/v1/expenses/7  |
|8|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 8, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5003/v1/expenses/8  |
|9|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 9, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5001/v1/expenses/9  |
|10|{"category": "training", "status": "pending", "link": "http://www.apple.com/shop", "name": "do2", "decision_date": "09-08-2016", "submit_date": "09-08-2016", "description": "iPad", "id": 10, "estimated_costs": 700.0, "email": "foo@bar.com"} http://127.0.0.1:5003/v1/expenses/10  |

### Conclusion ###
* From the above GET responses, we see that the requests are consistently distributed between the 3 application instances. 

| Server        | Number of requests recieved           | 
| ------------- |:-------------:| 
| http://127.0.0.1:5001       | 5 | 
| http://127.0.0.1:5002      | 1      |
| http://127.0.0.1:5003 | 4      |