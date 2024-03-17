# Cat-Hero-Idle-RPG-Tools-Backend

This is the backend for a website designed to provide tools, guides, and more for Cat Hero Idle RPG. Below is a comprehensive guide on setting it up locally, including prerequisites, steps for initial setup, database configuration, migration, and creating an admin user.

## Prerequisites
- Python 3.x
- pip (Python package installer)
- Virtual environment (recommended)

## Setup Instructions

1. **Clone the repository**:  
   `git clone https://github.com/AcclaimedAP/Cat-Hero-Idle-RPG-tools-backend.git`
2. **Navigate to the project directory**:  
   `cd Cat-Hero-Idle-RPG-tools-backend`
3. **Create and activate a virtual environment** (optional but recommended):  
   - Linux/macOS: `python3 -m venv venv && source venv/bin/activate`
   - Windows: `python -m venv venv && .\venv\Scripts\activate`
4. **Install dependencies**:  
   `pip install -r requirements.txt`

## Environment Configuration
- Copy `.env.example` to a new file named `.env` and fill in the necessary values.

## Database Setup
- Ensure your database is running and accessible.
- Update the database configurations in your `.env` file accordingly.

## Apply Migrations
- Run `python manage.py migrate` to apply database migrations.

## Creating an Admin User
- To create an admin user, execute `python manage.py createsuperuser` and follow the prompts.

## Running the Project
- Start the server with `python manage.py runserver`.
- The backend will now be accessible at `http://127.0.0.1:8000/`.

## Additional Information

### Running Tests
- Execute `pytest` or `python manage.py test` to run tests.