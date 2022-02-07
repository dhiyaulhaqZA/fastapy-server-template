class Responsify:

    @staticmethod
    def success(data):
        return {
            "data": data,
            "error": None
        }
    
    @staticmethod
    def failure(code, message):
        return {
        "data": None,
        "error": {
            "code": code,
            "message": message
            }
        }