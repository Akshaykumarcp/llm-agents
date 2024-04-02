from dotenv import load_dotenv
import os
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain

if __name__ == "__main__":
    load_dotenv()
    print("hello langchain!")

    information = """ 
    Back to OpenAI. Built a small team, launched a model to ChatGPT, great pleasure to build with the top notch talent within.
    2017 - 2022

    I was the Sr. Director of AI at Tesla, where I led the computer vision team of Tesla Autopilot. This includes in-house data labeling, neural network training, the science of making it work, and deployment in production running on our custom inference chip. Today, the Autopilot increases the safety and convenience of driving, but the team's goal is to develop and deploy Full Self-Driving to our rapidly growing fleet of millions of cars. Our Aug 2021 Tesla AI Day provides the most detailed and up-to-date overview of this effort.

    """

    summary_template = """ 
    Given the information {information} about a person I want you to create:
    1. short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = Ollama(model="llama2")
    llm = Ollama(model="mistral")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    res = chain.invoke(input={"information": information})
    print(res)
    """ 
    {'information': " \n    Back to OpenAI. Built a small team, launched a model to ChatGPT, great pleasure to build with the top notch talent within.\n    2017 - 2022\n\n    I was the Sr. Director of AI at Tesla, where I led the computer vision team of Tesla Autopilot. This includes in-house data labeling, neural network training, the science of making it work, and deployment in production running on our custom inference chip. Today, the Autopilot increases the safety and convenience of driving, but the team's goal is to develop and deploy Full Self-Driving to our rapidly growing fleet of millions of cars. Our Aug 2021 Tesla AI Day provides the most detailed and up-to-date overview of this effort.\n\n    ", 'text': ' Sure, here is a potential profile for the person you described:\n\n**Summary:**\nAs the former Sr. Director of AI at Tesla, Sarah Lee is a seasoned expert in computer vision and neural networks. With over a decade of experience in the field, she led the team responsible for developing and deploying the Autopilot system, which has significantly improved the safety and convenience of driving for millions of Tesla owners. Today, Sarah is passionate about her work on Full Self-Driving and is dedicated to making autonomous technology a reality.\n\n**Interesting Facts:**\n\n1. Sarah Lee is an accomplished pianist and has been playing since she was just five years old. She finds that the creative process of music-making helps her approach problems in a more nuanced and innovative way.\n2. Before joining Tesla, Sarah worked at Google Brain, where she contributed to the development of deep learning algorithms for image recognition. She is particularly proud of her work on a project that used AI to identify endangered species in wildlife photos, which was later adopted by conservation organizations around the world.'} """
