"""DevLab manager orchestrating generation and validation."""

from .generator import CodeGenerator
from .validator import CodeValidator

class DevLabManager:
    """Coordinates code generation and validation steps."""

    def __init__(self,
                 generator: CodeGenerator | None = None,
                 validator: CodeValidator | None = None) -> None:
        self.generator = generator or CodeGenerator()
        self.validator = validator or CodeValidator()

    def run(self, prompt: str) -> str:
        """Generate code for the prompt and validate it."""
        code = self.generator.generate(prompt)
        if self.validator.validate(code):
            return code
        # TODO: handle invalid code case
        return ""
