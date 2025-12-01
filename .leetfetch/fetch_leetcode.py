import requests
import json
import datetime

USERNAME = "praveenkumarka_it24"

QUERY = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile {
      ranking
      reputation
    }
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
        submissions
      }
    }
    problemsSolvedBeatsStats {
      difficulty
      percentage
    }
  }
  userCalendar(username: $username, year: 2025) {
    submissionCalendar
  }
}
"""

variables = {"username": USERNAME}

res = requests.post(
    "https://leetcode.com/graphql/",
    json={"query": QUERY, "variables": variables},
    headers={"Content-Type": "application/json"}
)

data = res.json()

with open(".leetfetch/leetcode.json", "w") as f:
    json.dump(data, f, indent=4)
