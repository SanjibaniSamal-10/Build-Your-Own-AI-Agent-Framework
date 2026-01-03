class Guardrails:
    def validate(self, output):
        if output is None or output == "":
            raise ValueError("Guardrail violation: Empty output")