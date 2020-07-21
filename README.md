## Masters India assignment

## Backend
- It is written in Python3 with Django & Django rest framework. The project name is **eshop** and app name is **store**.


### APIS:
- List category api
- Create category api (Not part of assignment)
- List subcategory api
- Create subcategory api (Not part of assignment)
- List product api
- Create product api

##### Install instruction
- $ git clone https://github.com/rishikant42/mastersindia

- $ cd mastersindia/backend/eshop/

##### Create virtual env & Install dependencies:
- $ virtualenv --python=/usr/bin/python3.6 env

- $ source env/bin/activate

- $ pip install -r requirements/production.txt

##### DB setup
- Using default django default SQLite DB.


- Apply migration to DB ` $ python manage.py migrate`

##### Run test cases
- *Unit tests* are written for each api.
- $ python manage.py test

##### Load test data in DB & run runserver
- $ python manage.py loaddata testdata.json

- $ python manage.py runserver

### Examples

##### List all category

```
$ curl http://127.0.0.1:8000/api/store/categories/ | json_pp

{
   "previous" : null,
   "count" : 2,
   "results" : [
      {
         "uid" : "c311292b-7958-4985-9333-b120c2a3bbee",
         "name" : "Electronics"
      },
      {
         "uid" : "c32af9e3-9efc-48cd-947e-a48388fa4da4",
         "name" : "Sports"
      }
   ],
   "next" : null
}
```

##### Create new category
```
$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/store/categories/ -d '{"name":"Clothes"}' | json_pp

{
   "name" : "Clothes",
   "uid" : "52cc463d-6fb2-4d68-8d65-74fabc9d4ceb"
}
```

##### List all subcategory
```
$ curl http://127.0.0.1:8000/api/store/subcategories/?limit=2 | json_pp

{
   "results" : [
      {
         "name" : "Headphones",
         "category" : {
            "name" : "Electronics",
            "uid" : "c311292b-7958-4985-9333-b120c2a3bbee"
         },
         "uid" : "95609eae-d793-45c6-816a-dedb96e147ca"
      },
      {
         "name" : "Laptop",
         "uid" : "78cace76-0442-46da-ba64-4b5ab1711126",
         "category" : {
            "name" : "Electronics",
            "uid" : "c311292b-7958-4985-9333-b120c2a3bbee"
         }
      }
   ],
   "next" : "http://127.0.0.1:8000/api/store/subcategories/?limit=2&offset=2",
   "previous" : null,
   "count" : 8
}
```
##### Create new subcategory
```
$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/store/subcategories/ -d '{"name":"Earphone", "category_uid": "c311292b-7958-4985-9333-b120c2a3bbee"}' | json_pp

{
   "name" : "Earphone",
   "uid" : "5ab3c064-6432-4b26-adf9-fc5f231af609",
   "category" : {
      "name" : "Electronics",
      "uid" : "c311292b-7958-4985-9333-b120c2a3bbee"
   }
}
```

##### List product
```
$ curl http://127.0.0.1:8000/api/store/products/?limit=2 | json_pp

{
   "next" : "http://127.0.0.1:8000/api/store/products/?limit=2&offset=2",
   "count" : 15,
   "results" : [
      {
         "name" : "Acer volte",
         "uid" : "d423cb63-6506-449f-b1b5-aeda8430c750",
         "subcategory" : {
            "category" : {
               "name" : "Electronics",
               "uid" : "c311292b-7958-4985-9333-b120c2a3bbee"
            },
            "name" : "Laptop",
            "uid" : "78cace76-0442-46da-ba64-4b5ab1711126"
         }
      },
      {
         "name" : "Dell XPS",
         "uid" : "53f3dd8f-3a9f-459e-a671-d1b03cf6c20c",
         "subcategory" : {
            "name" : "Laptop",
            "uid" : "78cace76-0442-46da-ba64-4b5ab1711126",
            "category" : {
               "uid" : "c311292b-7958-4985-9333-b120c2a3bbee",
               "name" : "Electronics"
            }
         }
      }
   ],
   "previous" : null
}
```

##### Create new product
```
$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/store/products/ -d '{"name":"Acer 2", "subcategory_uid": "78cace76-0442-46da-ba64-4b5ab1711126"}' | json_pp 

{
   "name" : "Acer 2",
   "subcategory" : {
      "uid" : "78cace76-0442-46da-ba64-4b5ab1711126",
      "name" : "Laptop",
      "category" : {
         "uid" : "c311292b-7958-4985-9333-b120c2a3bbee",
         "name" : "Electronics"
      }
   },
   "uid" : "c85d5d67-b6a8-4d4b-b2d9-cb45d26b5e74"
}
```
## Frontend
- Frontend is written in **VueJs** framework.

##### Install instruction
- $ https://github.com/rishikant42/mastersindia

- $ cd mastersindia/frontend/eshop

- npm install

##### Start frontend dev server
- $ npm run serve

##### Screenshot

![screenshot](https://github.com/rishikant42/mastersindia/blob/master/Screenshot.png?raw=true)
