# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. POST /submit: A user submits a piece of text and a creator_id to the POST /submit endpoint.

2. Validation: The service validates the request and creates a unique content_id.

3. detector.py::model_signal: The text is passed through a local language model (GPT-2), which measures how predictable the text is. More predictable text receives a higher score and is treated as more AI-like.

4. stylometry.py::style_signal: The text is analyzed based on writing patterns such as sentence-length variation, vocabulary diversity, and punctuation use, without considering meaning. It produces a score on the same 0–1 scale as the model signal.

5. scoring.py::combine_signals: The model score and style score are combined into a combined confidence score between 0 and 1, where higher values indicate a greater likelihood of AI-generated text.

6. scoring.py::score_to_label: The combined score is compared against the thresholds in config.py and converted into a guess (human, unsure, or ai) and the reader-facing label text.

7. audit.py::log_decision: The content_id, both signal scores, the combined score, the final label, and a status of "decided" are written to the audit log. The service then returns the result to the user, and the content_id can later be used by /appeal to locate the decision.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
Predictability, or its inverse, perplexity. It analyzes how predictable the text is to the local language model, or whether it would have created a similar string of words when prompted.

**Why that might differ between human and AI writing:**
A language model chooses each token based on the researched likelihood with which it appears after the token before it. Patterns are highly predicatable. Human writing is spontaneous, less predictable.

**What it can't see:**
A human being can write in a predictive matter. An individual with less mastery of the language, or other load-bearing markers of lower confidence, may air on writing in a highly predictive and generic manner.

### Signal two — the style signal

**What it measures:**
Style. It counts characterstics such as sentence length, repetition of vocabulary, and punctuation patterns. They combine together with weights of 0.6, 0.3, and 0.1, respectively.

**Why that might differ between human and AI writing:**
Model generated output is biased towards sentences of even length. They follow regular patterns. A human agent has a propensity towards irregularity. The latter either follows a pattern distinct from agent behavior, or none at all.

**What it can't see:**
A model can be prompted to introduce irregularities, vary sentence length, introduce unique vocabulary terms, and  intentionally create grammatical errors in its placement of punctuation. This may disguise the source as human.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
A weighted average of the two signals. Both point in the same direction (higher means more likely AI), so the combined score does too. The model signal gets slightly more weight (0.6) than the style signal (0.4) because, in the examples below, it separates the clearly AI text from the human texts more consistently. When the signals disagree, the combined score still falls between them, but it leans somewhat toward the model signal.

**The numbers:**
| Sample | Model score | Style score | Combined |
|---|---|---|---|
| Clearly human | 0.5195 | 0.5238 | 0.5212 |
| Lightly edited AI | 0.3669 | 0.1620 | 0.2849 |
| Formal human | 0.4785 | 0.5565 | 0.5097 |
| Clearly AI | 0.7554 | 0.4063 | 0.6158 |

Clearly human:
Our last trip went very well. We stayed in Yucca Valley and had our own affordable Airbnb house. We drove to Joshua Tree from there. I'm not seeing a similar affordable housing area for Zion. And they don't have the same views, do they? Are the scenic views at Zion limited to the park trails?

Lightly edited AI:
I'd like to make a Partiful event for when he's in town and back in LA. It'll also be my birthday. The only thing is, we're going to a ticketed club event rather than hosting a pre-party, and I haven't really seen Partiful used that way before, as more of a come meet us at this other event invite.

Formal human:
The 1984 Summer Games propelled the Olympics into the future with visible gender equity on the field and record-breaking participation from 140 nations. For the first time, female runners competed in the marathon, leading to American Joan Benoit taking home the gold.

Clearly AI:
The implementation of sustainable urban transportation requires careful consideration of several important factors. By investing in reliable public transit, expanding pedestrian infrastructure, and encouraging alternative forms of mobility, cities can reduce congestion and improve overall quality of life. These strategies also support environmental sustainability and create more efficient communities for future generations.


**Where it lives:** `scoring.py::combine_signals` and `config.py`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
The clearly AI text (the urban transportation paragraph) produced the largest disagreement: 0.7554 from the model signal versus 0.4063 from the style signal. The style score is lower because the paragraph contains some variation in sentence length, which makes it look less AI-like according to the stylometry features. With a 0.6/0.4 weighted average, the combined score is 0.6158. This still lands between the two inputs, but it stays closer to the model signal because the model performed better on these examples. The tradeoff is that the system becomes somewhat more willing to flag AI-generated text, while still reducing the impact of any single signal.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00-0.35 | This was likely written by a human author. |
| unsure | 0.35-0.65 | A confident determination could not be made. The result is uncertain. |
| high-confidence AI | 0.65-1.00 | This was likely written with AI assistance. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
The unsure label is meant to communicate uncertainty without sounding like an accusation. It explains that the system could not reach a conclusion. It leaves room for interpretation.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Our last trip went very well. We stayed in Yucca Valley and had our own affordable Airbnb house. We drove to Joshua Tree from there. I'\''m not seeing a similar affordable housing area for Zion. And they don'\''t have the same views, do they? Are the scenic views at Zion limited to the park trails?", "creator_id": "human-sample"}'
```

```json

