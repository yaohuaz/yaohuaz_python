import re
import json


if __name__ == '__main__':
    filename = 'tmp.txt'
    f_content = open(filename, 'r').read()

    # will cover escape situation
    f_content = f_content.replace('\\\\', '\\')
    f_content = f_content.replace('\\', '\\\\')
    
    f_table = json.loads(f_content)['Replace']
    print(f_table)

    tmp_strs = ['Moon', 'moon', 'tmp01']
    for i in range(len(tmp_strs)):
        for from_str, to_str in f_table.items():
            replaced = re.sub(from_str, to_str, tmp_strs[i])
            if replaced != tmp_strs[i]:
                tmp_strs[i] = replaced
                break

    print(tmp_strs)
