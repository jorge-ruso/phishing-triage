# Phishing header analysis - first test

Jorge Campos Bellido - October 2026

First test of my tool `triage.py`. For now it reads the headers of an .eml file and checks SPF, DKIM and DMARC. I tested it with 5 real phishing emails from [phishing_pot](https://github.com/rf-peixoto/phishing_pot) and 2 spam emails from my Gmail to compare.

I only looked at headers. I didn't open the emails or click links. Domains are written like `gmail[.]com` so nobody clicks them.

## Spam from my inbox (to compare)

Two newsletters from my spam folder. Sent with Mailjet, SPF/DKIM/DMARC all pass, and they have an unsubscribe link. Annoying but not phishing.

I saw two tricks here that phishing also uses: a 1x1 invisible image to track if I open the email, and links with the real address hidden in Base64.

## phish1 - fake Bradesco bank

- From: `BANCO DO BRADESCO LIVELO <banco.bradesco[@]atendimento[.]com[.]br>`
- Return-Path: `root[@]ubuntu-s-1vcpu-1gb-35gb-intel-sfo3-06`
- SPF temperror, DKIM none, DMARC temperror

The name says Bradesco but the domain is not from the bank. The Return-Path looks like a default name of a cheap cloud server, and it was sent as root. Nothing passed. Subject says the points expire today, so urgency.

## phish2 - solar panels

- From: `zonnepaneel[@]appjj[.]serenitepure[.]fr`
- Reply-To: `news[@]aichakandisha[.]com`
- Return-Path: `return[@]dturm[.]de`
- SPF, DKIM, DMARC none

Three different domains for one sender, and no authentication. Dutch email from a French domain.

## phish3 - fake Banco do Brasil

- From: `"[BB] - Seu saldo foi liberado..." <prestonconstance587[@]gmail[.]com>`
- SPF pass, DKIM pass, DMARC pass

This one passed everything and it's still phishing. It came from a real Gmail account, so the checks are correct, they only prove it came from gmail.com. The name says Banco do Brasil but a bank doesn't send from Gmail.

For me this was the most important one: all pass doesn't mean safe.

## phish4 - free gift

- Return-Path: `finley.walker[@]ghjgamerisons03[.]onmicrosoft[.]com`
- SPF fail, DKIM pass, DMARC none

onmicrosoft.com is the free domain you get with any Microsoft 365 account, also trials. Attackers use it because filters trust Microsoft. SPF failed.

## phish5 - fake Microsoft alert

- From: `"Microsoft account team" <no-reply[@]access-accsecurity[.]com>`
- Reply-To: `sotrecognizd[@]gmail[.]com`
- Return-Path: `bounce[@]thcultarfdes[.]co[.]uk`
- SPF none, DKIM none, DMARC permerror

Domain looks like Microsoft but it isn't. Replies go to a Gmail and the Return-Path is another domain. Classic "unusual sign-in" email to scare you.

## What I saw in all of them

- brand in the name, but the domain is something else
- different domains in From, Reply-To and Return-Path
- free accounts or cheap servers
- authentication failing (not always, see phish3)
- urgency or a prize in the subject

MITRE: T1566 Phishing, T1656 Impersonation, T1583 Acquire Infrastructure, T1585.002 Email Accounts.

Only 5 emails and only headers, no links or attachments yet.

## Next

Add these patterns as rules in the tool so it gives a risk score by itself.

Samples: [rf-peixoto/phishing_pot](https://github.com/rf-peixoto/phishing_pot)
