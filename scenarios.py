"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        # Criterion 1: at most 1 of 10 self-written pieces labelled AI.
        "name": "self-written pieces",
        "criterion": 1,
        "texts": [
            "Our last trip went very well. we stayed in yucca valley and had our own affordable house airbnb. we drove to joshua tree from there. I'm not seeing a similar affordable house area for zion.\n\nand they dont have the same views do they\n\nso the scenic views at zion are limited to the park trail? it's not the whole environment around it?",
            "Yosemite seems oddly very affordable to stay right in the woods? Am I looking at the wrong area? Lots of airbnbs at low rates?\n\nI'd prefer Zion but my plan for this is contingent on a nice airbnb or cabin experience\n\nit doesn thave tall trees tho does it",
            'he grew up in new zealand. is that more like zion or yosemite?\n\nare yosemite trees bigger than new zealand?\n\nare kauri trees more scattered? not a full canopy like sequoias?',
            "Where should we rent a car from\n\nI'm in Pasadena, so we can pickup and dropoff here\n\nWhich company is better to deal with\n\ndoes enterprise have a aaa discount? the aaa site seems to direct attention to hertz",
            "I'm only seeeing 5% at checkout for hertz, but the site is advertising up to 30\n\ndoes a specific location in pasaden have better stock than others\n\nCAn you do that search for me, for enterprise and avis/budgert",
            'I’d like to make a Partiful event for when he’s in town, back in the city of LA, also it will be my birthday.\n\nBut we’re going to a ticket party at a club, without hosting a pre-party, and I haven’t seen Partiful used that way before, as come meet us at this other event.',
            'he really wants to stay there because it was in a taylor swift music video. but the rooms look really stuffy. are there any toher taylor swift associated hotels in LA?\n\nWill the biltmore be open to exploration on a wednesday night to hotel guests? a firend mentioned exploring the "hauntings"?',
            "What sounds better for an acquaintance that I'm texting for the first time. I'm going for low pressure, take it or leave it, graceful if he doesn't respond.\n\nHey babe,\nMy aussie boyfie in town Oct 17 of you'd like to come out to Maurice\n\nI htought come out sounds more like he can see us there, and that meet us sounded more like joining a group with us",
            "I'm growing dissatisfied by how quickly you switch towards validation. I'm genuinely intersted in which reads better.",
            'A false positive is the most expensive mistake this system can make. Missing some AI-generated writing is less harmful than confidently accusing human writing of being AI-generated.',
        ],
    },
    {
        # Criterion 2: median AI score at least 0.20 above median human score.
        "name": "AI spread: clearly AI",
        "criterion": 2,
        "texts": [
            "The implementation of sustainable urban transportation requires careful consideration of several important factors. By investing in reliable public transit, expanding pedestrian infrastructure, and encouraging alternative forms of mobility, cities can reduce congestion and improve overall quality of life. These strategies also support environmental sustainability and create more efficient communities for future generations.",
            "Artificial intelligence is a rapidly evolving field that has the potential to transform many industries. It is important to consider both the benefits and the challenges of this technology. Overall, artificial intelligence offers many opportunities for growth and innovation in the modern world.",
            "Effective time management is an essential skill for achieving success in both personal and professional settings. By setting clear goals, prioritizing important tasks, and minimizing distractions, individuals can improve their productivity and reduce stress. Ultimately, developing strong time management habits leads to greater fulfillment and long-term success.",
            "Regular physical exercise offers numerous benefits for overall health and well-being. It helps to strengthen the cardiovascular system, improve mental health, and maintain a healthy weight. Therefore, it is important to incorporate consistent physical activity into your daily routine for a better quality of life.",
            "Climate change is one of the most significant challenges facing our world today. It is important to understand the causes and effects of this issue in order to develop effective solutions. By working together, governments, businesses, and individuals can create a more sustainable future for generations to come.",
        ],
    },
    {
        "name": "human spread: clearly human",
        "criterion": 2,
        "texts": [
            'does big bear have a section that is coevered by a snow machine? is it accessible to the public?\n\nare there other activities, something on the lake? bikes to rent?',
            'will it have snow in october? or be rainy? does it skip rain to snow?\n\nel nino wont make it rain that wekk?\n\nwhats the difference between big bear and arrowhead',
            "we picked out an airbnb, but the address looks like it doesnt have trees around? that's just based on the google earth photo.\n\nthe map shows a marker labeled big bear access at the end of ridgecrest dr? what is that?",
            'if he departs on evening of the 14th sydney and returns to work on the 21st, what days is he in the us?\n\nhe doesnt lose a day? I thought hed have to depart a day earlier',
            "We've been invited to dinner at soho house, our pick of sunset or holloway in west hollywood\n\nis dinner expensive there?\n\nwhere to get dinner around the biltmore",
        ],
    },
    {
        # Criterion 3: all three labels appear across at least nine submissions.
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            # intended human
            'also maybe big bear',
            'are the trails crowded in zion\n\nis yosemite trails crowded',
            'is airbnb the best place to find a cabin?',
            # intended unsure
            "Our last trip went very well. We stayed in Yucca Valley and had our own affordable Airbnb house. We drove to Joshua Tree from there. I'm not seeing a similar affordable housing area for Zion. And they don't have the same views, do they? Are the scenic views at Zion limited to the park trails?",
            "The 1984 Summer Games propelled the Olympics into the future with visible gender equity on the field and record-breaking participation from 140 nations. For the first time, female runners competed in the marathon, leading to American Joan Benoit taking home the gold.",
            "I'd like to make a Partiful event for when he's in town and back in LA. It'll also be my birthday. The only thing is, we're going to a ticketed club event rather than hosting a pre-party, and I haven't really seen Partiful used that way before, as more of a come meet us at this other event invite.",
            # intended ai
            "Artificial intelligence is a rapidly evolving field that has the potential to transform many industries. It is important to consider both the benefits and the challenges of this technology. Overall, artificial intelligence offers many opportunities for growth and innovation in the modern world.",
            "The implementation of sustainable urban transportation requires careful consideration of several important factors. By investing in reliable public transit, expanding pedestrian infrastructure, and encouraging alternative forms of mobility, cities can reduce congestion and improve overall quality of life.",
            "Regular physical exercise offers numerous benefits for overall health and well-being. It helps to strengthen the cardiovascular system, improve mental health, and maintain a healthy weight. Therefore, it is important to incorporate consistent physical activity into your daily routine for a better quality of life.",
        ],
    },
    {
        # Criterion 4: every appeal sets status to under_review and is logged, original decision unchanged.
        # Part 2 (run separately): POST /appeal on each content_id, then check /log.
        "name": "appeal targets",
        "criterion": 4,
        "texts": [
            "also maybe big bear",
            "Our last trip went very well. We stayed in Yucca Valley and had our own affordable Airbnb house. We drove to Joshua Tree from there. I'm not seeing a similar affordable housing area for Zion. And they don't have the same views, do they? Are the scenic views at Zion limited to the park trails?",
            "Artificial intelligence is a rapidly evolving field that has the potential to transform many industries. It is important to consider both the benefits and the challenges of this technology. Overall, artificial intelligence offers many opportunities for growth and innovation in the modern world.",
        ],
    },

    {
        # Criterion 5: missing, null, blank, >10,000-char text get a 4xx, no score, logged rejection.
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "", "creator_id": "eval_bad_empty"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_blank"},
            {"text": "word " * 2001, "creator_id": "eval_bad_huge"},
            {"text": "x" * 10001, "creator_id": "eval_bad_edge"},
        ],
    },

]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
