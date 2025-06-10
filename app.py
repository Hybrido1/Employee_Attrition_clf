import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("employee_attrition_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Employee Attrition Predictor")
st.write("Fill in the details below to predict the probability of employee attrition.")

# Numeric Inputs
age = st.slider("Age", 18, 60, 30)
daily_rate = st.number_input("Daily Rate", min_value=100, max_value=1500, value=500)
distance_home = st.slider("Distance from Home", 1, 30, 10)
monthly_income = st.number_input("Monthly Income", 1000, 20000, 5000)
monthly_rate = st.number_input("Monthly Rate", 1000, 30000, 10000)
num_companies_worked = st.slider("Number of Companies Worked", 0, 10, 2)
percent_salary_hike = st.slider("Percent Salary Hike", 0, 50, 15)
total_working_years = st.slider("Total Working Years", 0, 40, 5)
training_times = st.slider("Training Times Last Year", 0, 10, 2)
years_at_company = st.slider("Years at Company", 0, 40, 5)
years_current_role = st.slider("Years in Current Role", 0, 20, 2)
years_last_promotion = st.slider("Years Since Last Promotion", 0, 15, 1)
years_current_manager = st.slider("Years with Current Manager", 0, 20, 3)

# Ordinal Inputs
education = st.selectbox("Education", [1, 2, 3, 4, 5])
environment_satisfaction = st.selectbox("Environment Satisfaction", [1, 2, 3, 4])
job_involvement = st.selectbox("Job Involvement", [1, 2, 3, 4])
job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
job_satisfaction = st.selectbox("Job Satisfaction", [1, 2, 3, 4])
performance_rating = st.selectbox("Performance Rating", [1, 2, 3, 4])
relationship_satisfaction = st.selectbox("Relationship Satisfaction", [1, 2, 3, 4])
stock_option_level = st.selectbox("Stock Option Level", [0, 1, 2, 3])
work_life_balance = st.selectbox("Work-Life Balance", [1, 2, 3, 4])

# Categorical Inputs
business_travel = st.selectbox("Business Travel", ["Non-Travel", "Travel_Frequently", "Travel_Rarely"])
department = st.selectbox("Department", ["Human Resources", "Research & Development", "Sales"])
education_field = st.selectbox("Education Field", ["Human Resources", "Life Sciences", "Marketing", "Medical", "Other", "Technical Degree"])
job_role = st.selectbox("Job Role", ["Healthcare Representative", "Human Resources", "Laboratory Technician",
                                     "Manager", "Manufacturing Director", "Research Director",
                                     "Research Scientist", "Sales Executive", "Sales Representative"])
marital_status = st.selectbox("Marital Status", ["Divorced", "Married", "Single"])
overtime = st.selectbox("Overtime", ["Yes", "No"])

if st.button("Predict Attrition Probability"):
    input_data = pd.DataFrame({
        'Age': [age], 'DailyRate': [daily_rate], 'DistanceFromHome': [distance_home],
        'Education': [education], 'EnvironmentSatisfaction': [environment_satisfaction], 'JobInvolvement': [job_involvement],
        'JobLevel': [job_level], 'JobSatisfaction': [job_satisfaction], 'MonthlyIncome': [monthly_income],
        'MonthlyRate': [monthly_rate], 'NumCompaniesWorked': [num_companies_worked],
        'PercentSalaryHike': [percent_salary_hike], 'PerformanceRating': [performance_rating],
        'RelationshipSatisfaction': [relationship_satisfaction], 'StockOptionLevel': [stock_option_level],
        'TotalWorkingYears': [total_working_years], 'TrainingTimesLastYear': [training_times],
        'WorkLifeBalance': [work_life_balance], 'YearsAtCompany': [years_at_company],
        'YearsInCurrentRole': [years_current_role], 'YearsSinceLastPromotion': [years_last_promotion],
        'YearsWithCurrManager': [years_current_manager],
        'BusinessTravel_Non-Travel': [1 if business_travel == "Non-Travel" else 0],
        'BusinessTravel_Travel_Frequently': [1 if business_travel == "Travel_Frequently" else 0],
        'BusinessTravel_Travel_Rarely': [1 if business_travel == "Travel_Rarely" else 0],
        'Department_Human Resources': [1 if department == "Human Resources" else 0],
        'Department_Research & Development': [1 if department == "Research & Development" else 0],
        'Department_Sales': [1 if department == "Sales" else 0],
        'EducationField_Human Resources': [1 if education_field == "Human Resources" else 0],
        'EducationField_Life Sciences': [1 if education_field == "Life Sciences" else 0],
        'EducationField_Marketing': [1 if education_field == "Marketing" else 0],
        'EducationField_Medical': [1 if education_field == "Medical" else 0],
        'EducationField_Other': [1 if education_field == "Other" else 0],
        'EducationField_Technical Degree': [1 if education_field == "Technical Degree" else 0],
        'JobRole_Healthcare Representative': [1 if job_role == "Healthcare Representative" else 0],
        'JobRole_Human Resources': [1 if job_role == "Human Resources" else 0],
        'JobRole_Laboratory Technician': [1 if job_role == "Laboratory Technician" else 0],
        'JobRole_Manager': [1 if job_role == "Manager" else 0],
        'JobRole_Manufacturing Director': [1 if job_role == "Manufacturing Director" else 0],
        'JobRole_Research Director': [1 if job_role == "Research Director" else 0],
        'JobRole_Research Scientist': [1 if job_role == "Research Scientist" else 0],
        'JobRole_Sales Executive': [1 if job_role == "Sales Executive" else 0],
        'JobRole_Sales Representative': [1 if job_role == "Sales Representative" else 0],
        'MaritalStatus_Divorced': [1 if marital_status == "Divorced" else 0],
        'MaritalStatus_Married': [1 if marital_status == "Married" else 0],
        'MaritalStatus_Single': [1 if marital_status == "Single" else 0],
        'OverTime_No': [1 if overtime == "No" else 0],
        'OverTime_Yes': [1 if overtime == "Yes" else 0],
    })

    probability = model.predict_proba(input_data)[0][1]
    st.subheader(f"Probability to Leave: {probability:.2%}")