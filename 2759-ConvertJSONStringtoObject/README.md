Given a string str, return parsed JSON parsedStr. You may assume the str is a valid JSON string hence it only includes strings, numbers, arrays, objects, booleans, and null. str will not include invisible characters and escape characters. 

Please solve it without using the built-in JSON.parse method.

 
Example 1:

Input: str = '{"a":2,"b":[1,2,3]}'
Output: {"a":2,"b":[1,2,3]}
Explanation: Returns the object represented by the JSON string.

Example 2:

Input: str = 'true'
Output: true
Explanation: Primitive types are valid JSON.

Example 3:

Input: str = '[1,5,"false",{"a":2}]'
Output: [1,5,"false",{"a":2}]
Explanation: Returns the array represented by the JSON string.

 
Constraints:


	str is a valid JSON string
	1 <= str.length <= 105

