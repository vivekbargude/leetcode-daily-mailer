
````markdown
# 📬 LeetCode Daily Challenge Email Bot

Automatically receive the **LeetCode Daily Coding Challenge** in your email inbox every day at **8:00 AM IST** using **GitHub Actions**.

No servers or paid services required — just GitHub + Gmail!

---

## 🚀 Features

- 📌 Automatically fetches LeetCode's Daily Challenge using their GraphQL API
- 📧 Sends a nicely formatted email to your inbox
- ⏰ Fully automated using GitHub Actions (`cron`) — runs **daily**
- 🔐 Keeps your credentials secure using GitHub Secrets

---

## 🛠️ How It Works

This project uses:
- A Python script (`daily_leetcode.py`) to:
  - Fetch the daily question from LeetCode
  - Send it to your email
- GitHub Actions (`.github/workflows/daily.yml`) to:
  - Schedule the script to run every day at 8:00 AM IST (2:30 AM UTC)
  - Run it without your intervention

---

## 📦 Requirements

- A [GitHub](https://github.com) account
- A Gmail account with [2FA enabled](https://myaccount.google.com/security)
- A [Gmail App Password](https://myaccount.google.com/apppasswords)

---

## 🔧 Setup Instructions

### 1. **Fork or Clone this Repository**
You can either fork this repo or clone it and push it to your own GitHub repo.

```bash
git clone https://github.com/yourusername/leetcode-daily-mailer.git
cd leetcode-daily-mailer
````

---

### 2. **Add Your Secrets to GitHub**

Go to your repo → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add the following:

| Name             | Value                                                                    |
| ---------------- | ------------------------------------------------------------------------ |
| `SENDER_EMAIL`   | Your Gmail address (e.g. [you@gmail.com](mailto:you@gmail.com))          |
| `RECEIVER_EMAIL` | Where you want the daily question sent                                   |
| `EMAIL_PASSWORD` | Your [App Password](https://myaccount.google.com/apppasswords) for Gmail |

---

### 3. **Check the Cron Schedule (optional)**

In `.github/workflows/daily.yml`, the job is scheduled like this:

```yaml
schedule:
  - cron: '30 2 * * *'  # This is 8:00 AM IST (2:30 AM UTC)
```

You can change the time by modifying the cron expression. Use [crontab.guru](https://crontab.guru/) for help.

---

### 4. **Test it Manually (optional)**

Go to the **Actions** tab of your repo → Select **"LeetCode Daily Mailer"** → Click **"Run workflow"** to test it now.

---

## 🧪 Output Example

You'll receive an email like:

```
LeetCode Daily Question:

Title: Maximum Depth of Binary Tree
Difficulty: Easy
Tags: Depth-First Search, Tree

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
```

---


