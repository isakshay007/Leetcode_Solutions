from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.time = 0 
        self.tweets = defaultdict(list)  # Stores tweets {userId: [(time, tweetId)]}
        self.followees = defaultdict(set)  # Stores follow relationships {userId: set(followeeIds)}

    def postTweet(self, userId: int, tweetId: int):
        self.time += 1  # Increment time
        self.tweets[userId].append((self.time, tweetId))  # Save tweet as (time, tweetId)

        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)

    def getNewsFeed(self, userId: int):
        min_heap = []


        users_to_check = set(self.followees[userId])  # Get followees
        users_to_check.add(userId)  # Include user themselves

        for user in users_to_check:
            for tweet in self.tweets[user]:
                heapq.heappush(min_heap, tweet)  
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)  
        
        # Sort tweets in descending order of time and return only tweet IDs
        min_heap.sort(reverse=True)
        return [tweet[1] for tweet in min_heap]

    def follow(self, followerId: int, followeeId: int):

        if followerId != followeeId:  # Prevent self-following
            self.followees[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int):

        self.followees[followerId].discard(followeeId) 

t = Twitter()

# User 1 posts a tweet (ID = 101)
t.postTweet(1, 101)

# User 1 posts another tweet (ID = 102)
t.postTweet(1, 102)

# User 1 should see their tweets in the news feed
print(t.getNewsFeed(1))  # Expected output: [102, 101]

# User 2 follows User 1
t.follow(2, 1)

# User 2 should see User 1's tweets in their feed
print(t.getNewsFeed(2))  # Expected output: [102, 101]

# User 2 posts a tweet (ID = 201)
t.postTweet(2, 201)

# User 2 should now see their own tweet along with User 1's tweets
print(t.getNewsFeed(2))  # Expected output: [201, 102, 101]

# User 2 unfollows User 1
t.unfollow(2, 1)

# Now User 2 should only see their own tweets
print(t.getNewsFeed(2))  # Expected output: [201]

# User 1 posts multiple tweets to test the 10-tweet limit
for i in range(103, 113):  # Tweet IDs from 103 to 112
    t.postTweet(1, i)

# User 1 should only see the latest 10 tweets in their feed
print(t.getNewsFeed(1))  
# Expected output: [112, 111, 110, 109, 108, 107, 106, 105, 104, 103] (Latest 10 tweets)

