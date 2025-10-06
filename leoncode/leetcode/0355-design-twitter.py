# 355 - https://leetcode.com/problems/design-twitter/

class Twitter:
    def __init__(self):
        self.time = 0
        self.followeeMap = defaultdict(set) # stores the user's following
        self.tweetMap = defaultdict(list) # stores the user's tweet and also the time of the tweet

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.followeeMap[userId].add(userId) # make the user follow himself for displaying his own tweets
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1 # making it negative because we are using max heap to get the latest tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        if len(self.followeeMap[userId]) == 0:
            return []

        # Store each followee's latest tweet in the max heap
        maxHeap = []
        for followeeId in self.followeeMap[userId]:
            if len(self.tweetMap[followeeId]) > 0:
                lastIndex = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][lastIndex]
                heapq.heappush(maxHeap, (time, tweetId, followeeId, lastIndex - 1))
        
        # Retrieve 10 latest tweets or until heap is empty
        res = []
        while maxHeap and len(res) != 10:
            _, tweetId, followeeId, lastIndex = heapq.heappop(maxHeap)
            res.append(tweetId)
            if lastIndex >= 0:
                time, tweetId = self.tweetMap[followeeId][lastIndex]
                heapq.heappush(maxHeap, (time, tweetId, followeeId, lastIndex - 1))    
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followeeMap[followerId]:
            self.followeeMap[followerId].remove(followeeId)