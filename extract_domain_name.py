# https://www.codewars.com/kata/514a024011ea4fb54200004b/solutions/python

def domain_name(url):
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")

    return url.split(".")[0]

