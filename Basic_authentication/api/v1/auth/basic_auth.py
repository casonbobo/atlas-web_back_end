#!/usr/bin/env python3
"""Redux Auth class but now its basic"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth class, inherits from Auth"""
    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """This returns the Base64 decoded"""
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(' ', 1)[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """This function is to decode the base64 auth"""
        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
        except Exception:
            return None

        return decoded_bytes.decode('utf-8')

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None or not \
                isinstance(decoded_base64_authorization_header, str) \
                or ':' not in decoded_base64_authorization_header:
            return None, None
        else:
            user_email, user_password = \
                decoded_base64_authorization_header.split(':')
            return user_email, user_password
