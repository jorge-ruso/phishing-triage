# phishing-triage

Small Python tool to help triage suspicious emails. You give it an .eml file and it shows the headers that matter and the SPF / DKIM / DMARC results.

I'm building it step by step while I learn email analysis for SOC work. It's a work in progress.

## What it does now

- Reads an .eml file
- Shows From, Reply-To, Return-Path, Subject, Date and number of server hops
- Checks SPF, DKIM and DMARC from the `Authentication-Results` header

Only uses the Python standard library, nothing to install.

## How to use

```
python triage.py samples/email.eml
```

Example with a real phishing email:

```
from: "[BB] - Seu saldo foi liberado - Código: 11084339647130851921" <prestonconstance587@gmail.com>
reply_to: None
return_path: prestonconstance587@gmail.com
subject: Liberação de IRPF - 6NwlyfzWcsNerv0
date: Wed, 26 Jul 2023 17:59:01 +0000

Saltos de servidor: 6

--- Autenticación ---
spf: pass
dkim: pass
dmarc: pass
```

Everything passes, but it's phishing. The name pretends to be a bank and the address is a random Gmail. More about this in the report.

## Analysis

- [First test - 5 phishing emails](reports/initial-header-analysis.md)

## Next steps

- [ ] Compare domains between From, Reply-To and Return-Path
- [ ] Detect brand names in the display name that don't match the domain
- [ ] Flag free email providers
- [ ] Extract URLs and decode hidden links (Base64)
- [ ] Check IPs and URLs with VirusTotal / AbuseIPDB
- [ ] Risk score and automatic verdict
- [ ] Save the result as a report

## Safety

Phishing samples are real. Don't open them in an email client and don't visit the links. The script only reads text, it doesn't open or run anything.

My own emails stay in `samples/raw/`, which is in `.gitignore` and never gets uploaded.

## Samples

Phishing emails from [rf-peixoto/phishing_pot](https://github.com/rf-peixoto/phishing_pot).
