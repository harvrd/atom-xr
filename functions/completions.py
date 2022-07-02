# NLG FUNCTIONS
import openai
openai.api_key = "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"

# def getValidCommand(speechString: str) -> str:
# 	fewShotPrompt = f"""
# 	... few shot ...
# 	{speechString}
# 	"""
# 	completion = openai.Completion.create(
# 		engine="davinci",
# 		prompt=fewShotPrompt).strip()
# 	validCommand = completion.choices[0].text
# 	return validCommand

def getCompletion(prompt):
  # print("PROMPT:\n", prompt)
  completion = openai.Completion.create(
    engine = "text-davinci-002",
    temperature = 0.5,
    max_tokens = 200,
    prompt = prompt,
    stop = "###"
  ).choices[0].text
  return completion