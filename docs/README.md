# Basic Usage Examples

## 1. Analyzing a Calculus Problem

```python
from math_assistant import MathAssistant

assistant = MathAssistant()

# Get explanation for a problem
explanation = assistant.explain_problem(
    "calculus_problem.jpg",
    "I'm struggling with setting up the integral."
)

print(explanation)
```

## 2. Generating Practice Problems

```python
# Generate similar problems
similar = assistant.generate_similar_problems(
    "calculus_problem.jpg",
    num_problems=3
)

print(similar)
```

## 3. Checking Solutions

```python
# Check your solution
feedback = assistant.check_solution(
    "calculus_problem.jpg",
    """
    Here's my solution:
    1. First, I set up the integral...
    2. Then I used u-substitution...
    """
)

print(feedback)
```
