# IBM HR Analytics: Employee Attrition & Performance
This project focuses on analyzing factors that contribute to employee attrition using the IBM HR dataset. Through extensive exploratory data analysis (EDA), feature engineering, and classification modeling, the goal was to identify key drivers of attrition and develop a predictive model. The application is deployed using Streamlit for interactive exploration.

- Project Objective
The primary objective of this project is to gain insights into employee attrition trends and build a machine learning classifier that predicts whether an employee is likely to leave the organization. The insights can help businesses design more effective retention strategies.

- Dataset
The dataset used is IBM’s publicly available HR analytics data, consisting of 1,470 employee records and 35 features, including demographic details, work-related attributes, compensation, job satisfaction, and performance scores.

- Key Analysis and Insights
  - Unbalanced Attrition: Only 16.12% of employees in the dataset had left the company.
  - Influencing Factors: Lower income, high job involvement, poor work-life balance, frequent business travel, and overtime were found to correlate with higher attrition.
  - Demographic Trends: Employees under 40 and those living farther from the office were more likely to leave. Females showed different patterns of tenure and distance-related attrition compared to males.

- Machine Learning Approach
  - Features were preprocessed using label encoding and one-hot encoding for categorical variables.
  - A Decision Tree classifier was developed and tuned using GridSearchCV with cross-validation.
  - Model achieved an accuracy of approximately 84% on test data.
  - ROC-AUC analysis and confusion matrix were used for performance evaluation.
  - Visualizations include decision tree plots, distribution charts, and correlation heatmaps.

- Deployment
  - The Streamlit web application enables users to:
  - Explore how various attributes affect attrition
  - Interact with graphical plots generated using Seaborn and Matplotlib
  - Predict attrition using user-provided inputs

- Tech Stack
  - Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
  - Streamlit for web deployment
  - Google Colab for notebook-based exploration
  - Decision Tree for model training and classification

- How to Use
To run the application locally:
Clone the repository
Install dependencies using pip install -r requirements.txt
Run the Streamlit app with streamlit run app.py
Alternatively, access the live version hosted on Streamlit Cloud.

- Future Improvements
Introduce ensemble models (Random Forest, XGBoost) for better generalization.
Balance the dataset using techniques like SMOTE.
Add user input forms to simulate attrition predictions for new employees.
Extend the analysis with SHAP values to improve model explainability.
