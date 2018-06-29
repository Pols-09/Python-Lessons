from sys import argv

script, filename = argv

txt = open(filename)

print "This is your invoice: %r" % filename
print txt.read()

print "Please type your size and colour preference:"
confirm = raw_input(">")

changes = open(confirm)

print changes.read()