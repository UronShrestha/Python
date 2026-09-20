# Exercise 5 — Programming Languages
student_a = frozenset({"Python", "Java", "C++", "JavaScript"})
student_b = frozenset({"Python", "Java", "PHP", "Laravel"})

"""Find the languages that only Student A knows.

Expected:

frozenset({'C++', 'JavaScript'})"""

PL = student_a-student_b
print(PL)