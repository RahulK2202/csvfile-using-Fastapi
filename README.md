# csvfile-using-Fastapi

This project demonstrates a FastAPI backend with a frontend using Jinja templates. Users can upload a CSV file, map the Name and Age columns on the frontend, and submit the file. 
The data from the CSV file is then saved in an SQLite database.

- **File Upload:** Users can upload a CSV file through the web interface.
- **Data Saving:** Submitted CSV data is stored in an SQLite database.
- **Duplicate Handling:** Existing data is checked to avoid duplicates in the database.

1. Create a virtual environment and install dependencies:

  cd CSV-data-saving-Using-FAST-API
python -m venv myenv
.\myenv\Scripts\activate  # On Windows
pip install -r requirements.txt

2. Run the FastAPI application:

uvicorn main:app --reload



