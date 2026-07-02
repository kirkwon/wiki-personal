# Connecting Google Workspace to Hermes Agent (OAuth 2.0 Setup Guide)

**Date:** 2026-06-27  
**Tags:** #hermes, #google-workspace, #oauth, #setup-guide  
**Difficulty:** ⭐⭐⭐ (straightforward once you know the gotchas)  

---

## TL;DR

Setting up Google Workspace OAuth for an AI agent feels intimidating, but the actual flow is clean once you sidestep two traps: **use Desktop app credentials** (not Web), and **run a local HTTP callback server** to catch the redirect. This guide walks through the full setup with all the dead ends marked.

---

## Why Connect Google Workspace?

If you're running an AI agent like [Hermes](https://hermes-agent.nousresearch.com), connecting Google Workspace gives it:

- **Gmail** — read, send, triage email
- **Calendar** — check upcoming events, morning briefings
- **Drive** — search and read documents
- **Sheets** — read and write spreadsheet data
- **Docs** — read (and write) documents
- **Contacts** — look up contact info

That's a massive upgrade over IMAP-only email access. Calendar, Drive, Sheets, and Docs all become agent-accessible in a single OAuth flow.

---

## Prerequisites

- A Google account (Gmail or Google Workspace)
- [Google Cloud Console](https://console.cloud.google.com/) access
- Python 3.8+ with `google-api-python-client`, `google-auth-oauthlib`, `google-auth-httplib2`
- An agent framework with a Google Workspace integration (this guide uses Hermes Agent)

---

## Step-by-Step

### Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click the project dropdown → **New Project**
3. Name it (e.g., "Hermes Agent Workspace")
4. Create it

### Step 2: Enable APIs

Navigate to **APIs & Services → Library** and enable each of these:

| API | Purpose |
|---|---|
| Gmail API | Email read/send |
| Google Calendar API | Events and scheduling |
| Google Drive API | File and document access |
| Google Sheets API | Spreadsheet read/write |
| Google Docs API | Document access |
| People API | Contacts |

### Step 3: Configure the OAuth Consent Screen

1. Go to **APIs & Services → OAuth consent screen**
2. Choose **External** (unless you have a Google Workspace org)
3. Fill in:
   - App name: "Hermes Agent"
   - User support email: your email
   - Developer contact: your email
4. Add the scopes you'll need (they can match what you request later)
5. **Add yourself as a Test User** — this is critical
   - Under "Test users", click **Add Users**
   - Add your Gmail address
   - Without this, you'll get "Access blocked"

### Step 4: Create OAuth Credentials — ⚠️ USE DESKTOP APP

> **🚨 GOTCHA #1: Do NOT create a Web application credential.**
>
> Web credentials require you to pre-register every redirect URI in the Google Cloud Console. Desktop app credentials allow `http://localhost:PORT` dynamically — no registration needed. This is the single biggest time-saver in this guide.

1. Go to **APIs & Services → Credentials**
2. **Create Credentials → OAuth client ID**
3. Application type: **Desktop app** (NOT Web application)
4. Name it "Hermes Agent Desktop"
5. Download the JSON file
6. Save it somewhere safe (e.g., `~/Downloads/credentials.json`)

### Step 5: Set Up the Local Callback Server

The OAuth flow redirects to `http://localhost:PORT` after you approve. You need something listening there to catch the redirect.

> **🚨 GOTCHA #2: Port 1 hangs. Use port 8080.**
>
> The Hermes setup script defaults to `localhost:1`, which is a privileged port. No process can bind to it without root, so the browser hangs indefinitely waiting for a response that never comes. Use port 8080 (or any unprivileged port).

Here's a minimal callback server (`oauth_callback_server.py`):

```python
#!/usr/bin/env python3
"""Local OAuth callback server — catches the Google redirect with the auth code."""
import http.server
import json
import urllib.parse

class OAuthHandler(http.server.BaseHTTPRequestHandler):
    auth_data = None

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if 'code' in params:
            code = params['code'][0]
            OAuthHandler.auth_data = {'code': code, 'scope': params.get('scope', [''])[0]}

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(
                "<html><body style='font-family:sans-serif;text-align:center;padding:60px'>"
                "<h1>Authorization Successful!</h1>"
                "<p>You can close this tab and return to your chat.</p>"
                "</body></html>".encode()
            )
            print(f"AUTH_CODE_RECEIVED:{code}", flush=True)
        elif 'error' in params:
            self.send_response(400)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(f"<html><body><h1>Error</h1></body></html>".encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    port = 8080
    server = http.server.HTTPServer(('localhost', port), OAuthHandler)
    print(f"OAuth callback server listening on http://localhost:{port}")
    server.handle_request()
    if OAuthHandler.auth_data:
        with open('oauth_callback_result.json', 'w') as f:
            json.dump(OAuthHandler.auth_data, f, indent=2)
        print("Auth data saved to oauth_callback_result.json")
    server.server_close()
```

Run it before you click the OAuth link:

```bash
python3 oauth_callback_server.py
```

### Step 6: Build the OAuth URL and Authorize

You need a PKCE-enhanced OAuth URL. Here's how to build it:

```python
import json, hashlib, base64, os, secrets

# Load your downloaded credentials
with open('~/Downloads/credentials.json') as f:
    cs = json.load(f)

client_id = cs['installed']['client_id']

# Generate PKCE challenge
code_verifier = base64.urlsafe_b64encode(os.urandom(40)).decode('utf-8').rstrip('=')
code_challenge = base64.urlsafe_b64encode(
    hashlib.sha256(code_verifier.encode('utf-8')).digest()
).decode('utf-8').rstrip('=')
state = secrets.token_urlsafe(16)

# Define scopes
scopes = " ".join([
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/drive",          # full Drive access
    "https://www.googleapis.com/auth/contacts.readonly",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/documents",       # full Docs access
])

# Build the URL
url = (
    f"https://accounts.google.com/o/oauth2/auth"
    f"?response_type=code"
    f"&client_id={client_id}"
    f"&redirect_uri=http://localhost:8080"
    f"&scope={scopes.replace(' ', '+')}"
    f"&state={state}"
    f"&code_challenge={code_challenge}"
    f"&code_challenge_method=S256"
    f"&access_type=offline"
    f"&prompt=consent"
)

# Save PKCE data for token exchange
with open('oauth_pending.json', 'w') as f:
    json.dump({"state": state, "code_verifier": code_verifier, "redirect_uri": "http://localhost:8080"}, f)

print(url)
```

Open the generated URL in your browser. Google will:
1. Ask you to sign in
2. Show a consent screen (may warn about "unverified app" — this is normal for personal projects)
3. Redirect to `http://localhost:8080/?code=YOUR_AUTH_CODE&scope=...`

Your callback server catches it and saves the code.

### Step 7: Exchange Code for Token

```python
import json, requests

with open('oauth_pending.json') as f:
    pending = json.load(f)

with open('~/Downloads/credentials.json') as f:
    cs = json.load(f)

resp = requests.post("https://oauth2.googleapis.com/token", data={
    "code": "YOUR_AUTH_CODE",
    "client_id": cs['installed']['client_id'],
    "client_secret": cs['installed']['client_secret'],
    "redirect_uri": pending["redirect_uri"],
    "grant_type": "authorization_code",
    "code_verifier": pending["code_verifier"],
})

token_data = resp.json()
# Save as google_token.json — this is your persistent credential
with open('google_token.json', 'w') as f:
    json.dump({
        "token": token_data["access_token"],
        "refresh_token": token_data.get("refresh_token"),
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": cs['installed']['client_id'],
        "client_secret": cs['installed']['client_secret'],
        "scopes": token_data.get("scope", "").split(),
        "type": "authorized_user"
    }, f, indent=2)
```

### Step 8: Test the Connection

```python
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

creds = Credentials.from_authorized_user_file('google_token.json')
if creds.expired:
    creds.refresh(Request())

# Test Gmail
gmail = build('gmail', 'v1', credentials=creds)
results = gmail.users().messages().list(userId='me', maxResults=3).execute()
print(f"Gmail: {len(results.get('messages', []))} recent messages")

# Test Calendar
from datetime import datetime, timezone
cal = build('calendar', 'v3', credentials=creds)
now = datetime.now(timezone.utc).isoformat()
events = cal.events().list(calendarId='primary', timeMin=now, maxResults=5, singleEvents=True, orderBy='startTime').execute()
print(f"Calendar: {len(events.get('items', []))} upcoming events")
```

---

## The Three Traps (and How to Avoid Them)

### Trap 1: Web App vs Desktop App Credentials

**Symptom:** `Error 400: redirect_uri_mismatch`

**Cause:** Web application credentials require you to pre-register redirect URIs in Google Cloud Console. Desktop app credentials allow `http://localhost:PORT` dynamically.

**Fix:** Always create **Desktop app** credentials. Even if you're running a "server" locally, Desktop is the right choice for agent OAuth.

### Trap 2: Port 1 Hangs Forever

**Symptom:** Browser approves successfully but then hangs on a blank page. Nothing ever returns.

**Cause:** The redirect points to `localhost:1` (a privileged port). No user-space process can bind to it. The browser sends the request, waits for a response, and hangs.

**Fix:** Use port 8080 (or any unprivileged port 1024+). Update your redirect URI to `http://localhost:8080`.

### Trap 3: "Access blocked" / "This app's request is invalid"

**Symptom:** `Error 400: redirect_uri_mismatch` or "You can't sign in because this app sent an invalid request."

**Cause:** Either your email isn't in the Test Users list, or the consent screen is misconfigured.

**Fix:**
1. **OAuth consent screen → Test Users → Add your Gmail**
2. Verify your consent screen is published (not in draft)
3. Use Desktop app credentials (not Web — see Trap 1)

---

## Upgrading Scopes Later

Need to add write access to Drive or Docs after the initial setup? You need to re-authorize with the new scopes. The key is `prompt=consent` in the OAuth URL — it forces Google to show the consent screen again so you can approve the new permissions.

```python
# Upgrade from drive.readonly → drive, documents.readonly → documents
# Just change the scope URLs in the OAuth URL and re-authorize
```

Your old token gets overwritten with the new one. The refresh token carries forward the new scope set.

---

## Security Notes

- The `client_secret` in Desktop credentials is not actually secret — Google's [own documentation](https://developers.google.com/identity/protocols/oauth2/native-app) acknowledges this. The security model relies on PKCE + the redirect to localhost, not on the client secret.
- Store `google_token.json` securely. It contains your refresh token — anyone with it can generate access tokens until you revoke.
- To revoke: go to [Google Account Permissions](https://myaccount.google.com/permissions) and remove the app.
- If you have **Advanced Protection** enabled on your Google account, OAuth won't work for non-Google apps. You'll need to temporarily disable it or use a different account.

---

## What's Next?

Once connected, you can:

- **Morning briefings** — Calendar + email + weather, delivered on schedule
- **Email triage** — Automated urgency classification with negation-aware filtering
- **Document search** — Search across Drive for specific content
- **Spreadsheet automation** — Read/write Sheets for data pipelines
- **Contact lookup** — Enrich data with People API

The setup takes ~15 minutes once you know the traps. The payoff is a fully integrated Google Workspace agent.
