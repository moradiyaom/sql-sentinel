class response_analyzer:
    """
    Analyzes HTTP responses for SQL injection indicators.
    """
    def __init__(self):
        self.error_keywords = [
            "SQL syntax", "database error", "you have an error in your SQL",
            "unclosed quotation mark", "ORA-", "unexpected end of SQL command"
        ]

    def analyze_response(self, response_text):
        for keyword in self.error_keywords:
            if keyword in response_text:
                return True
        return False
