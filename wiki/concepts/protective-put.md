---
type: concept
title: Protective Put
description: "--
Protective Put (Married Put)"
created: 2026-04-24
updated: 2026-04-24
tags:
- personal-finance
- options
- derivatives
- hedging
sources:
- Options Trading.md
related:
- options-trading
- put-option
- covered-call
- risk-management
---
--
# Protective Put (Married Put)

Protective Put είναι μια στρατηγική όπου κατέχω μετοχή και αγοράζω put option ως ασφάλιση. Λειτουργεί σαν ασφαλιστικό polis για το portfolίου μου.

## Παράδειγμα
- Κατέχω 100 μετοχές σε $100
- Αγοράζω $95 put για $2 premium

## Σενάρια Κέρδους
- Μετοχή = $110: Κρατάω τη μετοχή, put λήγει άσκο — ζημιά $2 premium
- Μετοχή = $100: Κρατάω τη μετοχή, put λήγει άσκο — ζημιά $2 premium
- Μετοχή = $80: Put πληρώνει $15 ($95 strike - $80), καθαρό κέρδος $15 - $2 = $13

## Χρήση
Insurance against market crash. Κόστος: το premium που πληρώνομαι, σαν ασφαλιστικό polis.

## Σχετικές Έννοιες
- [[put-option]]
- [[covered-call]]
- [[options-trading]]