# test if upper
assert 'foo'.upper() == 'FOO'

# test if upper 2
assert 'FOO'.isupper() == True

# test if upper (false)
assert 'Foo'.isupper() == False

# test split string
s = 'hello world'
assert (s.split() == ['hello', 'world'])