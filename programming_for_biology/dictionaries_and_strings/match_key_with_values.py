#!/usr/bin/env python3

if __name__ == "__main__":
    l = ['nwnnnwwnnd', 'wdnndnnwwn', 45, 'nwwwnwnnnwd', 'dnwndddnw', 'nnnwdwdndd',
     'ndnnwwnwnn', 'nwdnnnnnww', 'dnddwndnd', 'wwnwdnnwdw', 'dwndwnnnd', 17, 
     'nwddwwnnnnw', 'nnwndwwddw', 'wnwnwnwnd', 'wdwwwnnnw', 'nnwnddnnw', 
     'nwdnndwnww', 81, 'wnwwwwwnnnw', 'nwndnnnnnww', 31]
    d = {'wnwwwwwnnnw': 48, 'nwndnnnnnww': 97, 'nnwdwdddnw': 63, 'nwndnnnnww': 45,
     'nwdnndnwnww': 39, 'nnwndddnnw': 82, 'wdnndnnwwn': 11, 'nnnwwwwnwdn': 31, 
     'dnwwwnnddw': 66, 'wnwnwnwnd': 89, 'dwdwwdnndww': 17, 'nnwnddnwnww': 80, 
     'dndwwnwwwwd': 94, 'nwwdnnwnd': 88, 'nwnnnwwnnd': 58, 'ndnwwnwwwd': 4, 
     'nwnwdwdnw': 45, 'nwwwnwnnnwd': 70, 'wdnnwnndnnd': 95, 'ndnddnwwwwn': 45, 
     'nwdnndddwd': 7, 'nwdnnnnnww': 5, 'nnwwnddnnwn': 45, 'nndwdnwwwwd': 29, 
     'nnwwdwddnww': 17, 'wnnwnnwnn': 24, 'dnwndddnw': 99, 'wwdnwwwndn': 36, 
     'wwwwwnndwn': 31, 'nwdnndwnww': 43, 'nwnndwwwwnd': 9, 'wdwwnnnnw': 71}
    key_list = [1 if potential_key in d else 0 for potential_key in l]
    print(key_list)