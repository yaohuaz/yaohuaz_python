import argparse
LOGIC_OPERATORS = ['eq',
                   'ne',
                   'gt',
                   'lt',
                   'gteq',
                   'lteq'
                   ]

class CustomCheckAction(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        val_1, logic_operator, val_2 = values
        if logic_operator not in LOGIC_OPERATORS:
            raise RuntimeError('Invalid logic operator: {}.\nLOGIC_OPERATORS: {}'.format(logic_operator, LOGIC_OPERATORS))
        try:
            int(val_1)
            int(val_2)
            if len(val_1.split('.')) != 1 or len(val_2.split('.')) != 1:
                raise RuntimeError()
        except:
            raise RuntimeError('Values should be integer.')
        setattr(args, self.dest, values)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action=CustomCheckAction, 
                        nargs=3, required=True,
                        metavar=('Val_1', 'Logic_Operator', 'Val_2'),
                        help='check if logic is true')
    args, _ = parser.parse_known_args()
    if args.check:
        val_1, logic_operator, val_2 = args.check
        if logic_operator == 'eq':
            print(val_1 == val_2)
        if logic_operator == 'ne':
            print(val_1 != val_2)
        if logic_operator == 'gt':
            print(val_1 > val_2)
        if logic_operator == 'lt':
            print(val_1 < val_2)
        if logic_operator == 'gteq':
            print(val_1 >= val_2)
        if logic_operator == 'lteq':
            print(val_1 <= val_2)


