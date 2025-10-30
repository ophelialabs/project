from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

class BaseAssistant:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.llm = ChatOpenAI(model_name=model_name)
        self.memory = ConversationBufferMemory()
        self.chain = ConversationChain(
            llm=self.llm,
            memory=self.memory
        )
    
    def chat(self, message: str) -> str:
        response = self.chain.predict(input=message)
        return response