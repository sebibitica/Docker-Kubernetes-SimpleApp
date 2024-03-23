# Simple Flask-Nginx Docker-Kubernetes Project

This project is a simple demonstration of Docker and Kubernetes orchestration, featuring a straightforward web application powered by Flask and Nginx.

## Overview

### The project is divided in two:

- **/docker**: This directory contains the implementation of Docker images. It also includes a docker-compose.yml file for easy deployment of the images.
- **/kubernetes**: This directory contains configuration files for Kubernetes deployment.

### Images used:

- **Backend**: A Flask application serving API endpoints.
- **Frontend**: A static website served by Nginx, consuming data from the Flask backend via API calls.

## Usage

### Docker Images used for this project are on Docker Hub:

- **Frontend**: `sebibitica/frontend:v1.0`
- **Backend**: `sebibitica/backend:v1.0`

#### To run the project locally using Docker Compose:

1. Clone this repository:

   ```bash
   git clone https://github.com/sebibitica/Docker-Kubernetes-SimpleApp
2. Navigate to **Docker-Kubernetes-SimpleApp/docker/** directory

   ```bash
   cd Docker-Kubernetes-SimpleApp/docker
3. Run Docker-Compose command

   ```bash
   docker-compose up --build
4. Go to **localhost** on your web browser

#### Deploying to a Kubernetes Cluster

1. Ensure you have a Kubernetes cluster configured and **kubectl** installed.

2. Clone this repository:

    ```bash
    git clone https://github.com/sebibitica/Docker-Kubernetes-SimpleApp
3. Navigate to the **Docker-Kubernetes-SimpleApp** directory:

    ```bash
    cd Docker-Kubernetes-SimpleApp

4. Apply the Kubernetes configuration files:
    ```bash
    kubectl apply -f kubernetes/

5. Go to **IP_OF_YOUR_KUBERNETES_CLUSTER:30001** on your web browser
