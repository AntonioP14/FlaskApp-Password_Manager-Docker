# Password Manager Web Application

## Overview
This repository contains a password management web application built using Flask and Docker. The application allows users to securely store and manage their passwords, leveraging Flask for the web framework and SQLAlchemy for database interactions.

## Features
- User-friendly interface for password management
- Secure password storage
- User authentication
- Containerized using Docker for consistent deployment

## Project Structure

FlaskApp-Password_Manager-Docker/
│
├── .github/
  │ └── workflows/
    ci.yml
    
├── app/

  │ ├── init.py
  │ ├── models.py
  │ ├── routes.py
  │ └── templates/
  │ └── index.html

├── instance/

├── tests/

  │ ├── test_routes.py
  
  │ └── init.py

├── .flake8
├── docker-compose.yaml
├── Dockerfile
├── README.md
├── requirements.txt
└── run.py


## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/AntonioP14/FlaskApp-Password_Manager-Docker.git
    ```
2. Navigate to the project directory:
    ```sh
    cd FlaskApp-Password_Manager-Docker
    ```
3. Build and start the Docker containers:
    ```sh
    docker-compose up --build
    ```

## Usage
- Access the web application at `http://localhost:5000`.
- Add, view, and manage passwords through the user interface.
