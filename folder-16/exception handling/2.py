instagram = [{'Photos': 6, 'disLikes': 22, 'Comments': 3}, {'disLikes': 13, 'Comments': 1, 'Shares': 6}, {'Photos': 6, 'disLikes': 33, 'Comments': 9, 'Shares': 4}, {'Comments': 5, 'Shares': 1}, {'Photos': 5, 'Comments': 4, 'Shares': 2}, {'Photos': 3, 'disLikes': 19, 'Comments': 3}]

total_dislikes = 0

try:
    for post in instagram:
        total_dislikes += post.get('dislike',0)  # Use get() to avoid KeyError
except KeyError:
    print("Post does not have a 'dislike' key.")

print(f"Total dislikes: {total_dislikes}")
