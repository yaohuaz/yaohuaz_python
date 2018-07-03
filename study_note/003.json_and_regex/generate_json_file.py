import os
import json
from collections import OrderedDict

if __name__ == '__main__':
    json_filename = 'test.txt'
    json_file = os.path.join(os.getcwd(), json_filename)

    json_file_content = {
        'Dog': {
            'Breed': ['Bulldog',
                      'Siberian Husky']
        },
        'Cat': {
            'Breed': ['Korat',
                      'Tonkinese']
            }
    }

    json_file_content = OrderedDict(json_file_content)
    f = open(json_file, 'w')
    f.write(json.dumps(json_file_content, indent=4, sort_keys=False))
    f.close()
