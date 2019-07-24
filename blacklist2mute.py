import requests
from beem.account import Account
from beem.steem import Steem
import time

# Blacklist URL
url = "https://steem.tools/planktontoken/api/blacklist.json"
bot_name = ""
beem_password = ""

req = requests.get(url)

data = req.json()

blacklisted_users = []

# Supports Blacklists in the form:
# Array of names like http://blacklist.usesteem.com/blacklist/actifit
# ["user1", "user2"]
# and
# Ones with a blacklist inside a blacklist array like https://steem.tools/planktontoken/api/blacklist.json
# {"name": "blacklist", "blacklist": ["user1", "user2"]}

try:
    blacklisted_users = data["blacklist"]
except Exception:
    blacklisted_users = data


print("-"*200 + "\n\n")

steem = Steem(node="https://rpc.usesteem.com")
steem.wallet.unlock(beem_password)
account = Account(steem_instance=steem, account=bot_name)

already_ignored = account.get_mutings()

for user in data["blacklist"]:
    if user not in already_ignored:
        print("Adding " + user + " to muted!")
        account.follow(user, what=['ignore'], account=bot_name)
        time.sleep(3)
