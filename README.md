# Transcribinoff

Transcribinoff is a service designed to handle the transcription of audio messages from WhatsApp to text. This application leverages the power of FastAPI to provide a robust and efficient solution for converting voice messages into written text.

## Features

- **Audio to Text Conversion**: Transcribe audio messages from WhatsApp into text.
- **FastAPI Integration**: Built using FastAPI for high performance and easy scalability.
- **Automated Testing**: Comprehensive test suite with pytest and coverage reports.
- **Continuous Integration**: CI/CD pipeline using GitHub Actions.

## Installation

To get started with Transcribinoff, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/transcribinoff.git
    cd transcribinoff
    ```

2. **Install dependencies**:
    ```sh
    poetry install
    ```

3. **Run the application**:
    ```sh
    poetry run uvicorn src.transcribinoff.main:app --reload
    ```

## Running Tests

To run the tests, use the following command:
```sh
poetry run pytest
```

## Configuration

The application configuration is managed using `pyproject.toml`. Key configurations include:

- **Python Version**: 3.12
- **Dependencies**: FastAPI, mypy, ruff, uvicorn, pytest-asyncio, pytest-cov, httpx

## CI/CD Pipeline

The CI/CD pipeline is configured using GitHub Actions. The workflow file is located at `.github/workflows/fastapi.yaml` and includes steps for:

- Checking out the code
- Caching the virtual environment
- Setting up Python
- Installing dependencies
- Running tests
- Generating test reports

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or contributions, please contact Moshe Reubinoff at [reubinoff@gmail.com](mailto:reubinoff@gmail.com).
