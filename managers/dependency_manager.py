from providers.provider_factory import ProviderFactory


class DependencyManager:

    def __init__(self):

        self.provider = ProviderFactory.dependencies()

    def resolve(self):

        return self.provider.dependencies()
