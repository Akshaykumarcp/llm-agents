import os
import requests


# def scrape_linkedin_profile(linkedin_profile_url: str): # scrape based on dynamic linkedin profile name
def scrape_linkedin_profile():
    """scrape information from linkedin profiles.
    Manually scrape the information from the linkedin profile"""

    api_endpoint = "https://gist.githubusercontent.com/Akshaykumarcp/62fa0761c8cb950f09d870b7e95efa4d/raw/2b2008912f12059d8d5c1beb75a9bd28ddeb5b4e/akshaykumarcp_linkedin_profile_json.json"

    response = requests.get(api_endpoint)

    # has empty values, remove them due to token limit
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certificatios"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
