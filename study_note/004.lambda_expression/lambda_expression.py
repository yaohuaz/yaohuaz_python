if __name__ == '__main__':
    # sorting dict list
    dict_list = [{
        'name': 'cat',
        'val': 1
    },
        {
        'name': 'dog',
        'val': 2
    },
        {
            'name': 'cat',
            'val': 3,
    },
        {
            'name': 'cat',
            'val': 2
    }
    ]
        
    '''
        In this case, sort dict_list by val first, then name.
        Output:
            Ind Name Val
            0   cat  1
            1   cat  2    --\ 
                            | Ind(2, 3) -> cat && dog have same val, 
                            | but str(cat) < str(dog), so (cat, 2) < (dog, 2)
            2   dog  2    --/
            3   cat  3
    '''
    sorted_dict_list = sorted(dict_list, key=lambda k: (k['val'], k['name']))
    print(sorted_dict_list)


    # sorting list 
    # using first 3 elements
    tmp_list = [[4, 2, 1, 3],
                [1, 3, 2, 5, 7],
                [8, 2, 1],
                [7, 4, 2],
                [9, 7, 3]
                ]

    class CustomObj(object):
        def __init__(self, 
                     val: list):
            self.val = val

        def __lt__(self,
                   other):
            for i in range(2, -1 , -1):
                if self.val[i] < other.val[i]:
                    return True
                elif self.val[i] > other.val[i]:
                    return False
            return False

    '''
    sort by two method
    '''
    # lambda expression
    fir_sorted_list = sorted(tmp_list, 
                             key=lambda k:(k[2], k[1], k[0]))
    print(fir_sorted_list)
    # overriding __lt__ method && sorting object list
    sec_sorted_list = sorted(tmp_list,
                             key=CustomObj)
    print(sec_sorted_list)


