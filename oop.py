class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)
class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)

    def calculate_class_average(self):
        total_scores = [student.calculate_average() for student in self.students.values()]
        return sum(total_scores) / len(total_scores)

    def display_student_performance(self):
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Student: {name}, Average: {average:.2f}, Status: {status}")
def main():
    print(f"Class Average: {tracker.calculate_class_average():.2f}")

if __name__ == "__main__":
    main()