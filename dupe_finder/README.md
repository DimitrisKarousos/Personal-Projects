# Overview
This is a small Python tool to notify the user for duplicate files in a given directory.
Intended for use in small throwaway files, in windows computers.

## Setup:
Before using, open the '.env.example' file and set the desired directory path as the value of 'TRGT'.
Save the file before closing and then rename it to '.env'.
To execute, double-click the 'run' file.

The script will display by name the files it has determined to be duplicates in the provided directory tree.
The script will NOT delete duplicated files.
The script checks for matching names and sizes to assign a file as duplicate.
The script will provide a 'confidence' value to express the accuracy of the result.

A confidence value of 1 means that only one of the checks succeeded, while a value of 2 means that both checks succeeded.
