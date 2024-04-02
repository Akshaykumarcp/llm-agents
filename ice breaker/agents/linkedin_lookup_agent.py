from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from tools.tools import get_profile_url


def lookup(name: str) -> str:
    # llm = Ollama(model="llama2")
    llm = Ollama(model="mistral")

    template = """ given the full name {name_of_person} I want you to get me a link to thier linkedin profile page. Your answer should contain only a url"""

    # https://smith.langchain.com/hub/hwchase17/react
    react_prompt = hub.pull("hwchase17/react")
    """ 
     Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:{agent_scratchpad} """

    tools_for_agent = [
        Tool(
            name="Crawl google 4 linkedin profile page",
            func=get_profile_url,
            description="useful for when you need get the linkedin page url.",
        )
    ]

    # https://python.langchain.com/docs/modules/agents/agent_types/react
    # Construct the ReAct agent
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    # Create an agent executor by passing in the agent and tools

    agent_executor = AgentExecutor(
        agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True
    )

    # agent_executor.invoke(input={"input": promp)
    result = agent_executor.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]

    return linkedin_profile_url