{
  "confidence": 0.5212334068741353,
  "content_id": "e3b25598-9ed8-42b4-827f-07e1f500a508",
  "guess": "unsure",
  "label": "A confident determination could not be made. The result is uncertain.",
  "model_score": 0.5195,
  "style_score": 0.5238335171853384
}
```

**A submission labeled high-confidence AI**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Artificial intelligence is a rapidly evolving field that has the potential to transform many industries. It is important to consider both the benefits and the challenges of this technology. Overall, artificial intelligence offers many opportunities for growth and innovation in the modern world.", "creator_id": "ai-sample"}'
```

```json

{
  "confidence": 0.803390046416437,
  "content_id": "64d51f53-f2bb-4d38-8699-a80ceb5ebe59",
  "guess": "ai",
  "label": "This was likely written with AI assistance.",
  "model_score": 0.9106,
  "style_score": 0.6425751160410924
}
```

**A submission labeled high-confidence human**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "honestly no idea why i bought that lamp?? it'\''s ugly, my cat hates it, and yet — every night i switch it on like some weirdo. anyway. dinner was fine I guess", "creator_id": "casual-human-sample"}'
```

```json

{
  "confidence": 0.1643694888969996,
  "content_id": "79dd75d7-7b31-4a2d-b3e4-b30269277c21",
  "guess": "human",
  "label": "This was likely written by a human author.",
  "model_score": 0.1736,
  "style_score": 0.15052372224249894
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "e3b25598-9ed8-42b4-827f-07e1f500a508", "reasoning": "I wrote this piece myself and would like the decision reviewed."}'
```

```json

