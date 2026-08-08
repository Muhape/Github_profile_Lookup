import requests
username = input("Enter a registered GitHub username: ")
git = requests.get(f"https://api.github.com/users/{username}")
if git.status_code == 200:
    gitu = git.json()
    print("====================")
    print("Github Profile")
    print("====================")
    print(f"Username: {gitu['login']}")
    print(f"Name: {gitu['name']}")
    print(f"Followers: {gitu['followers']}")
    print(f"Following: {gitu['following']}")
    print(f"Public Repos: {gitu['public_repos']}")
    print(f"Location: {gitu['location']}")
    print(f"Bio: {gitu['bio']}")
    print(f"Date account got created: {gitu['created_at']}")
    print("====================")
else:
    print(f"Github profile {username} not found")
