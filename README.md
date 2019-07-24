# Blacklist-To-Mutes
A python script to convert a blacklist into mutes through the Beem Library

### Why?
As you may know, SCOTBot/Distribubot use the muted/ignored list of the bot's account to decide whether or not a user should be rewarded. Because of this, I've made a script which will allow you to mute users from many blacklist API's. It knows not to duplicate, as it checks if you've already muted them before muting them.

Obviously, due to the 3 seconds per Custom_Json limitation of the steem blockchain, each mute requires 3 seconds to process.

### Blacklist Formats Supported:
- JSON Blacklists with an array of usernames like UseSteem (Global Blacklist API)
- JSON Blacklists containing a "blacklist" element like Plankton Token

### Blacklists Supported:
- Plankton Token Blacklist - https://steem.tools/planktontoken/api/blacklist.json
- UseSteem (Global Blacklist API) Individual App Blacklists:
   - http://blacklist.usesteem.com/blacklist/actifit
   - http://blacklist.usesteem.com/blacklist/buildawhale
   - http://blacklist.usesteem.com/blacklist/utopian-io
   - http://blacklist.usesteem.com/blacklist/redeemer
   - http://blacklist.usesteem.com/blacklist/minnowbooster
   - http://blacklist.usesteem.com/blacklist/oracle-d
   - http://blacklist.usesteem.com/blacklist/smartsteem
- Any other API following one of the formats above
