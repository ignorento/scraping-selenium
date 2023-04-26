from functools import wraps


def social_login_required(func):
    @wraps(func)
    def wrapper(self, * args, ** kwargs):
        # Check if user is already logged in
        if self.is_logged_in:
            return func(self, *args, **kwargs)

        # If not logged in, perform social login
        self.social_network_login()

        # Call the original function
        return func(self, *args, **kwargs)

    return wrapper


def social_reg_required(func):
    @wraps(func)
    def wrapper(self, * args, ** kwargs):

        if self.is_reg_in:
            return func(self, *args, **kwargs)

        self.social_network_register()

        return func(self, *args, **kwargs)

    return wrapper
