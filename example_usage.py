"""Example usage of the Math Assistant package demonstrating various features."""

from math_assistant.math_assistant import MathAssistant
import argparse
from pathlib import Path
import sys
import time


def basic_usage_example(assistant: MathAssistant):
    """Demonstrate basic features."""
    print("\n=== Basic Usage Example ===")

    # Simple problem explanation
    image_path = input("Enter path to your math problem image: ")
    if not Path(image_path).exists():
        print(f"Error: Image file not found: {image_path}")
        return

    print("\nGetting explanation with rich formatting...")
    assistant.explain_problem(
        image_path, "Please explain this step by step.", format_style="rich"
    )

    # Generate similar problems
    if (
        input("\nWould you like to see similar practice problems? (y/n): ").lower()
        == "y"
    ):
        num_problems = int(input("How many problems would you like? "))
        assistant.generate_similar_problems(
            image_path, num_problems=num_problems, format_style="rich"
        )

    # Check a solution
    if input("\nWould you like to check a solution? (y/n): ").lower() == "y":
        print("\nEnter your solution (press Ctrl+D or Ctrl+Z when finished):")
        solution_lines = []
        try:
            while True:
                line = input()
                solution_lines.append(line)
        except (EOFError, KeyboardInterrupt):
            pass

        solution = "\n".join(solution_lines)
        assistant.check_solution(image_path, solution, format_style="rich")


def interactive_session(assistant: MathAssistant):
    """Run an interactive conversation session."""
    print("\n=== Interactive Session ===")

    # Start with or without an image
    image_path = input(
        "Enter path to math problem image (or press Enter to start without image): "
    )

    if image_path.strip():
        if not Path(image_path).exists():
            print(f"Error: Image file not found: {image_path}")
            return

        assistant.start_conversation(image_path)
        current_image = image_path
    else:
        assistant.start_conversation()
        current_image = None

    print("\nCommands:")
    print("- Type 'quit' to exit")
    print("- Type 'new image: [path]' to switch to a new problem")
    print("- Type 'save' to save the conversation")
    print("- Type 'help' to see these commands again")

    while True:
        try:
            question = input("\nYour question: ")

            if question.lower() == "quit":
                break

            elif question.lower() == "help":
                print("\nCommands:")
                print("- Type 'quit' to exit")
                print("- Type 'new image: [path]' to switch to a new problem")
                print("- Type 'save' to save the conversation")
                print("- Type 'help' to see these commands again")
                continue

            elif question.lower() == "save":
                filename = input("Enter filename to save conversation: ")
                assistant.save_conversation(filename)
                print(f"Conversation saved to {filename}")
                continue

            elif question.lower().startswith("new image:"):
                new_image = question.split(":", 1)[1].strip()
                if not Path(new_image).exists():
                    print(f"Error: Image file not found: {new_image}")
                    continue
                current_image = new_image
                assistant.ask_about_problem(new_image, "Can you explain this problem?")

            else:
                if current_image:
                    assistant.ask_about_problem(current_image, question)
                else:
                    assistant.continue_conversation(question)

        except KeyboardInterrupt:
            print("\nUse 'quit' to exit properly")
        except Exception as e:
            print(f"\nError: {str(e)}")


def batch_processing(assistant: MathAssistant):
    """Process multiple problems in batch."""
    print("\n=== Batch Processing ===")

    print(
        "Enter paths to math problems (one per line, press Ctrl+D or Ctrl+Z when finished):"
    )
    image_paths = []
    try:
        while True:
            path = input()
            if Path(path).exists():
                image_paths.append(path)
            else:
                print(f"Warning: File not found: {path}")
    except (EOFError, KeyboardInterrupt):
        pass

    if not image_paths:
        print("No valid image paths provided")
        return

    for i, path in enumerate(image_paths, 1):
        print(f"\nProcessing problem {i}/{len(image_paths)}: {path}")
        assistant.explain_problem(path, format_style="rich")
        time.sleep(1)  # Prevent rate limiting


def main():
    """Main function with command line interface."""
    parser = argparse.ArgumentParser(description="Math Assistant Usage Examples")
    parser.add_argument(
        "--mode",
        choices=["basic", "interactive", "batch"],
        default="interactive",
        help="Operation mode (default: interactive)",
    )

    args = parser.parse_args()

    try:
        assistant = MathAssistant()
    except Exception as e:
        print(f"Error initializing Math Assistant: {str(e)}")
        print("Make sure your ANTHROPIC_API_KEY environment variable is set!")
        sys.exit(1)

    try:
        if args.mode == "basic":
            basic_usage_example(assistant)
        elif args.mode == "interactive":
            interactive_session(assistant)
        elif args.mode == "batch":
            batch_processing(assistant)

    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")


if __name__ == "__main__":
    main()
