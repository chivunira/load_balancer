# Load Balancer Project

This project features a load balancer developed in Docker, utilizing an Ubuntu base image. It leverages consistent hashing to evenly distribute incoming requests across multiple server replicas, enhancing both load distribution and scalability within a distributed system.

## Design Choices

### Architecture
- **Flask**: Chosen for its straightforward and lightweight nature, ideal for crafting simple web servers efficiently.
- **Docker**: Employs containerization to ensure consistent environments for server instances and the load balancer across various stages of development and production.
- **Docker Compose**: Facilitates the orchestration of multiple containers, simplifying deployment and enhancing connectivity and interaction between containers.

### Components
- **Server Instances**: Comprises three server containers (`server1`, `server2`, `server3`), each running a Flask application that outputs a unique identifier (`SERVER_ID`).
- **Load Balancer**: Operates independently with a Flask application that employs a round-robin algorithm for distributing requests among the servers.
- **Consistent Hashing**: Implemented to optimize load distribution across servers.

## Project Structure

- **`Server files`**: 
  - **`Dockerfile`**: Constructs the Docker image for the server replicas.
  - **`app.py`**: Manages server operations, including request handling and heartbeat responses.
- **`Load Balancer files`**: 
  - **`Dockerfile_load_balancer`**: Creates the Docker image for the load balancer.
  - **`load_balancer.py`**: Administers load balancer operations using consistent hashing and request routing.
  - **`consistentHash.py`**: Contains the implementation of the consistent hashing algorithm.
- **`Test file`**:
  - **`test_consistent_hash_map.py`**: Provides tests for validating the consistent hashing algorithm.
- **`Scripts/`**:
  - Hosts scripts designed to test the load balancer by dispatching 10,000 requests and capturing the request handling logs.
- **`docker-compose.yml`**: Specifies the Docker services configuration for both the load balancer and server replicas.

## Load Balancer Functionality

- **Request Routing**: Allocates incoming requests to the corresponding server replica based on the consistent hashing framework.
- **Server Management**: Dynamically adjusts the number of server replicas to scale up or down as required.
- **Fault Tolerance**: Monitors and detects server failures, redistributing loads to maintain operational continuity.
- **Monitoring**: Tracks and reports the status of server replicas through designated endpoints.

## Usage

1. **Build and Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```
    This command constructs the Docker images for the load balancer and server replicas, then initiates the containers.

2. **Access Load Balancer Endpoints**:
    Access the load balancer at `http://localhost:5000`. Utilize these endpoints for management and monitoring:
    - **`GET /rep`**: Retrieves the status of server replicas.
    - **`POST /add`**: Incorporates new server replicas.
    - **`DELETE /rm`**: Removes existing server replicas.

## Assumptions
- **Homogeneous Servers**: Assumes that all server instances possess equivalent capabilities and performance.
- **Stateless Servers**: Servers do not retain session data, allowing for flexible request routing.
- **Network Stability**: Relies on stable network communication between the load balancer and servers.
- **Local Traffic**: Presumes that all interactions with the load balancer originate from local clients within the same network or device, mainly for testing and initial deployment.

## Performance Analysis

The load balancer has undergone extensive testing across various scenarios, including the dynamic addition and removal of servers, and evaluation of request distribution efficacy. Testing results confirm that the load balancer proficiently equalizes the load across server replicas and adapts swiftly to configuration changes.
