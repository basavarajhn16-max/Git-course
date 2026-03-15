a = 10   # global variable

def something():
    global a
    a = 20      # modifies global variable

    a = 15      # reassigns again
    print("inside :", a)

something()

print("outside :", a)