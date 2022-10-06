# 💻 Assignment 05
## Requirements
- The program must provide a menu-driven console user interface.
- Use classes to represent the following:
    - The domain entity (`complex`,  `expense`,  `student`, `book`)
    - A services class that implements the required functionalities
    - The ui class which implements the user interface
- Have 10 programmatically generated entries in the application at start-up.
- Unit tests and specifications for non-UI functions related to the first functionality.

## Problem Statement
### Expenses
Manage a list of expenses. Each expense has a `day` (integer between 1 and 30), `amount` of money (positive integer) and expense `type` (string). Provide the following features:
1. Add an expense. Expense data is read from the console.
2. Display the list of expenses.
3. Filter the list so that it contains only expenses above a certain value read from the console.
4. Undo the last operation that modified program data. This step can be repeated.
