# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 16:34
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `d8bcadf1-f589-4647-9afa-c8b5aded417e` | human | 0.318 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `69ad0a05-bfbc-47b9-99e6-38e50bf83511` | unsure | 0.416 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f82725e5-6610-40a4-8cdf-17890647344e` | unsure | 0.559 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `3931fc2b-32bd-42eb-ab8f-a5b5f3d08566` | unsure | 0.584 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `7c8bb36e-7be6-42f0-a916-d6d1e883a3fb` | human | 0.306 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d0067b9e-f977-4b4c-9c04-8279b7968078` | unsure | 0.376 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `3f3e1160-ca07-40c4-91a1-23e371cbb42e` | unsure | 0.632 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `512473ed-cf2b-48c0-89a1-de33d7f30a8f` | human | 0.319 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `1674ad9f-cf7f-4417-b22a-01825c599ebe` | unsure | 0.574 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `e108f3f5-83a7-4095-870c-d29af2ac2a50` | ai | 0.815 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `1529e741-79d9-496c-86e3-2b649a5c2f0e` | unsure | 0.538 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `27249852-eb67-480a-8e59-e25d4d004a7d` | ai | 0.661 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `ac4ea52a-88db-4f20-9963-1b8b70109d6f` | ai | 0.678 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `5a98483d-f74b-4ec8-94c0-78b5bbee5da3` | ai | 0.676 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `3d07475d-0238-458d-a396-486e2c439189` | ai | 0.706 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `2b6cf02e-8ea4-4a18-a56f-04ab4ec0102d` | ai | 0.677 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `70af09f8-7b24-4818-be44-9712a18492f5` | ai | 0.662 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `2de3b3f0-d7f2-4cf8-bb18-ec02860f2b0b` | human | 0.329 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `cf114924-7b2c-4e1a-aaa2-74d8a0a7a462` | unsure | 0.366 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `46cad7f9-fda0-4fa7-8d51-a53424381da9` | human | 0.217 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f572c658-84d3-4613-a71a-241f14225fe2` | unsure | 0.529 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `e740641d-935a-4157-a087-39b574cc91d2` | unsure | 0.486 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `6fc9bc11-3cf8-472a-8079-27eb32ee2fb3` | unsure | 0.549 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `85bdc857-14ea-4e60-b458-44e13cd531b5` | unsure | 0.505 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `33b2a6d1-4d9f-461a-a1dd-306bff4f228f` | human | 0.280 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `93f164cf-8eab-4383-baba-683c55060825` | human | 0.207 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `56be536b-a9d4-425b-ac0c-3252f01b2d7a` | ai | 0.839 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `8093c24b-a0fb-4381-9040-04788678001e` | ai | 0.798 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `3ecb536f-bce0-4f73-9613-f0f1487d2d8e` | ai | 0.744 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `2021ef4c-ec8f-4482-bd20-ef592900af80` | unsure | 0.384 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | `be226d37-fb89-457a-bb2a-3cb7861dd6e3` | human | 0.270 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 429 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a948d215-49cf-4dfe-98f1-f8ca8f874bad` | human | 0.257 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e97d7fb3-2ea3-4e96-bb10-1532565b7009` | human | 0.257 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `81c92ddd-a4e8-466d-9c37-4d677ae435ca` | human | 0.257 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3d1cb528-b8a2-42dd-803d-500120b4fafe` | human | 0.257 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "d8bcadf1-f589-4647-9afa-c8b5aded417e",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.31784011238590987,
  "model_score": 0.1635,
  "style_score": 0.5493502809647747,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "69ad0a05-bfbc-47b9-99e6-38e50bf83511",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4164756808377093,
  "model_score": 0.5943,
  "style_score": 0.14973920209427327,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "f82725e5-6610-40a4-8cdf-17890647344e",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5585162579936132,
  "model_score": 0.6662,
  "style_score": 0.39699064498403286,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "3931fc2b-32bd-42eb-ab8f-a5b5f3d08566",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5838997598079025,
  "model_score": 0.6114,
  "style_score": 0.5426493995197564,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "7c8bb36e-7be6-42f0-a916-d6d1e883a3fb",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.30583045188298713,
  "model_score": 0.3212,
  "style_score": 0.28277612970746785,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "d0067b9e-f977-4b4c-9c04-8279b7968078",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.3758057923497268,
  "model_score": 0.5727,
  "style_score": 0.08046448087431694,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "3f3e1160-ca07-40c4-91a1-23e371cbb42e",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.6324334273606983,
  "model_score": 0.5862,
  "style_score": 0.7017835684017456,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "512473ed-cf2b-48c0-89a1-de33d7f30a8f",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3192377490060915,
  "model_score": 0.2452,
  "style_score": 0.43029437251522856,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "1674ad9f-cf7f-4417-b22a-01825c599ebe",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5744450569244941,
  "model_score": 0.7042,
  "style_score": 0.37981264231123535,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "e108f3f5-83a7-4095-870c-d29af2ac2a50",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8145212831031555,
  "model_score": 0.9792,
  "style_score": 0.567503207757889,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "1529e741-79d9-496c-86e3-2b649a5c2f0e",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5375506697268327,
  "model_score": 0.6175,
  "style_score": 0.4176266743170818,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "27249852-eb67-480a-8e59-e25d4d004a7d",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6612680406279576,
  "model_score": 0.7387,
  "style_score": 0.5451201015698942,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "ac4ea52a-88db-4f20-9963-1b8b70109d6f",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6775476811264989,
  "model_score": 0.8051,
  "style_score": 0.48621920281624714,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "5a98483d-f74b-4ec8-94c0-78b5bbee5da3",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6757419505431139,
  "model_score": 0.8329,
  "style_score": 0.440004876357785,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "3d07475d-0238-458d-a396-486e2c439189",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7060304306134102,
  "model_score": 0.8005,
  "style_score": 0.5643260765335256,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "2b6cf02e-8ea4-4a18-a56f-04ab4ec0102d",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6774949524010564,
  "model_score": 0.8814,
  "style_score": 0.3716373810026411,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "70af09f8-7b24-4818-be44-9712a18492f5",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.6615137708117849,
  "model_score": 0.8816,
  "style_score": 0.33138442702946225,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "2de3b3f0-d7f2-4cf8-bb18-ec02860f2b0b",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.32945695154586735,
  "model_score": 0.3223,
  "style_score": 0.3401923788646684,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "cf114924-7b2c-4e1a-aaa2-74d8a0a7a462",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.36646289741069854,
  "model_score": 0.4625,
  "style_score": 0.2224072435267463,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "46cad7f9-fda0-4fa7-8d51-a53424381da9",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.21724721505939099,
  "model_score": 0.2044,
  "style_score": 0.23651803764847745,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "f572c658-84d3-4613-a71a-241f14225fe2",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5288828727402219,
  "model_score": 0.5943,
  "style_score": 0.43075718185055495,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "e740641d-935a-4157-a087-39b574cc91d2",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.485595382005774,
  "model_score": 0.4998,
  "style_score": 0.46428845501443505,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "6fc9bc11-3cf8-472a-8079-27eb32ee2fb3",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5493315171606901,
  "model_score": 0.6401,
  "style_score": 0.4131787929017251,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "85bdc857-14ea-4e60-b458-44e13cd531b5",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5047870874666223,
  "model_score": 0.5583,
  "style_score": 0.42451771866655574,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "33b2a6d1-4d9f-461a-a1dd-306bff4f228f",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.27999999999999997,
  "model_score": 0.0,
  "style_score": 0.7,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "93f164cf-8eab-4383-baba-683c55060825",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.20672000000000001,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "56be536b-a9d4-425b-ac0c-3252f01b2d7a",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.83856,
  "model_score": 0.9976,
  "style_score": 0.6,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "8093c24b-a0fb-4381-9040-04788678001e",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7981400000000001,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "3ecb536f-bce0-4f73-9613-f0f1487d2d8e",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7438400000000001,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "This was likely written with AI assistance.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "2021ef4c-ec8f-4482-bd20-ef592900af80",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.3837,
  "model_score": 0.2395,
  "style_score": 0.6,
  "label": "A confident determination could not be made. The result is uncertain.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "be226d37-fb89-457a-bb2a-3cb7861dd6e3",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.26952,
  "model_score": 0.0492,
  "style_score": 0.6,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "a948d215-49cf-4dfe-98f1-f8ca8f874bad",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "e97d7fb3-2ea3-4e96-bb10-1532565b7009",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "81c92ddd-a4e8-466d-9c37-4d677ae435ca",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "3d1cb528-b8a2-42dd-803d-500120b4fafe",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.25722,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This was likely written by a human author.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
