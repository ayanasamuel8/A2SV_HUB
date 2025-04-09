# Problem: Design Authentication Manager - https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.Auth_manager = defaultdict(lambda: -inf)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.Auth_manager[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if currentTime - self.Auth_manager[tokenId] < self.time_to_live:
            self.Auth_manager[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        lst = list(self.Auth_manager.items())
        for key, val in lst:
            if currentTime - val < self.time_to_live:
                cnt += 1
            else:
                del self.Auth_manager[key]
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)