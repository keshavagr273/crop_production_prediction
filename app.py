from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import pickle

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required to use session

# Load the trained CatBoost model
with open('catboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = {
                'Crop': request.form['Crop'],
                'Crop_Year': int(request.form['Crop_Year']),
                'Season': request.form['Season'],
                'State': request.form['State'],
                'Area': float(request.form['Area']),
                'Annual_Rainfall': float(request.form['Annual_Rainfall']),
                'Fertilizer': float(request.form['Fertilizer']),
                'Pesticide': float(request.form['Pesticide'])
            }

            input_df = pd.DataFrame([data])
            prediction = round(model.predict(input_df)[0], 2)

            session['prediction'] = prediction  # Store prediction in session

        except Exception as e:
            print("Prediction Error:", e)
            session['prediction'] = None

        return redirect(url_for('index'))  # Redirect to clear POST data

    # GET request: retrieve and remove prediction from session
    prediction = session.pop('prediction', None)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
