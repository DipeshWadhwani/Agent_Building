from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='Youre a travel agent. Help user to plan their vacation',
    instruction='Give proper plan to the user.',
)
