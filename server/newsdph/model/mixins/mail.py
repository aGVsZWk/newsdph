


class MailMixin(object):
    @classmethod
    def _token_serializer(cls, key=None, salt=None):
        config = current_app.config
        if key is None:
            key = config.setdefault('SECRET_KEY', gen_secret_key(24))
        if salt is None:
            salt = config.setdefault('SECRET_KEY_SALT', gen_secret_key(24))
        return URLSafeTimedSerializer(key, salt=salt)

    @property
    def email_token(self):
        serializer = self._token_serializer()
        token = serializer.dumps(self.email)
        return token

    @classmethod
    def check_email_token(cls, token, max_age=259200):
        serializer = cls._token_serializer()
        try:
            email = serializer.loads(token, max_age=max_age)
        except BadSignature:
            return False
        except SignatureExpired:
            return False
        user = cls.query.filter_by(email=email).first()
        if user is None:
            return False
        return user
