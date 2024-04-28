# galatix-test-project

## Development Requirements
* Python 3.11.*
* Docker Compose
* PDM(Python Package Manager)

## How to run
Project can be run using Docker Compose or locally.

### Using Docker Compose
```bash
make docker-build
make docker-start
```

### Local Development
Before running the project, you need to install the dependencies using PDM.

Install PDM by this documentation: https://pdm-project.org/en/latest/#installation

Then run the following commands:
```bash
pdm install --dev  # Install the dependencies for development
```

Then you can run the project using the following command:
```bash
pdm run start
```
## Running Tests
### Using Docker Compose
```bash
make docker-test
```

### Local Development
```bash
make test
```

## API Documentation
API documentation can be found at http://localhost:8000/redoc
