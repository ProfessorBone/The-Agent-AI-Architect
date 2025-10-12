# Contributing to Agentic Coder

We love your input! We want to make contributing to Agentic Coder as easy and transparent as possible.

## Development Process

We use GitHub to sync code, track issues and feature requests, as well as accept pull requests.

## Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Setup

1. Clone your fork of the repository
2. Run `./scripts/dev_setup.sh` to set up the development environment
3. Create a new branch for your feature: `git checkout -b feature/amazing-feature`
4. Make your changes
5. Run tests: `poetry run pytest`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

## Code Style

- We use `black` for code formatting
- We use `isort` for import sorting
- We use `flake8` for linting
- We use `mypy` for type checking

## Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting PR
- Include integration tests for complex features
- Test coverage should be maintained above 90%

## License

By contributing, you agree that your contributions will be licensed under the MIT License.