class ResponseProvider:

    def success(
        self,
        data=None,
        message="Success",
    ):

        return {
            "success": True,
            "message": message,
            "data": data,
        }

    def error(
        self,
        message,
    ):

        return {
            "success": False,
            "message": message,
        }
