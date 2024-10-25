# Stage 1: Build Next.js app
FROM node:16 AS frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build Flask app
FROM python:3.8 AS backend
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY backend/ ./

# Set the environment variable for Flask
ENV FLASK_APP=app.py
EXPOSE 5000  # Change this to your Flask app's port

# Start Flask server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
