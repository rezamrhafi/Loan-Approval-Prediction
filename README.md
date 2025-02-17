# Loan Approval Prediction 💡

This repository contains a project on conversion prediction using multiple classification models (KNN, SVM, Decision Tree, Random Forest, XGBoost) with base parameters. The best-performing model was then fine-tuned using hyperparameter tuning, resulting in XGBoost being selected as the final prediction model. This project aims to apply machine learning models to predict conversions based on the available dataset. The repository includes a Jupyter Notebook file explaining the entire process, from data exploration to model experimentation using unseen data.

---
## Project Overview 📝

In this project, I used multiple classification models with base parameters, followed by hyperparameter tuning on the best-performing model to analyze the data and build a conversion prediction model. The key steps covered in this project are:

1. **Importing Libraries and Data Exploration**:
    - Loading the dataset and performing an initial exploration to understand the structure and characteristics of the data.

2. **Data Preprocessing**:
    - Cleaning and preparing the data, including handling outliers and imputing missing values.

3. **Model Development**:
    - Building and training five classification models to predict conversions.

4. **Model Evaluation**:
    - Using evaluation metrics to assess model performance.

5. **Hyperparameter Tuning**:
   - Conducting hyperparameter tuning on the best-performing model.

7. **Final Model Evaluation**:
   - Evaluating the fine-tuned model.

9. **Decision-Making for Model and Business**:
    - Making informed decisions regarding the model and its business implications.

---
## Problem Background 🧐

In the banking industry, loan approvals are a key service that contributes to profitability and business growth. However, determining creditworthiness for loan applicants is often challenging, particularly in minimizing default risk and improving operational efficiency.

With the advancement of technology and data-driven decision-making, predictive models based on machine learning can assist banks in assessing the likelihood of an applicant receiving loan approval. These models analyze various factors such as credit history, income, employment status, and other variables to provide accurate predictions of a borrower's eligibility.

Such predictive models enable applicants to conduct a preliminary check on their loan eligibility before formally applying. This enhances transparency for customers while helping banks optimize the approval process, reduce default risk, and improve customer satisfaction.

Thus, developing a loan approval prediction model is a strategic step toward increasing the efficiency and accuracy of the credit evaluation process in banks.

---
## Dataset Description

This dataset contains demographic, financial, and credit history information about individuals. Below is a description of each column:

| **Column Name**                   | **Data Type** | **Description**                                                                |
|------------------------------------|---------------|-------------------------------------------------------------------------------|
| **person_age**                    | Float         | Individual's age in years.                                                    |
| **person_gender**                 | Categorical   | Individual's gender ("Male", "Female").                                      |
| **person_education**              | Categorical   | Highest level of education attained.                                         |
| **person_income**                 | Float         | Individual's annual income.                                                  |
| **person_emp_exp**                | Integer       | Years of employment experience.                                              |
| **person_home_ownership**         | Categorical   | Home ownership status ("Rent", "Own", "Mortgage").                           |
| **loan_amnt**                     | Float         | Loan amount requested.                                                       |
| **loan_intent**                   | Categorical   | Purpose of the loan ("Education", "Business", "Home Improvement", etc.).       |
| **loan_int_rate**                 | Float         | Loan interest rate.                                                          |
| **loan_percent_income**           | Float         | Ratio of loan amount to annual income.                                      |
| **cb_person_cred_hist_length**    | Float         | Length of credit history in years.                                          |
| **credit_score**                  | Integer       | Credit score (typically 300-850).                                           |
| **previous_loan_defaults_on_file**| Categorical   | Indicator of previous loan default ("Yes"/"No").                            |
| **loan_status**                   | Categorical   | Loan approval status (1 = Approved, 0 = Denied).                            |

---
## Methods Used 🛠️

- Inferential Statistics
- Machine Learning
- Data Visualization
- Predictive Modeling

---
## Analytical Conclusions 🧠
- After comparing five models, XGBoost demonstrated the best and most stable performance, despite slight overfitting.
- Hyperparameter tuning improved the model’s performance by adjusting parameters to suit the dataset.
- By optimizing the F1-score, the model can minimize incorrect approvals and denials.
- Education and healthcare were the most common reasons for loan applications.
- **Recommendation 1**: Borrowers should align their requested loan amount with their annual income.
- **Recommendation 2**: Using this model, borrowers can assess their loan eligibility based on their provided data.
- **Recommendation 3**: Borrowers with previous loan defaults should avoid excessive borrowing.
