## hour converter


s = '12:40:22AM'
time_list = ['12:40:22AM', '01:10:22AM', '12:00:00PM']


def convert_stamp(s):
    if s[-2:] == 'AM' and s[:2] != '12':
        new_stamp = "{}".format(s[:-2])
        return (new_stamp)
    if s[-2:] == 'PM' and s[:2] == '12':
        converter = str(int(s[:2]) - 12)
        new_stamp = s[:-2]
        return (new_stamp)
    if s[-2:] == 'PM' and s[:2] != 12:
        converter = str(int(s[:2]) + 12)
        new_stamp = "{}{}".format(converter, s[2:-2])
        return (new_stamp)
    if s[-2:] == 'AM' and s[:2] == '12':
        new_stamp = '00{}'.format(s[2:-2])
        return (new_stamp)
        

for i in time_list:
    print (convert_stamp(i))
