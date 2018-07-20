# Author: Yan Wang
# Date: 2018-07


# Coding how weight changes affect accuracy

# Its weights have been pre-loaded as weights_0. 
# Your task in this exercise is to update a single weight in weights_0 to create weights_1, 
#    which gives a perfect prediction (in which the predicted value is equal to target_actual: 3).


# The data point you will make a prediction for
input_data = np.array([0, 3])

# Sample weights
weights_0 = {'node_0': [2, 1],
             'node_1': [1, 2],
             'output': [1, 1]
            }

# The actual target value, used to calculate the error
target_actual = 3

# Make prediction using original weights
model_output_0 = predict_with_network(input_data, weights_0)

# Calculate error: error_0
error_0 = model_output_0 - target_actual

# Create weights that cause the network to make perfect prediction (3): weights_1
weights_1 = {'node_0': [1, 0],
             'node_1': [0, 1],
             'output': [0, 1]
            }

# Make prediction using new weights: model_output_1
model_output_1 = predict_with_network(input_data, weights_1)

# Calculate error: error_1
error_1 = model_output_1 - target_actual

# Print error_0 and error_1
print(error_0)
print(error_1)

