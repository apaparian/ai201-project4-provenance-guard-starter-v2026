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

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



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
