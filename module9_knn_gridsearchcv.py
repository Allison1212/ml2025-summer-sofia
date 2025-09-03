import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,precision_score,recall_score


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

# Function to read label (positive integer)
def read_label(prompt: str) -> int:
    try:
        v = int(input(prompt).strip())
        if v >= 0:
            return v
        else:
            print("Please enter a positive integer.")
            return read_label(prompt)
    except ValueError:
        print("Invalid value. Please enter a positive integer.")
        return read_label(prompt)

def read_xy_pairs(count: int, title: str):
    print(f"Enter {count} (x,y) pairs for {title}:")
    X = np.empty((count, 1), dtype=float)
    y = np.empty(count, dtype=int)
    for i in range(count):
        print(f"Pair {i+1}:")
        X[i, 0] = read_real_number(f"  x[{i}]: ")
        y[i] = read_label(f"  y[{i}]: ")
    return X, y


def main():
    # Read N
    N = read_positive("Enter N (number of training samples): ")

    # Read training data
    X_train, y_train = read_xy_pairs(N, "TrainS")

    # Read testing data
    M = read_positive("Enter M (number of test samples): ")
    X_test, y_test = read_xy_pairs(M, "TestS")

    # Grid search for KNN
    param_grid = {
        'n_neighbors': [1, 2, 3],
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan']
    }

    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    print("Cross-validation results:")
    print("Best parameters:", grid_search.best_params_)
    print(f"Best CV accuracy: {grid_search.best_score_:.4f}")

    # Test with the best model and report accuracy
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    test_acc = accuracy_score(y_test, y_pred)

    print("Final Test Results")
    print("Test accuracy with best model:", f"{test_acc:.4f}")

if __name__ == "__main__":
    main()
    


    