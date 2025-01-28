from flask import Flask, render_template, request, jsonify
from model import predict

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def make_prediction():
    try:
        data = request.get_json()  # Ensure you're receiving data as JSON
        print(f"Received data: {data}")  # Debugging: print the received data to the console

        # Ensure all required fields are present
        required_fields = ['Age', 'Gender', 'Tumor_Size(cm)', 'Biopsy_Result', 'Treatment', 'Response_to_Treatment']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

        age = float(data['Age'])
        gender = int(data['Gender'])
        tumor_size = float(data['Tumor_Size(cm)'])
        biopsy_result = int(data['Biopsy_Result'])
        treatment = int(data['Treatment'])
        response_to_treatment = int(data['Response_to_Treatment'])

        input_data = [[age, gender, tumor_size, biopsy_result, treatment, response_to_treatment]]

        prediction = predict(input_data)
        print(f"Prediction: {prediction}")
        return jsonify({'Survival_Status': prediction[0]})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)