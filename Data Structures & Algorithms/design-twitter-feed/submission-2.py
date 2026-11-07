import heapq

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.i = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.i, tweetId])
        self.i -= 1

    def getNewsFeed(self, userId: int) -> List[int]:    
        res = []
        minheap = []

        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index-1])
        
        while minheap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
