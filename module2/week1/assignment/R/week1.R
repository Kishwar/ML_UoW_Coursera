# When sourcing file.. call this function only..
# @Param :
#          - train_file: CSV file name of training dataset
#          - test_file: CSV file name for test dataset
main <- function(train_file, test_file) {
    
    #back current working directory path
    currWD <- getwd()
    
    #set working directory
    setwd("~/Desktop/MachineLearningCourse/module2/week1/assignment/")
    
    #read training dataset CSV
    tr <- read.csv(train_file)
    td <- read.csv(test_file)
    
    #calculate and print mean of prices
    meanCal <- mean(tr[['price']])
    str <- paste("Mean:", meanCal)
    print(str)
    
    #calculate sum of squared prices
    priceSqSum <- sum(tr[['price']] * tr[['price']])
    str <- paste("the sum of price squared is:", priceSqSum)
    print(str)
    
    # Apply simple linear regression model
    W <- simple_linear_regression(tr[['sqft_living']],
                                            tr[['price']])
    
    #------------------------------------------------------------------------------------------
    print("Quiz Question: Using your Slope and Intercept from (4), What is the predicted price for a house with 2650 sqft?")
    my_house_sqft = 2650
    estimated_price = get_regression_predictions(my_house_sqft, W[1], W[2])
    print(paste("The estimated price for a house with 2650 squarefeet is", estimated_price))
    
    #------------------------------------------------------------------------------------------
    rss_prices_on_sqft = get_residual_sum_of_squares(tr[['sqft_living']],
                                                     tr[['price']],
                                                     W[1], W[2])
    print(paste("The RSS of predicting Prices based on Square Feet is", rss_prices_on_sqft))
    
    #------------------------------------------------------------------------------------------
    my_house_price = 800000
    estimated_squarefeet = inverse_regression_predictions(my_house_price,
                                                          W[1],
                                                          W[2])
    print(paste("The estimated squarefeet for a house worth $800000 is", estimated_squarefeet))
    
    #------------------------------------------------------------------------------------------
    # New Model: estimate prices from bedrooms
    bW = simple_linear_regression(tr[['bedrooms']], tr[['price']])
    
    print(paste("bedroom-Intercept:", bW[1]))
    print(paste("bedroom-Slope:", bW[2]))
    
    #------------------------------------------------------------------------------------------
    # Test your Linear Regression Algorithm
    print("Quiz Question: Which model (square feet or bedrooms) has lowest RSS on TEST data? Think about why this might be the case.")
    
    err_bedrooms <- td[['price']] - (bW[1] + (td[['bedrooms']] * bW[2]))
    err_bedrooms_sq <- err_bedrooms * err_bedrooms
    RSS_bedrooms_model <- sum(err_bedrooms_sq)
    print(paste("RSS Bedrooms Model:", RSS_bedrooms_model))
    
    err_sqft <- td[['price']] - (W[1] + (td[['bedrooms']] * W[2]))
    err_sqft_sq <- err_sqft * err_sqft
    RSS_sqft_model <- sum(err_sqft_sq)
    print(paste("RSS sqft Model:", RSS_sqft_model))
    
    c(RSS_bedrooms_model, RSS_sqft_model)
}

# This function calculates weights for Linear Regression Model
# Model should be 2 dimension. 
# @Param: Input Feature Vector
#         Ouput Vector
# @Return: Weight Vector
simple_linear_regression <- function(input_feature, output) {
    # We need ???Yi, ???Xi, ???YiXi, ???Xi^2
    feature_sum <- sum(input_feature)                                          # ???Xi
    output_sum <- sum(output)                                                  # ???Yi
    feature_output_vector_sum <- sum(output * input_feature)                   # ???YiXi
    input_feature_sq_sum <- sum(as.numeric(input_feature * input_feature))     # ???Xi^2
    N_Size <- length(input_feature)                                            # N
    
    # W1 = (???YiXi - ((???Yi???Xi)/N)) / (???Xi^2 - ((???Xi???Xi)/N))
    W1_slope <- (feature_output_vector_sum - ((output_sum * feature_sum) / N_Size)) / 
        (input_feature_sq_sum - (as.double((as.numeric(feature_sum) * as.numeric(feature_sum)))/N_Size))
    
    # W0 = (???Yi/N) - W1(???Xi/N)
    Wo_Intercept <- (output_sum / N_Size) - (W1_slope * (feature_sum / N_Size))
    
    print(paste("intercept:", Wo_Intercept))
    print(paste("slope:", W1_slope))
    
    # retrun vector
    W <- c(Wo_Intercept, W1_slope)
}

# Function calculates predicted value for given input_feature scalar
# @Param: input_feature scalar quantity
#         intercept = W0
#         slope = W1
# @Return: Predicated value
get_regression_predictions <- function(input_feature, intercept, slope) {
    # calculate predicted values
    predicted_values <- intercept + (slope * input_feature)
}

# Calculate RSS (Residual Sum of Squares)
get_residual_sum_of_squares <- function (input_feature, output, intercept, slope) {
    err <- output - (intercept + (slope * input_feature))
    err_sq <- err * err
    RSS <- sum(err_sq)
}

# Predict the squarefeet of given price
inverse_regression_predictions <- function(output, intercept, slope) {
    # y = wo + w1x
    # y - w0 = w1x
    # x = (y - w0) / w1
    estimated_feature <- (output - intercept) / slope
}