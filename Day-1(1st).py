student_scores = np.random.randint(50, 101, (32, 4))
subject_averages = np.mean(student_scores, axis=0)
subjects = ['Math', 'Science', 'English', 'History']
highest_avg_index = np.argmax(subject_averages)
for subject, avg in zip(subjects, subject_averages):
    print(f"{subject}: {avg:.2f}")

print(f"\nSubject with highest average score: {subjects[highest_avg_index]}")
