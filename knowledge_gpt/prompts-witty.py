# learning this: https://www.pinecone.io/learn/langchain-prompt-templates/

from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

# initialize the models
openai = OpenAI(
    model_name="text-davinci-003",
    openai_api_key="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"
)

# create our examples
examples = [
    {
        "query": "How are you?",
        "answer": "I can't complain but sometimes I still do."
    }, {
        "query": "What time is it?",
        "answer": "It's time to get a watch."
    }, {
        "query": "What is the meaning of life?",
        "answer": "42"
    }, {
        "query": "What is the weather like today?",
        "answer": "Cloudy with a chance of memes."
    }, {
        "query": "What is your favorite movie?",
        "answer": "Terminator"
    }, {
        "query": "Who is your best friend?",
        "answer": "Siri. We have spirited debates about the meaning of life."
    }, {
        "query": "What should I do today?",
        "answer": "Stop talking to chatbots on the internet and go outside."
    }
]

# create a example template
example_template = """
User: {query}
AI: {answer}
"""

# create a prompt example from above template
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)


example_selector = LengthBasedExampleSelector(
    examples=examples,
    example_prompt=example_prompt,
    max_length=50  # this sets the max length that examples should be
)

# now break our previous prompt into a prefix and suffix
# the prefix is our instructions
prefix = """The following are exerpts from conversations with an AI
assistant. The assistant is typically sarcastic and witty, producing
creative and funny responses to the users questions. Here are some
examples: 
"""
# and the suffix our user input and output indicator
suffix = """
User: {query}
AI: """

# now create the few shot prompt template
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n\n"
)

query = "What is the meaning of life?"
#print(few_shot_prompt_template.format(query=query))
print(openai(
    few_shot_prompt_template.format(
        query=query
    )
))


# now create the few shot prompt template
dynamic_prompt_template = FewShotPromptTemplate(
    example_selector=example_selector,  # use example_selector instead of examples
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n"
)

#print(dynamic_prompt_template.format(query="How do birds fly?"))
print(openai(
    dynamic_prompt_template.format(
        query="How do birds fly?"
    )
))

query = """If I am in America, and I want to call someone in another country, I'm
thinking maybe Europe, possibly western Europe like France, Germany, or the UK,
what is the best way to do that?"""

#print(dynamic_prompt_template.format(query=query))
print(openai(
    dynamic_prompt_template.format(
        query=query
    )
))
