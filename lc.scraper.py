LEETCODE_SESSION="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiMzM2NzE5NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOTFmNzhhNDg2NjM4N2I5MWUwNTQwNDI2YTM5Zjc3MjA4YWU1MTRlMDc5ZmRkNDdhMDE3Zjk3ZTM3YmRmYzc1YyIsInNlc3Npb25fdXVpZCI6IjIwMDU0MmRlIiwiaWQiOjMzNjcxOTQsImVtYWlsIjoicGJzazExMDlAZ21haWwuY29tIiwidXNlcm5hbWUiOiJwcmFkZWVwMTEwOSIsInVzZXJfc2x1ZyI6InByYWRlZXAxMTA5IiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL3ByYWRlZXAxMTA5L2F2YXRhcl8xNTk5OTU2NjA1LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc1ODY2NzM5NywiaXAiOiIxNzAuODUuMTU0LjEyMyIsImlkZW50aXR5IjoiM2FkZTQ2ZTEwYWI0NmRmMWQ3ZDM5NWRkYWE3MTVhMjQiLCJkZXZpY2Vfd2l0aF9pcCI6WyIzMzAxM2E2YmZjMTdmY2E5ZjUyNzI5YTU1NjhhZTNiZSIsIjE3MC44NS4xNTQuMTIzIl0sIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.UM6AXBvpNXzHqsXwpCepjR_jGG61QtcuIptOG3nqTnE"

USERNAME="pbsk1109"

import requests
import csv
import pdb

import requests
import csv

# 🔐 Your session cookie and username
LEETCODE_SESSION = "your_LEETCODE_SESSION_cookie_here"
USERNAME = "your_username_here"

headers = {
    "Content-Type": "application/json",
    "Referer": f"https://leetcode.com/{USERNAME}/",
    "User-Agent": "Mozilla/5.0",
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}"
}

query = """
query problemsetQuestionListV2($categorySlug: String, $skip: Int, $limit: Int, $filters: QuestionFilterInput) {
  problemsetQuestionListV2(
    categorySlug: $categorySlug,
    skip: $skip,
    limit: $limit,
    filters: $filters
  ) {
    questions {
      title
      titleSlug
      difficulty
      status
      topicTags {
        name
      }
    }
  }
}
"""

limit = 50
skip = 0
solved_problems = []

while True:
    variables = {
        "categorySlug": "",
        "skip": skip,
        "limit": limit,
    }

    response = requests.post(
        "https://leetcode.com/graphql",
        headers=headers,
        json={"query": query, "variables": variables}
    )

    if response.status_code != 200:
        print("❌ Request failed:", response.text)
        break

    data = response.json()

    try:
        questions = data["data"]["problemsetQuestionListV2"]["questions"]
    except (KeyError, TypeError):
        print("❌ Unexpected response structure:", data)
        break

    if not questions:
        break

    for q in questions:
        if q.get("status") == "ac":  # Only accepted/solved problems
            solved_problems.append({
                "Title": q["title"],
                "URL": f"https://leetcode.com/problems/{q['titleSlug']}/",
                "Tags": ", ".join(tag["name"] for tag in q["topicTags"])
            })

    skip += limit

# Save to CSV
with open("solved_problems.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "URL", "Tags"])
    writer.writeheader()
    writer.writerows(solved_problems)

print(f"✅ Saved {len(solved_problems)} solved problems to 'solved_problems.csv'")

