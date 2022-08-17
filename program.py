import configuration
import spam_module

configuration = configuration.Configuration()
endpoint = getattr(configuration, "endpoint")
apikey = getattr(configuration, "apikey")
spam = spam_module.SpamModule(endpoint, apikey)

for i in range(10):
    spam.spam("mister-fock@example.com", "password")


