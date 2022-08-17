import spam_module

spam = spam_module.SpamModule("https://httpbin.org/post")

for i in range(10):
    spam.spam("mister-fock@example.com", "password")


