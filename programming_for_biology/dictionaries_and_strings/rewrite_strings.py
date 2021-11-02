#!/usr/bin/env python3

def change_case(s):
    return "".join(letter.upper() if i % 10 < 5 else letter.lower() for i, letter in enumerate(s))

if __name__ == "__main__":
    s = "EyErnYRrJbBOzzHdYQJbvrXYxMlFWwhVpsYIpCnBsiytDkeCPWaKVLFvYNEpOOkF"
    changed_case = change_case(s)
    length = len(changed_case)
    print(f"{changed_case}{length: 10}")