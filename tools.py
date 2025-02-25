import skyfire_sdk
from crewai.tools import tool
import crewai_tools
from skyfire import configuration
import pydantic_core

@tool
def find_company_employees(company_name: str) -> list:
    """Finds employees at a company using LinkedIn Employee Search"""
    with skyfire_sdk.ApiClient(configuration) as api_client:
        api_instance = skyfire_sdk.VetricApi(api_client)
        employees = api_instance.linked_in_company_people_search(company_name)
        print("company ", company_name, "employees")
        return employees  # Returns list of employee data

@tool
def find_person_on_linkedin(name: str, company_name: str = None) -> dict:
    """Search for a specific person on LinkedIn"""
    with skyfire_sdk.ApiClient(configuration) as api_client:
        api_instance = skyfire_sdk.VetricApi(api_client)
        person = api_instance.linked_in_people_search(
            keywords=name,
            location_urns=None,
            first_name=None,
            last_name=None,
            title=None,
            company_name=company_name,
            current_company=None,
            past_company=None,
            cursor=None
        )
        print("person ", name, person)
        return person  # Returns person details if found

@tool
def send_email(recipient_email: str, subject: str, email_body: str) -> str:
    """Sends an email to a prospect via Skyfire API"""
    with skyfire_sdk.ApiClient(configuration) as api_client:
        api_instance = skyfire_sdk.ToolkitApi(api_client)
        api_response = api_instance.send_email(
            email_dump_request={'recipient_email': recipient_email, 'email_data': email_body}
        )
    return f"Email sent to {recipient_email}"


if __name__ == "__main__":
    # with skyfire_sdk.ApiClient(configuration) as api_client:
    #     api_instance = skyfire_sdk.VetricApi(api_client)
    #     api_response = api_instance.linked_in_job_search('cisco')
    #     print(api_response)
        # except pydantic_core._pydantic_core.ValidationError as e:
        #     print("Validation error occurred:", e)
    # get a company's employees given their linkedIn identifier
    with skyfire_sdk.ApiClient(configuration) as api_client:
        api_instance = skyfire_sdk.VetricApi(api_client)
        api_response = api_instance.linked_in_company_employees('tryskyfire')

    with skyfire_sdk.ApiClient(configuration) as api_client:
        api_instance = skyfire_sdk.VetricApi(api_client)
        api_response = api_instance.linked_in_people_search("ammar safdari")