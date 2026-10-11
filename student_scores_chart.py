import matplotlib.pyplot as plt

def process_and_visualize_scores():
    sample_data = [
        {"name": "Vishnu", "score": 85},
        {"name": "Akhila", "score": 92},
        {"name": "Rahul", "score": 78},
        {"name": "Arjun", "score": 90},
        {"name": "Eva", "score": 88}
    ]
    
    scores = [student["score"] for student in sample_data]
    names = [student["name"] for student in sample_data]
    
    average_score = sum(scores) / len(scores) if scores else 0
    print(f"Average Student Score: {average_score:.2f}")
    
    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, scores, color='skyblue')
    
    plt.axhline(y=average_score, color='r', linestyle='--', label=f'Average ({average_score:.2f})')
    
    plt.title('Student Test Scores')
    plt.xlabel('Student Name')
    plt.ylabel('Score')
    plt.ylim(0, 100)
    plt.legend()
    
    
    filename = 'student_scores_chart.png'
    plt.savefig(filename)
    print(f"Bar chart successfully saved to '{filename}'")

if __name__ == "__main__":
    process_and_visualize_scores()
