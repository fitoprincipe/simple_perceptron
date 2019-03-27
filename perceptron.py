# -*- coding: utf-8 -*-

# Author: Rodrigo E. Principe
# Email: fitoprincipe82 at gmail

# Make a prediction with weights
# one vector has n elements
# p = (element1*weight1) + (element2*weight2) + (elementn*weightn) + bias
# if p >= 0; 1; 0
def predict(vector, bias, weights):
    pairs = zip(vector, weights) # [[element1, weight1], [..]]
    for (element, weight) in pairs:
        bias += element * weight
    return 1.0 if bias >= 0.0 else 0.0

# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch, bias=0):
    first_vector = train[0][0]
    # weights = [0.0 for i in range(len(first_vector))]
    weights = [random() for i in range(len(first_vector))]
    # iterate over the epochs
    for epoch in range(n_epoch):
        # each epoch has a sum_error, starting at 0
        sum_error = 0.0
        for row in train:
            vector = row[0]
            expected = row[1]
            prediction = predict(vector, bias, weights)
            error = expected - prediction
            sum_error += error**2

            # update activation (weights[0]))
            bias = bias + (l_rate * error)

            # update weights
            for i in range(len(vector)):
                # for each element of the vector
                weights[i] = weights[i] + (l_rate * error * vector[i])

        # print('>epoch={}, lrate={}, error={}'.format(epoch, l_rate, sum_error))
    return bias, weights

# Perceptron Algorithm With Stochastic Gradient Descent
def perceptron(train, test, l_rate, n_epoch):
    predictions = list()
    weights = train_weights(train, l_rate, n_epoch)
    for row in test:
        prediction = predict(row, weights)
        predictions.append(prediction)
    return(predictions)
