# Food Order API


## Routes to Implement

| METHOD | ROUTE                           | FUNCTIONALITY            |
|--------|-------------------------------- |---------------------------|
| POST   | /auth/register/                   | Register new user            | All users   |
| POST   | /auth/jwt/create/               | Login user                 |
| POST   | /orders/                        | Place an order|
| GET    | /orders/                        | Get all orders     |   
| GET    | /order/{order_id}/              | Retrieve an order  |      
| PUT    | /orders/{order_id}/             | Update an order     | 
| DELETE    | /orders/{order_id}/             | Delete order     |

## 1. Register New User

- **Method:** `POST`  
- **Route:** `/auth/register/`  
- **Functionality:** Allows new users to create an account in the food delivery system.  
- **Sample URL:** `http://127.0.0.1:8000/auth/register/`  
- **Request Body:**
  ```json
  {
    "username": "ramu",
    "email": "ramu@gmail.com",
    "phone_number": "34803242434",
    "password": "ramu@123"
}
- **Output:**
![Screenshot (12)](https://github.com/user-attachments/assets/2a0236f7-5c66-4bbd-86e4-c5407928b2aa)

## 2. Login User

- **Method:** `POST`  
- **Route:** `/auth/jwt/create/ `  
- **Functionality:** Login to food delivery system.  
- **Sample URL:** `http://127.0.0.1:8000/auth/jwt/create/ `  
- **Request Body:**
  ```json
     {
    
    "email": "admin@gmail.com",
    "password": "admin"
        }
- **Output:**
![Screenshot (13)](https://github.com/user-attachments/assets/9a061fb2-f416-4c7e-abd8-1f76886987a0)


## 3. Post Order

- **Method:** `POST`  
- **Route:** `orders/ `  
- **Functionality:** Post Order  
- **Sample URL:** `http://127.0.0.1:8000/orders/ `  
- **Request Body:**
  ```json
     {
    "food_name": "Cheeseburger",
    "size": "MEDIUM",
    "quantity": 2,
    "order_status": "PENDING"
      }

- **Output:**
![Screenshot (19)](https://github.com/user-attachments/assets/edd0f958-0b97-42da-9f55-6551a2ec147c)


## 4. Get All Orders

- **Method:** `Get`  
- **Route:** `orders/ `  
- **Functionality:** Get all Orders  
- **Sample URL:** `http://127.0.0.1:8000/orders/ `  
- **Output:**
![Screenshot (16)](https://github.com/user-attachments/assets/673acbc2-ebc0-4b10-b40b-40ac5c191475)


## 5. Get Single Order

- **Method:** `Get`  
- **Route:** `orders/id/ `  
- **Functionality:** Get Single Order Details 
- **Sample URL:** `http://127.0.0.1:8000/orders/3/ `  
- **Output:**
![Screenshot (18)](https://github.com/user-attachments/assets/d7bd175e-8715-4e79-83eb-e996c410e441)


## 6. Update Order

- **Method:** `POST`  
- **Route:** `/orders/id/`  
- **Functionality:** Update Order
- **Sample URL:** `http://127.0.0.1:8000/orders/4/`  
- **Request Body:**
  ```json
    {
   "food_name": "Chicken Tikka Masala",
    "size": "MEDIUM",
    "quantity": 2,
    "order_status": "PENDING"
    }

- **Output:**

![Screenshot (20)](https://github.com/user-attachments/assets/2927ec85-0204-45cf-a31f-415d9386f1f5)


## 7. delete Order

- **Method:** `POST`  
- **Route:** `/orders/id/`  
- **Functionality:** Delete Order
- **Sample URL:** `http://127.0.0.1:8000/orders/6/`  
- 

- **Output:**
![Screenshot (21)](https://github.com/user-attachments/assets/fdf8c31a-ffe4-4440-9c36-73ce2daa5d42)






