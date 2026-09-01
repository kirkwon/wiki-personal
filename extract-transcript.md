---
type: concept
title: Extract Transcript
created: 2026-08-31
updated: 2026-08-31
tags:
  - Skill
  - video
---

# extract-transcript

>-

## Usage

# YouTube Video Transcript Extraction

## Purpose

Given a YouTube video URL or video ID, return the video's title, channel/uploader name, duration in seconds, the full transcript as timestamped segments, and a flag indicating whether the captions are auto-generated (`asr`) or human-authored. Read-only — never likes, comments, subscribes, or watches.

## When to Use

- Summarizing or indexing the spoken content of a video.
- Search/discovery agents that need to grep video bodies for a query.
- Translation / accessibility flows that need source-language captions to retranslate from.
- Any pipeline that previously screen-scraped the "Show transcript" UI panel — the InnerTube API path is faster, cheaper, and degrades more honestly when captions are unavailable.

## Workflow

YouTube's web UI is a thin client over the public **InnerTube** API at `https://www.youtube.com/youtubei/v1/`. The transcript task needs two API calls (one optional) and zero browser pixels for ~95% of videos — only fall back to a browser session when InnerTube returns a `LOGIN_REQUIRED` / `AGE_VERIFICATION_REQUIRED` playability status and the caller wants to attempt the consent flow.

### 1. Normalize the input to a video ID

Accept any of:
- `https://www.youtube.com/watch?v=<ID>` (canonical)
- `https://youtu.be/<ID>`
- `https://www.youtube.com/shorts/<ID>`
- `https://www.youtube.com/embed/<ID>`
- `https://m.youtube.com/watch?v=<ID>`
- bare 11-char id (`[A-Za-z0-9_-]{11}`)

Strip query params other than `v=` and any list/playlist context. The video ID is always exactly 11 characters; reject anything else early.

### 2. (Cheap, ~0.1s) Fetch title + channel via the oEmbed endpoint

```
GET https://www.youtube.com/oembed?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D<ID>&format=json
```

Returns JSON with `title`, `author_name` (channel), `author_url`, and `thumbnail_url`. No auth, no key. ~450 bytes. Use this for the metadata even if you later succeed at the InnerTube call — it's a sanity check that the video actually exists publicly:

- **404** → video is private/deleted/unlisted-without-access. Return `success: false, reason: "video_unavailable"` and stop.
- **401** → embedding disabled but the video may still be public; do not stop. Continue to step 3 and read `videoDetails.title` / `author` from the InnerTube response.

### 3. POST to InnerTube `/player` for caption track URLs + duration

```
POST https://www.youtube.com/youtubei/v1/player?prettyPrint=false
Content-Type: application/json
Origin: https://www.youtube.com

{
  "context": {
    "client": {
      "clientName": "ANDROID",
      "clientVersion": "19.09.37",
      "androidSdkVersion": 30,
      "hl": "en",
      "gl": "US",
      "userAgent": "com.google.android.youtube/19.09.37 (Linux; U; Android 14) gzip"
    }
  },
  "videoId": "<ID>"
}
```

**Why the `ANDROID` client over `WEB`?**

| Client       | Needs API key? | Needs visitorData / PoToken? | Returns captionTracks? | Notes |
|---|---|---|---|---|
| `WEB`    

...(truncated)