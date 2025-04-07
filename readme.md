# Crop Production Prediction

This project is a web application that predicts crop production based on various input parameters. The application is built using Flask and a trained CatBoost model.

## Deployment

The application is deployed on Render. You can access it using the following link:

[Crop Production Prediction](https://crop-production-prediction-3uq8.onrender.com)

## Contributors

- Utakrsh Rai
- Keshav Agrawal

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Fill in the form with the required input parameters.
3. Submit the form to get the crop production prediction.

## Project Overview

The Crop Production Prediction project is a web application designed to predict crop production based on various input parameters. The application uses a machine learning model (CatBoost) to make predictions. Users can input details such as crop type, crop year, season, state, area, annual rainfall, fertilizer usage, and pesticide usage. The application processes these inputs and provides a prediction of the crop production.

### Main Components

1. **Flask Web Application**: The project uses Flask, a lightweight web framework for Python, to create the web interface and handle HTTP requests.
2. **Machine Learning Model**: A pre-trained CatBoost model is used to make predictions based on the input parameters provided by the user.
3. **User Interface**: The web interface allows users to input the required parameters and submit the form to get the prediction.
4. **Session Management**: Flask sessions are used to store and retrieve the prediction results.

## Files

- `app.py`: The main Flask application file.
- `catboost_model.pkl`: The trained CatBoost model used for predictions.
- `templates/index.html`: The HTML template for the web interface.
