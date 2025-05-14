import pandas as pd
from joblib import load
from sklearn.preprocessing import LabelEncoder

# Data input tunggal untuk prediksi
testing = {
    'Age': [37],
    'BusinessTravel': ['Travel_Rarely'],
    'DailyRate': [1141],
    'Department': ['Research & Development'],
    'DistanceFromHome': [11],
    'Education': [2],
    'EducationField': ['Medical'],
    'EmployeeCount': [1],
    'EnvironmentSatisfaction': [1],
    'Gender': ['Female'],
    'HourlyRate': [61],
    'JobInvolvement': [1],
    'JobLevel': [2],
    'JobRole': ['Healthcare Representative'],
    'JobSatisfaction': [2],
    'MaritalStatus': ['Married'],
    'MonthlyIncome': [71777],
    'MonthlyRate': [14382],
    'NumCompaniesWorked': [5],
    'Over18': ['Y'],
    'OverTime': ['No'],
    'PercentSalaryHike': [15],
    'PerformanceRating': [3],
    'RelationshipSatisfaction': [1],
    'StandardHours': [80],
    'StockOptionLevel': [0],
    'TotalWorkingYears': [15],
    'TrainingTimesLastYear': [2],
    'WorkLifeBalance': [1],
    'YearsAtCompany': [7],
    'YearsInCurrentRole': [0],
    'YearsSinceLastPromotion': [0],
    'YearsWithCurrManager': [0],
}

# Ubah menjadi DataFrame
sample_df = pd.DataFrame(testing)

# Load model yang sudah dilatih
rf = load('random_forest_model.joblib')

# Label Encoding untuk kolom kategorikal
cat_cols = sample_df.select_dtypes(include='object').columns
le = LabelEncoder()

for col in cat_cols:
    sample_df[col] = le.fit_transform(sample_df[col])

# Prediksi
prediction = rf.predict(sample_df)

# Menampilkan hasil prediksi
print("Prediksi Attrition:", "Keluar" if prediction[0] == 1 else "Bertahan")