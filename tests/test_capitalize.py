from main_package.capitalize import capitalize

assert capitalize('hello') == 'Hello'
assert capitalize('') == ''
assert capitalize('2') == '2'
assert capitalize(' ') == ' '