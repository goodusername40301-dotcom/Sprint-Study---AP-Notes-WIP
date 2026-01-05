import requests


api_endpoint = "https://api.openai.com/v1/responses"
api_key = "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"


def generate_SAT_question(section, topic, difficulty):
    prompt = f"""
    You are an SAT test writer. Create one original SAT-style question from the section "{section}"
    and the topic "{topic}".

    Difficulty level: {difficulty}

    Difficulty guidelines:
    - Easy: Straightforward wording, minimal traps, clear answer choice.
    - Medium: Moderate complexity, plausible distractors, some reasoning required.
    - Hard: Subtle distinctions, close answer choices, deeper reasoning required.

    Requirements:
    - The question should match official SAT style and tone.
    - Provide exactly 4 answer choices (A–D).
    - Clearly indicate the correct answer.
    - Include a step-by-step explanation justifying why the correct answer is correct
      and why the others are incorrect.
    - Use clear, concise language appropriate for high school students.

    Output format:
    Question
    Answer Choices (A–D)
    Correct Answer
    Explanation
    """

    request_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }

    request_data = {
        "model": "gpt-4.1-mini",
        "input": prompt,
        "max_output_tokens": 750,
        "temperature": 0.5,
    }

    response = requests.post(api_endpoint, headers=request_headers, json=request_data)

    response_text = response.json()["output"][0]["content"][0]["text"]
    return response_text


question = generate_SAT_question("Reading and Writing","Information and Ideas","Hard")

print(question)
