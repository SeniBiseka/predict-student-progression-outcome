
# Student and Staff Data Tracker with Histogram Visualization

This Python script allows staff and students to input academic data (PASS, DEFER, and FAIL credits) and then generates a summary report with a histogram visualization using the graphics.py module. The program tracks various outcomes such as "Progress," "Trailer," "Retriever," and "Exclude" based on user input. The results are saved in a text file and visually displayed in a histogram.


## Features

- Data Input: The program prompts the user to enter their total PASS, DEFER, and FAIL credits.

- Outcome Classification: The program classifies the outcomes into four categories:
  - Progress: If the student has 120 PASS credits.

  - Progress (module trailer): If the student has 100 PASS credits.

  - Module Retriever: If the student has more PASS and DEFER credits than FAIL credits.

  - Exclude: If the total FAIL credits are greater than the combined PASS and DEFER credits.

- Data Storage: The input data is stored in a list and can be accessed later.

- Text File Output: The inputted data is saved to a text file named progression_outcomes.txt.

- Histogram Visualization: The program uses the graphics.py module to display a histogram based on the input data.

