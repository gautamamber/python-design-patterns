"""
Visitor Design patterns: It is one of the Behavioral design pattern.
It separate the algorithm from an object structure on which it operates
It helps us to add new features to an existing class hierarchy dynamically without changing it.
A visitor pattern consist two parts:
1. method name visit() implemented by the visitor and used and called
for every element of the data structure
2. Visitable classes providing Accept() methods that accept a visitor
"""