# Diabetes Prediction System

## Description

The Diabetes Prediction System is a machine learning project designed to predict the likelihood of developing diabetes based on various health metrics. The system uses the Pima Indian Diabetes dataset to train a logistic regression model, providing a user-friendly interface for making predictions.

## Installation

1. **Clone the Repository**

   ```
   git clone <repository-url>
   cd DiabetesPrediction
   ```

2. **Install Dependencies**

   Ensure you have Python 3.x installed. Install the required packages using:

   ```
   pip install -r requirements.txt
   ```

3. **Setup Dataset**

   Download the Pima Indian Diabetes dataset from Kaggle:

   [Pima Indian Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

   Place the dataset in the `DiabetesPrediction` directory. Make sure the dataset file is named `diabetes.csv` or update the path in `views.py` accordingly.

4. **Run the Project**

   Start the Django development server:

   ```
   python manage.py runserver
   ```

   Navigate to `http://127.0.0.1:8000/` in your browser to access the application.

## Usage

1. **Home Page**

   Visit the home page to get an overview of the Diabetes Prediction System. Click on "Let's go" to proceed to the prediction page.

2. **Prediction Page**

   On the prediction page, enter the required health metrics and submit the form. A popup will display the prediction result.

3. **Dataset Details**

   The dataset used for training and testing the model includes:

   - `Pregnancies`: Number of pregnancies
   - `Glucose`: Plasma glucose concentration
   - `Blood Pressure`: Diastolic blood pressure
   - `Skin Thickness`: Triceps skin fold thickness
   - `Insulin`: 2-Hour serum insulin
   - `BMI`: Body mass index
   - `Diabetes Pedigree Function`: Diabetes pedigree function
   - `Age`: Age in years
   - `Outcome`: Binary outcome variable indicating diabetes presence (1) or absence (0)

## Contributing

If you’d like to contribute to this project:

1. **Fork the Repository**

   Click the "Fork" button on GitHub to create your own copy of the repository.

2. **Create a New Branch**

   ```
   git checkout -b <feature-branch>
   ```

3. **Make Changes**

   Implement your feature or bug fix.

4. **Commit Your Changes**

   ```
   git add .
   git commit -m "Description of changes"
   ```

5. **Push to Your Fork**

   ```
   git push origin <feature-branch>
   ```

6. **Submit a Pull Request**

   Go to the repository on GitHub and submit a pull request detailing your changes.

## License

This project is licensed under the MIT License.

## Credits

Developed by Yoon Thiri Ko. Special thanks to YouTube tutorials and Kaggle for the dataset.
