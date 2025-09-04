from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Configure LangChain to connect to the local vLLM server
# openai_api_base points to our vLLM server address instead of OpenAI.
# openai_api_key can be anything as it's not required for the local server.
llm = ChatOpenAI(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    openai_api_key="not-needed",
    openai_api_base="http://localhost:8000/v1",
    temperature=0.7,
)

# 2. Create a prompt template
# We will insert the user's question into the template using {question}.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{question}")
])

# 3. Create a simple chain
# This chain takes user input, inserts it into the prompt, sends it to the LLM,
# and parses the output as a string.
chain = prompt | llm | StrOutputParser()

# 4. Make the application interactive
print("Hello! You can ask a question to the vLLM and LangChain based assistant.")
print("Type 'exit' or 'quit' to end the conversation.")

while True:
    try:
        user_input = input("\nQuestion: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        # Invoke the chain and print the result
        response = chain.invoke({"question": user_input})
        print("Answer:", response)

    except KeyboardInterrupt:
        print("\nExiting...")
        break