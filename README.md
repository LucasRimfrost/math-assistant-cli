# Math Assistant

A Python package that uses the Claude AI to help with mathematics problems. It can analyze problems from images, provide explanations, generate similar practice problems, and check solutions.

## Features

- Parse mathematical problems from images
- Get detailed explanations and solutions
- Generate similar practice problems
- Check and provide feedback on solutions
- Handle complex mathematical notation and diagrams

## Installation

```bash
pip install math-assistant
```

## Quick Start

```python
from math_assistant import MathAssistant

# Initialize the assistant
assistant = MathAssistant()

# Get help with a problem
explanation = assistant.explain_problem(
    "problem.jpg",
    "Can you explain the approach to this integral?"
)

# Generate practice problems
similar = assistant.generate_similar_problems("problem.jpg")

# Check your solution
feedback = assistant.check_solution(
    "problem.jpg",
    "Here's my solution: ..."
)
```

## Configuration

Set your Anthropic API key as an environment variable:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or provide it when initializing:
```python
assistant = MathAssistant(api_key='your-api-key-here')
```

## Documentation

For full documentation, visit [docs/README.md](docs/README.md)
