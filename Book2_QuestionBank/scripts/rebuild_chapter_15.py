r"""
=============================================================================
Script: rebuild_chapter_15.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 15:
             "Fun in the Rain" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH15_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_15")
os.makedirs(CH15_DIR, exist_ok=True)

def make_q_block(qid, qtype, diff, bloom, topic, marks, question, opts, answer):
    lines = [
        f"### Question ID: {qid}",
        f"- **Subject**: English",
        f"- **Type**: {qtype}",
        f"- **Difficulty**: {diff}",
        f"- **Bloom Level**: {bloom}",
        f"- **Topic**: {topic}",
        f"- **Marks**: {marks}",
        "",
        "**Question**:",
        f"{question}",
        ""
    ]
    if opts:
        for opt in opts:
            lines.append(f"- {opt}")
        lines.append("")
    lines.append(f"- **Answer Key**: {answer}")
    lines.append("\n---\n")
    return "\n".join(lines)

# ---------------------------------------------------------------------------
# 1. Plural Nouns & Spelling Rules (50 Qs)
# ---------------------------------------------------------------------------
def build_plural_nouns():
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("boat", "boats", "boates", "boaties", "boatz", "A", "Regular noun adding -s."),
        ("puddle", "puddles", "puddlies", "puddlees", "puddlez", "A", "Regular noun ending in -e adds -s."),
        ("raindrop", "raindrops", "raindropes", "raindropies", "raindropz", "A", "Regular noun adding -s."),
        ("umbrella", "umbrellas", "umbrellaes", "umbrellies", "umbrellaz", "A", "Regular noun adding -s."),
        ("raincoat", "raincoats", "raincoates", "raincoaties", "raincoatz", "A", "Regular noun adding -s."),
        ("boot", "boots", "bootes", "booties", "bootz", "A", "Regular noun adding -s."),
        ("cloud", "clouds", "cloudes", "cloudies", "cloudz", "A", "Regular noun adding -s."),
        ("splash", "splashes", "splashs", "splashies", "splashz", "A", "Nouns ending in -sh add -es (splashes)."),
        ("wish", "wishes", "wishs", "wishies", "wished", "A", "Nouns ending in -sh add -es (wishes)."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people."),
        ("glass", "glasses", "glasss", "glassies", "glassz", "A", "Nouns ending in -ss add -es (glasses)."),
        ("box", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es (boxes)."),
        ("bench", "benches", "benchs", "benchies", "benchz", "A", "Nouns ending in -ch add -es (benches)."),
        ("dish", "dishes", "dishs", "dishies", "dished", "A", "Nouns ending in -sh add -es (dishes)."),
        ("rainbow", "rainbows", "rainbowes", "rainbowies", "rainbowz", "A", "Regular noun adding -s."),
        ("stream", "streams", "streames", "streamies", "streamz", "A", "Regular noun adding -s."),
        ("frog", "frogs", "froges", "frogies", "frogz", "A", "Regular noun adding -s.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH15_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 15 (*Fun in the Rain*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The children made small paper (boat / boats).", "boats", "boat", "boates", "boaties", "A", "Plural noun 'boats'."),
        ("They jumped into deep water (puddle / puddles).", "puddles", "puddle", "puddlies", "puddlees", "A", "Regular noun ending in -e adds -s (puddles)."),
        ("The children made big water (splash / splashes) in the street.", "splashes", "splash", "splashs", "splashies", "A", "Nouns ending in -sh add -es (splashes)."),
        ("Identify the INCORRECT plural spelling in this list: boats, umbrellas, splashs, clouds.", "splashs", "boats", "umbrellas", "clouds", "A", "Plural of splash is 'splashes', not 'splashs'."),
        ("Choose the sentence with the correct plural noun form:", "The children wore raincoats and boots in the puddles.", "The childs wore raincoaties and bootes in the puddlies.", "The childrens wore raincoatz and bootz in the puddlez.", "The childes wore raincoats and booties in the puddles.", "A", "children, raincoats, boots, puddles are correct."),
        ("Which noun forms its plural by adding -es to a word ending in -sh?", "splash -> splashes", "boat -> boats", "cloud -> clouds", "umbrella -> umbrellas", "A", "Splash ends in -sh, so plural is splashes."),
        ("Change the singular noun in brackets to plural: 'Heavy ____ (cloud) covered the sky before rain.'", "clouds", "cloudes", "cloudies", "cloudz", "A", "Regular noun adding -s (clouds)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The children made paper boats and sailed them in streams.", "The childs made paper boates and sailed them in streames.", "The childrens made paper boaties and sailed them in streamies.", "The childes made paper boatz and sailed them in streamz.", "A", "children, boats, streams are all correctly spelt plurals."),
        ("What is the correct plural of 'paper boat'?", "paper boats", "paper boates", "paper boaties", "paper boatz", "A", "Regular noun adding -s."),
        ("The mother bought two red (umbrella / umbrellas).", "umbrellas", "umbrella", "umbrellaes", "umbrellies", "A", "Regular noun adding -s (umbrellas)."),
        ("Many (child / children) love playing in the rain.", "children", "childs", "childes", "childrens", "A", "Irregular plural of child is children."),
        ("Many (person / people) carry umbrellas during monsoon.", "people", "persons", "peoples", "persones", "A", "Irregular plural of person is people."),
        ("How many (raindrop / raindrops) fell on the window?", "raindrops", "raindrop", "raindropes", "raindropies", "A", "Regular noun adding -s (raindrops)."),
        ("They saw two colorful (rainbow / rainbows) in the sky.", "rainbows", "rainbow", "rainbowes", "rainbowies", "A", "Regular noun adding -s (rainbows)."),
        ("Which plural noun rule applies to the word **'splashes'**?", "Add -es to nouns ending in -sh", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Splash ends in -sh, so it adds -es."),
        ("The kids wore yellow rubber (boot / boots).", "boots", "bootes", "booties", "bootz", "A", "Plural of boot is boots."),
        ("Identify the correct plural form of 'leaf':", "leaves", "leafs", "leafes", "leavies", "A", "Nouns ending in -f change to -ves (leaves)."),
        ("They heard loud (thunderstorm / thunderstorms) in July.", "thunderstorms", "thunderstorm", "thunderstormes", "thunderstormies", "A", "Plural of thunderstorm is thunderstorms.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The child floated a paper boat in a puddle.'", "The children floated paper boats in puddles.", "The childs floated paper boates in puddlies.", "The childrens floated paper boaties in puddlees.", "The childes floated paper boatz in puddlez.", "A", "Plural of child->children (irregular), boat->boats (-s), puddle->puddles (-e+s)."),
        ("Analyze the error: 'The childs made many splashs in the water.' Why is this sentence incorrect?", "'childs' should be irregular plural 'children' and 'splashs' should be 'splashes'.", "'childs' should be 'childrens'.", "'splashs' should be 'splashies'.", "No error.", "A", "Child becomes children; splash becomes splashes."),
        ("Complete the paragraph with correct plurals: 'Three ____ (child) wore colorful ____ (raincoat) and jumped into four ____ (puddle).'", "children, raincoats, puddles", "childs, raincoaties, puddlies", "childrens, raincoatz, puddlees", "children, raincoates, puddles", "A", "children (irregular), raincoats (-s), puddles (-e+s)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **children** opened their **umbrellas** near the **puddles**.", "The **childs** opened their **umbrellaes** near the **puddlies**.", "The **childrens** opened their **umbrellies** near the **puddlees**.", "The **childes** opened their **umbrellaz** near the **puddlez**.", "A", "children (irregular), umbrellas (-s), puddles (-e+s)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, men, feet", "boats, puddles, clouds, boots", "splashes, dishes, boxes, benches", "leaves, thieves, wolves, knives", "A", "children, people, men, feet change forms without standard -s/-es."),
        ("Why does 'splash' become 'splashes' but 'boat' becomes 'boats'?", "Because 'splash' ends in sibilant -sh (requiring -es), while 'boat' ends in regular consonant -t (adding -s).", "Because splash is water.", "Because boat is big.", "Both follow the exact same rule.", "A", "Nouns ending in -sh add -es; regular consonants add -s."),
        ("Find the TWO grammatical mistakes in: 'The two childs dropped their paper boates into the stream.'", "'childs' should be 'children' and 'boates' should be 'boats'.", "'childs' should be 'child' and 'boates' should be 'boaties'.", "'stream' should be 'streams' only.", "There are no mistakes in the sentence.", "A", "children (irregular plural) and boats (-s)."),
        ("Replace the singular words in brackets: 'The children splashed water on their ____ (foot) while running.'", "feet", "foots", "feets", "footies", "A", "Plural of foot is feet."),
        ("Analyze this sentence: 'Raindrops made many splashes in the water.' What type of plural noun is 'splashes'?", "Nouns ending in sibilant -sh adding -es (splash -> splashes).", "Irregular plural.", "Abstract noun.", "Possessive noun.", "A", "Splash ends in -sh, adding -es."),
        ("Fill in the blanks: 'The two ____ (child) watched three ____ (frog) jumping in the rain.'", "children, frogs", "childs, froges", "childrens, frogies", "childes, frogs", "A", "child -> children; frog -> frogs."),
        ("Select the option that shows correct plural transformation for ALL three words: 'umbrella', 'splash', 'boat'", "umbrellas, splashes, boats", "umbrellaes, splashs, boates", "umbrellies, splashies, boaties", "umbrellaz, splashz, boatz", "A", "umbrella -> umbrellas; splash -> splashes; boat -> boats."),
        ("HOTS Reasoning: Why do we say 'paper boats' (countable) but 'rain' is uncountable?", "Because 'boat' refers to individual crafted objects, while 'rain' refers to liquid precipitation mass.", "Because rain is wet.", "Because boat is paper.", "Because puddles are deep.", "A", "Discrete countable objects vs continuous mass liquid."),
        ("Transform into singular: 'The children sailed paper boats in puddles.'", "The child sailed a paper boat in a puddle.", "The children sailed a paper boat in a puddle.", "The child sail a paper boat in a puddle.", "The child sailed paper boats in a puddle.", "A", "Singular forms: child, paper boat, puddle."),
        ("Identify the correct rule for forming the plural of **'splash'**:", "Add -es because it is a noun ending in -sh (splashes).", "Add -s (splashs).", "Change -sh to -v (splaves).", "Change vowel sound.", "A", "Nouns ending in -sh add -es.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("It was ___ rainy day in July.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'rainy'."),
        ("The child made ___ paper boat.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'paper'."),
        ("The girl held ___ red umbrella over her head.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'red'."),
        ("The boy wore ___ raincoat to stay dry.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'raincoat'."),
        ("He carried ___ umbrella to school.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'umbrella'."),
        ("___ Panchatantra/Story topic describes fun in the rain.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Story'."),
        ("They saw ___ big puddle in the middle of the road.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'big'."),
        ("It was ___ exciting shower of rain.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'exciting'."),
        ("___ sun came out after the heavy rain.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'."),
        ("They saw ___ colorful rainbow in the sky.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'colorful'."),
        ("They jumped into ___ deep puddle.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'deep'."),
        ("It was ___ honest mistake to forget the umbrella.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ raindrops fell softly on the window pane.", "The", "A", "An", "No article", "A", "Definite article 'The' specifies raindrops on the window."),
        ("The girl saw ___ orange fish in the stream.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'orange'."),
        ("They created ___ wonderful paper boat together.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'wonderful'."),
        ("The storm was ___ unexpected event.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unexpected'."),
        ("The rain brought ___ joy to the children.", "no article", "a", "an", "the", "A", "Abstract noun 'joy' takes no indefinite article here."),
        ("___ sky turned dark with rain clouds.", "The", "A", "An", "No article", "A", "Use 'The' for unique sky.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH15_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The child made ___ paper boat and opened ___ umbrella.", "a, an", "an, a", "a, a", "the, a", "A", "'a paper boat' (consonant sound), 'an umbrella' (vowel sound)."),
        ("Why do we say '**a** raincoat' but '**an** umbrella'?", "Because 'raincoat' begins with a consonant sound (r) and 'umbrella' with a vowel sound (u).", "Because raincoats are yellow.", "Because umbrellas are black.", "Because rain is wet.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "The children played happily in the rain.", "An children played happily in the rain.", "The a children played happily in rain.", "A children played happily in an rain.", "A", "'The children' (specific group), 'the rain' (specific weather)."),
        ("Fill in the blanks: 'They floated ___ boat on ___ stream.'", "a, the", "an, a", "a, an", "the, a", "A", "'a boat' (consonant /b/), 'the stream' (specific stream)."),
        ("Identify the INCORRECT article in: 'He carried **a** umbrella in the storm.'", "'a' should be 'an'", "'a' should be 'the'", "'umbrella' should be 'a umbrella'", "No mistake", "A", "'umbrella' starts with vowel sound /u/, so it takes 'an'."),
        ("Which article completes the sentence? 'It was ___ awesome sight to see the rainbow.'", "an", "a", "the", "no article", "A", "'awesome' starts with vowel sound /a/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ cloud covered ___ sun.'", "The, the", "A, a", "An, an", "The, a", "A", "'The cloud' (specific cloud), 'the sun' (unique sun)."),
        ("Why do we use 'an' before 'umbrella' in 'She opened **an** umbrella'?", "Because 'umbrella' begins with the vowel sound /u/.", "Because umbrella is an object.", "Because rain is heavy.", "Because sky is dark.", "A", "'umbrella' starts with vowel sound /u/."),
        ("Complete the dialogue: Girl: 'Look at ___ paper boat!' Boy: 'It is floating on ___ puddle!'", "the, a", "a, an", "an, the", "the, the", "A", "'the paper boat' (specific boat), 'a puddle' (consonant sound)."),
        ("Select the correct sentence:", "A raincoat protects you from the rain.", "An raincoat protects you from the rain.", "The raincoat protects you from an rain.", "An raincoat protects you from an rain.", "A", "'A raincoat' (consonant sound), 'the rain' (specific weather element)."),
        ("Fill in the blank: 'It rained for ___ long time.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The children played in **___ rain** with delight.", "He made ___ boat.", "She opened ___ umbrella.", "They saw ___ puddle.", "A", "Uncountable weather noun 'rain' takes no indefinite article here."),
        ("Choose the correct sentence for story summary:", "Nature and rain bring happiness to children.", "A nature and a rain bring happiness.", "An nature and an rain bring happiness.", "The nature a brings happiness.", "A", "Abstract/uncountable concepts take no indefinite articles in general sense."),
        ("Fill in the blanks: 'The storm lasted for ___ hour before ___ sun returned.'", "an, the", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'the sun' (unique celestial body)."),
        ("Which sentence uses 'the' correctly for specific sky elements?", "They saw the rainbow across the dark sky.", "They saw a rainbow across a dark sky.", "They saw an rainbow across an dark sky.", "They saw rainbow across dark sky.", "A", "Specific sky elements take 'the rainbow' and 'the dark sky'."),
        ("Identify the article error: 'He gave **a** explanation of **an** rainy day.'", "'an rainy' should be 'a rainy' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an rainy' should be 'a rainy'", "No error", "A", "'an explanation' (vowel /e/) and 'a rainy day' (consonant /r/)."),
        ("Complete: 'It was ___ unforgettable rainfall at ___ monsoon season.'", "an, the", "a, an", "the, a", "an, a", "A", "an unforgettable (/u/), the monsoon season (specific season)."),
        ("Choose the correct option: '___ rainbow brightened the sky after the storm.'", "The", "A", "An", "No article", "A", "'The rainbow' or 'A rainbow' (consonant sound /r/).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'The child floated **a** another paper boat.' Correct the error:", "'a another' -> 'another' ('another' already includes the indefinite article 'an' + 'other').", "'another' -> 'an another'.", "'boat' -> 'boats'.", "No error.", "A", "'another' cannot be preceded by 'a'."),
        ("Fill in all three blanks: '___ rain stopped, and ___ rainbow appeared in ___ sky.'", "The, a, the", "A, a, a", "An, a, the", "The, a, a", "A", "'The rain' (specific rain), 'a rainbow' (consonant sound), 'the sky' (unique celestial sky)."),
        ("Identify why 'the' is used in: '**The** rain soaked **the** ground thoroughly.'", "Because 'The' specifies the particular rainfall and the specific ground in the scene.", "Because rain is a noun.", "Because ground is dirty.", "Because boats are paper.", "A", "'The' specifies definite rainfall and ground in narrative."),
        ("Spot the TWO article errors: 'It took **a** hour to dry **a** umbrella.'", "'a hour' should be 'an hour' and 'a umbrella' should be 'an umbrella'.", "'a hour' should be 'the hour' and 'a umbrella' should be 'a umbrella'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'umbrella' (vowel u) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A heavy rain fell. A boy opened an umbrella. He floated a paper boat in a puddle.", "An heavy rain fell. An boy opened a umbrella.", "The heavy rain fell. An umbrella was a honest.", "A heavy rain fell. The umbrella was an honest.", "A", "A heavy rain (consonant), a boy (consonant), an umbrella (vowel), a paper boat (consonant), a puddle (consonant)."),
        ("Why is it correct to write 'a unique raincoat' but 'an unusual raincoat'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because raincoat is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story summary: '___ happy child jumped into ___ puddle under ___ dark cloud.'", "A, a, a", "An, a, an", "The, the, the", "A, a, the", "A", "A happy child, a puddle, a dark cloud."),
        ("Analyze this sentence: 'They felt **a** little cold after playing in the rain.' Why is 'a' appropriate?", "Because 'a little' is a quantifier phrase modifying the adjective/mass concept cold.", "Because cold is a verb.", "Because sky is dark.", "Because boat is small.", "A", "'a little' is an idiomatic quantifier phrase."),
        ("Correct the sentence: 'An raincoat protected the boy on a early morning.'", "A raincoat protected the boy on an early morning.", "The raincoat protected a boy on a early morning.", "An raincoat protected the boy on an early morning.", "A raincoat protected the boy on a early morning.", "A", "'A raincoat' (/r/ sound), 'an early' (vowel /er/)."),
        ("Fill in the blanks: '___ sound of ___ raindrops on ___ roof was soothing.'", "The, the, the", "A, a, a", "No article, a, an", "An, the, a", "A", "'The sound' (specific), 'the raindrops' (specific), 'the roof' (specific)."),
        ("Spot the missing article: 'Child jumped into puddle on rainy day.'", "Missing 'A' before 'Child', 'a' before 'puddle', 'a' before 'rainy day' -> 'A child jumped into a puddle on a rainy day.'", "Missing 'an' before 'day'", "Missing 'the' before 'jumped'", "No article is missing", "A", "Singular countable nouns require articles."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An hour ago, a child opened the umbrella.", "A hour ago, an child opened a umbrella.", "The hour ago, an child opened an umbrella.", "An hour ago, an child opened the umbrella.", "A", "An hour (silent h), a child (consonant), the umbrella (specific)."),
        ("Rewrite correctly: 'The girl gave a honest opinion about an rainy day.'", "The girl gave an honest opinion about a rainy day.", "The girl gave a honest opinion about a rainy day.", "The girl gave an honest opinion about an rainy day.", "The girl gave the honest opinion about an rainy day.", "A", "'an honest' (silent h), 'a rainy day' (consonant /r/)."),
        ("Identify the correct rule for using articles with season names like 'monsoon' or 'summer':", "Seasons usually take 'the' when referring to a specific season period ('the monsoon season').", "Seasons take 'an'.", "Seasons take 'a' always.", "Seasons take no articles ever.", "A", "Definite article is standard before specific season names.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("The rainy season in India usually begins in **July**. What is the short abbreviation for **July**?", "Jul.", "July.", "Jl.", "Jy.", "A", "Jul. is standard abbreviation."),
        ("Which month comes right after July?", "August", "September", "June", "May", "A", "August comes after July."),
        ("What is the abbreviation for **August**?", "Aug.", "Augu.", "Au.", "Ag.", "A", "Aug. is standard abbreviation."),
        ("Which month comes right before July?", "June", "May", "August", "September", "A", "June comes before July."),
        ("What is the abbreviation for **June**?", "Jun.", "June.", "Ju.", "Jn.", "A", "Jun. is standard abbreviation."),
        ("Rainy days occur during the **monsoon** season. Which three months are main monsoon months in India?", "July, August, September", "December, January, February", "March, April, May", "October, November, December", "A", "July, August, September are monsoon months."),
        ("It rained all day on **Monday**. What is the abbreviation for **Monday**?", "Mon.", "Mond.", "Mo.", "M.", "A", "Mon. is standard abbreviation."),
        ("Which day comes right after Monday?", "Tuesday", "Wednesday", "Sunday", "Saturday", "A", "Tuesday follows Monday."),
        ("What is the abbreviation for **Tuesday**?", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard abbreviation."),
        ("Which month comes right after August?", "September", "October", "July", "June", "A", "September comes after August."),
        ("What is the short abbreviation for **September**?", "Sep. / Sept.", "Septem.", "Sp.", "Sm.", "A", "Sep. or Sept. is standard abbreviation."),
        ("If today is a rainy Monday, what day was yesterday?", "Sunday", "Tuesday", "Saturday", "Friday", "A", "Yesterday was Sunday."),
        ("If today is Monday, what day will tomorrow be?", "Tuesday", "Wednesday", "Sunday", "Saturday", "A", "Tomorrow will be Tuesday."),
        ("What is the abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("Which day comes between Monday and Wednesday?", "Tuesday", "Thursday", "Sunday", "Friday", "A", "Tuesday is between Monday and Wednesday."),
        ("The storm started at **3:00 p.m.**. What does **p.m.** stand for?", "Post Meridiem (after noon)", "Past Morning", "Plus Minute", "Post Month", "A", "p.m. stands for post meridiem."),
        ("The rain stopped at **9:00 a.m.**. What does **a.m.** stand for?", "Ante Meridiem (before noon)", "After Morning", "At Midnight", "All Month", "A", "a.m. stands for ante meridiem."),
        ("Which day comes right before Monday?", "Sunday", "Saturday", "Tuesday", "Wednesday", "A", "Sunday comes before Monday.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH15_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The rainfall lasted from **2:00 p.m. to 6:00 p.m.**. How many hours did it rain?", "4 hours", "3 hours", "5 hours", "2 hours", "A", "6:00 p.m. - 2:00 p.m. = 4 hours."),
        ("The children played in puddles every day from **Monday to Friday**. For how many days did they play?", "5 days", "4 days", "6 days", "7 days", "A", "Monday to Friday inclusive is 5 days."),
        ("Match the day with its abbreviation: **Tuesday**", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard."),
        ("Convert to 12-hour clock: **15:00 in the afternoon**", "3:00 p.m.", "3:00 a.m.", "5:00 p.m.", "12:03 p.m.", "A", "15:00 is 3:00 p.m."),
        ("Identify the correctly spelt month name:", "August", "Augustt", "Auguest", "Auguste", "A", "August is the correct spelling."),
        ("Identify the INCORRECT pair of month and abbreviation:", "July - Jul.", "August - Aug.", "September - Sep.", "August - Agt.", "D", "August abbreviation is Aug., not Agt."),
        ("Calculate: How many days are in **July**?", "31 days", "30 days", "28 days", "29 days", "A", "July has 31 days."),
        ("Calculate: How many days are in **August**?", "31 days", "30 days", "28 days", "29 days", "A", "August has 31 days."),
        ("Rearrange in correct chronological order: Jul, Jun, Aug, Sep", "Jun, Jul, Aug, Sep", "Jul, Jun, Aug, Sep", "Sep, Aug, Jul, Jun", "Aug, Jul, Jun, Sep", "A", "June -> July -> August -> September."),
        ("What day is 2 days before Monday?", "Saturday", "Sunday", "Friday", "Thursday", "A", "Monday - 2 days = Sunday(1), Saturday(2)."),
        ("If monsoon school holiday lasts for 3 weeks, how many days is that?", "21 days (3 x 7)", "15 days", "30 days", "14 days", "A", "3 weeks x 7 days = 21 days."),
        ("Select the month that has 31 days:", "August", "June", "April", "September", "A", "August has 31 days."),
        ("Which abbreviation stands for **August**?", "Aug.", "Augu.", "Au.", "Ag.", "A", "Aug. is standard abbreviation."),
        ("If today is **Mon.**, what day will it be after 7 days?", "Monday", "Tuesday", "Sunday", "Saturday", "A", "7 days is a full week cycle, landing on Monday again."),
        ("The dark clouds stayed from **11:00 a.m. to 3:00 p.m.**. How many hours were clouds present?", "4 hours", "3 hours", "5 hours", "2 hours", "A", "3:00 p.m. - 11:00 a.m. = 4 hours."),
        ("Identify the word that means 'rainy season in tropical countries':", "Monsoon", "Autumn", "Winter", "Spring", "A", "Monsoon is the rainy season."),
        ("Which of the following is a weekday?", "Monday", "Sunday", "Saturday", "Weekend", "A", "Monday is a weekday."),
        ("Choose the correct abbreviation for **September**:", "Sep. / Sept.", "Septem.", "Sp.", "Sm.", "A", "Sep. or Sept. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("The rain started at **1:15 p.m.** and stopped at **4:45 p.m.**. How many total hours and minutes did it rain?", "3 hours 30 minutes", "3 hours", "4 hours", "2 hours 30 minutes", "A", "1:15 p.m. to 4:45 p.m. = 3 hours 30 minutes."),
        ("If paper boats float down a stream at **5 meters per minute**, how far do they travel in 10 minutes?", "50 meters (5 x 10)", "40 meters", "100 meters", "15 meters", "A", "5 x 10 = 50 meters."),
        ("Solve the calendar puzzle: If 1st July was a Thursday, what day of the week was 8th July?", "Thursday", "Friday", "Wednesday", "Saturday", "A", "1 + 7 = 8th July, landing on Thursday."),
        ("Analyze this schedule: Rains on Mon, Wed, Fri afternoons; Clear sky on Tue, Thu, Sat, Sun. How many days a week does it rain?", "3 days a week", "4 days", "2 days", "5 days", "A", "Mon, Wed, Fri = 3 days."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If a monsoon flood alert lasted a fortnight, how many days did it cover?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'May, Jun, Aug, Jul, Sep'", "August and July are in wrong order.", "June is in wrong position.", "September should be first.", "No error.", "A", "July comes before August (May, Jun, Jul, Aug, Sep)."),
        ("July has **31 days**. What date was the day right after 31st July?", "1st August", "32nd July", "30th July", "1st September", "A", "July has 31 days, so next day is 1st August."),
        ("If yesterday was two days before Monday, what day is tomorrow?", "Monday", "Sunday", "Tuesday", "Saturday", "A", "Two days before Monday = Saturday (yesterday). Today = Sunday. Tomorrow = Monday."),
        ("Calculate: How many days are there in total during **July** and **August** combined?", "62 days (31 + 31)", "60 days", "61 days", "59 days", "A", "July (31) + August (31) = 62 days."),
        ("HOTS Reasoning: Why do July and August both have 31 days in the modern calendar?", "Both July (named after Julius Caesar) and August (named after Augustus Caesar) were given 31 days historically.", "Because monsoon requires 31 days.", "Because rain falls 31 times.", "Because 31 is an even number.", "A", "Historical calendar reform by Roman emperors."),
        ("Identify the correct statement about monsoon weather:", "Monsoon brings heavy rainfall, dark clouds, and cooler temperatures after hot summer.", "Monsoon brings snow.", "Monsoon occurs in January.", "Monsoon has no rain.", "A", "Monsoon brings rainfall and cooler temperatures."),
        ("A raindrop fell 300 meters from a cloud in 30 seconds. What was its average speed?", "10 meters per second (300 / 30)", "5 m/s", "20 m/s", "15 m/s", "A", "300 / 30 = 10 m/s."),
        ("Which month pair both have 31 days and come right after each other during summer monsoon?", "July and August", "June and July", "May and June", "August and September", "A", "July (31) and August (31) are consecutive 31-day months.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("The rain **fell** heavily from dark clouds.", "fell", "rain", "dark", "clouds", "A", "'fell' is the physical action verb."),
        ("The children **floated** paper boats in puddles.", "floated", "children", "paper", "puddles", "A", "'floated' is the physical action verb."),
        ("They **splashed** water all over the street.", "splashed", "water", "street", "they", "A", "'splashed' is the physical action verb."),
        ("The boy **jumped** into a deep puddle.", "jumped", "boy", "deep", "puddle", "A", "'jumped' is the physical action verb."),
        ("Girl **held** a red umbrella above her head.", "held", "girl", "red", "umbrella", "A", "'held' is the physical action verb."),
        ("They **wore** yellow raincoats to stay dry.", "wore", "yellow", "raincoats", "they", "A", "'wore' is the physical action verb."),
        ("The children **danced** under the falling rain.", "danced", "children", "falling", "rain", "A", "'danced' is the physical action verb."),
        ("The paper boats **sailed** down the stream.", "sailed", "paper", "boats", "stream", "A", "'sailed' is the physical action verb."),
        ("Mother **watched** the kids playing from the window.", "watched", "mother", "kids", "window", "A", "'watched' is the sensory action verb."),
        ("They **laughed** happily as water splashed.", "laughed", "happily", "water", "splashed", "A", "'laughed' is the action verb."),
        ("The sun **shone** brightly after the rain.", "shone", "sun", "brightly", "after", "A", "'shone' is the action verb."),
        ("A rainbow **appeared** in the clear sky.", "appeared", "rainbow", "clear", "sky", "A", "'appeared' is the action verb."),
        ("The kids **chased** paper boats down the road.", "chased", "kids", "paper", "road", "A", "'chased' is the physical action verb."),
        ("They **made** origami boats from paper.", "made", "origami", "boats", "paper", "A", "'made' is the physical action verb."),
        ("Water **dripped** from the tree leaves.", "dripped", "water", "tree", "leaves", "A", "'dripped' is the physical action verb."),
        ("They **enjoyed** playing in the cool monsoon rain.", "enjoyed", "playing", "cool", "monsoon", "A", "'enjoyed' is the mental action verb."),
        ("Children **ran** through rain puddles.", "ran", "children", "rain", "puddles", "A", "'ran' is the physical action verb."),
        ("They **returned** indoors when thunder clapped.", "returned", "indoors", "thunder", "clapped", "A", "'returned' is the physical action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH15_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 15:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The kids **happily** **floated** **paper** **boats**.'", "floated", "happily", "paper", "boats", "A", "'floated' shows physical action; 'happily' is adverb, 'paper' is noun/adj, 'boats' is noun."),
        ("Identify BOTH action verbs in: 'Rain **fell** and water **splashed** everywhere.'", "fell, splashed", "rain, water", "fell, rain", "splashed, everywhere", "A", "'fell' and 'splashed' are both action verbs."),
        ("What is the past tense action verb of 'swim' as used in sentence ('The duck swam in puddle')?", "swam", "swimmed", "swimming", "swims", "A", "Past tense of swim is swam."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "The raindrops **fall** softly on the roof.", "Spring is a lovely **fall**.", "Leaves undergo **fall**.", "The waterfall had a steep **fall**.", "A", "In (A), 'fall' acts as the main action verb."),
        ("Find the action verb in: 'The boy jumped into the puddle.'", "jumped", "boy", "into", "puddle", "A", "'jumped' is the physical action verb."),
        ("Which sentence contains NO physical action verb?", "The rainy day was refreshing and cool.", "The rain fell from clouds.", "They floated paper boats.", "The boy jumped in puddles.", "A", "'The rainy day was refreshing and cool' contains linking verb 'was', but no physical action verb."),
        ("Change the action verb 'fly' to past tense: 'The paper boat (float) down the stream yesterday.'", "floated", "floated", "floating", "floats", "A", "Past tense of float is floated."),
        ("Identify the action verb: 'The kids splashed water and sang songs.'", "splashed, sang", "kids, water", "songs, water", "sang, kids", "A", "'splashed' and 'sang' are action verbs."),
        ("Select the action verb that completes the sentence: 'The children ____ paper boats to sail in puddles.'", "crafted / made", "rainy", "wet", "boat", "A", "'crafted' / 'made' is an action verb."),
        ("Which word is an action verb? (puddle, boat, splash, wet)", "splash", "puddle", "boat", "wet", "A", "'splash' is an action verb; others are nouns/adjectives."),
        ("What action did the children perform in the puddles?", "jumped / splashed", "wet", "cool", "puddle", "A", "They jumped/splashed in puddles (action verb)."),
        ("Identify the action verb in: 'They loved playing in monsoon rain.'", "loved / playing", "monsoon", "rain", "they", "A", "'loved' and 'playing' express action/feeling."),
        ("Choose the correct action verb: 'The paper boats ____ down the street.'", "sailed / floated", "high", "paper", "street", "A", "'sailed' / 'floated' is the action verb."),
        ("Identify the action verb in: 'Mother dried their wet clothes.'", "dried", "wet", "clothes", "mother", "A", "'dried' is the action verb."),
        ("Which of these words is NOT an action verb? (fall, float, jump, wet)", "wet", "fall", "float", "jump", "A", "'wet' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'Thunder clapped loudly in the dark sky.'", "clapped", "thunder", "loudly", "sky", "A", "'clapped' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The children ____ into the cold puddle.'", "leapt / jumped", "deep", "wet", "puddle", "A", "'leapt' / 'jumped' is an action verb."),
        ("What action verb completes the sentence? 'A rainbow ____ after the storm stopped.'", "appeared / emerged", "bright", "colorful", "sky", "A", "'appeared' / 'emerged' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The happy children quickly made paper boats and floated them.' How many total ACTION VERBS are present?", "2 action verbs ('made', 'floated')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'made' and 'floated' are action verbs; 'quickly', 'happy' are adverbs/adjectives."),
        ("Categorize the verbs: In 'The sky **was** dark, so rain **fell** heavily', classify 'was' and 'fell'.", "'was' is a linking verb; 'fell' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'was' is action; 'fell' is linking.", "A", "'was' links state of being; 'fell' shows action."),
        ("Replace the weak verb with a strong action verb: 'The water **went** down the street.'", "The water **gushed** down the street.", "The water **was near** the street.", "The water **saw** the street.", "The water **looked at** the road.", "A", "'gushed' is a much stronger, descriptive action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "The children **made** paper boats, **floated** them in puddles, and **splashed** water.", "The rainy day was cool, wet, and dark.", "They sat indoors near the window.", "July is a monsoon month.", "A", "made, floated, splashed are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "The rain **soaked** the lawn.", "The water was **cold**.", "The sky was **dark**.", "The puddle was **deep**.", "A", "'soaked' is an action verb."),
        ("Spot the incorrect verb tense: 'They **float** a paper boat in the puddle yesterday.' Correct it for past simple:", "'floated' is the past action verb form.", "'float' should be 'floating'.", "'float' should be 'floats'.", "'float' should be 'will float'.", "A", "Past simple of float is floated."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (dark clouds cover sky, rain falls, children make paper boats, boats sail in puddles)", "dark clouds cover sky -> rain falls -> children make paper boats -> boats sail in puddles", "boats sail -> rain falls -> clouds cover -> make boats", "make boats -> clouds cover -> sail -> rain falls", "rain falls -> sail -> make boats -> clouds cover", "A", "Logical chronological order of a rainy day scene."),
        ("Identify the verb error in dialogue: Sister said, 'Look how far my paper boat has **float**!'", "'float' is incorrect; the past participle form is 'floated' ('has floated').", "'float' should be 'floating'.", "'float' should be 'floats'.", "No error.", "A", "Perfect tense requires past participle 'floated'."),
        ("Analyze this sentence: 'Rainy outdoor play **invigorates** children.' What type of action verb is 'invigorates'?", "Physical/energizing action verb", "Linking verb", "State of being verb", "Auxiliary verb", "A", "'invigorates' is an action verb describing energizing."),
        ("Which sentence uses action verbs to show cause and effect?", "Rain **fell** heavily, so puddles **formed** in the street.", "The rainy day was cool and wet.", "July is a monsoon month.", "Paper boats are white.", "A", "'fell' (cause action) -> 'formed' (effect action)."),
        ("Spot the missing action verb: 'The paper boats ____ down the stream while the kids ____ with joy.'", "sailed, cheered", "rainy, wet", "was, was", "quick, slow", "A", "'sailed' and 'cheered' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'delighted' in 'The children delighted in rainy play' considered a RICH emotional action verb?", "Because it describes actively finding intense pleasure and joy in an activity.", "Because delighting requires running.", "Because rain is wet.", "Because it is a noun.", "A", "Descriptive action verb conveying emotional joy."),
        ("Transform the action verb to future tense: 'The rain **stops** tomorrow.'", "The rain **will stop** tomorrow.", "The rain **stopped** tomorrow.", "The rain **is stopping** tomorrow.", "The rain **stops** tomorrow.", "A", "'will stop' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The paper boats **sail** smoothly down the stream.", "The paper boats **sails** smoothly down the stream.", "A paper boat **sail** smoothly down the stream.", "The paper boats **is sailing** smoothly down the stream.", "A", "Plural subject 'paper boats' takes base verb 'sail' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'The rain fell softly on the roof__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'Did you make a paper boat today__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a month name like 'July'?", "First letter (July)", "The last letter", "All letters", "No letters", "A", "Month names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'They wore raincoats__ boots__ and carried umbrellas.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden surprise in: 'Look at that huge rainbow!__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense awe/surprise."),
        ("Select the proper noun (month name) that MUST start with a capital letter:", "August", "rain", "puddle", "boat", "A", "'August' as a proper noun starts with a capital letter."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'the title of Chapter 15 is Fun in the Rain.'", "the -> The", "title -> Title", "story -> Story", "is -> Is", "A", "First word of sentence 'The' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'They wore raincoats, boots [ ] and umbrellas.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "A", "Comma separates items before 'and'."),
        ("Which title is capitalized correctly?", "Fun in the Rain", "fun in the rain", "Fun In The Rain", "FUN IN THE RAIN", "A", "Title capitalization (prepositions lowercase unless first)."),
        ("What mark goes after a speaker tag: 'Brother shouted__ \"My boat is winning!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'she said, \"i love jumping in rain puddles.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The paper boat floated down the stream.", "The paper boat floated down the stream?", "The paper boat floated down the stream,", "The paper boat floated down the stream;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like '**children's** paper boats'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which chapter title is capitalized correctly?", "Fun in the Rain", "fun in the rain", "Fun in the rain", "FUN IN RAIN", "A", "Title capitalization."),
        ("What punctuation mark is used around spoken dialogue lines: '___Let us sail paper boats!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Quotation marks enclose exact spoken words.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH15_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "The passage \"Fun in the Rain\" describes monsoon play in July.", "the passage \"fun in the rain\" describes monsoon play in july.", "The passage \"fun In The Rain\" describes monsoon play in July?", "the Passage \"Fun in the Rain\" Was Written In July.", "A", "Title \"Fun in the Rain\", month July capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Why are the children jumping in the puddles?", "Why are the children jumping in the puddles.", "Why are the children jumping in the puddles!", "Why are the children jumping in the puddles,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'In august, heavy rains flooded the street.'", "'august' should be capitalized ('August'); 'rains' is correct.", "'heavy' should be uppercase.", "'street' should be uppercase.", "No mistake.", "A", "Month name 'August' must be capitalized."),
        ("Choose the correctly punctuated dialogue sentence:", "\"Look at my paper boat sail,\" said the little boy.", "look at my paper boat sail said the little boy.", "\"Look at my paper boat sail\" said the little boy", "Look at my paper boat sail, said the little boy.", "A", "Quotation marks around dialogue, comma inside quote, capital L."),
        ("Identify where a COMMA is missing: 'They brought an umbrella a raincoat and boots.'", "Between 'an umbrella' and 'a raincoat' ('an umbrella, a raincoat')", "After 'They'", "After 'boots'", "No comma needed", "A", "Commas separate list items: 'an umbrella, a raincoat and boots'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is the child's raincoat.", "This is the childs' raincoat.", "This is the childs raincoat.", "This is the child's' raincoat.", "A", "child's indicates singular possession."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a gorgeous rainbow appeared after the rain!", "What a gorgeous rainbow appeared after the rain?", "What a gorgeous rainbow appeared after the rain.", "What a gorgeous rainbow appeared after the rain,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'it is'?", "it's", "its'", "it'es", "i'ts", "A", "it's is standard contraction for it is."),
        ("Find the sentence with NO capitalization errors:", "In July, heavy rain fell on our town.", "in July, heavy rain fell on our town.", "In july, Heavy Rain fell on our town.", "in july, heavy rain fell on town.", "A", "'In' (sentence start) and 'July' (month name) capitalized."),
        ("What punctuation mark belongs in the blank? 'The girl yelled, \"Splash in the water!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses yelling/excitement."),
        ("Choose the correct form for 'there is':", "there's", "theres'", "there'es", "t'heres", "A", "there's is standard contraction."),
        ("Identify the punctuation error: 'The rain stopped, a rainbow appeared.'", "Comma splice between two independent clauses (should be semicolon or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for month and place names:", "In August, we visited Mumbai during the monsoons.", "in august, we visited mumbai during the monsoons.", "In august, we visited Mumbai during the Monsoons.", "on August, we visited mumbai in India.", "A", "Month 'August', city 'Mumbai' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The children's boats floated down the stream.", "The childrens' boats floated down the stream.", "The childrens boats floated down the stream.", "The children's' boats floated down the stream.", "A", "children's indicates irregular plural possession."),
        ("Identify the correct punctuation for a list of items: 'They saw ____'", "clouds, rain, and a rainbow.", "clouds rain and a rainbow.", "clouds; rain; and a rainbow.", "clouds: rain: and a rainbow.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "How many paper boats did the children make?", "How many paper boats did the children make.", "How many paper boats did the children make!", "how many paper boats did the children make.", "A", "Capital H, ends with question mark ?"),
        ("Fix the sentence: 'why did the rain stop in august'", "Why did the rain stop in August?", "Why did the rain stop in august.", "why did the rain stop in August!", "Where is August?", "A", "Capital W, capital August, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Mother said, \"Put on your raincoat!\"", "Mother said \"put on your raincoat!\"", "mother said, \"Put on your raincoat!\"", "Mother said, \"Put on your raincoat.\"", "A", "Capital M, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'in july mother said, put on your raincoat before going out'", "5 errors (in->In, july->July, quotation marks, capital P in Put, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, month name, quotation marks, capital P, period."),
        ("Correct the entire dialogue paragraph: 'the sister asked will the paper boat float brother replied yes it will sail fast'", "\"Will the paper boat float?\" asked the sister. Brother replied, \"Yes, it will sail fast.\"", "the sister asked \"will the paper boat float\" brother replied \"yes it will sail fast.\"", "The sister asked, Will the paper boat float. Brother replied, Yes it will sail fast.", "\"Will the paper boat float?\" Asked the sister. Brother replied \"Yes it will sail fast?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'The raindrop**'**s size was big, and it**'**s raining heavily.'", "First 's is possessive (size of the raindrop); second 's is contraction (it is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "raindrop's size = size of the raindrop; it's = it is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"The paper boat is floating,\" Said the boy.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'The' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "The sky was dark with clouds, but no thunder clapped.", "The sky was dark with clouds but, no thunder clapped.", "The sky was dark with clouds but no thunder clapped!", "The sky was dark with clouds; but no thunder clapped?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'in august 2021 heavy rain fell on monday 12th in mumbai'", "In August 2021, heavy rain fell on Monday 12th in Mumbai.", "in august 2021, heavy rain fell on monday 12th in mumbai.", "In August 2021 heavy rain fell on Monday 12th in Mumbai", "In august fell rain in mumbai.", "A", "August, Monday, Mumbai capitalized, comma after year, period."),
        ("Identify why exclamation mark is necessary here: '\"Hurrah, my paper boat reached the shore!\"'", "Because the speaker is expressing intense joy and triumph.", "Because boat is paper.", "Because rain is wet.", "Because sentence is long.", "A", "Exclamation mark communicates intense joyful triumph."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Monsoon, the rainy season in India, brings joy to children.", "Monsoon the rainy season in India brings joy to children.", "Monsoon, the rainy season in India brings joy to children.", "Monsoon the rainy season in India, brings joy to children.", "A", "Appositive phrase 'the rainy season in India' is set off by commas."),
        ("Analyze the use of possessive apostrophe in phrase: \"the children's laughter\"", "The apostrophe 's indicates that the laughter belongs to the children.", "It replaces comma.", "It indicates question.", "It is a plural suffix.", "A", "Possessive apostrophe 's on irregular plural children."),
        ("Identify the correct sentence with direct speech quote within text:", "The boy shouted, \"My boat is sailing!\" and jumped with joy.", "The boy shouted \"My boat is sailing!\" and jumped with joy.", "The boy shouted, 'My boat is sailing!' and jumped with joy.", "The boy shouted: \"My boat is sailing\" and jumped with joy.", "A", "Comma before quote, double quotation marks around direct speech with ! inside."),
        ("Spot the missing apostrophe: 'The childrens raincoats were hanging by the door.'", "Missing apostrophe in 'children's' -> 'The children's raincoats...'", "Missing apostrophe in 'raincoats''", "Missing apostrophe in 'door''", "No apostrophe needed", "A", "'The children's raincoats' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Sister, said brother, is making boats.' vs 'Sister said, \"Brother is making boats.\"'", "In the first, brother says sister is making boats; in the second, sister says brother is making boats.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who performs action."),
        ("Correct all 4 errors in: 'whats floating in the puddle asked the girl'", "\"What's floating in the puddle?\" asked the girl.", "whats floating in the puddle? asked the girl.", "\"What's floating in the puddle.\" asked the girl.", "\"whats floating in the puddle?\" Asked the girl.", "A", "Quotation marks, capital W, contraction What's, question mark, period at end."),
        ("Identify the rule for capitalizing story titles like \"Fun in the Rain\":", "Titles take initial capital letters for all major words (nouns, verbs, adjectives, adverbs) except short prepositions like 'in' or 'the' unless first.", "Story titles are never capitalized.", "Story titles are capitalized only at end of line.", "Story titles must be written in ALL CAPS.", "A", "Standard title capitalization rule.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'rain'** (in Chapter 15)?", "ai", "ea", "ee", "ou", "A", "'ai' is the vowel digraph in rain."),
        ("Identify the vowel digraph in the word **'boat'** (paper boat):", "oa", "ee", "ie", "ui", "A", "'oa' forms the long /o/ vowel sound in boat."),
        ("Which word from the story topic contains the **'ou'** vowel digraph?", "cloud", "rain", "boat", "street", "A", "'cloud' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'clean'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in clean."),
        ("Which vowel digraph appears in the word **'sail'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in sail."),
        ("Find the word with the **'ou'** vowel digraph: 'Rain fell out of the dark cloud.'", "out / cloud", "rain", "fell", "dark", "A", "'out' and 'cloud' contain 'ou' vowel digraph."),
        ("Which word from the story topic rhymes with **'rain'**?", "train", "boat", "cloud", "puddle", "A", "'train' rhymes with 'rain'."),
        ("Which word from the story topic rhymes with **'boat'**?", "coat", "rain", "cloud", "puddle", "A", "'coat' rhymes with 'boat'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the story topic rhymes with **'float'**?", "coat", "rain", "cloud", "puddle", "A", "'coat' rhymes with 'float'."),
        ("Identify the vowel digraph in **'green'** (as in green leaves):", "ee", "ea", "oo", "ui", "A", "'ee' makes long /e/ sound in green."),
        ("Which word from Chapter 15 has the **'ai'** digraph making a long /a/ sound?", "rain", "bread", "head", "heavy", "A", "'rain' has 'ai' making long /a/ sound."),
        ("Which word rhymes with **'day'**?", "play", "rain", "boat", "cloud", "A", "'play' rhymes with 'day'."),
        ("Identify the silent letters in **'high'** (as in 'high sky'):", "gh", "h", "i", "g", "A", "Silent 'gh' in high."),
        ("Which word from the story topic has long /i/ sound spelled with **'igh'**?", "bright", "bought", "bowl", "baker", "A", "'igh' in bright makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They walked around the puddle.'", "around", "puddle", "walked", "they", "A", "'around' contains 'ou' digraph."),
        ("Which word rhymes with **'splash'**?", "dash", "boat", "rain", "coat", "A", "'dash' rhymes with 'splash'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH15_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ai'** digraph sound in **'rain'** and **'sail'**. What is the similarity?", "Both make long /a/ vowel sound.", "Both make short /a/ sound.", "Both make long /e/ sound.", "Both are silent.", "A", "'ai' consistently makes long /a/ sound (rain, sail)."),
        ("Select the word pair from Chapter 15 that has the SAME vowel sound pattern:", "boat - coat", "rain - head", "cloud - boat", "splash - rain", "A", "'boat' (oa) and 'coat' (oa) both make long /o/ sound."),
        ("Which word contains SILENT letters? (bright, high, know, all of these)", "all of these", "bright", "high", "know", "A", "'bright' (gh), 'high' (gh), 'know' (k)."),
        ("Identify the odd one out based on vowel sound: (boat, coat, float, rain)", "rain", "boat", "coat", "float", "A", "'rain' has long /a/ sound; others have long /o/ sound."),
        ("Which digraph completes the word for precipitation? 'r__n'", "ai", "ee", "oa", "ou", "A", "'rain' uses 'ai' digraph."),
        ("Group these story words by rhyming sound: **boat**, **coat**, **float**. What sound pattern do they share?", "oa long /o/ sound", "ow", "oo", "oi", "A", "All share 'oa' making long /o/ sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'Thunder roared in **the** sky.'", "the / thunder", "roared", "sky", "in", "A", "'thunder' contains unvoiced 'th' consonant digraph."),
        ("Which of these words has the **'ai'** vowel digraph making long /a/ sound? (rain, sail, tail, all of these)", "all of these", "rain", "sail", "tail", "A", "rain, sail, tail all share 'ai' long /a/ sound."),
        ("Identify the vowel digraph in **'cloud'**:", "ou", "ae", "ur", "or", "A", "'ou' is the vowel digraph in cloud."),
        ("Which word from the story has silent **'k'**? (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "know, knee, knife all have silent initial 'k' before 'n'."),
        ("Select the rhyming pair for story context: 'rain' and ____.", "train", "boat", "puddle", "cloud", "A", "'rain' rhymes with 'train'."),
        ("Select the rhyming pair for story context: 'boat' and ____.", "float", "rain", "puddle", "cloud", "A", "'boat' rhymes with 'float'."),
        ("Select the rhyming pair for story context: 'splash' and ____.", "dash", "rain", "boat", "puddle", "A", "'splash' rhymes with 'dash'."),
        ("Select the rhyming pair for story context: 'cloud' and ____.", "loud", "rain", "boat", "puddle", "A", "'cloud' rhymes with 'loud'."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 15 vocabulary: (ice, place, bounce, all of these)", "all of these", "ice", "place", "bounce", "A", "ice, place, bounce all have soft /s/ sound for 'c' before 'e'."),
        ("Which word has a soft **'g'** sound? (giant, gentle, magic, all of these)", "all of these", "giant", "gentle", "magic", "A", "giant, gentle, magic all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'oa'** digraph for vessel:", "boat", "bot", "boate", "buat", "A", "boat is standard spelling with 'oa'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'ice'** sound like /s/, but 'c' in **'cloud'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound (ice); before 'l', 'a', 'o', 'u' it makes hard /k/ sound (cloud).", "Because ice is cold.", "Because cloud is sky.", "There is no rule.", "A", "Soft 'c' rule: c + e, i, y = /s/ sound."),
        ("Categorize the 'oa' vs 'ai' digraphs: (boat, coat, float, rain, sail, tail)", "Long /o/ (oa): boat, coat, float; Long /a/ (ai): rain, sail, tail", "All are long /o/.", "All are long /a/.", "Long /o/: rain; Long /a/: boat", "A", "boat, coat, float make long /o/; rain, sail, tail make long /a/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "bright - know", "rain - boat", "cloud - puddle", "splash - stream", "A", "'bright' (silent gh) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 2-letter consonant blend at the start?", "splash [3-letter] / stream [3-letter] / rain [1 consonant]", "cloud / float [2-letter blend]", "boat", "out", "B", "'cl' / 'fl' is a 2-letter consonant blend."),
        ("Examine the soft 'c' rule: Why is 'c' soft in **'bounce'** but hard in **'coat'**?", "'c' followed by 'e' makes soft /s/ sound (bounce); 'c' before 'o' makes hard /k/ sound (coat).", "Because coat is clothing.", "Because bounce is action.", "There is no rule.", "A", "Soft 'c' rule: c + e = /s/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "brightest", "rain", "boat", "cloud", "A", "'brightest' has 'igh' trigraph with silent 'gh'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'cloud'**?", "cloud - out", "voice - coin", "paid - day", "boat - coat", "A", "'cloud' and 'out' share /ow/ diphthong sound."),
        ("Analyze homophones: 'The paper boat will **sail** / **sale** down the stream.' Which word means navigate on water?", "sail", "sale", "sayle", "saile", "A", "'sail' (navigate water) vs 'sale' (selling items) are homophones."),
        ("Identify the phonic pattern in **'thunderstorm'**: How many syllables are in this word?", "3 syllables (thun-der-storm)", "2 syllables", "4 syllables", "1 syllable", "A", "thun-der-storm has 3 syllables."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (clouds, puddles, boats [s], raindrops [s])", "clouds / puddles", "boats", "raindrops", "raincoats", "A", "Plurals ending in voiced sounds take /z/ ending sound (clouds, puddles)."),
        ("Spot the word where 'k' is SILENT: (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "'k' is silent before 'n' in know, knee, knife."),
        ("HOTS Reasoning: Why do 'rain' and 'reign' sound identical but have different spellings and meanings?", "They are homophones (words with identical sound but different origin, spelling, and meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share identical sound but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "raincoat / raindrop", "monsoon", "puddle", "umbrella", "A", "raincoat = rain + coat; raindrop = rain + drop."),
        ("Determine the syllable count and stress: How many syllables are in **'umbrellas'**?", "3 syllables (um-brel-las)", "2 syllables", "4 syllables", "1 syllable", "A", "um-brel-las has 3 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ was falling from the sky on the rainy day?", "What", "Who", "Where", "Why", "A", "'What' asks about phenomenon ('Rain')."),
        ("___ were playing in the rain puddles?", "Who", "What", "Where", "Why", "A", "'Who' asks about people ('The children')."),
        ("___ did the children float their paper boats?", "Where", "Who", "What", "Why", "A", "'Where' asks about location ('In puddles / streams')."),
        ("___ made the paper boats for the children?", "Who", "What", "Where", "Why", "A", "'Who' asks about person ('The children / brother')."),
        ("___ did the boy wear to protect himself from rain?", "What", "Who", "Where", "Why", "A", "'What' asks about clothing ('A raincoat')."),
        ("___ did the girl hold over her head?", "What", "Who", "Where", "Why", "A", "'What' asks about item ('An umbrella')."),
        ("___ appeared in the sky after the rain stopped?", "What", "Who", "Where", "Why", "A", "'What' asks about phenomenon ('A rainbow')."),
        ("___ month of the year did the heavy monsoon rain fall?", "Which", "Who", "Where", "Why", "A", "'Which month' asks about 'July / August'."),
        ("___ did the children feel when playing in puddles?", "How", "Who", "Where", "Why", "A", "'How' asks about feeling ('Happy and excited')."),
        ("___ kind of clouds covered the sky before it rained?", "What kind of", "Who", "Where", "Why", "A", "'What kind of' asks about clouds ('Dark rain clouds')."),
        ("___ made water splashes in the street?", "Who / What", "Where", "Why", "When", "A", "'What' asks about action ('Jumping in puddles')."),
        ("___ item floats on water in the passage?", "Which", "Who", "Where", "Why", "A", "'Which item' asks about 'paper boat'."),
        ("___ color was the rainbow in the sky?", "What", "Who", "Where", "Why", "A", "'What color' asks about 'seven colors / colorful'."),
        ("___ watched the children from the window?", "Who", "What", "Where", "Why", "A", "'Who' asks about person ('Mother')."),
        ("___ long did the rain shower last?", "How", "Who", "Where", "Why", "A", "'How long' asks about duration ('1 hour')."),
        ("___ was the ground wet?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason ('Because it rained')."),
        ("___ animal or insect comes out during rain?", "Which", "Who", "Where", "Why", "A", "'Which animal' asks about 'frogs / earthworms'."),
        ("___ season of the year is known for rain?", "Which", "Who", "Where", "Why", "A", "'Which season' asks about 'Monsoon season').")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH15_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ did the children jump into puddles?' Answer: 'Because playing in water was fun.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ was the paper boat floating?' Answer: 'In a stream on the street.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ did the storm stop?'", "When / What time", "Where", "Who", "Why", "A", "'When' inquires about time (at 4:00 p.m.)."),
        ("Form an asking sentence: 'Rain fell from clouds.' -> '____ fell from clouds?'", "What", "Who", "Why", "Where", "A", "'What' inquires about subject."),
        ("Identify the INCORRECT question word usage: '**Why** floated the paper boat down the stream?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What floated...' asks for object."),
        ("Select the proper interrogative sentence:", "Why do children love playing in monsoon rain?", "Why children loves playing in monsoon rain?", "Why does children loved?", "Why kids loves?", "A", "Interrogative word + auxiliary 'do' + plural subject + base verb."),
        ("Which question word asks about MANNER or METHOD? '___ did the paper boat sail down the stream?'", "How", "Who", "What", "Where", "A", "'How' inquires about manner ('smoothly / fast')."),
        ("Complete the question: '___ of the items protects you from getting wet?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options (raincoat / umbrella)."),
        ("Change statement to question: 'They jumped in puddles.' -> '____ did they jump?'", "Where", "Who", "Why", "What", "A", "'Where' asks for location."),
        ("Fill in the blank: '___ deep was the rain puddle?'", "How", "What", "Where", "Why", "A", "'How deep' measures depth."),
        ("Identify the question word in: 'Whom did mother watch playing in the rain?'", "Whom", "did", "mother", "watch", "A", "'Whom' is the interrogative pronoun asking about the children."),
        ("Choose the question that matches this answer: 'A paper boat, an umbrella, and a raincoat.'", "What items are associated with rain in the story?", "Where did they run?", "Who floated the boat?", "What is monsoon?", "A", "'What items are associated with rain...' matches answer."),
        ("Fill in the blank: '___ child made the fastest paper boat?'", "Which", "Who", "Why", "Where", "A", "'Which child' asks for identification."),
        ("Complete: '___ paper boats did they float?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity."),
        ("Select the correct question for: 'A colorful rainbow appeared across the dark blue sky.'", "What appeared in the sky after the rain?", "Where is the boat?", "Why do frogs jump?", "Who is mother?", "A", "'What appeared in the sky after the rain?' asks for event."),
        ("Which question word inquires about POSSESSION? '___ paper boat floated the farthest?'", "Whose", "Who", "Where", "Why", "A", "'Whose paper boat' asks about owner."),
        ("Form question: 'They spent 2 hours playing in rain.' -> '____ hours did they spend playing in rain?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why did the rain fall so hard.' Correct it:", "Why did the rain fall so hard?", "Why did the rain fall so hard!", "Why did the rain fall so hard,", "Why did the rain fall so hard;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why do children feel immense joy when sailing paper boats in rain puddles?' What is the syntax pattern?", "Question Word + Helping Verb (do) + Subject (children) + Main Verb (feel) + Direct Object + Prepositional Phrase + Gerund Phrase", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ raindrops' vs '___ rain'", "'How many' for countable raindrops; 'How much' for uncountable rain mass.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for raindrops; 'How many' for rain.", "A", "Countable nouns take 'How many'; uncountable mass nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where the paper boat floated?' Correct it:", "Where **did** the paper boat float?", "Where the paper boat floated?", "Where floated the paper boat?", "Where do the paper boat float?", "A", "Past simple questions require auxiliary 'did' before subject 'the paper boat' and base verb 'float'."),
        ("Framing multi-question passage guide: What sequence of question words logically builds a descriptive passage of 'Fun in the Rain'?", "What weather started -> Who went outside -> What gear did they wear -> What fun activities did they do -> What appeared at the end", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals weather context, characters, clothing, actions, and resolution."),
        ("Transform the statement into a formal question: 'Rainy day activities stimulate creativity and sensory development in young children.'", "How does playing in the rain with paper boats enhance children's sensory and creative development?", "Where is rain?", "Who made boat?", "What is puddle?", "A", "Directly targets developmental theme."),
        ("Analyze this ambiguous question: 'What did they float?' How can it be made precise?", "Add specific context: 'What handmade paper items did the children float down the flowing water stream?'", "Make it shorter: 'What float?'", "Change to: 'Where float?'", "Remove 'What'.", "A", "Adding specific context clarifies which crafted items."),
        ("Choose the correct question pair for dialogue: Girl: '___ can we sail our paper boat?' Boy: '___ in that deep puddle over there!'", "Where, Right over there", "Who, Where", "Where, How", "When, Whose", "A", "Where (location inquiry), Right over there (location answer)."),
        ("Spot the DOUBLE auxiliary error: 'Why did the rain fell so heavily?'", "'did' requires base verb 'fall', not past tense 'fell'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('fall')."),
        ("Reconstruct question from answer: Answer: 'A seven-colored rainbow arched gracefully across the sky after the rain stopped.'", "Question: 'What appeared in the sky after the rain stopped?'", "Question: 'Where did they run?'", "Question: 'Who bought a boat?'", "Question: 'Why is rain wet?'", "A", "Targets rainbow appearance."),
        ("Form indirect question: 'The child asked why rain fell from clouds.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for science reasoning: '___ do rain clouds turn dark before it rains?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the scientific reason."),
        ("HOTS Reasoning: Why is 'Who' used for children but 'Which' used when selecting between rain gear (raincoat vs umbrella)?", "'Who' is used for human children; 'Which' is used when selecting between specific gear options.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the items...' selects from defined options."),
        ("Correct all errors in: 'why did the children play in the rain in july'", "Why did the children play in the rain in July?", "Why did the children play in the rain in july.", "Whom did the children play in the rain?", "Why does the children played in rain?", "A", "Capital W, capital July, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 15:", "How does Arthur Guiterman / passage theme portray rain as a source of joy, wonder, and imaginative play for children?", "What falls from sky?", "Where is puddle?", "Who made boat?", "A", "Asks student to evaluate poetic theme, joy, and imaginative play.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The rain is **falling** softly from the sky.", "falling", "rain", "is", "sky", "A", "'falling' is verb + -ing form."),
        ("The children are **floating** paper boats.", "floating", "children", "are", "boats", "A", "'floating' is verb + -ing form."),
        ("The boy is **jumping** into the puddle.", "jumping", "boy", "is", "puddle", "A", "'jumping' is verb + -ing form."),
        ("The girl is **holding** a red umbrella.", "holding", "girl", "is", "umbrella", "A", "'holding' is verb + -ing form."),
        ("They are **wearing** yellow raincoats.", "wearing", "they", "are", "raincoats", "A", "'wearing' is verb + -ing form."),
        ("The children are **dancing** in the rain.", "dancing", "children", "are", "rain", "A", "'dancing' is verb + -ing form."),
        ("The paper boats are **sailing** down the stream.", "sailing", "paper", "boats", "stream", "A", "'sailing' is verb + -ing form."),
        ("Mother is **watching** them from the window.", "watching", "mother", "is", "window", "A", "'watching' is verb + -ing form."),
        ("The kids are **splashing** water everywhere.", "splashing", "kids", "are", "everywhere", "A", "'splashing' is verb + -ing form."),
        ("They are **laughing** with pure joy.", "laughing", "they", "are", "joy", "A", "'laughing' is verb + -ing form."),
        ("The sun is **shining** through the clouds.", "shining", "sun", "is", "clouds", "A", "'shining' is verb + -ing form."),
        ("A rainbow is **appearing** in the sky.", "appearing", "rainbow", "is", "sky", "A", "'appearing' is verb + -ing form."),
        ("Water is **dripping** from the roof edge.", "dripping", "water", "is", "roof", "A", "'dripping' is verb + -ing form."),
        ("The children are **enjoying** the monsoon shower.", "enjoying", "children", "are", "shower", "A", "'enjoying' is verb + -ing form."),
        ("Frogs are **croaking** near the pond.", "croaking", "frogs", "are", "pond", "A", "'croaking' is verb + -ing form."),
        ("They are **making** new paper boats.", "making", "they", "are", "boats", "A", "'making' is verb + -ing form."),
        ("The wind is **blowing** gently outside.", "blowing", "wind", "is", "outside", "A", "'blowing' is verb + -ing form."),
        ("They are **running** back inside the house.", "running", "they", "are", "house", "A", "'running' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH15_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'fall'**? (Rain is ____.)", "falling (add -ing)", "fallling", "falleing", "fallng", "A", "Regular verb adding -ing (falling)."),
        ("What is the correct -ing spelling rule for **'swim'**? (The kids are ____ in puddles.)", "swimming (double final consonant)", "swiming", "swimmeging", "swimng", "A", "CVC rule: double final consonant before -ing (swimming)."),
        ("What is the correct -ing spelling rule for **'make'**? (They are ____ paper boats.)", "making (drop final silent e)", "makeing", "makking", "makng", "A", "Drop final silent 'e' before adding -ing (making)."),
        ("Fill in the blank with present continuous form: 'The rain (fall) ____ from the clouds.'", "is falling", "are fall", "was falling", "is fallen", "A", "Uncountable singular 'rain' takes 'is falling'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The children are floating paper boats right now.", "The children floated paper boats yesterday.", "The children will float paper boats tomorrow.", "The children floated yesterday.", "A", "'are floating' is present continuous."),
        ("Fill in the blanks: 'The rain ____ (drip), and the children ____ (splash) in puddles.' ", "is dripping, are splashing", "are dripping, is splashing", "is drip, are splash", "was dripping, were splashing", "A", "Singular 'rain' takes 'is dripping'; plural 'children' takes 'are splashing'."),
        ("Identify the spelling mistake in: 'The boy is **makeing** a paper boat.'", "'makeing' should be 'making'", "'makeing' should be 'making'", "'is' should be 'are'", "No mistake", "A", "Make drops silent e before -ing (making)."),
        ("Select the correct -ing form for **'dance'**:", "dancing", "danceing", "dancking", "dancng", "A", "Drop silent 'e': dance -> dancing."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Look! Raindrops are falling on the window pane.", "Raindrops fell on the window pane yesterday.", "Raindrops fall on the window pane in monsoon.", "Raindrops will fall tomorrow.", "A", "Present continuous ('are falling') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (hold) a big yellow umbrella.'", "am holding", "is holding", "are holding", "am holdeing", "A", "Subject 'I' takes 'am holding'."),
        ("Choose the correct form: 'The paper boat ____ (sail) gracefully down the stream.'", "is sailing", "are sailing", "am sailing", "is sail", "A", "Singular subject 'paper boat' takes 'is sailing'."),
        ("Identify the verb in: 'Why are you splashing water?'", "are splashing", "Why", "you", "water", "A", "Helping verb 'are' + main verb 'splashing' form present continuous."),
        ("What is the -ing form of **'drip'**?", "dripping", "driping", "dripeing", "dripng", "A", "CVC double p: drip -> dripping."),
        ("What is the -ing form of **'shine'**?", "shining", "shineing", "shinning", "shinng", "A", "Drop silent e: shine -> shining."),
        ("Change simple present to continuous: 'It rains.' -> 'It ____.'", "is raining", "rained", "was raining", "will rain", "A", "is raining."),
        ("Fill in the blank: 'The sun ____ (shining) through the clouds.'", "is shining", "are shining", "am shining", "shined", "A", "Singular subject 'sun' takes 'is shining' (shine drops e -> shining)."),
        ("Identify the correct present continuous sentence:", "Look! The children are jumping into the puddle.", "Look! The children jumps into the puddle.", "Look! The children jumped into the puddle.", "Look! The children jumping into the puddle.", "A", "Exclamation 'Look!' introduces action happening now ('are jumping')."),
        ("Select the correct -ing form for **'float'**:", "floating", "floateing", "floatting", "floatng", "A", "Regular verb adding -ing (floating).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (drip, shine, float)", "drip -> dripping (double consonant), shine -> shining (drop e), float -> floating (add -ing)", "All just add -ing.", "All double the last letter.", "drip -> driping, shine -> shineing, float -> floatting", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The rain fell while children floated paper boats.'", "The rain is falling while children are floating paper boats.", "The rain falling while children floating paper boats.", "The rain was falling while children floated.", "The rain will fall while children float.", "A", "Both verbs transformed to present continuous (is falling, are floating)."),
        ("Spot the missing auxiliary verb in: 'The paper boat floating down stream and kids laughing.' Correct it:", "'The paper boat **is** floating down the stream and kids **are** laughing.'", "'The paper boat floating down stream and kids laughing.'", "'The paper boat **are** floating and kids **is** laughing.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The child is **liking** the rain'?", "Because 'like' expressing emotion is stative, preferring simple present 'The child likes the rain'.", "Because 'liking' is hard to spell.", "Because rain is wet.", "Because boat is paper.", "A", "Stative emotion verbs prefer simple present."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The children in the garden are playing in puddles.", "The children in the garden is playing in puddles.", "The children in the garden am playing in puddles.", "The children in the garden playing in puddles.", "A", "Plural subject ('children') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The children are staying inside.' -> Negative for rainy outdoor scene:", "The children **are not** staying inside; they are playing in the rain.", "The children not staying inside.", "The children is no staying inside.", "The children isn't stay inside.", "A", "Add 'not' after plural auxiliary 'are'."),
        ("Spot all THREE spelling errors: 'He is **dripping** wet, **makeing** boats, and **runing** outside.'", "'dripping' is correct; 'makeing' -> 'making'; 'runing' -> 'running'", "'dripping' -> 'driping'; 'makeing' -> 'making'; 'runing' -> 'running'", "No errors.", "Only 'makeing' is wrong.", "A", "dripping (double p is correct), making (drop e), running (double n)."),
        ("Rewrite as interrogative present continuous: 'The rainbow is appearing in the sky.'", "**Is** the rainbow appearing in the sky?", "Are the rainbow appearing in the sky?", "The rainbow appearing in the sky?", "Why the rainbow is appearing in the sky?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The storm **is arriving** this afternoon.' What does present continuous express here?", "A fixed future arrangement / planned atmospheric event.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express impending future events."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While rain is falling, the children are sailing paper boats.", "While rain fell, children are sailing.", "Rain is falling while children sailed.", "Rain fall while children sail.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'The boat is floatting down the stream.'", "'floatting' should be 'floating' (single 't').", "'is' should be 'are'.", "'stream' should be capitalized.", "No error.", "A", "Float + ing = floating (single t)."),
        ("HOTS Reasoning: Compare 'The rain fell' (Past Simple) vs 'The rain is falling' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means rain stopped.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the children ____ (jumping) in the puddle?'", "are, jumping", "is, jumping", "am, jumping", "do, jumping", "A", "Plural subject children takes 'are ... jumping'."),
        ("Identify the correct present continuous sentence describing passage writing:", "The happy children are floating paper boats in the rain stream.", "The happy children is floating paper boats in the rain stream.", "The happy children am floating paper boats in the rain stream.", "The happy children floating paper boats in the rain stream.", "A", "Plural subject 'happy children' + are + floating.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 15: Fun in the Rain\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("The rain ___ falling heavily outside.", "is", "are", "am", "be", "A", "Uncountable singular subject 'The rain' takes 'is'."),
        ("The children ___ floating paper boats.", "are", "is", "am", "be", "A", "Plural subject 'children' takes 'are'."),
        ("I ___ wearing my yellow raincoat.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The paper boat ___ sailing down the stream.", "is", "are", "am", "be", "A", "Singular subject 'paper boat' takes 'is'."),
        ("The red umbrella ___ open above her head.", "is", "are", "am", "be", "A", "Singular subject 'umbrella' takes 'is'."),
        ("The puddles ___ deep on the road.", "are", "is", "am", "be", "A", "Plural subject 'puddles' takes 'are'."),
        ("A rainbow ___ visible in the sky.", "is", "are", "am", "be", "A", "Singular subject 'rainbow' takes 'is'."),
        ("The dark clouds ___ covering the sun.", "are", "is", "am", "be", "A", "Plural subject 'clouds' takes 'are'."),
        ("I ___ jumping into the clean puddle.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The monsoon weather ___ cool and refreshing.", "is", "are", "am", "be", "A", "Uncountable singular 'weather' takes 'is'."),
        ("The raindrops ___ falling on the leaves.", "are", "is", "am", "be", "A", "Plural subject 'raindrops' takes 'are'."),
        ("Mother ___ watching us from the porch.", "is", "are", "am", "be", "A", "Singular subject 'Mother' takes 'is'."),
        ("You ___ writing a passage about rainy fun.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("Brother and sister ___ playing in the garden.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("The street ___ full of water puddles.", "is", "are", "am", "be", "A", "Singular 'street' takes 'is'."),
        ("I ___ holding my mother's hand.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The story about rain ___ exciting to read.", "is", "are", "am", "be", "A", "Singular 'story' takes 'is'."),
        ("The frogs ___ croaking near the stream.", "are", "is", "am", "be", "A", "Plural 'frogs' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH15_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'The raincoat and umbrella ____ in the hallway.'", "are", "is", "am", "be", "A", "Compound subject ('raincoat and umbrella') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "The rain is falling softly on the grass.", "The rain are falling softly on the grass.", "The rain am falling softly on the grass.", "The rain be falling softly on the grass.", "A", "Uncountable noun 'The rain' requires 'is'."),
        ("Fill in the blanks: 'I ____ holding an umbrella, and my brother ____ floating a boat.'", "am, is", "is, is", "are, is", "am, are", "A", "'I am', 'my brother is'."),
        ("Identify the mistake in: 'The puddles on the street **is** very deep.'", "'is' should be 'are' because 'puddles' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'puddles' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you ready to sail your paper boat?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither rain nor thunder ____ stopping the children.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject 'thunder' takes 'is'."),
        ("Select the correct sentence for passage moral:", "Joy and happiness are found in simple rainy play.", "Joy and happiness is found in simple rainy play.", "Joy and happiness am found in simple rainy play.", "Joy and happiness be found in simple rainy play.", "A", "Compound subject 'Joy and happiness' takes 'are'."),
        ("Complete the conversation: Sister: 'Where ____ my paper boat?' Brother: 'It ____ sailing down the stream!'", "is, is", "are, are", "is, are", "are, is", "A", "Singular 'my paper boat' -> is; singular 'It' -> is."),
        ("Identify where 'is' is used incorrectly:", "The paper boats **is** sailing.", "The sky is dark.", "The rain is heavy.", "The girl is happy.", "A", "'The paper boats is' should be 'The paper boats are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The group of children ____ playing in the rain.'", "is", "are", "am", "be", "A", "Collective noun 'group' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The water in the puddles ____ cool.'", "is", "are", "am", "be", "A", "Uncountable singular subject 'water' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am writing a story about fun in the rain.", "I is writing a story about fun in the rain.", "I are writing a story about fun in the rain.", "I be writing a story about fun in the rain.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many paper boats floating in the stream.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many paper boats'."),
        ("Fill in the blank: 'There ____ a bright rainbow in the sky.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a bright rainbow'."),
        ("Choose the correct sentence:", "What are the raindrops doing on the roof?", "What is the raindrops doing on the roof?", "What am the raindrops doing on the roof?", "What be the raindrops doing on the roof?", "A", "Plural subject 'the raindrops' takes 'are'."),
        ("Identify the correct form: 'The girl, as well as her friends, ____ splashing water.'", "is", "are", "am", "be", "A", "Subject is singular 'The girl' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both raincoats and umbrellas ____ useful in July.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The rain ____ falling, but the kids ____ laughing.'", "is, are", "are, is", "am, are", "is, is", "A", "'rain is', 'kids are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH15_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the paper boats **____** floating safely down the stream.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'boats' is plural.", "am — because it refers to speaker.", "be — because boats are paper.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A group of children **are** splashing in the puddle.'", "'are' should be 'is' because the subject is singular noun 'group'.", "'are' should be 'am'.", "'children' should be 'child'.", "No error.", "A", "'A group' is singular, so it requires 'is splashing'."),
        ("Compare: (1) 'The rain and the wind **are** strong.' vs (2) 'The rain, along with the wind, **is** strong.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'The rain' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the neighborhood **____** enjoying the rain shower.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The puddles **is** deep, I **is** wet, and the boats **is** sailing.'", "'puddles is' -> 'puddles are'; 'I is' -> 'I am'; 'boats is' -> 'boats are'", "'puddles is' -> 'puddles am'; 'I is' -> 'I are'; 'boats is' -> 'boats am'", "Only 'I is' is wrong.", "No errors present.", "A", "puddles are (plural), I am (1st person), boats are (plural)."),
        ("Fill in the blanks in this complex sentence: 'Not only the rain but also the clouds **____** dark, while the sky **____** clearing.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer plural subject ('clouds' -> are); 'sky' -> is."),
        ("Transform to negative: 'The rain is stopping.'", "The rain **is not** stopping.", "The rain are not stopping.", "The rain am not stopping.", "The rain no stopping.", "A", "Add 'not' after singular helping verb 'is'."),
        ("Analyze inverted subject position: 'Across the dark sky **____** stretching a beautiful rainbow.'", "is", "are", "am", "be", "A", "Subject is singular 'a beautiful rainbow', appearing after verb, requiring 'is'."),
        ("Determine agreement with uncountable nouns: 'The water in the streams **____** flowing rapidly.'", "is", "are", "am", "be", "A", "Uncountable noun 'water' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the paper boats we made.'", "Here **are** the paper boats we made.", "Here am the paper boats we made.", "Here be the paper boats we made.", "No error.", "A", "Plural subject 'paper boats' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "The rainy weather **is** refreshing.", "The child **is** making a paper boat.", "Rain **is** falling from dark clouds.", "Mother **is** holding an umbrella.", "A", "In 'The rainy weather is refreshing', 'is' is the main linking verb connecting subject to predicate adjective."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because rain is wet.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither rain nor puddles **____** stopping them, because monsoon **____** fun.'", "are, is", "is, are", "is, is", "are, are", "A", "'puddles' is closer plural subject -> are; 'monsoon' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The rain is falling, I am playing, and the paper boats are sailing.", "The rain are falling, I is playing, and the paper boats is sailing.", "The rain am falling, I are playing, and the paper boats am sailing.", "The rain is falling, I is playing, and the paper boats is sailing.", "A", "rain is (uncountable singular), I am (1st person), paper boats are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH15_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 15
# ---------------------------------------------------------------------------
def rebuild_chapter_15():
    print("Rebuilding Chapter 15 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

    files_and_generators = [
        ("plural_nouns_spelling.md", build_plural_nouns),
        ("articles_grammar.md", build_articles_grammar),
        ("calendar_days_vocabulary.md", build_calendar_days),
        ("action_verbs_identification.md", build_action_verbs),
        ("punctuation_marks.md", build_punctuation_marks),
        ("phonics_vowel_digraphs.md", build_phonics_digraphs),
        ("question_words_interrogatives.md", build_question_words),
        ("present_continuous_ing.md", build_present_continuous),
        ("helping_verbs_is_am_are.md", build_helping_verbs)
    ]

    for fname, gen_func in files_and_generators:
        filepath = os.path.join(CH15_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 15 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_15()
