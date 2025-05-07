# try:
#     import sys
#     import os
#     import traceback

#     def handle_exception(exc_type, exc_value, exc_traceback):
#         if issubclass(exc_type, KeyboardInterrupt):
#             sys.__excepthook__(exc_type, exc_value, exc_traceback)
#             return
#         # Log the exception to a file
#         with open("error_log.txt", "a") as f:
#             f.write("Uncaught exception:\n")
#             traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)
#         # Print the exception to the console
#         print("Uncaught exception:", exc_value)

#     sys.excepthook = handle_exception
# except ImportError:
#     print("Error: Required modules not found. Please ensure you have the necessary dependencies installed.")

# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
#     with open("error_log.txt", "a") as f:
#         f.write(f"Unexpected error: {e}\n")
#         trace
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
#     with open("error_log.txt", "a") as f:
#         f.write(f"Unexpected error: {e}\n")
#         trace
try:
    # Open the file "sample.txt" in read mode
    file = open("sample.txt", "r")
    # Read the entire contents of the file into the variable 'data'
    data = file.read()
# If the file does not exist, handle the exception
except FileNotFoundError:
    # Print an error message if the file is not found
    print("File not found.")
# This block will execute no matter what (whether an exception occurred or not)
finally:
    # Close the file to free up system resources
    file.close()
