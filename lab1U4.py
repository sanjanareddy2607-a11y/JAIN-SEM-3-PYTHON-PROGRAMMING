
# try:
#     # Open the log file in read mode
#     with open("log.txt", "r") as file:
 
#         error_count = 0

#         print("Log File Contents:\n")

#         # Read and display each line
#         for line in file:
#             print(line, end="")

#             # Count ERROR messages
#             if "ERROR" in line:
#                 error_count += 1

#         # Display total number of errors
#         print("\n\nTotal number of ERROR messages:", error_count)

# except FileNotFoundError:
#     print("Error: The file log.txt does not exist.")
    # Open the log file in read mode
with open("log.txt", "r") as file:
 
    error_count = 0

    print("Log File Contents:\n")

        # Read and display each line
    for line in file:
        print(line, end="")