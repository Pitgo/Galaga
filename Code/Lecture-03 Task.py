midterm_scores = [8, 5, 7, 8, 9]
final_scores = [3, 10, 7, 6]
all_scores = midterm_scores + final_scores

print(f"{len(midterm_scores)} students took the midterm.")
print(f"{len(final_scores)} students took the final.")
print(f"{len(midterm_scores) - len(final_scores)} students must have dropped the class.")
print(f"Final scores ranged from {min(all_scores)} - {max(all_scores)}")