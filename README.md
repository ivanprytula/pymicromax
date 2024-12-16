# PyMicroMax

Project about the journey of learning, experimenting, and mastering tech stacks for cloud-native microservices.
Starting with Python frameworks and tools. Future - add more frameworks and tools.

## Project Structure

```text
project-root/
│
├── microservices/
│   ├── backend/            # FastAPI-based public/private APIs
│   ├── admin_panel/    # Django-based admin panel
│   ├── data_pipelines/            # Flask-based data pipelines
│   ├── data_visualizations/      # Streamlit-based dashboard/visualization
│
├── shared/
│   ├── auth/       # Shared Python libraries (e.g., authentication)
│   ├── libs/       # Shared Python libraries (e.g., logging, error_handling)
│   ├── contracts/  # API contracts (e.g., OpenAPI specs)
│   ├── models/     # Shared Pydantic/Django models or schema definitions
│   ├── utils/      # Shared Python libraries (e.g., utilities)
|   |── data_processing/           # Shared data processing logic (ETL transformations)
│   ├── message_broker/            # Kafka/RabbitMQ message producers and consumers
│
├── infra/
│   ├── docker/     # Dockerfiles for services
│   ├── k8s/        # Kubernetes manifests and Helm charts
│   ├── iac/        # Terraform IaC for cloud resources
|   |── config_management /  # TODO:
│
├── cicd/           # CI/CD pipelines
│   ├── .github/
|       ├── workflows/   # GitHub Actions workflows
|               ├── ci.yml
|               ...
|
│
├── docs/           # Documentation for APIs, architecture, workflows
│
└── scripts/        # Utility scripts (e.g., for data seeding, setup)
```

## Web Platform Stack Overview

1. Python Frameworks for Microservices
   1. Django: For building monolithic or admin panel-based services. Use Django REST Framework (DRF) for API development and Django ORM for interacting with SQL databases.
   2. Flask: Lightweight framework for creating microservices. Good for smaller services where you don’t need the overhead of Django.
   3. FastAPI: High-performance framework for APIs. Great for building asynchronous microservices with automatic OpenAPI documentation.
   4. Streamlit (Optional): For quickly creating data-driven, interactive web apps, suitable for building dashboards.
2. Database Solutions
   1. SQL Databases:
      1. PostgreSQL: Powerful open-source relational database, great for handling complex queries and large datasets.
      2. MySQL: Another widely used open-source relational database for high-performance applications.
   2. NoSQL Databases:
      1. MongoDB: NoSQL database for handling semi-structured data, good for microservices with varying data schemas.
      2. Redis: For in-memory data storage, caching, and message brokering.
3. Message Brokers and Event-Driven Communication
   1. RabbitMQ: Open-source message broker for handling asynchronous tasks and communication between services.
   2. Apache Kafka: Distributed event streaming platform, useful for high-throughput, fault-tolerant data streaming between microservices.
4. Containerization and Orchestration
   1. Docker: For creating containers to run your microservices locally and in the cloud.
   2. Docker Compose: To manage multi-container Docker applications, ideal for local service orchestration.
   3. Kubernetes: For orchestrating and managing containerized applications in production (cloud or on-premise).
      1. Helm: Package manager for Kubernetes, helps with deploying apps and managing Kubernetes resources.
5. DevOps Tools
   1. Terraform: For Infrastructure as Code (IaC), managing and provisioning cloud resources (VMs, databases, etc.).
   2. Ansible: For automating server configuration and deployment tasks.
   3. CI/CD Tools:
      1. GitLab CI or GitHub Actions: For automating testing, building, and deployment pipelines.
      2. Jenkins: Open-source automation server for continuous integration and delivery.
   4. Prometheus: For monitoring services and creating alerting rules.
   5. Grafana: For visualizing Prometheus metrics and monitoring microservices.
6. Authentication and Authorization
   1. OAuth2 / OpenID Connect: Use OAuth2 for secure API authentication. For managing user roles and permissions, JWT (JSON Web Tokens) is commonly used.
   2. Authlib: Python library for implementing OAuth2.0 in your applications.
   3. Keycloak: Open-source Identity and Access Management tool, supports Single Sign-On (SSO) and RBAC.
7. API Documentation
   1. OpenAPI/Swagger: Use FastAPI’s automatic OpenAPI generation, or use drf-spectacular for Django.
   2. Redoc: For presenting your OpenAPI specs in an easily readable format.
   3. Swagger UI: For testing APIs and generating documentation.
