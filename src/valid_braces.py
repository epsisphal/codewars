# Valid braces from CodeWars

import codewars_test as test

def valid_braces_alexis(string):
	elements = ["(", "[", "{", ")", "]", "}"]
	for i in range(0, int(len(string)/2)):
		closing_elements_positions = [string.find(")"), string.find("]"), string.find("}")]
		if any(i > 0 for i in closing_elements_positions):
			first_closing_position = min([i for i in closing_elements_positions if i > 0])
		else:
			first_closing_position = 0
		if first_closing_position > 0 and elements.index(string[first_closing_position]) - elements.index(string[first_closing_position-1]) == 3:
			string = string[:first_closing_position-1] + string[first_closing_position+1:]
	return True if len(string) == 0 else False

def valid_braces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

def assert_valid(string):
    test.assert_equals(valid_braces(string), True, 'Expected "{0}" to be valid'.format(string))

def assert_invalid(string):
    test.assert_equals(valid_braces(string), False, 'Expected "{0}" to be invalid'.format(string))

@test.describe("Valid Braces")
def tests():
	@test.it("sample Tests")
	def sample_tests():
		assert_valid( "()" )
		assert_invalid( "(}" )
		assert_valid( "[]" )
		assert_invalid("[(])")
		assert_valid( "{}" )
		assert_valid( "{}()[]" )
		assert_valid( "([{}])" )
		assert_invalid( "([}{])" )
		assert_valid( "{}({})[]" )
		assert_valid( "(({{[[]]}}))" )
		assert_invalid( "(((({{" )
		assert_invalid( ")(}{][" )
		assert_invalid( "())({}}{()][][" )

# valid_braces("[(])")
# valid_braces("{}()[]")

# print(valid_braces(")(}{]["))
# print(valid_braces("())({}}{()][]["))

# print(valid_braces("()"))

