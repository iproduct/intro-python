class InvalidEntityData(Exception):
    def __init__(self, message: str = None, violations: list[str] = None) -> None:
        super().__init__(message)
        self.violations = violations

    def __str__(self):
        return f'{super().__str__()}, {str(self.violations)}'
