# LeetGenie

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-brightgreen)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-Required-blue)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

LeetGenie is an AI-powered DSA (Data Structures and Algorithms) problem-solving assistant. It leverages multi-agent collaboration and Docker-based code execution to solve coding problems, explain solutions, and provide test cases. The app features both a command-line and a Streamlit web interface.

---

![LeetGenie Screenshot](https://user-images.githubusercontent.com/your-username/leetgenie-demo.png)

*Screenshot: Example of LeetGenie solving a DSA problem in the Streamlit web app.*

---

## Project Structure

```text
LeetGenie/
├── app.py                  # Streamlit web app for interactive DSA problem solving
├── main.py                 # Command-line interface for running the DSA team
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API keys, etc.)
├── agents/
│   ├── code_executor_agent.py   # Defines the agent that executes code in Docker
│   └── problem_solver.py        # Defines the agent that solves DSA problems
├── config/
│   ├── constant.py         # Constants (model name, timeouts, etc.)
│   ├── docker_executor.py  # Docker code executor setup
│   ├── docker_utils.py     # Async helpers to start/stop Docker containers
│   └── settings.py         # Loads model client and API keys
├── team/
│   └── dsa_team.py         # Assembles the DSA team (problem solver + executor)
├── temp/                   # Temporary directory for generated/solved code
│   └── ...                 # Solution and temp code files
```

## What Each File Does

- **app.py**: Streamlit web app for user-friendly DSA problem solving. Lets you enter a problem, runs the agent team, and displays results.
- **main.py**: Command-line entry point. Runs the DSA team on a sample or user-provided problem, prints agent messages and results.
- **requirements.txt**: Lists all required Python packages, including AI agent libraries, Docker, and Streamlit.
- **.env**: Store your API keys here (e.g., `OPENAI_API_KEY`).

### agents/
- **code_executor_agent.py**: Defines the agent that executes code using Docker.
- **problem_solver.py**: Defines the agent that generates and explains DSA solutions.

### config/
- **constant.py**: Sets model name, stop word, working directory, timeout, and max turns.
- **docker_executor.py**: Returns a Docker-based code executor for safe code execution.
- **docker_utils.py**: Async functions to start/stop Docker containers.
- **settings.py**: Loads environment variables and provides the model client for agents.

### team/
- **dsa_team.py**: Assembles the problem solver and code executor agents into a team with a round-robin chat and termination condition.

### temp/
- **solution.py** and temp files: Stores generated code and temporary files during execution.

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd LeetGenie
   ```
2. **Create and activate a Python environment**
   ```sh
   conda create -n leetgenie python=3.10
   conda activate leetgenie
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables**
   - Create a `.env` file in the root directory:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Running the Application

### Command-Line Interface
Run a sample DSA problem from the terminal:
```sh
python main.py
```

### Streamlit Web App
Launch the web interface:
```sh
streamlit run app.py
```

Enter your DSA problem in the input box and click "Run" to see the solution and code execution results.

## Usage Examples

### Example 1: Command-Line
```sh
$ python main.py
Docker container started successfully.
========================================
DSA_Problem_Solver_Agent : Here is my plan to solve the task: ...
CodeExecutorAgent : Code executed successfully. Output: ...
Stop Reason: STOP
```

### Example 2: Streamlit Web App
1. Start the app: `streamlit run app.py`
2. Enter: `Write a function to reverse a linked list` and click **Run**
3. See the agent's plan, code, test cases, and execution results in the browser.

### Example 3: Custom Problem with Test Cases
You can enter any DSA problem, such as:

```
Find the longest palindromic substring in a given string.
```

The agent will generate a plan, code, and at least 3 test cases, then execute and explain the results.

### Example 4: Error Handling
If your code has a bug or fails a test case, LeetGenie will display the error and suggest corrections. You can iteratively refine your problem statement and rerun.

---

## Notes
- Requires Docker to be installed and running on your system for code execution.
- Supports OpenAI models (e.g., `gpt-4o`).
- All code is executed in a sandboxed Docker container for safety.

## Troubleshooting
- **Docker not running:** Make sure Docker Desktop is running before starting the app.
- **API key errors:** Ensure your `.env` file contains a valid `OPENAI_API_KEY`.
- **Module errors:** Double-check your Python environment and installed dependencies.

## License
MIT License
