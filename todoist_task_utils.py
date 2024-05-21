import os
import datetime
import requests
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI


def get_completed_weekly_tasks():
    # Load environment variables from .env file
    load_dotenv()

    # Get the API token from an environment variable
    API_TOKEN = os.environ["TODOIST_API_TOKEN"]

    # Calculate the dates for the previous Monday and Sunday
    today = datetime.date.today()
    last_monday = today - datetime.timedelta(days=today.weekday() + 7)
    last_sunday = last_monday + datetime.timedelta(days=6)

    # Set up the API request parameters
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    params = {
        "since": last_monday.strftime("%Y-%m-%dT00:00:00"),
        "until": last_sunday.strftime("%Y-%m-%dT23:59:59"),
    }

    try:
        # Make the API request to get completed tasks
        response = requests.get(
            "https://api.todoist.com/sync/v9/completed/get_all", headers=headers, params=params
        )
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        # Extract the completed tasks from the response
        completed_tasks = response.json()["items"]

        # Create a dictionary to store project names
        project_names = {}

        # Retrieve project names for each completed task
        for task in completed_tasks:
            project_id = task["project_id"]
            if project_id not in project_names:
                # Make an API request to get the project details
                project_response = requests.get(
                    f"https://api.todoist.com/sync/v9/projects/get?project_id={project_id}",
                    headers=headers,
                )
                project_response.raise_for_status()
                project_data = project_response.json()
                project_names[project_id] = project_data["project"]["name"]

        # Create a collection of completed tasks with project names
        task_collection = []
        for task in completed_tasks:
            project_name = project_names.get(task["project_id"], "Unknown Project")
            task_collection.append({
                "completed_at": task["completed_at"],
                "project_name": project_name,
                "content": task["content"]
            })

        return task_collection

    except Exception as error:
        print(f"Error: {error}")
        return None

def get_current_tasks():
    # Load environment variables from .env file
    load_dotenv()

    # Get the API token from an environment variable
    API_TOKEN = os.environ["TODOIST_API_TOKEN"]

    # Initialize the Todoist API client
    api = TodoistAPI(API_TOKEN)

    try:
        # Retrieve all active tasks
        tasks = api.get_tasks()

        # Create a dictionary to store project names
        project_names = {}

        # Retrieve project names for each active task
        for task in tasks:
            project_id = task.project_id
            if project_id not in project_names:
                # Get the project details
                project = api.get_project(project_id)
                project_names[project_id] = project.name

        # Create a collection of tasks with project names
        task_collection = []
        for task in tasks:
            project_name = project_names.get(task.project_id, "Unknown Project")
            task_collection.append({
                "project_name": project_name,
                "content": task.content
            })

        return task_collection

    except Exception as error:
        print(f"Error: {error}")
        return None

if __name__ == '__main__':
    print("Getting upcoming tasks ............................")
    for task in get_current_tasks():
        if task["project_name"] != "Reading List":
          print("Upcoming:", task["project_name"], task["content"])
    
    print("Getting completed tasks ............................")
    for task in get_completed_weekly_tasks():
        print("Completed:", task["project_name"], task["content"])