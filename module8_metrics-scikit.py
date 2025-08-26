import numpy as np
from sklearn.metrics import precision_score, recall_score

# Function to read positive integer
def read_positive(prompt: str) -> int:
    try:
        k = int(input(prompt).strip())
        if k > 0:
            return k
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid number. Please enter a positive integer.")

# Function to read binary one by one to provide N (x,y) points 
def read_binary(prompt):
    while True:
        try:
            v = int(input(prompt).strip())
            if v in (0, 1):
                return v
        except ValueError:
            pass
        print("Invalid input. Please enter 0 or 1.")

def main():
    # Read N
    N = read_positive("Enter N, must be a positive integer: ")

    # X = ground-truth labels, Y = predicted labels
    X = np.empty(N, dtype=int)
    Y = np.empty(N, dtype=int)

    print("Enter N pairs (x, y). x is true label, y is predicted label, both x and y should be binary.")
    for i in range(N):
        x = read_binary(f"Sample {i+1} - x: ")
        y = read_binary(f"Sample {i+1} - y: ")
        X[i] = x
        Y[i] = y
    
    # Compute metrics using sklearn
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")


if __name__ == "__main__":
    main()
    


    