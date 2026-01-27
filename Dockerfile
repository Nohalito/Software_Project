# Shoutout to those guys here : https://docs.streamlit.io/deploy/tutorials/docker
# Advice from admin 1 to admin 2, "va voir le cour du prof c smart" : https://github.com/virgilus/docker/blob/main/02_EXO_My_App.ipynb

# Get python version
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# we get our requirements 1st
COPY requirements.txt .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Since we removed our data from github, we make our user download the data first, then run the app
CMD ["bash", "-c", "python src/download_data.py && streamlit run app/app.py --server.port=8501 --server.address=0.0.0.0"]