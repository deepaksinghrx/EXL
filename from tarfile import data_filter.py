from tarfile import data_filter
from tkinter.filedialog import SaveFileDialog


if df is not None:
    gender_map = {"Female": 0, "Male": 1, "Other": 2}
    married_map = {"No": 0, "Yes": 1}
    residence_map = {"Rural": 0, "Urban": 1}
    work_type_map = {
    "Private": 0,
    "Self-employed": 1,
    "Govt_job": 2,
    "children": 3,
    "Never_worked": 4
}
smoking_map = {
    "never smoked": 0,
    "formerly smoked": 1,
    "smokes": 2,
    "Unknown": 0
}

risk_score = (
    (df['age'] * 0.06) +
    (df['hypertension'] * 2.0) +
    (df['heart_disease'] * 2.5) +
    (df['avg_glucose_level'] * 0.01) +
    (df['bmi'] * 0.02) +
    (df['smoking_status'].isin(['smokes', 'formerly smoked']).astype(int) * 1.0)
)

# Create balanced target
threshold = risk_score.median()

df['stroke'] = (risk_score > threshold).astype(int)

print(df['stroke'].value_counts())
print(df['stroke'].value_counts(normalize=True) * 100)






Linear Regression
MSE: 0.0985039101707981
MAE: 0.24765633429709133
R2: 0.6053798577374438
Accuracy: 0.9099804305283757



Linear Regression
MSE: 0.029473579197855787
MAE: 0.12235087178731004
R2: 0.7884519629820218
Accuracy: 0.9911937377690803





# Create metrics dataframe from model predictions
metrics_data = []
model_names_list = ['Logistic Regression', 'Decision Tree', 'Random Forest', 'KNN', 'Linear Regression']
predictions = [y_pred_lr, y_pred_dt, y_pred_rf, y_pred_knn, y_pred_lr_class]
probabilities = [y_prob_lr, y_prob_dt, y_prob_rf, y_prob_knn, y_pred_lr]

for i, model_name in enumerate(model_names_list):
    y_pred = predictions[i]
    y_prob = probabilities[i]
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    try:
        roc_auc = roc_auc_score(y_test, y_prob)
    except:
        roc_auc = np.nan
    
    metrics_data.append({
        'Model': model_name,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1': f1,
        'ROC_AUC': roc_auc
    })

metrics_df = pd.DataFrame(metrics_data)

















problem statement
approch
processed data 
saved metadata of the processed data
model training and evaluation
prediction on new data
of new data changes the error metrics

saved the plots in excel or make report in excel








take data
aman(java,python)
aman,(sql,airflow)
nikita(it,finance)
nikita(marketing,media)
sonu(java,C++)


output:
name,skills
aman,java
amaan,python
sonu,C++
