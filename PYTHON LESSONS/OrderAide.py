from sys import argv

apparel, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, apparel)
print "I'd like to ask you a few questions."
print "What are you looking for %s?" % user_name
likes = raw_input(prompt)

print "What size are you %s?" % user_name
size = raw_input(prompt)

print "What colour would you like it in?"
colour = raw_input(prompt)

print """
Alright, so you said %r about what you wanted.
You wear a size %r. We'd let you know if there's an issue.
And you would like it in %r . Nice.
""" % (likes, size, colour)
