import json
import pickle

with open("../tasks/D1.pickle", "rb") as f:
    data = pickle.load(f)

# Data is in format {ambiguous_term: task}
tasks = list(data.values())
print(f"Found {len(tasks)} tasks.\n")

"""
Task is an object with multiple subtasks, having the form of
{
  ambiguous: str,
  context: {correct_sense: serialized_input_sentence},
  gloss: {sense: serialized_definition}
}
"""
task = tasks[0]

# Convert serializations back to objects
for key, value in task["context"].items():
    task["context"][key] = json.loads(value)

for key, value in task["gloss"].items():
    task["gloss"][key] = json.loads(value)

"""
After parsing the texts are a list of tokens,
where each token is an object with keys
{lemma, upos, ner, form}
"""

solution, query = list(task["context"].items())[0]

print("The task is, given the following sentence:\n")
print(f"'{' '.join([t['form'] for t in query])}'\n")
print(f"Which is the correct sense for the word '{task['ambiguous']}'?\n")
print("The sense choices are:")
for i, (sense, gloss) in enumerate(task["gloss"].items()):
    print(f"{i + 1}. {sense}")
    definition = " ".join([t["form"] for t in gloss])
    print(f"Definition: {definition[:80]}...")

print(f"\nThe correct solution is: {solution}.")
