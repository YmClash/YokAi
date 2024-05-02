from llama_index.llms import Ollama

shaka = Ollama(model="mixtral")

response = shaka.complete("Who is Laurie Voss?")
print(response)


