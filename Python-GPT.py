# Set the API_Key
import openai
import os
import subprocess
import time 
from tqdm import tqdm

OPENAI_API_KEY = "Your openai api key"

# Take task and instructions
task = input("Enter The Program  : ")
instructions = "After getting the program, generate the Python code without anything else, just generate the Python code "

# Connect to OpenAI API_Key
client = openai.OpenAI(
    api_key=os.getenv(OPENAI_API_KEY)
)

# Completion and Set the Model GPT
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": instructions},
        {"role": "user", "content": task}
    ]
)

# Message from OpenAI
response = completion.choices[0].message.content
print("")
print("")
print("")
# Print the message
print(response)
print("")
print("")
print("")
# Wait
os.system("color a")
time.sleep(3)
for i in tqdm(range(100)):
    time.sleep(0.01)
print("")
print("")
# Save the code
folder_name = "code"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Path File
file_path = os.path.join(folder_name, task + ".py")

# Create file
with open(file_path, "w") as file:
    file.write(response)

print("Save ")

# Show Output
os.system("color d")
for i in tqdm(range(100)):
    time.sleep(0.065)
print("")
print("")
print("\n\nOUTPUT : ")
file_name = file_path
print("\n\n")

# Run python file 
subprocess.run(["python", file_name])
