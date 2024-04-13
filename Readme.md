# Backend

## Deployment of Backend Application

### Prerequisites
- Python3 installed

### Installation Steps
1. [Download Python3](https://www.python.org/downloads/) installer and install.
2. After installation, navigate to the base directory of the application.
3. Install required Python libraries using the following command:
    ```
    cd Backend
    python3 -m pip install -r requirements.txt
    ```

### Running the Backend API
1. Navigate to the Backend directory.
2. Run the following command:
    ```
    cd Backend
    python3 manage.py runserver
    ```
3. The application will start running on port localhost:8000.

# Frontend

## Setting up Frontend Application

### Prerequisites
- npm installed

### Installation Steps
1. Follow the steps in [installing Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
2. Navigate to the Frontend directory.
3. Install dependencies using the following command:
    ```
    cd Frontend
    npm install
    ```

### Running the Frontend Application
1. Navigate to the Frontend directory.
2. Run the following command:
    ```
    cd Frontend
    npm run serve
    ```
3. The application will start running on localhost:8080.

### Testing the Application
Open http://localhost:8080 in your browser to check and test the features.
