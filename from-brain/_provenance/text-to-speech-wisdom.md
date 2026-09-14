---
title: "Extracted Wisdom: Text-to-Speech"
source: /Users/kirkwon/wiki-personal/concepts/text-to-speech.md
date: 2026-05-09
type: wisdom
tags: [tts, insights]
---

# Extracted Wisdom: Text-to-Speech

## Provider Options
- For quick cloud-based audio in MARP presentations, use `gtts` (Google Text-to-Speech).
- For offline synthesis in MARP presentations, use `pyttsx3` for cross-platform, no-internet TTS.
- Explore KittenTTS (GitHub: KittenML/KittenTTS) as an open-source, lightweight alternative.
- Consider ElevenLabs for high-quality, natural-sounding TTS via API.
- Evaluate Microsoft Azure Cognitive Services Text to Speech for scalable, enterprise-grade voices.
- Google Cloud Text-to-Speech offers WaveNet voices and extensive language support.
- The Python package `gTTS` provides a simple interface to Google's TTS engine.

## Local Setup (MARP presentations)
- Use `gtts` for generating audio files directly from Markdown slide notes.
- Use `pyttsx3` when internet access is unavailable or for privacy-sensitive content.
- Both tools can be invoked via command line or integrated into slide generation scripts.

## Integration and Linking
- Link this TTS concept from AI-related notes (e.g., [[ai-as-decision-enhancement]]) or tool pages for easy reference.
- Maintain a centralized concept note to avoid duplicating provider details across multiple files.

## Related Concepts
- Connect TTS to [[local-ai-models]] when considering offline, self-hosted solutions.
- TTS intersects with [[mcp-protocol]] for potential voice-enabled AI agent interactions.
- Consider TTS as a component of [[ai-as-decision-enhancement]] for auditory feedback in decision systems.

---
*Extracted from source text. All insights are directly derived from the original content.*
