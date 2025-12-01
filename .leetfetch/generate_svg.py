import json

with open(".leetfetch/leetcode.json") as f:
    data = json.load(f)

stats = data["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]

easy = stats[1]["count"]
medium = stats[2]["count"]
hard = stats[3]["count"]

rank = data["data"]["matchedUser"]["profile"]["ranking"]

svg = f"""
<svg width="450" height="220" xmlns="http://www.w3.org/2000/svg">
<style>
text {{
  font-family: 'Segoe UI', sans-serif;
  fill: #00ff66;
}}
</style>

<rect width="100%" height="100%" fill="#000000" />

<text x="20" y="40" font-size="26" font-weight="bold">LeetCode Stats</text>

<text x="20" y="90" font-size="18">Easy   : {easy}</text>
<text x="20" y="120" font-size="18">Medium : {medium}</text>
<text x="20" y="150" font-size="18">Hard   : {hard}</text>

<text x="20" y="190" font-size="18">Ranking: {rank}</text>

</svg>
"""

with open(".leetfetch/leetcode.svg", "w") as f:
    f.write(svg)
