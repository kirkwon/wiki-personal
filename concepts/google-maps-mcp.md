---
date: 2026-07-19
type: concept
title: Google Maps Mcp
created: 2026-07-19
updated: '2026-09-09'
tags:
- skill
- MCP
- maps
- geocoding
- routing
- mcp
sources:
- hermes://skill/google-maps-mcp
description: MCP server for Google Maps API — geocoding, places search, directions,
  distance matrix, elevation, and place details.
---

# Google Maps Mcp

> MCP server for Google Maps API — geocoding, places search, directions, distance matrix, elevation, and place details.

## Overview

- **Tools** — | Tool | Description | |------|-------------| | `geocode` | Address → lat/lng coordinates | | `reverse_geocode` | Lat/lng → address | | `search_places` | Text search for places (with optional location bias) | | `get_place_details` | Full place info: name, address, contact, hours, ratings | | `get_distance_matrix` | Pairwise distances/times between multiple origins and destinations | | `get_directions` | Turn-by-turn route from A to B | | `get_elevation` | Elevation for lat/lng points |
- **Hermes Integration** — Once connected via mcporter, these tools are available to the Hermes agent automatically. Just ask natural-language location/routing questions.

## Related

- Skill source: `/Users/kirkwon/.hermes/skills/mcp/google-maps-mcp/SKILL.md`
- Auto-filled from the skill body on 2026-09-09 (was a bodyless stub).
