# Your first gradebook
# AI Anytime Academy — Python from zero
# Passed 100% of graded checks on 2026-11-21
# https://academy.aianytime.net/learn/python-basics

def average(scores):
    if not scores:
        return 0.0
    total = 0
    for s in scores:
        total = total + s
    mean = total/len(scores)
    return round(mean,1)

def letter_grade(score):
    """A for 90+, B for 75+, C for 60+, D for 40+, otherwise F."""
    if score >= 90:
        return "A"
    elif score>= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
    pass


def top_student(marks):
    """marks is a dict like {"Asha": 82}. Return the name with the highest score."""
    max = 0
    top_name = ""
    best_score = -1
    for name, score in marks.items():
        if score > max or (score == best_score and name < top_name):
            best_score = score
            max = score
            top_name = name
    return top_name
    pass


def passed(marks, cutoff=40):
    """Names that scored at least cutoff, sorted alphabetically."""
    p = []
    for name, score in marks.items():
        if score >= cutoff:
            p.append(name)
    return sorted(p)
    pass


def count_words(text):
    """Lowercase word -> count. Ignore the characters . , ! ?"""
    text = text.lower()
    for ch in ".,!?":
        text = text.replace(ch,"")
    count = {}

    for word in text.split():
        count[word] = count.get(word, 0) + 1
    return count
    pass
