#variables:

name = 'Mohammed Sanaan'
role = 'AI engineer in progress'
experiance_level = 'Beginner'

print(f"Name: {name} | Role: {role} | Experience Level: {experiance_level}")


#numbers:

token_used = 1200
reponse_time = 1.45


print("Token used :", token_used)
print("reponse_time", reponse_time)

#Lists:

ai_topics = [
    "python",
    "fastAPI",
    "LLMs",
    "Embeddings",
    "RAG",
    "Agents"
]

for i in ai_topics:
    print("AI topics", i)


#Dictionary

ai_project = {
    "project_name" : "Ai engineering",
    "current_day": 1,
    "current_topic": "python basics",
    "status": "Started"
}

print("project Info", ai_project)

#Function

def summary_ai_learning(name, topic):
    return f"{name} started learning {topic}"

summary = summary_ai_learning("sanaan", "python basics")
print(summary)

#Json like data

user_request = {
    "name": "mohammed Sanaan",
    "country": "India",
    "language": "english"
}

print("user_ewquests:", user_request)