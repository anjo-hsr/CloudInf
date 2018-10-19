class Connection:
    def __init__(self, https_address, cookie, token):
        self.https_address = https_address
        self.token = token
        self.cookie = cookie

    def get_https_address(self):
        return self.https_address

    def get_cookie(self):
        return self.cookie

    def get_token(self):
        return self.token
