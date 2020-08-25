followers = {}

while True:
    input_command = input()

    if input_command == "Log out":
        break

    tokens = input_command.split(": ")
    command = tokens[0]
    username = tokens[1]

    if command == "New follower":
        if username in followers:
            continue
        followers[username] = {}
        followers[username]['likes'] = 0
        followers[username]['comments'] = 0
    elif command == "Like":
        likes_count = int(tokens[2])
        if username not in followers.keys():
            followers[username] = {}
            followers[username]['likes'] = likes_count
            followers[username]['comments'] = 0
        else:
            followers[username]['likes'] += likes_count
    elif command == "Comment":
        if username not in followers.keys():
            followers[username] = {}
            followers[username]['likes'] = 0
            followers[username]['comments'] = 1
        else:
            followers[username]['comments'] += 1
    elif command == "Blocked":
        if username in followers.keys():
            followers.pop(username)
        else:
            print(f"{username} doesn't exist.")

followers = dict(sorted(followers.items(), key=lambda x: (-(x[1]['likes']), x[0])))

print(f"{len(followers)} followers")
[print(f"{follower}: {likes['likes'] + likes['comments']}") for follower, likes in followers.items()]
