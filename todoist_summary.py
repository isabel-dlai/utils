import requests
from datetime import datetime, timedelta
from openai import OpenAI
from dotenv import load_dotenv
import os
from todoist_task_utils import get_completed_weekly_tasks, get_current_tasks

# Load environment variables from .env file
load_dotenv()

def generate_summary(completed_tasks, current_tasks):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    completed_tasks_formatted = "\n".join([f"- {task}" for task in completed_tasks])
    current_tasks_formatted = "\n".join([f"- {task['content']}" for task in current_tasks])

    prompt = f"""
    Please summarize the following completed tasks from the past week, highlighting the most 
    important accomplishments. Also, prioritize the remaining tasks for the coming week and 
    mention any challenges, blockers, delays, or help needed. Do not include any extra 
    information in your response; only include the summary in the format below. Be concise, 
    with each task condensed to no more than 20 words. Include the project name in the task 
    explanation. Do NOT add more information to each task.

    Follow this process:
    1. Identify the most important 4-6 tasks that are completed.
    2. Summarize each task in 20 words or fewer, highlighting why it's important
    3. Group the tasks by project
    4. Do the same steps 1-3 but this time for outstanding tasks.
    5. Consider what 0-2 blockers might be for upcoming tasks. Zero blockers is fine as applicable.
    6. Format the tasks in the SUMMARY FORMAT below. Use natural English, not JSON

    Here's an example. Instead of saying "Comprehensive update and upload of MLEP course content 
    to Coursera, enhancing course availability." just say "Comprehensive update and upload of MLEP 
    course content to Coursera."

    Completed tasks:
    {completed_tasks_formatted}

    Current tasks:
    {current_tasks_formatted}

    SUMMARY FORMAT:
    Date: MM/DD/YYYY
    Accomplishments:
    - Completed activities and notable victories.
    Priorities for the coming week:
    - Prioritized tasks
    Challenges/Blockers/Delays/Help needed/Solutions:
    - Any challenges, blockers, delays, or areas where help is needed, along with potential solutions.
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    summary = response.choices[0].message.content.strip()
    return summary

def save_summary(summary):
    today = datetime.now().date()
    previous_monday = today - timedelta(days=today.weekday())
    summary_file_name = f"Work summary week of {previous_monday.strftime('%Y-%m-%d')}.txt"
    with open(summary_file_name, 'w') as file:
        file.write(summary)
    print(f"Summary saved to {summary_file_name}")

def main():
    completed_tasks = get_completed_weekly_tasks()
    current_tasks = get_current_tasks() 

    summary = generate_summary(completed_tasks, current_tasks)

    save_summary(summary)

if __name__ == '__main__':
    main()