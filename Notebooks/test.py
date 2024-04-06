from jsonpath_ng import parse
document = { 
	"people": [
		{"name": "Alice", "age": 28},
	]
}
try:
    expr = parse("$.people[?(@.age > 30)]")
    
    for match in expr.find(document):
        print(match.value)
        
except Exception as e:
    print(f"Error: {str(e)}")
