# Simple REST API with Flask in Docker

A simple REST API using Flask, dockerized for easy execution in any environment.

## Description

This is a basic Python program using Flask. The application exposes a REST API with a single endpoint (`/`) that responds with a greeting message when accessed via a GET request.

## Technologies Used

- Python 3.9
- Flask
- Docker

## Prerequisites

To run this project, you need to have Docker installed on your machine. If you don't have it, you can download it from [here](https://www.docker.com/products/docker-desktop).

## Instructions to Run the Project

1. **Clone this repository:**

   If you haven't cloned the repository yet, you can do so with the following command:

   ```bash
   git clone https://github.com/your_username/rest_api.git

2. **Build the Docker image:**

   Before running the container, build the Docker image using the following command:

   ```bash
   docker build -t ksrobalino/rest_api:v1 .

3. **Push the image to Docker Hub (if needed):**

   If you'd like to upload the image to Docker Hub for others to use, you can do so with:

   ```bash
   docker push ksrobalino/rest_api:v1

4. **Run the Docker container:**

   After building the image, run the container with the following command:

   ```bash
   docker run -d -p 5000:5000 --name my_container ksrobalino/rest_api:v1

5. **Access the application:**

   Once the container is running, you can access the API in your browser or with tools like Postman, at the following URL:
   ```bash
   http://localhost:5000
   
