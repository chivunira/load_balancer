# Load Balancer Project

This project contains a load balancer implemented in Docker using an Ubuntu image.

## Design Choices
### Architecture
- **Flask**: Selected for its simplicity and lightweight nature, making it ideal for building straightforward web servers with minimal overhead.
- **Docker**: Utilized to containerize server instances and the load balancer, ensuring consistent environments across different development and production setups.
- **Docker Compose**: Used for orchestrating multiple containers, defining their interactions and connectivity, which simplifies deployment and scaling.

### Components
- **Server Instances**: Consists of three server containers (`server1`, `server2`, `server3`), each running a Flask application that responds with a unique identifier (`SERVER_ID`).
- **Load Balancer**: A separate Flask application that uses a round-robin algorithm to distribute requests among the server instances.

## Assumptions
- **Homogeneous Servers**: Each server instance has identical capacity and performance capabilities.
- **Stateless Servers**: No session information is maintained between requests, allowing for unrestricted request routing.
- **Network Stability**: Assumes reliable network communication between the load balancer and servers.
- **Local Traffic**: All requests to the load balancer are presumed to be sent from local clients within the same network or machine, primarily for testing and initial deployment phases.

## Perfomance Analysis
