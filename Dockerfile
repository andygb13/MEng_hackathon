FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port number that the Streamlit app runs on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "nurse_app.py"]
