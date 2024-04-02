from dotenv import load_dotenv
import os
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import person_intel_parser, PersonIntel

def ice_break(name: str) -> str:
    
    information = """ 
    Back to OpenAI. Built a small team, launched a model to ChatGPT, great pleasure to build with the top notch talent within.
    2017 - 2022

    I was the Sr. Director of AI at Tesla, where I led the computer vision team of Tesla Autopilot. This includes in-house data labeling, neural network training, the science of making it work, and deployment in production running on our custom inference chip. Today, the Autopilot increases the safety and convenience of driving, but the team's goal is to develop and deploy Full Self-Driving to our rapidly growing fleet of millions of cars. Our Aug 2021 Tesla AI Day provides the most detailed and up-to-date overview of this effort.
    """

    summary_template = """ 
    Given the Linkedin information {information} about a person I want you to create:
    1. short summary
    2. two interesting facts about them
    3. A topic that may interest them 
    4. 2 creative ice breakers to open a conversation with them
    """
    # \n {format_instructions}

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        # partial_variables={"format_instructions": person_intel_parser.get_format_instructions()}
    )

    # llm = Ollama(model="llama2")
    llm = Ollama(model="mistral")
    
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # res = chain.invoke(input={"information": scrape_linkedin_profile()}) # simple llm chain

    linkedin_profile_url = linkedin_lookup_agent(name)
    print(f"linkedin_profile_url: {linkedin_profile_url}")
    result = chain.invoke(input={"information": linkedin_profile_url})  # agents

    return result
    # print(person_intel_parser.parse(result))
    # return person_intel_parser.parse(result)

if __name__ == "__main__":
    load_dotenv()
    print("hello langchain!")

    result = ice_break(name="akshaykumarcp linkedin")
    """ Here's a summary, two interesting facts, and an image for the person you described:\n\nSummary:\nAkshay Kumar C P is a highly skilled structural engineering graduate with a passion for technology and innovation. He has extensive experience in machine learning, artificial intelligence, data engineering, and programming, and is always looking to expand his knowledge and skills. In his free time, Akshay enjoys reading articles on future technologies and attending tech conferences.\n\nInteresting Facts:\n\n1. Akshay is an associate volunteer at ISKCON International Society for Krishna Consciousness, where he helps with various activities related to arts and culture.\n2. Despite his technical background, Akshay has a hidden talent for writing poetry and articles on future technologies. He has published several articles on LinkedIn Pulse and is looking to explore this passion further.\n\nImage: A photo of Akshay Kumar C P with a futuristic backdrop, showcasing his interest in technology and innovation.\n\nI hope this helps! Let me know if you have any other questions."} """
