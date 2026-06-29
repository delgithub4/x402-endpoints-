class AuditLogger:

    def __init__(self):

        self.records = []

    def record(
        self,
        action,
        actor,
    ):

        self.records.append(
            {
                "action": action,
                "actor": actor,
            }
        )

    def history(self):

        return self.records
