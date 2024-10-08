
def viralAdvertising(n):
    shared = 5  # Initial number of people who receive the ad
    cumulative_likes = 0
    
    for day in range(n):
        liked = shared // 2  # Half of the people like the ad
        cumulative_likes += liked  # Add liked people to the cumulative likes
        shared = liked * 3  # Each person who likes shares with 3 more people

    return cumulative_likes

# Example usage:
n = int(input())  # Input number of days
print(viralAdvertising(n))
