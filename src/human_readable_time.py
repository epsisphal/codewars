# Human readable time from CodeWars
import codewars_test as test

def make_readable_alexis(seconds):
    return str(int(seconds/3600/10))+str(int(seconds/3600) % 10)+':'+str(int((seconds/60/10)) % 6)+str(int((seconds/60) % 10))+':'+str(int(seconds/10) % 6)+str(seconds % 10)

def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

test.assert_equals(make_readable(0), "00:00:00")
test.assert_equals(make_readable(5), "00:00:05")
test.assert_equals(make_readable(60), "00:01:00")
test.assert_equals(make_readable(86399), "23:59:59")
test.assert_equals(make_readable(359999), "99:59:59")
