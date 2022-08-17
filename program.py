import configuration
import inputifier
import spam_module

configuration = configuration.Configuration()
inputifier = inputifier.Inputifier();
endpoint = getattr(configuration, "endpoint")
apikey = getattr(configuration, "apikey")
spam_count = getattr(configuration, "spam_count")

spam = spam_module.SpamModule(endpoint, apikey)

for i in range(spam_count):
    email = inputifier.GetRandomEmailAddress()
    password = inputifier.GetRandomPassword()
    spam.spam(email, password)


