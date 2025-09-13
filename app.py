from flask import Flask, render_template, request, session, redirect, url_for
import random
import requests
import html

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for sessions

# Map simple category names to API categories
categories_map = {
    "Science": "17",
    "Math": "19",
    "General Knowledge": "9"
}

def fetch_question(category_name):
    """
    Fetch a question from Open Trivia DB API or fallback if API fails.
    Returns a dictionary with question, answer, and options.
    """
    category_id = categories_map.get(category_name, "9")  # Default to General Knowledge
    try:
        response = requests.get(f'https://opentdb.com/api.php?amount=1&category={category_id}&type=multiple', timeout=5)
        response.raise_for_status()
        data = response.json()
    except Exception:
        data = {}

    # If API fails or returns no results, provide a fallback question
    if 'results' not in data or not data['results']:
        return {
            "question": "API not available. What is 2 + 2?",
            "answer": "4",
            "options": ["3", "4", "5", "6"]
        }

    question_data = data['results'][0]

    # Combine correct and incorrect answers, unescape HTML, shuffle
    options = question_data['incorrect_answers'] + [question_data['correct_answer']]
    options = [html.unescape(opt) for opt in options]
    random.shuffle(options)

    return {
        "question": html.unescape(question_data['question']),
        "answer": html.unescape(question_data['correct_answer']),
        "options": options
    }

@app.route('/')
def home():
    return render_template('index.html', name="M K Chetan")


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    categories = list(categories_map.keys())

    if request.method == 'POST':
        category_name = request.form.get('category')
        session['category'] = category_name
        session['score'] = 0
        session['question_number'] = 1

        question = fetch_question(category_name)
        progress_width = (session['question_number'] * 100) // 10  # compute for progress bar

        return render_template(
            'quiz_page.html',
            question=question,
            category=category_name,
            score=session['score'],
            question_number=session['question_number'],
            progress_width=progress_width
        )

    return render_template('quiz_select.html', categories=categories)


@app.route('/check_answer', methods=['POST'])
def check_answer():
    user_answer = request.form.get('user_answer')
    correct_answer = request.form.get('correct_answer')
    category = request.form.get('category')
    question_number = int(request.form.get('question_number'))

    # Initialize session if missing
    if 'score' not in session:
        session['score'] = 0

    # Update score
    if user_answer == correct_answer:
        session['score'] += 1
        result = "Correct ✅"
    else:
        result = f"Wrong ❌ | Correct answer: {correct_answer}"

    # Next question
    question_number += 1
    session['question_number'] = question_number

    if question_number > 10:
        # Quiz finished
        final_score = session['score']
        session.pop('score', None)
        session.pop('question_number', None)
        return render_template('quiz_result.html', final_score=final_score, total_questions=10)

    # Fetch next question
    question = fetch_question(category)
    progress_width = (question_number * 100) // 10

    return render_template(
        'quiz_page.html',
        question=question,
        category=category,
        score=session['score'],
        result=result,
        question_number=question_number,
        progress_width=progress_width
    )


if __name__ == "__main__":
    app.run(debug=True)
