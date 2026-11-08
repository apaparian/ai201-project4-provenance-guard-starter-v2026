# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-08 12:41
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `8d6d4b74-e1c6-487c-ae95-d6a99c8d2b21` | human | 0.318 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `558d676a-3c27-42cc-9ad9-8203484782d2` | unsure | 0.416 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `e05c0c94-25b9-4c03-9dcc-ff4f73fd9de7` | unsure | 0.559 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `24b2cef7-6764-4e5a-a4ad-aa8c45d26573` | unsure | 0.584 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `4458ebaf-3330-4164-b689-d0b698b1e3a2` | human | 0.306 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `fb71a5bf-dfff-4d5b-9cee-f376627d49f5` | unsure | 0.376 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `e68368c1-31ca-454b-b9df-2a2d08996894` | unsure | 0.632 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `a03989f9-ac5b-419a-ba74-23d427eaa98a` | human | 0.319 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `5b2e887f-e9a5-4193-beb8-d9a2841edc50` | unsure | 0.574 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a852f662-0365-4132-a805-695d4e16dad9` | ai | 0.815 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `a0c3cc13-aa54-4170-be5f-ccc18f205aaa` | unsure | 0.538 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `dff0143d-021a-4d48-af50-61b9c1c13d2e` | ai | 0.661 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `187e962c-6220-4377-9bf8-3698ddfc0225` | ai | 0.678 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `9ee18116-0bcf-4f80-80ba-d92534cdc4ee` | ai | 0.676 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `6c71db14-6079-456d-8ecc-179a66883337` | ai | 0.706 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `57381a79-9375-4cfa-916e-73a3418f10b8` | ai | 0.677 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c9d3dd94-3dfa-4413-a3f7-cc80696584e0` | ai | 0.662 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `f035bbfe-a061-4ac1-ab8a-67c93c350101` | human | 0.329 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `770042de-4f89-44d1-aa6b-c3a64cff585d` | unsure | 0.366 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `bcc96bda-55c7-452d-9cc9-19bccb12ae13` | human | 0.217 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `10f067d8-93c5-49cd-ae2d-ea6e7a7cf40a` | unsure | 0.529 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `bfe38a08-3b75-47ab-be4f-d5a73c8a9748` | unsure | 0.486 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `4cba49b5-e33a-43a8-a40c-89ca9c28976d` | unsure | 0.549 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c89c06dc-10df-4036-b4b6-d38ffd7ede7e` | unsure | 0.505 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `96ee0fed-fa5d-44a4-84b5-24a41281066b` | human | 0.280 |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `be22a771-29e6-4e92-8578-c29451aa531f` | unsure | 0.384 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 429 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `66f28392-2a17-4446-97fd-ff1b68af645a` | human | 0.257 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a0f572a5-a93c-4718-a70b-01d81a056d4f` | human | 0.257 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2366a1b7-6c46-4a7b-b244-8154075ed9a1` | human | 0.257 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5afc476c-755d-419f-a2e3-2cbc145dcdc7` | human | 0.257 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "8d6d4b74-e1c6-487c-ae95-d6a99c8d2b21",
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
  "content_id": "558d676a-3c27-42cc-9ad9-8203484782d2",
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
  "content_id": "e05c0c94-25b9-4c03-9dcc-ff4f73fd9de7",
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
  "content_id": "24b2cef7-6764-4e5a-a4ad-aa8c45d26573",
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
  "content_id": "4458ebaf-3330-4164-b689-d0b698b1e3a2",
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
  "content_id": "fb71a5bf-dfff-4d5b-9cee-f376627d49f5",
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
  "content_id": "e68368c1-31ca-454b-b9df-2a2d08996894",
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
  "content_id": "a03989f9-ac5b-419a-ba74-23d427eaa98a",
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
  "content_id": "5b2e887f-e9a5-4193-beb8-d9a2841edc50",
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
  "content_id": "a852f662-0365-4132-a805-695d4e16dad9",
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
  "content_id": "a0c3cc13-aa54-4170-be5f-ccc18f205aaa",
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
  "content_id": "dff0143d-021a-4d48-af50-61b9c1c13d2e",
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
  "content_id": "187e962c-6220-4377-9bf8-3698ddfc0225",
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
  "content_id": "9ee18116-0bcf-4f80-80ba-d92534cdc4ee",
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
  "content_id": "6c71db14-6079-456d-8ecc-179a66883337",
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
  "content_id": "57381a79-9375-4cfa-916e-73a3418f10b8",
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
  "content_id": "c9d3dd94-3dfa-4413-a3f7-cc80696584e0",
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
  "content_id": "f035bbfe-a061-4ac1-ab8a-67c93c350101",
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
  "content_id": "770042de-4f89-44d1-aa6b-c3a64cff585d",
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
  "content_id": "bcc96bda-55c7-452d-9cc9-19bccb12ae13",
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
  "content_id": "10f067d8-93c5-49cd-ae2d-ea6e7a7cf40a",
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
  "content_id": "bfe38a08-3b75-47ab-be4f-d5a73c8a9748",
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
  "content_id": "4cba49b5-e33a-43a8-a40c-89ca9c28976d",
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
  "content_id": "c89c06dc-10df-4036-b4b6-d38ffd7ede7e",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "96ee0fed-fa5d-44a4-84b5-24a41281066b",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "be22a771-29e6-4e92-8578-c29451aa531f",
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
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "66f28392-2a17-4446-97fd-ff1b68af645a",
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
  "content_id": "a0f572a5-a93c-4718-a70b-01d81a056d4f",
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
  "content_id": "2366a1b7-6c46-4a7b-b244-8154075ed9a1",
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
  "content_id": "5afc476c-755d-419f-a2e3-2cbc145dcdc7",
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
