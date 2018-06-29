from sys import argv 

script, filename = argv

print "Do you you really want to clear your order? %r" %filename
print "If not the hit esc."
print "If you want that hit enter."

raw_input("Response?")

print "opening invoice..."
target = open(filename, 'w')


