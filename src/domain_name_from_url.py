# Extract the domain name from a url from CodeWars
import codewars_test as test

def domain_name_alexis(url):
    out = ''
    if url.startswith('www.'):
        out = url.split('.')[1]
    elif url.startswith('http://www.'):
        out = url.split('.')[1]
    elif url.startswith('http://'):
        out = url.split('.')[0].split('/')[2]
    elif url.startswith('https://'):
        out = url.split('.')[0].split('/')[2]
    else:
        out = url.split('.')[0]
    return out

def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]

test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")
test.assert_equals(domain_name("icann.org"), "icann")

