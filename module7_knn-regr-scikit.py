import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Function to read input k (positive integer)
def read_positive(prompt: str) -> int:
    try:
        k = int(input(prompt).strip())
        if k > 0:
            return k
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid k. Please enter a positive integer.")

# Function to read real numbers one by one to provide N (x,y) points 
def read_real_number(prompt: str) -> float:
    try:
        return float(input(prompt).strip())
    except ValueError:
        print("Invalid value. Please enter a real number.")
def main():
    # Read N and K
    N = read_positive("Enter N, must be a positive integer: ")
    K = read_positive("Enter K, must be a positive integer: ")

    # Read N points: x then y for each point
    points_x = np.empty(N, dtype=float)
    points_y= np.empty(N, dtype=float)

    for i in range(N):
        print(f"Point {i + 1}:")
        points_x[i] = read_real_number(f"Enter x[{i}]: ")
        points_y[i] = read_real_number(f"Enter y[{i}]: ") 
    
    # Variance of the labels
    y_variance = float(np.var(points_y))
    print(f"\nVariance of labels: {y_variance}") 

    X = read_real_number("Enter x for prediction: ")

    # Check if K is smaller than N
    if K > N:
        print("K cannot be greater than N. Exiting.")
        return
    
    # knn via scikit-learn ---
    X_train = points_x.reshape(-1, 1)
    y_train = points_y

    # Create and fit knn regressor
    knn = KNeighborsRegressor(n_neighbors=K, metric="euclidean", weights="uniform")
    knn.fit(X_train, y_train)
    # Get prediction 
    y_pred = float(knn.predict(np.array([[X]]))[0])

    print(f"k-NN regression prediction at X={X} with k={K}): {y_pred}")

if __name__ == "__main__":
    main()
    


    