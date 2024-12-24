class SettingsMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Settings(metaclass=SettingsMeta):
    pass


class PlatformSettings(Settings):
    def __init__(self):
        self.theme = "Light"
        self.language = "English"

    def update_settings(self, theme: str = None, language: str = None) -> None:
        if theme:
            self.theme = theme
        if language:
            self.language = language

    def display(self) -> dict:
        return {"theme": self.theme, "language": self.language}


# Использование
settings1 = PlatformSettings()
settings2 = PlatformSettings()

settings1.update_settings(theme="Dark", language="Spanish")
print(settings2.display())  # {'theme': 'Dark', 'language': 'Spanish'}
print(settings1 is settings2)  # True
