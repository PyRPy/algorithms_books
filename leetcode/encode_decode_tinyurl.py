# encode and decode tinyurl
import string   
import random 
import math 
full_tiny = {}
tiny_full = {}
letters = string.ascii_letters + string.digits 

class Codec:
    def encode(self, longUrl):
        """
        encode a url to a shortened url
        type longUrl: str 
        rtype: str
        """
        def short_addr():
            ans = ''
            tmp = ''
            for i in range(6):
                tmp = letters[random.randint(0, 10000) % 62]
                ans += tmp
            return ans
        
        if longUrl in full_tiny:
            return "http://tinyurl.com/" + full_tiny[longUrl]
        else:
            suffix = short_addr()
            full_tiny[longUrl] = suffix
            tiny_full[suffix] = longUrl
            return "http://tinyurl.com/" + suffix

    def decode(self, shortUrl):
        """
        decode a shortened url to its original url
        type shortUrl : str 
        rtype: str
        """
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return None 

longUrl = "https://www.wsj.com/news"
sol = Codec()
print(longUrl)
print(sol.encode(longUrl))
long_encoded = sol.encode(longUrl)
print(sol.decode(long_encoded))
