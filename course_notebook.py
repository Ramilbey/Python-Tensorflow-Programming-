# Python and TensorFlow Course Notebook
# This file will be used to store codes and notes learned throughout the course.

def main():
    print("Welcome to the Python and TensorFlow Programming Course!")
    
    # Check if TensorFlow is available (once installed)
    try:
        import tensorflow as tf
        print(f"TensorFlow version: {tf.__version__}")
    except ImportError:
        print("TensorFlow is not installed yet. You can install it using: pip install tensorflow")

if __name__ == "__main__":
    main()
