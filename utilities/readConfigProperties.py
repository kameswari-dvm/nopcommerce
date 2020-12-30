import configparser


class get_login_info:
    config = configparser.RawConfigParser()
    config.read(".//configuration//config.ini")

    @staticmethod
    def get_base_url():
        base_url = get_login_info.config.get('site info', 'base_url')
        return base_url

    @staticmethod
    def get_username():
        username = get_login_info.config.get('site info', 'username')
        return username

    @staticmethod
    def get_password():
        password = get_login_info.config.get('site info', 'password')
        return password
