# Data Science Flashcards

A collection of data science questions and answers —ideal for interview preparation, revision, and efficient spaced repetition learning.

## Features

- **Curated Questions:** Covers a wide range of data science topics, including statistics, machine learning, data preprocessing, model evaluation, and more.
- **Interview-Focused:** Questions and answers are tailored for technical interview preparation as well as skill reinforcement.
- **Collaborative:** Contributions are welcome—add new cards, suggest improvements, or open issues for discussion.
- **Automated Dependency Management:** The repository uses a GitHub Action to automatically update `requirements.txt` based on Python imports whenever code changes are pushed to the main branch.

## Contributing

We welcome and encourage contributions!

- To contribute, simply **add new cards** or **edit existing ones** in the `cards` folder.
- Each card should be a Markdown file with clear questions and answers. You can add non-technical explanations as well.
- If you're adjusting content, please ensure your edits improve clarity, accuracy, or usefulness.
- After making changes, open a pull request describing your additions or modifications.

**Your contributions help improve this resource for everyone preparing for data science interviews or strengthening their expertise!**

## Automated Requirements Management

This repository includes a GitHub Action that automatically maintains the `requirements.txt` file:

- **Automatic Updates:** Whenever Python files are modified and pushed to the main branch, the action scans all imports and updates `requirements.txt` accordingly.
- **Manual Trigger:** You can also manually trigger the workflow from the Actions tab if needed.
- **Smart Deduplication:** The action automatically handles duplicate dependencies and keeps the highest version when conflicts occur.

The workflow ensures that `requirements.txt` always reflects the actual dependencies used in the codebase, making it easier for contributors to set up their development environment.
