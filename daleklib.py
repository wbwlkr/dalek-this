#!/usr/bin/env python3

"""Title : Dalek This
Author : wbwlkr (wbwlkr.github.io)
Description :
Removing posts from your Facebook wall has never been this fast before DalekThis.
"""

import facebook

class DalekThis:
    """Main class to interact with the Facebook API
    """
    def __init__(self):
        self.access_token = "token"
        self.api_version = "2.11"
        self.graphAPI = facebook.GraphAPI(
            access_token = self.access_token,
            version = self.api_version)
        pass

    def get_all_post(self):
        pass

    def delete_all(self):
        pass

    def delete_posts_since(self):
        pass
