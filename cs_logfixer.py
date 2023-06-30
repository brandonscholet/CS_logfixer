import argparse
import re

# Create a command-line argument parser
parser = argparse.ArgumentParser(description="Process log output")
parser.add_argument("log_file", help="path to log file")

# Parse the command-line arguments
args = parser.parse_args()

# Read the log from the file
with open(args.log_file, "r") as f:
    log = f.read()

# Remove the lines with timestamp and "received output"
log = re.sub(r"\n\n\d{2}/\d{2}\s\d{2}:\d{2}:\d{2}\s\w+\s\[output\]\nreceived output:\n", "", log)

print(log)
