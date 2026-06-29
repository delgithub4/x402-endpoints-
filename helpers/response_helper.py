class ResponseHelper:

    @staticmethod
    def success(data=None):

        return {
            "success": True,
            "data": data,
        }

    @staticmethod
    def failure(message):

        return {
            "success": False,
            "message": message,
        }
