import json
# Load the JSON dataset
json_data = """ { 'id': 1,'age': 35,'credit_history': [
      { 'type': 'loan','status': 'paid','duration': 12},
      { 'type': 'credit card', 'status': 'paid','duration': 15}],
    'income': 60000, 'loan_amount': 30000} """
data = json.loads(json_data)

# Define the weights for each attribute
age_weight = 0.3
income_weight = 0.4
paid_installments_weight = 0.3

# Calculate the credit score using a weighted sum of the attribute values
credit_score = 0
for item in data['credit_history']:
    if item['status'] == 'paid':
        credit_score += item['duration']
credit_score = age_weight * data['age'] + income_weight * data['income'] + paid_installments_weight * credit_score

# Sort the data based on the credit score
sorted_data = sorted(data, key=lambda x: x['credit_score'], reverse=True)

# Print the sorted data
for item in sorted_data:
    print(json.dumps(item))