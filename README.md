# MSCI446 Project
Group 4
# NourishNudge
In the category of Empirical Evaluation (category 2), we focus on the application area of Food
and Wellness. Our proposed machine learning algorithm streamlines meal planning by
customizing recipes based on individual dietary preferences, health goals, and restrictions.
Tailored for university students and those with dietary limitations, the system addresses
environmental concerns by minimizing food waste through diverse alternatives and substitutes,
maximizing ingredient use. Economically, it aids individuals with time constraints, particularly
budget-conscious students, offering cost-effective and time-efficient meal options. In summary,
the system promotes inclusivity, encourages healthier choices, reduces food waste, and provides
economical, time-saving meal solutions.

# Running the code

# Neural Network

Neural Network Model Summary
-----------------------------
- Objective: Predict the caloric content of recipes based on ingredients and dietary preferences.

Inputs:
- Text data from the 'Ingredient' column, tokenized and padded to uniform length.
- Categorical data from 'Dietary Preference', one-hot encoded.

Output:
- Predicted 'Calories' for each recipe, a continuous variable representing the caloric content.

Model Architecture:
1. InputLayer: Specifies the input shape that matches the combined features' dimensionality.
2. Embedding Layer: Transforms tokenized ingredients into dense vector representations.
   - input_dim: 10001 (size of vocabulary + 1 for padding token)
   - output_dim: 64 (dimensionality of the embedding vectors)
3. Flatten: Flattens the output of the embedding layer to fit into dense layers.
4. Dense Layer 1: First fully connected layer with ReLU activation.
   - Units: 128
   - Activation: ReLU
5. Dropout: Regularization layer to prevent overfitting.
   - Rate: 0.5
6. Dense Layer 2: Second fully connected layer with ReLU activation.
   - Units: 64
   - Activation: ReLU
7. Dropout: Another dropout layer with the same rate to further regularize the model.
8. Dense Layer 3 (Output Layer): Outputs the predicted caloric content.
   - Units: 1 (since predicting a single continuous value)
   - Activation: Linear

Training Parameters:
- Optimizer: Adam
- Loss Function: Mean Squared Error (for regression)
- Metrics: Mean Absolute Error (to assess model performance)
- Epochs: 20
- Batch Size: 32
- Validation Split: 0.2 (20% of the training data used for validation)
  
"""



