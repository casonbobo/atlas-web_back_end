#!/usr/bin/env python3
"""Redux Auth class but now its basic"""

from api.v1.auth.auth import Auth
import Base64


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
        if base64_authorization_header is None
        or not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
        except Exception:
            return None

        return decoded_bytes.decode('utf-8')
