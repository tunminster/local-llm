from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained("zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf")

prompt = """What is the best university in the world, she asked.
          Please only respond with the city name and then stop talking. 
          He answered: """

print(llm(prompt))