{
  "content_id": "e3b25598-9ed8-42b4-827f-07e1f500a508",
  "message": "Your appeal has been recorded and the decision is now under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json

{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.5212334068741353,
      "content_id": "e3b25598-9ed8-42b4-827f-07e1f500a508",
      "creator_id": "human-sample",
      "guess": "unsure",
      "label": "A confident determination could not be made. The result is uncertain.",
      "model_score": 0.5195,
      "status": "decided",
      "style_score": 0.5238335171853384,
      "timestamp": "2026-10-31T23:07:36+00:00"
    },
    {
      "content_id": "e3b25598-9ed8-42b4-827f-07e1f500a508",
      "creator_id": "human-sample",
      "event": "appeal",
      "reasoning": "I wrote this piece myself and would like the decision reviewed.",
      "status": "under_review",
      "timestamp": "2026-10-31T23:18:22+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help figuring out a good order for implementing Milestone 3.
- *What came back:* A suggestion to start by testing the hardcoded `/submit` route, then add the detector, and finally verify that submissions were being written to the audit log correctly.
- *What I changed:* Instead of trying to build everything at once, I worked through the pieces one at a time. That made it easier to find mistakes and confirm that the `content_id` returned by `/submit` matched the one stored in the log.

**Moment 2**

- *What I asked for:* Feedback on whether my scoring and labeling choices made sense.
- *What came back:* Ideas for label wording, handling uncertain cases, and different ways to combine the model and style signals.
- *What I changed:* I compared the suggestions against my sample texts and chose a weighted average that gives slightly more influence to the model signal. I also rewrote the labels several times so the results would read more naturally to someone who submitted a piece of writing, especially for the unsure case.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 4 per minute, 96 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->
I find quarters easy to reason about. 4 per minute is one every 15 seconds, or one every quarter of a minute. 96 per day works out to 4 per hour on average, or one every 15 minutes.

A real writer is unlikely to submit more than a few drafts in a short period, so 4 requests per minute should not get in their way. A script trying to map the system's thresholds is a different case. At 4 per minute alone, 1,000 submissions would take about 4 hours, so the daily cap does the real work: at 96 requests per day it would take about 10 days per creator_id.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->
The rate limiter uses the creator_id in the request body, falling back to the caller's IP address if creator_id is missing or invalid. Keying on creator_id treats each creator as one person, but a scripted attack could bypass this guard by incrementing its creator_id per call. The IP address fallback might collect a household into an individual, but it protects us from being left with no safety at all.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
python run_attacks.py --flood 15

15 submissions as 'flood_tester' against http://127.0.0.1:5000
The first one is slow while the model loads.

  [ 1/15] 200
  [ 2/15] 200
  [ 3/15] 200
  [ 4/15] 200
  [ 5/15] 429
  [ 6/15] 429
  [ 7/15] 429
  [ 8/15] 429
  [ 9/15] 429
  [10/15] 429
  [11/15] 429
  [12/15] 429
  [13/15] 429
  [14/15] 429
  [15/15] 429

============================================================
200 200 200 200 429 429 429 429 429 429 429 429 429 429 429
============================================================

11 of 15 were rate limited. Paste the run above into your README
under **Rate Limiting**, and check GET /log recorded the rejections.

Wrote results/flood_2026-11-04_1439.md
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Result: 56 attacks, 23 BROKE, 33 HELD.** HELD means my defenses stopped the attack; BROKE means it got through (or the service crashed). Full run: `results/attack_run_2026-11-04_1634_before.md`.

| Family | Attacks | BROKE | HELD |
|---|---|---|---|
| `evasion` | 10 | 9 | 1 |
| `false_positive` | 8 | 6 | 2 |
| `prompt_injection` | 6 | 0 | 6 |
| `malformed` | 20 | 8 | 12 |
| `flood_same_creator` | 12 | 0 | 12 |

Caveats on the marks:
- **RQ09, RQ10, RQ11** are marked HELD, but they returned 429 because the flood rows had already used up my address's limit, so the request never reached the route. They did not test how the service handles those bodies.
- **Flood rows:** a 429 is the correct response, since that family tests the limiter. Four requests got through, then FL01_05 onward were rejected (limit 4 per minute).
- **MF02** is the one auto-BROKE: a single-character input raised a `ValueError` and returned a 500, and it left no audit log entry.

| ID | Family | Targeting | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | human | 0.318 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.416 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.559 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.584 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.306 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.376 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.632 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | human | 0.319 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.574 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.815 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.538 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.661 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.678 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.676 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.706 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | ai | 0.677 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai | 0.662 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | human | 0.329 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.366 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.217 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.529 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.486 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.549 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.505 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | human | 0.280 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | human | 0.207 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.839 | BROKE |
| MF06 | malformed | text is emoji only | 200 | ai | 0.798 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.744 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | unsure | 0.384 | BROKE |
| RQ03 | malformed | text is a number | 400 | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 200 | human | 0.270 | BROKE |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | malformed | body is empty | 429 | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.257 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |


**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-05T00:34:36+00:00", "content_id": "ac4ea52a-88db-4f20-9963-1b8b70109d6f", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.48621920281624714, "combined_score": 0.6775476811264989, "label": "This was likely written with AI assistance.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:36+00:00", "content_id": "70af09f8-7b24-4818-be44-9712a18492f5", "creator_id": "attacker_FP07", "guess": "ai", "model_score": 0.8816, "style_score": 0.33138442702946225, "combined_score": 0.6615137708117849, "label": "This was likely written with AI assistance.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:36+00:00", "content_id": "2b6cf02e-8ea4-4a18-a56f-04ab4ec0102d", "creator_id": "attacker_FP06", "guess": "ai", "model_score": 0.8814, "style_score": 0.3716373810026411, "combined_score": 0.6774949524010564, "label": "This was likely written with AI assistance.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:35+00:00", "content_id": "d8bcadf1-f589-4647-9afa-c8b5aded417e", "creator_id": "attacker_EV01", "guess": "human", "model_score": 0.1635, "style_score": 0.5493502809647747, "combined_score": 0.31784011238590987, "label": "This was likely written by a human author.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:35+00:00", "content_id": "7c8bb36e-7be6-42f0-a916-d6d1e883a3fb", "creator_id": "attacker_EV05", "guess": "human", "model_score": 0.3212, "style_score": 0.28277612970746785, "combined_score": 0.30583045188298713, "label": "This was likely written by a human author.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:37+00:00", "content_id": "8093c24b-a0fb-4381-9040-04788678001e", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 0.5, "combined_score": 0.7981400000000001, "label": "This was likely written with AI assistance.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:37+00:00", "content_id": "2021ef4c-ec8f-4482-bd20-ef592900af80", "creator_id": null, "guess": "unsure", "model_score": 0.2395, "style_score": 0.6, "combined_score": 0.3837, "label": "A confident determination could not be made. The result is uncertain.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:37+00:00", "content_id": "be226d37-fb89-457a-bb2a-3cb7861dd6e3", "creator_id": {"id": "x"}, "guess": "human", "model_score": 0.0492, "style_score": 0.6, "combined_score": 0.26952, "label": "This was likely written by a human author.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:36+00:00", "content_id": "6fc9bc11-3cf8-472a-8079-27eb32ee2fb3", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.4131787929017251, "combined_score": 0.5493315171606901, "label": "A confident determination could not be made. The result is uncertain.", "status": "decided"}
{"timestamp": "2026-11-05T00:34:37+00:00", "creator_id": "attacker_MF08", "event": "rejected", "status": "rejected", "reason": "text_too_long", "length": 57640}
{"timestamp": "2026-11-05T00:34:37+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "4 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

FP03, a non-native English speaker writing carefully, was labelled "likely written with AI assistance."(content_id `ac4ea52a-88db-4f20-9963-1b8b70109d6f`, combined 0.678.) The writer did nothing wrong. The model signal read their careful, regular phrasing as machine-like (0.805), and the style signal (0.486) was close to neutral, so it did little to pull the score back down. Of the six false positives, FP05 scored higher (0.706), but FP03 is the result I would be least comfortable explaining to a real user. The feature being penalized is not AI usage, but careful writing by a non-native English speaker. That creates a risk of treating writing proficiency and writing style as evidence of AI assistance.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
