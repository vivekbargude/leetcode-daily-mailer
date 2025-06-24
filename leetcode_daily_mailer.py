import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def get_title_slug():
    query = {
        "query": """
        query questionOfToday {
            activeDailyCodingChallengeQuestion {
                date
                link
                question {
                    title
                    titleSlug
                    difficulty
                    topicTags {
                        name
                    }
                }
            }
        }
        """
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post("https://leetcode.com/graphql", json=query, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch daily question")

    data = response.json()['data']['activeDailyCodingChallengeQuestion']
    question = data['question']
    return {
        "title": question['title'],
        "titleSlug": question['titleSlug'],
        "difficulty": question['difficulty'],
        "tags": [tag['name'] for tag in question['topicTags']],
        "link": "https://leetcode.com" + data['link']
    }

def get_full_question_data(title_slug):
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                title
                content
                difficulty
                exampleTestcases
            }
        }
        """,
        "variables": {
            "titleSlug": title_slug
        }
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post("https://leetcode.com/graphql", json=query, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch question details")

    return response.json()['data']['question']

def send_email(subject, body_html):
    sender_email = os.environ['SENDER_EMAIL']
    receiver_email = os.environ['RECEIVER_EMAIL']
    
    password = os.environ['EMAIL_PASSWORD']

    msg = MIMEMultipart("alternative")
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    part = MIMEText(body_html, "html")
    msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def main():
    print("Fetching daily LeetCode problem...")
    basic_info = get_title_slug()
    full_question = get_full_question_data(basic_info["titleSlug"])

    html_body = f"""
    <h2>🧠 LeetCode Daily Challenge: {full_question['title']}</h2>
    <p><b>Difficulty:</b> {full_question['difficulty']}</p>
    <p><b>Tags:</b> {', '.join(basic_info['tags'])}</p>
    <p><a href="{basic_info['link']}">🔗 View Problem on LeetCode</a></p>
    <hr>
    {full_question['content']}
    <hr>
    <h4>Example Testcases:</h4>
    <pre>{full_question['exampleTestcases']}</pre>
    """

    send_email(f"📌 LeetCode Daily Challenge: {full_question['title']}", html_body)
    print("✅ Email sent successfully!")

if __name__ == "__main__":
    main()
