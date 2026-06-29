class RequestValidator:

    @staticmethod
    def validate(data):

        if data is None:

            raise ValueError(
                "Request body is required."
            )

        return True
