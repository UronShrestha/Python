# Challenge — Build a Frozenset Analyzer
"""
Create a program that starts with:

set_a = frozenset({1, 2, 3, 4, 5})
set_b = frozenset({4, 5, 6, 7, 8})

Your program should display:

========== FROZENSET ANALYZER ==========

Set A: ...
Set B: ...

1. Copy Set A
2. Difference A - B
3. Difference B - A
4. Intersection
5. Check Disjoint
6. Check A is Subset of B
7. Check A is Superset of B
8. Symmetric Difference
9. Union
10. Exit

The user should enter a choice:

Enter your choice: 4

Output:

Intersection: frozenset({4, 5})
"""

set_a = frozenset({1, 2, 3, 4, 5})
set_b = frozenset({4, 5, 6, 7, 8})
while True:
   print("\n========== FROZENSET ANALYZER ==========")
   print(f"\nSet A : {set_a}")
   print(f"Set B : {set_b}")
   print("\n1. Copy Set A")
   print("2. Difference A - B")
   print("3. Difference B - A")
   print("4. Intersection")
   print("5. Check Disjoint")
   print("6. Check A is Subset of B")
   print("7. Check A is Superset of B")
   print("8. Symmetric Difference")
   print("9. Union")
   print("10. Exit")

   choice = input("\nEnter your choice from 1-10 : ")

   if choice == "1":
      copy_a = set_a.copy()
      print(f"\nCopy of set_a : {copy_a}")
   elif choice == "2":
      diff = set_a-set_b
      print(f"\nDifference A - B : {diff}")
   elif choice == "3":
            diff = set_b-set_a
            print(f"\nDifference B - A : {diff}")
   elif choice == "4":
            diff = set_b&set_a
            print(f"\nIntersection A and B : {diff}")
   elif choice == "5":
        disjoint = set_a.isdisjoint(set_b)
        print(f"\nAre set_a and set_a Disjoint? : : {disjoint}")

   # Check A is Subset of B
   elif choice == "6":
        subset = set_a.issubset(set_b)
        print(f"\nIs set_a subest of set_b? : : {subset}")


   #   Check A is Superset of B
   elif choice == "7":
              superset = set_a.issuperset(set_b)
              print(f"\nIs set_a superset of set_b? : : {subset}")

   # Symmetric Difference
   elif choice == "8":
              symmetricDifference = set_a.symmetric_difference(set_b)
              print(f"\nSymmetric Difference : {symmetricDifference}")

   # Union
   elif choice == "9":
              uni = set_a.union(set_b)
              print(f"\nUnion : {uni}")

   elif choice == "10":
          print("THANK YOU!!!")
          break
   


   else:
      print("Choose from 1-10.")