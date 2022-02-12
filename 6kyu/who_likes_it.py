# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python

def likes(names):
    # how many names?
    names_len = len(names)

    if names_len <= 1:
        end_text = " likes this"
    else:
        end_text = " like this"

    if names_len == 0:
        pre_text = "no one"
    if names_len == 1:
        pre_text = names[0]
    if names_len == 2:
        pre_text = names[0] + " and " + names[1]
    if names_len == 3:
        pre_text = ", ".join([names[0], names[1]]) + " and " + names[2]
    if names_len > 3:
        pre_text = ", ".join([names[0], names[1]]) + " and " +  \
        str(len(names[2:])) + " others"

    return pre_text + end_text


print(likes([]))
print(likes(['Peter']))
print(likes(['Peter', 'Jacob']))
print(likes(['Peter', 'Jacob', 'Alex']))
print(likes(['Peter', 'Jacob', 'Alex', 'Matt']))
print(likes(['Peter', 'Jacob', 'Alex', 'Matt', 'Mike']))
print(likes(['Peter', 'Jacob', 'Alex', 'Matt', 'Mike', 'Missy']))
print(likes(['Peter', 'Jacob', 'Alex', 'Matt', 'Mike', 'Missy', 'Ellie']))

