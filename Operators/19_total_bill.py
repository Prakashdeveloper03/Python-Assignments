new_videos = int(input("Enter the number of new videos : "))
old_movies = int(input("Enter the number of old movies : "))
no_of_days = int(input("Enter the no of days : "))
print(
    f"Total bill for the videos is {(new_videos * no_of_days * 75) + (old_movies * no_of_days * 50)}"
)
