from crewai.tools import BaseTool

"""
Your CalculateTool is a custom tool for an AI agent.
It does not run by itself — it only runs when an agent calls it.

What the tool does:
✔ The agent can call this tool
✔ It expects one argument: equation: str
✔ It uses Python eval() to compute the math
✔ It returns a string result
✔ If something goes wrong → returns "Error: ..."

How an Agent uses this tool:
1️⃣ Instantiate the tool
2️⃣ Pass it into the agent
3️⃣ Ask the agent a question involving math
"""

class CalculateTool(BaseTool):
    name: str = "calculate"
    description: str = "Useful for solving math equations"

    def _run(self, equation: str) -> str:
        try:
            return str(eval(equation))
        except Exception as e:
            return f"Error: {e}"



if __name__ == '__main__':
    c = CalculateTool()
    print(c._run("2 * 9 / 4 + 6 - 3"))
    print(c)
