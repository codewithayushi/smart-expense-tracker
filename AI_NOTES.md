# AI Notes

## 1. Which parts of the code were AI-generated vs. written by you
- **AI-Generated:** The foundational structure of the FastAPI application, Pydantic models for request validation, helper functions for reading and writing to the local `expenses.json` file, and the core CRUD API endpoints.
- **Written by You:** Project directory setup, virtual environment configuration (`venv`), debugging test environment import paths, and executing the test suites locally.

## 2. What you validated, tested, or changed in the AI's output, and why
- **Validation:** Tested all API endpoints locally using `pytest` and verified the interactive API documentation via FastAPI's Swagger UI (`/docs`).
- **Changes Made:** Updated data serialization methods to align with Pydantic V2 standards and resolved module import configurations for the test environment to ensure all tests pass successfully.

## 3. Any AI suggestion you decided not to use, and why
- **Database Integration:** The AI initially suggested using SQLite/SQLAlchemy. This was rejected because the project instructions explicitly stated that data can be stored in memory or a local JSON file, keeping the setup lightweight without unnecessary database overhead.