8. Logging and Monitoring
   1. ELK Stack (Elasticsearch, Logstash, Kibana): For aggregating, searching, and visualizing logs.
   2. Fluentd: For log aggregation and forwarding logs to different destinations like Elasticsearch.
   3. Sentry: For application error monitoring and logging.
9. Frontend Frameworks
   1. React or Vue.js: JavaScript libraries for building responsive frontends, useful for dashboards and admin interfaces
   2. TailwindCSS: A utility-first CSS framework for rapid UI development.
10. Cloud-Native Transition Tools: For when you transition to the cloud, these tools will allow for a smoother migration from open source to cloud-native services:
    1. AWS (Amazon Web Services), Azure, or Google Cloud Platform: Start with any provider that offers the services you need for compute, storage, and networking.
       1. Elastic Kubernetes Service (EKS) or Google Kubernetes Engine (GKE) for Kubernetes orchestration.
       2. CloudWatch (AWS) or Stackdriver (GCP) for monitoring cloud infrastructure.
       3. RDS (AWS) or Cloud SQL (GCP) for fully managed databases.
    2. Serverless Options:
       1. AWS Lambda or Azure Functions for running code without provisioning servers, great for microservices and event-driven workflows.
11. Infrastructure Monitoring and Observability
    1. Jaeger or OpenTelemetry: For distributed tracing, helping to monitor and analyze performance issues in a microservices environment.
    2. Datadog: Cloud monitoring and observability platform (can also be used for local setups).
12. Local Development Tools
    1. Postman: For testing and documenting your APIs locally.
    2. Docker Desktop: To run Docker containers locally.
    3. Minikube or K3d or k3s: Lightweight Kubernetes clusters for local development.

## Centralized Authentication

To streamline user authentication across our microservices architecture, we have implemented a centralized authentication service. This service acts as a single point for user authentication, handling user login, token generation, and validation. By centralizing authentication, we ensure a consistent and secure approach to managing user access across all services.

## Additional Authentication for Microservices

While the centralized authentication service provides a robust mechanism for user authentication, each microservice can implement its own additional authentication mechanisms as needed. This allows for specific security requirements or access controls to be enforced at the microservice level, enhancing the overall security posture of our application.

## Git Branching Strategy Overview

The key is to maintain a single repository's branching model where the overall codebase reflects the current development cycle, and each microservice or shared component lives within the same branches.

1. Main Branches:
   1. `main`: Always production-ready, deployable code.
   2. `dev`: Active development. All new features and bug fixes are merged here before staging and production.
2. Feature Branches:
   1. For each new feature, create a branch like `feature/<feature-name>` where `<feature-name>` is related to the specific feature or change you’re working on (e.g., `feature/service1-auth`).
   2. These branches will primarily affect the corresponding microservice's directory but can also involve changes in the shared libraries if necessary.
3. Hotfix Branches:
   1. For urgent fixes, create a `hotfix/<issue-id>` branch based off the master branch. This is useful for patching live issues.
4. Release Branches:
   1. For preparing releases, you can have a branch like `release/<version-number>` which is stable and ready for deployment.
5. Directory-Specific Considerations:
   1. Shared libraries (e.g., `shared/auth`): If changes in these shared components affect multiple microservices, feature branches related to these can also exist, such as `feature/shared-auth`.
   2. Terraform: Infrastructure changes can follow the same process, such as `feature/terraform-update`. This allows you to deploy infrastructure changes in parallel with service features.

### Shell commands heap

TODO: sort later

### Development

```shell
# Enter needed microservice directory
docker compose up --build


# option 1: automatically grabs compose.yaml and compose.override.yaml files
docker compose watch

# option 2: implicit set
docker compose -f compose.yaml -f compose.admin.yaml run backup_db


```

Generate Secret Keys

```shell
python -c "import secrets; print(secrets.token_urlsafe(32))"
export POSTGRES_PASSWORD=$(echo "pymicromax-password" | openssl passwd -6 -stdin)
```

#### Init DB scripts

Behavior Explanation:

- Volume `app-db-data`: This stores the database data persistently. If this volume already exists, initialization scripts won't run again unless the volume is deleted.
- Initialization Scripts: Any `.sql` or `.sh` script in /docker-entrypoint-initdb.d will execute only during the first startup of the container (if the data directory is empty).
- Check for Database: The SQL script ensures the database is created only if it doesn't already exist.

```shell
docker compose down
docker volume rm <project_name>_app-db-data
docker compose up
```
