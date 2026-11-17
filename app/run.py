from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from app.agent.graphs.order_graph import order_graph


def start_chat():

    print("Shopping agent ")


    print("\n Ask questuion about your orders. tpe exit to stop")

    #maintaion messages history
    messages = []

    while True:

        user_input = input(" You : ")

        if user_input.lower() == "exit":
            break

        messages.append(
            HumanMessage(content=user_input)
        )

        #execute Langgraph
        result = order_graph.invoke({
            "messages" : messages
        })

        #update conversation history
        messages = result["messages"]

        final_message = messages[-1]

        print(final_message.content)
        print()


if __name__ == "__main__" :

    start_chat()