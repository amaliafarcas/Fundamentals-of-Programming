# 💻 Assignment 3

## Requirements
- Use procedural programing and the simple feature-driven software development process
- Provide a command-based console user interface that accepts given commands **exactly** as stated
- Handle the case of incorrect user input by displaying error messages. The program must not crash!
- Use built-in compound types to represent entities in the problem domain and access/modify them using *getter* and *setter* functions
- Have at least 10 items in your application at startup
- Provide **specification** and **tests** for all non-UI functions related to every functionality

## Problem Statement
### Apartment Building Administrator
Jane is the administrator of an apartment building and she wants to manage the monthly expenses for each apartment. Each expense is stored using the following elements: `apartment` (*number of apartment, positive integer*), `amount` (*positive integer*), `type` (*from one of the predefined categories `water`, `heating`, `electricity`, `gas` and `other`*). Write a program that implements the functionalities exemplified below:

**(A) Add new transaction**
`add <apartment> <type> <amount>`\
e.g.\
`add 25 gas 100` – add to apartment 25 an expense for `gas` in amount of `100 RON`

**(B) Modify expenses**\
`remove <apartment>`\
`remove <start apartment> to <end apartment>`\
`remove <type>`\
`replace <apartment> <type> with <amount>`\
e.g.\
`remove 15` – remove all expenses for apartment 15\
`remove 5 to 10` – remove all expenses for apartments between 5 and 10\
`remove gas` – remove all `gas` expenses from all apartments\
`replace 12 gas with 200` – replace the amount of the expense with type `gas` for apartment 12 with `200 RON`
 
**(C)	Display expenses having different properties**\
`list`\
`list <apartment>`\
`list [ < | = | > ] <amount>`\
e.g.\
`list` – display all expenses\
`list 15` – display all expenses for apartment 15\
`list > 100` - display all apartments having total expenses `>100 RON`\
`list = 17` - display all apartments having total expenses `=17 RON`


# 💻 Assignment 4
## New Requirements
- Continue the problem statement started at **A3** by adding its code to this repository
- Implement **modular programming** by having a **UI** module, a **Functions** module and a **Start** module
## Common with A3
- Use procedural programing and the simple feature-driven software development process
- Provide a console-based user interface that accepts given commands **exactly** as required, and works when additional whitespaces are included
- Use built-in compound types to represent entities in the problem domain and access them using *getter* and *setter* functions
- Have at least 10 items in your application at startup
- Provide **specification** and **tests** for all non-UI functions related to every functionality

## Problem Statement
Jane is the administrator of an apartment building and she wants to manage the monthly expenses for each apartment. Each expense is stored using the following elements: `apartment` (*number of apartment, positive integer*), `amount` (*positive integer*), `type` (*from one of the predefined categories `water`, `heating`, `electricity`, `gas` and `other`*). Write a program that implements the functionalities exemplified below:

**(A) Add new transaction**\
`add <apartment> <type> <amount>`\
e.g.\
`add 25 gas 100` – add to apartment 25 an expense for `gas` in amount of `100 RON`

**(B) Modify expenses**\
`remove <apartment>`\
`remove <start apartment> to <end apartment>`\
`remove <type>`\
`replace <apartment> <type> with <amount>`\
e.g.\
`remove 15` – remove all expenses for apartment 15\
`remove 5 to 10` – remove all expenses for apartments between 5 and 10\
`remove gas` – remove all `gas` expenses from all apartments\
`replace 12 gas with 200` – replace the amount of the expense with type `gas` for apartment 12 with `200 RON`

**(C)	Display expenses having different properties**\
`list`\
`list <apartment>`\
`list [ < | = | > ] <amount>`\
e.g.\
`list` – display all expenses\
`list 15` – display all expenses for apartment 15\
`list > 100` - display all apartments having total expenses `>100 RON`\
`list = 17` - display all apartments having total expenses `=17 RON`

**(D) Obtain different characteristics of the expenses**\
`sum <type>`\
`max <apartment>`\
`sort apartment`\
`sort type`\
e.g.\
`sum gas` – display the total amount for the expenses having type `gas`\
`max 25` – display the maximum amount per each expense type for apartment `25`\
`sort apartment` – display the list of apartments sorted ascending by total amount of expenses\
`sort type` – display the total amount of expenses for each type, sorted ascending by amount of money

**(E) Filter**\
`filter <type>`\
`filter <value>`\
e.g.\
`filter gas` – keep only expenses for `gas`\
`filter 300` – keep only expenses having an amount of money smaller than 300 RON

**(F) Undo**\
`undo` – the last operation that modified program data is reversed. The user can undo all operations performed since program start by repeatedly calling this function.

