LLMsAPI


For poetry

```bash
poetry run uvicorn main:app --reload
```
Fir non poetry

```bash
uvicorn main:app --reload
```
### FastAPI Chatbot API with Language Models

#### Introduction
This project is about building an API using FastAPI, which allows users to have text-based conversations with a Language Model. Language Models, like GPT-3, can generate human-like text based on the input provided, making it an interesting tool for various applications, including chatbots.

#### Technologies Used
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
- Language Model (e.g., GPT-3): Used to generate responses to user queries.
- Python: The programming language used for the development.

#### Features

##### API Endpoints
1. **POST /chat**: This endpoint accepts user input and returns the model's response. Users can initiate a conversation by sending a message.

    Example Request:
    ```json
    POST /chat
    {
        "message": "Hello, can you tell me a joke?"
    }
    ```

    Example Response:
    ```json
    {
        "message": "Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!"
    }
    ```

2. **GET /docs**: FastAPI automatically generates interactive API documentation using Swagger UI. Users can explore the API and test it using this interface.

##### Authentication
To protect access to the API and manage usage, API key authentication or other authorization mechanisms can be implemented.

#### How to Run
1. Clone the repository:
   ```shell
   git clone <repository-url>
   cd fastLLMs-api
