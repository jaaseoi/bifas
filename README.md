# bifas
Secure ledger system, near real-time payment processing time and market deterministic transaction fee all in BIFAS.

# Where to get it
The source code is currently hosted on GitHub at: https://github.com/jaaseoi/bifas.

# Code Standards for Contribution

## Environment
1.	The minimum Python version supported is **3.9**.
2.	Your code is expected to be executable on **Windows**, **MacOS** and **Linux**.

## State Management
1.	**No global states or variables**, all stateful operations should be implemented as **classes**.
2.	**Limit the use of helper functions** only to generic operations that are shared among multiple parts of the code.
3.	**Avoid returning multiple values** from a function, instead consider to **returning a class instance**.

## Name Conventions
1.	Always use **snake_case** for **variable** and **function name**, and use **PascalCase** for **class names**, **UPPERCASE** for **constants**.
2.	Try at all costs to give a proper, **clear name** to your **variables**, **functions**, **arguments**, and **classes**, from which the user can directly understand its purposes.
3.	Class initialization and function calls should use **named arguments**.

## Documentation
1.	For each **publicly available class and functions**, **document their purpose, parameters, and returns** in the docstring format along with your code. Read this [guide](https://pandas.pydata.org/docs/development/contributing_docstring.html).
2.	Keep the documentation simple and precise, no need to repeat what is already obvious in their names, no need to include implementation details (make in-line comments instead).

## Code Commits
1. Create a **branch for each feature** that you are working on. Submit a **Pull Request** to respective branch for merging.