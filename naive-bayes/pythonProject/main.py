import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, roc_curve, auc
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
file_path = 'a.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv(file_path)

# Assuming 'Outcome' is the target variable, you can replace it with the actual target column name
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Naive Bayes classifier
naive_bayes = GaussianNB()

# Train the classifier
naive_bayes.fit(X_train, y_train)



# Make predictions on the test set
y_pred = naive_bayes.predict(X_test)

# Print probabilities for all classes in Naive Bayes
probabilities = naive_bayes.predict_proba(X_test)
print("Probabilities for Naive Bayes:")
print(probabilities)



# Calculate ROC curve for Naive Bayes
fpr_nb, tpr_nb, thresholds_nb = roc_curve(y_test, y_pred)
roc_auc_nb = auc(fpr_nb, tpr_nb)


# Evaluate the models
accuracy_naive_bayes = accuracy_score(y_test, y_pred)
print(f"Accuracy of Naive Bayes: {accuracy_naive_bayes:.2f}")


# Display classification report for Naive Bayes
print("Classification Report for Naive Bayes:")
print(classification_report(y_test, y_pred))

# Plot ROC curve for Naive Bayes
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(fpr_nb, tpr_nb, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc_nb:.2f}) - Naive Bayes')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Naive Bayes')
plt.legend(loc='lower right')


# Initialize the Decision Tree classifier
dt_classifier = DecisionTreeClassifier()

# Train the Decision Tree classifier
dt_classifier.fit(X_train, y_train)

# Make predictions on the test set using Decision Tree
dt_pred = dt_classifier.predict(X_test)

# Calculate ROC curve for Decision Tree
fpr_dt, tpr_dt, thresholds_dt = roc_curve(y_test, dt_pred)
roc_auc_dt = auc(fpr_dt, tpr_dt)


accuracy_decision_tree = accuracy_score(y_test, dt_pred)
print(f"Accuracy of Decision Tree: {accuracy_decision_tree:.2f}")


# Display classification report for Decision Tree
print("Classification Report for Decision Tree:")
print(classification_report(y_test, dt_pred))


# Plot ROC curve for Decision Tree
plt.subplot(1, 2, 2)
plt.plot(fpr_dt, tpr_dt, color='green', lw=2, label=f'ROC curve (AUC = {roc_auc_dt:.2f}) - Decision Tree')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Decision Tree')
plt.legend(loc='lower right')

plt.tight_layout()
plt.show()

# Plot Decision Tree
plt.figure(figsize=(12, 6))
plot_tree(dt_classifier, feature_names=X.columns, class_names=['0', '1'], filled=True, rounded=True)
plt.show()
