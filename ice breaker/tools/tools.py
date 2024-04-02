from langchain.serpapi import SerpAPIWrapper


def get_profile_url(text: str) -> str:
    """Searches for linkedin profile page"""

    # TODO: update serpAPIwrapper such that run() returns linkedin url 
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
