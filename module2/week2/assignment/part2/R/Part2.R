main <- function(csv_train, csv_test) {
    #set path to csv files directory
    setwd("~/Desktop/MachineLearningCourse/module2/week2/assignment/part2/R/")
    
    #read CSVs
    tr <- read.csv(csv_train)
    te <- read.csv(csv_test)
    
    print("++++++++++++++++++++++++++++++++++ SIMPLE REGRESSION ++++++++++++++++++++++++++++++++++++++++++")
    
    print("Q1:What is the value of the weight for sqft_living -- the second element of 'simple_weights'")
    step_size <- 7e-12
    tolerance <- 2.5e7
    feature_matrix <- tr[['sqft_living']]
    ones <- rep(1, length(feature_matrix))
    feature_matrix <- matrix(c(ones, feature_matrix), nrow = length(ones), ncol = 2)
    output <- tr[['price']]
    initial_weights <- c(-4.70000000e+04, 1.00000000e+00)
    weights <- regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance)
    print(paste("Answer:", round(weights[2], digits = 1)))
    
    print("Q2:What is the predicted price for the 1st house in the TEST data set for model 1 (round to nearest dollar)")
    p <- weights[1] + (te[['sqft_living']][1] * weights[2])
    print(paste("Answer: $", round(p, digits = 0), sep = ""))
    
    print("Q:RSS-Simple regression - test data")
    rss <- sum((te[['price']] - (weights[1] + (te[['sqft_living']] * weights[2])))^2)
    print(paste("RSS-Simple Regression:", signif(rss, 5)))
    
    print("++++++++++++++++++++++++++++++++++ MULTIPLE REGRESSION ++++++++++++++++++++++++++++++++++++++++++")
    
    print("Q1:What is the value of the weights for multiple features")
    initial_weights = c(-100000., 1., 1.)
    step_size = 4e-12
    tolerance = 1e9
    output <- tr[['price']]
    ones <- rep(1, length(tr[['sqft_living']]))
    feature_matrix <- matrix(c(ones, tr[['sqft_living']], tr[['sqft_living15']]), nrow = length(ones), ncol = 3)
    weights <- regression_gradient_descent(feature_matrix, output, initial_weights, step_size, tolerance)
    print(paste("Answer:", weights[1], weights[2], weights[3]))
    
    print("Quiz Question: What is the predicted price for the 1st house in the TEST data set for model 2 (round to nearest dollar)")
    p <- weights[1] + (te[['sqft_living']][1] * weights[2]) + (te[['sqft_living15']][1] * weights[3])
    print(paste("Answer: $", round(p, digits = 0), sep = ""))
    
    print(paste("Actual Price of House: $", te[['price']][1], sep = ""))
    
    print("Q:RSS-Multiple regression - test data")
    rss <- sum((te[['price']] - (weights[1] + (te[['sqft_living']] * weights[2]) + (te[['sqft_living15']] * weights[3])))^2)
    print(paste("RSS-Multiple Regression:", signif(rss, 5)))
}

regression_gradient_descent <- function(feature_matrix, output, initial_weights, step_size, tolerance) {
    Moving <- TRUE
    weights <- initial_weights
    while (Moving) {
        prediction <- feature_matrix %*% weights
        error <- prediction - output
        gradient_sum_squares <- 0
        for(i in 1:length(weights)) {
            derivative <- feature_matrix[,i] %*% error
            gradient_sum_squares <-  gradient_sum_squares + (as.numeric(derivative) * as.numeric(derivative))
            weights[i] <- weights[i] - (2 * step_size * as.numeric(derivative))
        }
        gradient_magnitude <- sqrt(gradient_sum_squares)
        #print(gradient_magnitude)
        if (as.numeric(gradient_magnitude) < as.numeric(tolerance))
            Moving = FALSE
    }
    return(weights)
}