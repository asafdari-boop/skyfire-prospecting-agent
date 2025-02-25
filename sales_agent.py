from skyfire import configuration
from crewai import Agent, Task, Crew, Process
from tools import *

skyfire_sales_agent = Agent(
    role="Sales Prospecting Specialist",
    goal="Find decision-makers at companies and pitch Skyfire's capabilities.",
    backstory="An expert in B2B sales and partnerships, skilled at identifying key decision-makers and crafting persuasive outreach.",
    verbose=True,
    tools=[find_company_employees, find_person_on_linkedin]
)

# Task 1: Find Key Employees
find_employees_task = Task(
    description="Find key decision-makers at {company_name} using by using linkedin find_company_employees and then find_person_on_linkedin. "
                "Return a list of potential contacts.",
    expected_output="A list of employees with names, titles, and email addresses.",
    agent=skyfire_sales_agent
)

# Task 2: Draft Outreach Emails
draft_email_task = Task(
    description="Generate a personalized email for each prospect from {company_name}. "
                "Highlight Skyfire's capabilities and how it can integrate with their services.",
    expected_output="A well-structured email ready for sending.",
    agent=skyfire_sales_agent
)

# Task 3: Send Emails
# send_email_task = Task(
#     description="Send the drafted emails to decision-makers at {company_name} using the Skyfire Email API.",
#     expected_output="Confirmation that emails were sent successfully.",
#     agent=skyfire_sales_agent
# )

skyfire_sales_crew = Crew(
    agents=[skyfire_sales_agent],
    tasks=[find_employees_task, draft_email_task],
    process=Process.sequential  # Executes tasks in order
)

# Kick off the workflow for multiple companies
target_companies = [
    "crewai-inc",
    # Add more companies as needed
]

results = {}
for company_name in target_companies:
    print(f"\nProcessing company: {company_name}")
    result = skyfire_sales_crew.kickoff(inputs={"company_name": company_name})
    results[company_name] = result

# Print summary of results
print("\nSummary of Results:")
for company, result in results.items():
    print(f"\n{company}:")
    print(result)
