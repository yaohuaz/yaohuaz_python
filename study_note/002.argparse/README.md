# Argparse

## Allowable Value of Argument
Suppose nargs > 1
- if all nargs come from same container, directly using `choices`
- otherwise, may need create custom action
	- sample: `01.custom_action.py`: check if integer_1 [logic_operator] integer_2 is true
	- logic_operators = `['eq', 'gt', 'lt', 'ne', 'gteq', 'lteq']`
	- `$ python3 01.custom_action --check [val_1] [logic_operator] [val_2]`
