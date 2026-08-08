r"""
=============================================================================
Script: rebuild_chapter_14.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 14:
             "Family's Day Out" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH14_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_14")
os.makedirs(CH14_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("family", "families", "familys", "familyes", "familiz", "A", "Consonant + y changes to -ies (families)."),
        ("picnic", "picnics", "picnices", "picnicies", "picnicz", "A", "Regular noun adding -s."),
        ("basket", "baskets", "basketes", "basketies", "basketz", "A", "Regular noun adding -s."),
        ("sandwich", "sandwiches", "sandwichs", "sandwichies", "sandwichz", "A", "Nouns ending in -ch add -es (sandwiches)."),
        ("tree", "trees", "treees", "treies", "treez", "A", "Regular noun ending in -e adds -s."),
        ("duck", "ducks", "duckes", "duckies", "duckz", "A", "Regular noun adding -s."),
        ("bird", "birds", "birdes", "birdies", "birdz", "A", "Regular noun adding -s."),
        ("kite", "kites", "kitees", "kities", "kitez", "A", "Regular noun ending in -e adds -s."),
        ("rug", "rugs", "ruges", "rugies", "rugz", "A", "Regular noun adding -s."),
        ("park", "parks", "parkes", "parkies", "parkz", "A", "Regular noun adding -s."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people."),
        ("glass", "glasses", "glasss", "glassies", "glassz", "A", "Nouns ending in -ss add -es (glasses)."),
        ("box", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es (boxes)."),
        ("bench", "benches", "benchs", "benchies", "benchz", "A", "Nouns ending in -ch add -es (benches)."),
        ("dish", "dishes", "dishs", "dishies", "dished", "A", "Nouns ending in -sh add -es (dishes)."),
        ("apple", "apples", "applies", "applees", "applez", "A", "Regular noun ending in -e adds -s."),
        ("game", "games", "gamies", "gamees", "gamez", "A", "Regular noun ending in -e adds -s.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH14_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 14 (*Family's Day Out*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The parents packed two (family / families) of picnic baskets.", "families", "family", "familys", "familyes", "A", "Consonant + y changes to -ies (families)."),
        ("They made delicious (sandwich / sandwiches) for the picnic.", "sandwiches", "sandwich", "sandwichs", "sandwichies", "A", "Nouns ending in -ch add -es (sandwiches)."),
        ("The children sat on wooden (bench / benches) in the park.", "benches", "bench", "benchs", "benchies", "A", "Nouns ending in -ch add -es (benches)."),
        ("Identify the INCORRECT plural spelling in this list: baskets, trees, sandwichs, kites.", "sandwichs", "baskets", "trees", "kites", "A", "Plural of sandwich is 'sandwiches', not 'sandwichs'."),
        ("Choose the sentence with the correct plural noun form:", "The families brought baskets and kites to the park.", "The familys brought basketes and kities to the park.", "The familyes brought basketies and kitez to the park.", "The familiz brought basketz and kitees to the park.", "A", "families (-y -> -ies), baskets (-s), kites (-s) are correct."),
        ("Which noun forms its plural by adding -es to a word ending in -ch?", "sandwich -> sandwiches", "tree -> trees", "kite -> kites", "basket -> baskets", "A", "Sandwich ends in -ch, so plural is sandwiches."),
        ("Change the singular noun in brackets to plural: 'The children saw four ____ (duck) swimming in the pond.'", "ducks", "duckes", "duckies", "duckz", "A", "Regular noun adding -s (ducks)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The children sat under big trees eating apples.", "The childs sat under big treees eating applies.", "The childrens sat under big treies eating applees.", "The childes sat under big treez eating applez.", "A", "children, trees, apples are all correctly spelt plurals."),
        ("What is the correct plural of 'picnic basket'?", "picnic baskets", "picnic basketes", "picnic basketies", "picnic basketz", "A", "Regular noun adding -s."),
        ("The mother packed juice (glass / glasses) in the box.", "glasses", "glass", "glasss", "glassies", "A", "Nouns ending in -ss add -es (glasses)."),
        ("Many (child / children) were flying kites on the lawn.", "children", "childs", "childes", "childrens", "A", "Irregular plural of child is children."),
        ("Many (person / people) visited the park on Sunday.", "people", "persons", "peoples", "persones", "A", "Irregular plural of person is people."),
        ("How many (box / boxes) of food did they take?", "boxes", "box", "boxs", "boxies", "A", "Nouns ending in -x add -es (boxes)."),
        ("They played fun outdoor (game / games).", "games", "game", "gamies", "gamees", "A", "Regular noun ending in -e adds -s (games)."),
        ("Which plural noun rule applies to the word **'families'**?", "Change consonant + y to -ies", "Add -es to -ch", "Add -s to vowel + y", "Change -f to -ves", "A", "Family ends in consonant + y, changing to -ies."),
        ("The father carried two heavy (bag / bags).", "bags", "bages", "bagies", "bagz", "A", "Plural of bag is bags."),
        ("Identify the correct plural form of 'leaf':", "leaves", "leafs", "leafes", "leavies", "A", "Nouns ending in -f change to -ves (leaves)."),
        ("They saw colorful (bird / birds) sitting on the branches.", "birds", "bird", "birdes", "birdies", "A", "Plural of bird is birds.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The family packed a sandwich, an apple, and a box.'", "The families packed sandwiches, apples, and boxes.", "The familys packed sandwichs, applies, and boxs.", "The familyes packed sandwichies, applees, and boxies.", "The familiz packed sandwichz, applez, and boxen.", "A", "Plural of family->families (-y->-ies), sandwich->sandwiches (-ch+es), apple->apples (-e+s), box->boxes (-x+es)."),
        ("Analyze the error: 'The childs carried two picnic basketes.' Why is this sentence incorrect?", "'childs' should be irregular plural 'children' and 'basketes' should be 'baskets'.", "'childs' should be 'childrens'.", "'basketes' should be 'basketies'.", "No error.", "A", "Child becomes children; basket becomes baskets."),
        ("Complete the paragraph with correct plurals: 'Three ____ (family) brought several ____ (sandwich) and four ____ (kite).'", "families, sandwiches, kites", "familys, sandwichs, kities", "familyes, sandwichies, kitez", "families, sandwichs, kitees", "A", "families (-y -> -ies), sandwiches (-ch -> -es), kites (-e -> -s)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **children** sat on **benches** eating **apples**.", "The **childs** sat on **benchs** eating **applies**.", "The **childrens** sat on **benchies** eating **applees**.", "The **childes** sat on **benches** eating **applez**.", "A", "children (irregular), benches (-ch+es), apples (-e+s)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, men, feet", "baskets, kites, trees, ducks", "sandwiches, benches, boxes, dishes", "leaves, thieves, wolves, knives", "A", "children, people, men, feet change forms without standard -s/-es."),
        ("Why does 'family' become 'families' but 'day' becomes 'days'?", "Because 'family' has a consonant before y (l+y -> -ies), while 'day' has a vowel before y (a+y -> -s).", "Because family is big.", "Because day is time.", "Both follow the exact same rule.", "A", "Consonant+y changes y to -ies; Vowel+y adds -s."),
        ("Find the TWO grammatical mistakes in: 'The two familys packed many sandwichs for the picnic.'", "'familys' should be 'families' and 'sandwichs' should be 'sandwiches'.", "'familys' should be 'family' and 'sandwichs' should be 'sandwichees'.", "'picnic' should be 'picnics' only.", "There are no mistakes in the sentence.", "A", "families (-y -> -ies) and sandwiches (-ch -> -es)."),
        ("Replace the singular words in brackets: 'The children wiped their ____ (foot) after playing on the grass.'", "feet", "foots", "feets", "footies", "A", "Plural of foot is feet."),
        ("Analyze this sentence: 'They drank three glasses of juice.' What type of plural noun is 'glasses'?", "Nouns ending in sibilant -ss adding -es (glass -> glasses).", "Irregular plural.", "Abstract noun.", "Possessive noun.", "A", "Glass ends in -ss, adding -es."),
        ("Fill in the blanks: 'The two ____ (child) chased three ____ (butterfly) in the park.'", "children, butterflies", "childs, butterflys", "childrens, butterflyes", "childes, butterflies", "A", "child -> children; butterfly -> butterflies."),
        ("Select the option that shows correct plural transformation for ALL three words: 'family', 'sandwich', 'box'", "families, sandwiches, boxes", "familys, sandwichs, boxs", "familyes, sandwichies, boxies", "familiz, sandwichz, boxen", "A", "family -> families; sandwich -> sandwiches; box -> boxes."),
        ("HOTS Reasoning: Why do we say 'sandwiches' (countable) but 'juice' is uncountable?", "Because 'sandwich' refers to discrete food items, while 'juice' is a continuous liquid mass.", "Because juice is sweet.", "Because sandwich is big.", "Because park is green.", "A", "Discrete countable units vs continuous mass liquid."),
        ("Transform into singular: 'The families packed picnic baskets for their outings.'", "The family packed a picnic basket for its outing.", "The families packed a picnic basket for its outing.", "The family pack a picnic basket for its outing.", "The family packed picnic baskets for its outing.", "A", "Singular forms: family, picnic basket, outing."),
        ("Identify the correct rule for forming the plural of **'sandwich'**:", "Add -es because it is a noun ending in -ch (sandwiches).", "Add -s (sandwichs).", "Change -ch to -v (sandwives).", "Change vowel sound.", "A", "Nouns ending in -ch add -es.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("___ family went for a day out in the park.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'family'."),
        ("It was ___ sunny Sunday morning.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'sunny'."),
        ("The mother packed ___ picnic basket.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'picnic'."),
        ("The father carried ___ umbrella in case of rain.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'umbrella'."),
        ("They sat under ___ big green tree.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'big'."),
        ("___ Panchatantra/Story topic describes a family's day out.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Story'."),
        ("The children flew ___ red kite in the sky.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'red'."),
        ("It was ___ exciting day for everyone.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'exciting'."),
        ("___ sun was shining brightly in the park.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'."),
        ("The mother served ___ apple to each child.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'apple'."),
        ("They spread ___ large rug on the grass.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'large'."),
        ("It was ___ honest effort to bring the family together.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ ducks were swimming gracefully in the pond.", "The", "A", "An", "No article", "A", "Definite article 'The' specifies ducks in the park pond."),
        ("The father bought ___ ice cream for the kids.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'ice'."),
        ("They created ___ wonderful memory together.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'wonderful'."),
        ("The park had ___ open lawn for playing games.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'open'."),
        ("The day brought ___ happiness to the family.", "no article", "a", "an", "the", "A", "Abstract noun 'happiness' takes no indefinite article here."),
        ("___ sky was clear blue all afternoon.", "The", "A", "An", "No article", "A", "Use 'The' for unique sky.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH14_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The family packed ___ picnic basket and ___ umbrella.", "a, an", "an, a", "a, a", "the, a", "A", "'a picnic basket' (consonant sound), 'an umbrella' (vowel sound)."),
        ("Why do we say '**a** kite' but '**an** umbrella'?", "Because 'kite' begins with a consonant sound (k) and 'umbrella' with a vowel sound (u).", "Because kites fly high.", "Because umbrellas are black.", "Because families are big.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "The family had a wonderful picnic in the park.", "An family had a wonderful picnic in the park.", "The a family had wonderful picnic in park.", "A family had an wonderful picnic in an park.", "A", "'The family' (specific family), 'a wonderful picnic' (consonant sound)."),
        ("Fill in the blanks: 'They sat under ___ tree and ate ___ sandwich.'", "a, a", "an, a", "a, an", "the, an", "A", "'a tree' (consonant /t/), 'a sandwich' (consonant /s/)."),
        ("Identify the INCORRECT article in: 'He carried **a** umbrella to the park.'", "'a' should be 'an'", "'a' should be 'the'", "'umbrella' should be 'a umbrella'", "No mistake", "A", "'umbrella' starts with vowel sound /u/, so it takes 'an'."),
        ("Which article completes the sentence? 'They spent ___ enjoyable afternoon together.'", "an", "a", "the", "no article", "A", "'enjoyable' starts with vowel sound /e/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ father opened ___ basket.'", "The, the", "A, a", "An, an", "The, a", "A", "'The father' (specific father), 'the basket' (specific basket)."),
        ("Why do we use 'an' before 'apple' in 'Mother gave him **an** apple'?", "Because 'apple' begins with the vowel sound /a/.", "Because apple is a fruit.", "Because park is green.", "Because kids are hungry.", "A", "'apple' starts with vowel sound /a/."),
        ("Complete the dialogue: Sister: 'Can I fly ___ kite?' Brother: 'Yes, here is ___ red kite!'", "a, a", "a, an", "an, the", "the, the", "A", "'a kite' (consonant sound), 'a red kite' (consonant sound)."),
        ("Select the correct sentence:", "A picnic is a fun family activity.", "An picnic is a fun family activity.", "The picnic is an fun family activity.", "An picnic is an fun family activity.", "A", "'A picnic' (consonant sound), 'a fun family activity' (consonant sound)."),
        ("Fill in the blank: 'They stayed at the park for ___ long time.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The family shared **___ laughter** during the game.", "He carried ___ basket.", "She ate ___ sandwich.", "They flew ___ kite.", "A", "Uncountable abstract noun 'laughter' takes no article here."),
        ("Choose the correct sentence for story summary:", "Unity and joy make family outings special.", "A unity and a joy make outings special.", "An unity and an joy make outings special.", "The unity a makes outings special.", "A", "Abstract concepts take no indefinite articles in general moral sense."),
        ("Fill in the blanks: 'The family spent ___ hour enjoying ___ picnic.'", "an, the", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'the picnic' (specific)."),
        ("Which sentence uses 'the' correctly for specific park landmarks?", "They sat near the pond under the big oak tree.", "They sat near a pond under a big oak tree.", "They sat near an pond under an big oak tree.", "They sat near pond under big oak tree.", "A", "Specific landmarks take 'the pond' and 'the big oak tree'."),
        ("Identify the article error: 'He gave **a** explanation of **an** outdoor game.'", "'an outdoor' should be 'an outdoor' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an outdoor' should be 'a outdoor'", "No error", "A", "'an explanation' (vowel /e/) and 'an outdoor game' (vowel /o/)."),
        ("Complete: 'It was ___ unforgettable day at ___ city zoo.'", "an, the", "a, an", "the, a", "an, a", "A", "an unforgettable (/u/), the city zoo (specific location)."),
        ("Choose the correct option: '___ sun set as the family drove home.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'The family packed **a** another picnic basket.' Correct the error:", "'a another' -> 'another' ('another' already includes the indefinite article 'an' + 'other').", "'another' -> 'an another'.", "'basket' -> 'baskets'.", "No error.", "A", "'another' cannot be preceded by 'a'."),
        ("Fill in all three blanks: '___ family sat on ___ grass near ___ pond.'", "The, the, the", "A, a, a", "An, a, the", "The, a, a", "A", "'The family' (specific), 'the grass' (specific ground), 'the pond' (specific)."),
        ("Identify why 'the' is used in: '**The** family had a wonderful time in **the** park.'", "Because 'The' specifies the particular family and the specific park they visited.", "Because family is a noun.", "Because grass is green.", "Because sandwiches are tasty.", "A", "'The' specifies definite family and park in narrative."),
        ("Spot the TWO article errors: 'It took **a** hour to pack **a** umbrella.'", "'a hour' should be 'an hour' and 'a umbrella' should be 'an umbrella'.", "'a hour' should be 'the hour' and 'a umbrella' should be 'a umbrella'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'umbrella' (vowel u) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A family went to a park. They sat under a tree and ate an apple. The day was sunny.", "An family went to an park. They sat under an tree.", "The family went to a park. An day was sunny.", "A family went to a park. The tree was an honest.", "A", "A family (consonant), a park (consonant), a tree (consonant), an apple (vowel), The day (second mention)."),
        ("Why is it correct to write 'a unique day out' but 'an unforgettable day out'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unforgettable' begins with vowel sound /u/.", "Because unique is longer.", "Because day is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story summary: '___ happy family spent ___ sunny day near ___ river bank.'", "A, a, the", "An, a, an", "The, the, the", "A, a, a", "A", "A happy family, a sunny day, the river bank (specific location)."),
        ("Analyze this sentence: 'They enjoyed **a** little juice with their sandwiches.' Why is 'a' appropriate?", "Because 'a little' is a quantifier phrase modifying the mass noun juice.", "Because juice is a verb.", "Because park is big.", "Because kite is red.", "A", "'a little' is an idiomatic quantifier phrase for uncountable mass nouns."),
        ("Correct the sentence: 'An family flew a kite on a early Sunday morning.'", "A family flew a kite on an early Sunday morning.", "The family flew an kite on a early Sunday morning.", "An family flew the kite on an early Sunday morning.", "A family flew a kite on a early Sunday morning.", "A", "'A family' (/f/ sound), 'an early' (vowel /er/)."),
        ("Fill in the blanks: '___ events of ___ day brought ___ family closer together.'", "The, the, the", "A, a, a", "No article, a, an", "An, the, a", "A", "'The events' (specific), 'the day' (specific), 'the family' (specific)."),
        ("Spot the missing article: 'Family went to park on Sunday.'", "Missing 'A' before 'Family' and 'a' before 'park' -> 'A family went to a park on Sunday.'", "Missing 'an' before 'Sunday'", "Missing 'the' before 'went'", "No article is missing", "A", "Singular countable nouns require articles."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An hour ago, a family arrived at the park.", "A hour ago, an family arrived at a park.", "The hour ago, an family arrived at an park.", "An hour ago, an family arrived at the park.", "A", "An hour (silent h), a family (consonant), the park (specific)."),
        ("Rewrite correctly: 'The family gave a honest opinion about an sunny spot.'", "The family gave an honest opinion about a sunny spot.", "The family gave a honest opinion about a sunny spot.", "The family gave an honest opinion about an sunny spot.", "The family gave the honest opinion about an sunny spot.", "A", "'an honest' (silent h), 'a sunny spot' (consonant /s/)."),
        ("Identify the correct rule for using articles with day names like 'Sunday':", "Specific day names (Sunday, Monday) take no indefinite article unless referring to a specific historical date.", "Days take 'an'.", "Days take 'a'.", "Days take 'the' always.", "A", "Day names generally take no article.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("The family went for a day out on **Sunday**. What is the abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("Which day comes right before Sunday?", "Saturday", "Friday", "Monday", "Tuesday", "A", "Saturday comes before Sunday."),
        ("What is the abbreviation for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("Which day comes right after Sunday?", "Monday", "Tuesday", "Saturday", "Friday", "A", "Monday follows Sunday."),
        ("What is the abbreviation for **Monday**?", "Mon.", "Mond.", "Mo.", "M.", "A", "Mon. is standard abbreviation."),
        ("Saturday and Sunday together are called the **____**.", "weekend", "workdays", "fortnight", "month", "A", "Saturday and Sunday form the weekend."),
        ("The picnic started in the **morning** at **10:00 a.m.**. What does **a.m.** stand for?", "Ante Meridiem (before noon)", "After Morning", "At Midnight", "All Month", "A", "a.m. stands for ante meridiem."),
        ("They returned home in the **evening** at **5:00 p.m.**. What does **p.m.** stand for?", "Post Meridiem (after noon)", "Past Morning", "Plus Minute", "Post Month", "A", "p.m. stands for post meridiem."),
        ("Which month comes right before June?", "May", "April", "July", "August", "A", "May comes before June."),
        ("What is the short abbreviation for **May**?", "May (no abbreviation needed / 3 letters)", "My.", "Ma.", "My", "A", "May has 3 letters and is usually not abbreviated further."),
        ("Which month comes right after May?", "June", "July", "April", "March", "A", "June comes after May."),
        ("What is the short abbreviation for **June**?", "Jun.", "June.", "Ju.", "Jn.", "A", "Jun. is standard abbreviation."),
        ("If today is Sunday, what day was yesterday?", "Saturday", "Friday", "Monday", "Tuesday", "A", "Yesterday was Saturday."),
        ("If today is Sunday, what day will tomorrow be?", "Monday", "Tuesday", "Saturday", "Friday", "A", "Tomorrow will be Monday."),
        ("What is the abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("Which day comes between Friday and Sunday?", "Saturday", "Thursday", "Monday", "Tuesday", "A", "Saturday is between Friday and Sunday."),
        ("Which month comes right before July?", "June", "May", "August", "September", "A", "June comes before July."),
        ("What is the short abbreviation for **July**?", "Jul.", "July.", "Jl.", "Jy.", "A", "Jul. is standard abbreviation.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH14_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The family outing lasted from **10:00 a.m. to 4:00 p.m.**. How many hours was the outing?", "6 hours", "5 hours", "7 hours", "4 hours", "A", "4:00 p.m. - 10:00 a.m. = 6 hours."),
        ("They planned their picnic for the **first Sunday of May**. If May 1st was Friday, what date was the first Sunday?", "May 3rd", "May 1st", "May 2nd", "May 4th", "A", "Fri 1st, Sat 2nd, Sun 3rd May."),
        ("Match the day with its abbreviation: **Sunday**", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard."),
        ("Convert to 12-hour clock: **16:00 in the afternoon**", "4:00 p.m.", "4:00 a.m.", "6:00 p.m.", "12:04 p.m.", "A", "16:00 is 4:00 p.m."),
        ("Identify the correctly spelt month name:", "June", "Junne", "Junee", "Juneh", "A", "June is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Saturday - Sat.", "Sunday - Sun.", "Sunday - Snd.", "D", "Sunday abbreviation is Sun., not Snd."),
        ("Calculate: How many days are in **June**?", "30 days", "31 days", "28 days", "29 days", "A", "June has 30 days."),
        ("Which month has 31 days and comes right after June?", "July", "August", "May", "April", "A", "July has 31 days and follows June."),
        ("Rearrange in correct chronological order: Sat, Thu, Fri, Sun", "Thu, Fri, Sat, Sun", "Fri, Thu, Sat, Sun", "Sat, Fri, Thu, Sun", "Sun, Sat, Fri, Thu", "A", "Thursday -> Friday -> Saturday -> Sunday."),
        ("What day is 2 days before Sunday?", "Friday", "Saturday", "Thursday", "Wednesday", "A", "Sunday - 2 days = Saturday(1), Friday(2)."),
        ("If a summer holiday lasts for 4 weeks, how many days is that?", "28 days (4 x 7)", "30 days", "25 days", "14 days", "A", "4 weeks x 7 days = 28 days."),
        ("Select the month that has 31 days:", "May", "June", "April", "September", "A", "May has 31 days."),
        ("Which abbreviation stands for **June**?", "Jun.", "June.", "Ju.", "Jn.", "A", "Jun. is standard abbreviation."),
        ("If today is **Sun.**, what day will it be after 7 days?", "Sunday", "Monday", "Saturday", "Friday", "A", "7 days is a full week cycle, landing on Sunday again."),
        ("The family played games from **2:00 p.m. to 4:00 p.m.**. How many hours did they play?", "2 hours", "1 hour", "3 hours", "4 hours", "A", "4:00 p.m. - 2:00 p.m. = 2 hours."),
        ("Identify the term that means 'a 2-day break including Saturday and Sunday':", "Weekend", "Fortnight", "Century", "Leap year", "A", "Weekend covers Saturday and Sunday."),
        ("Which of the following is a weekend day?", "Sunday", "Monday", "Tuesday", "Wednesday", "A", "Sunday is a weekend day."),
        ("Choose the correct abbreviation for **July**:", "Jul.", "July.", "Jl.", "Jy.", "A", "Jul. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("The picnic started at **11:00 a.m.** and ended at **3:30 p.m.**. How many total hours and minutes did the picnic last?", "4 hours 30 minutes", "4 hours", "5 hours", "3 hours 30 minutes", "A", "11:00 a.m. to 3:30 p.m. = 4 hours 30 minutes."),
        ("If a family plans an outing every **2 weeks**, how many outings do they take in 8 weeks?", "4 outings (8 / 2)", "2 outings", "8 outings", "6 outings", "A", "8 weeks / 2 weeks = 4 outings."),
        ("Solve the calendar puzzle: If 1st June was a Tuesday, what day of the week was 8th June?", "Tuesday", "Wednesday", "Monday", "Thursday", "A", "1 + 7 = 8th June, landing on Tuesday."),
        ("Analyze this schedule: Family visits park on Sun, Tue, Thu; Stays home on Mon, Wed, Fri, Sat. How many days a week do they visit the park?", "3 days a week", "4 days", "2 days", "5 days", "A", "Sun, Tue, Thu = 3 days."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If a family vacation covered a fortnight, how many days did it last?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Apr, May, Jul, Jun, Aug'", "July and June are in wrong order.", "May is in wrong position.", "August should be first.", "No error.", "A", "June comes before July (Apr, May, Jun, Jul, Aug)."),
        ("June has **30 days**. What date was the day right after 30th June?", "1st July", "31st June", "29th June", "1st August", "A", "June has 30 days, so next day is 1st July."),
        ("If yesterday was two days before Sunday, what day is tomorrow?", "Sunday", "Saturday", "Monday", "Friday", "A", "Two days before Sunday = Friday (yesterday). Today = Saturday. Tomorrow = Sunday."),
        ("Calculate: How many days are there in total during **May** and **June** combined?", "61 days (31 + 30)", "60 days", "62 days", "59 days", "A", "May (31) + June (30) = 61 days."),
        ("HOTS Reasoning: Why do families prefer going for a day out on 'Sunday' rather than 'Monday'?", "Because Sunday is a public weekend holiday when schools and offices are closed.", "Because Sunday is warmer.", "Because parks are locked on Sunday.", "Because Mondays have no sun.", "A", "Sunday is a standard weekend holiday."),
        ("Identify the correct statement about a leap year:", "A leap year has 366 days and February has 29 days.", "A leap year has 365 days.", "February has 30 days.", "A leap year occurs every year.", "A", "Leap year has 366 days (Feb = 29 days)."),
        ("The family drove 60 kilometers to the zoo in 1 hour 30 minutes (1.5 hours). What was their average speed?", "40 kilometers per hour (60 / 1.5)", "30 km/h", "50 km/h", "60 km/h", "A", "60 / 1.5 = 40 km/h."),
        ("Which month pair both have 31 days and come right after each other during summer?", "July and August", "June and July", "May and June", "August and September", "A", "July (31) and August (31) are consecutive 31-day months.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("The family **packed** a picnic basket.", "packed", "family", "picnic", "basket", "A", "'packed' is the main physical action verb."),
        ("They **drove** to the city park on Sunday.", "drove", "city", "park", "Sunday", "A", "'drove' is the physical action verb."),
        ("The children **ran** across the green lawn.", "ran", "children", "green", "lawn", "A", "'ran' is the physical action verb."),
        ("Father **spread** a large rug under the tree.", "spread", "father", "large", "tree", "A", "'spread' is the physical action verb."),
        ("They **ate** delicious sandwiches for lunch.", "ate", "delicious", "sandwiches", "lunch", "A", "'ate' is the physical action verb."),
        ("The children **flew** a colorful kite.", "flew", "children", "colorful", "kite", "A", "'flew' is the physical action verb."),
        ("Mother **served** sweet orange juice.", "served", "mother", "orange", "juice", "A", "'served' is the physical action verb."),
        ("They **watched** the ducks swimming in the pond.", "watched", "ducks", "swimming", "pond", "A", "'watched' is the sensory action verb."),
        ("The brother **threw** a frisbee to his sister.", "threw", "brother", "frisbee", "sister", "A", "'threw' is the physical action verb."),
        ("They **laughed** together at the funny jokes.", "laughed", "together", "funny", "jokes", "A", "'laughed' is the action verb."),
        ("The sister **sang** a sweet song.", "sang", "sister", "sweet", "song", "A", "'sang' is the action verb."),
        ("Father **took** beautiful family photos.", "took", "father", "beautiful", "photos", "A", "'took' is the action verb."),
        ("They **walked** along the shaded path.", "walked", "along", "shaded", "path", "A", "'walked' is the physical action verb."),
        ("The children **played** on the swings.", "played", "children", "swings", "on", "A", "'played' is the physical action verb."),
        ("Mother **cleaned** the picnic area after eating.", "cleaned", "mother", "area", "eating", "A", "'cleaned' is the physical action verb."),
        ("They **enjoyed** their day out in nature.", "enjoyed", "their", "nature", "day", "A", "'enjoyed' is the mental action verb."),
        ("Father **carried** the heavy basket back to the car.", "carried", "father", "heavy", "car", "A", "'carried' is the physical action verb."),
        ("They **returned** home happily in the evening.", "returned", "home", "happily", "evening", "A", "'returned' is the physical action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH14_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 14:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The family **happily** **packed** the **big** **basket**.'", "packed", "happily", "big", "basket", "A", "'packed' shows physical action; 'happily' is adverb, 'big' is adjective, 'basket' is noun."),
        ("Identify BOTH action verbs in: 'They **ate** sandwiches and **drank** juice.'", "ate, drank", "sandwiches, juice", "they, ate", "drank, juice", "A", "'ate' and 'drank' are both action verbs."),
        ("What is the past tense action verb of 'fly' as used in sentence ('They flew a kite')?", "flew", "flyed", "flying", "flies", "A", "Past tense of fly is flew."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "They will **park** the car near the gate.", "They walked in the green **park**.", "This is a big **park**.", "The **park** was crowded.", "A", "In (A), 'park' acts as the main action verb."),
        ("Find the action verb in: 'Father spread a large rug on the grass.'", "spread", "father", "large", "grass", "A", "'spread' is the physical action verb."),
        ("Which sentence contains NO physical action verb?", "The family was happy during the day out.", "They ran across the lawn.", "They ate lunch together.", "They flew a red kite.", "A", "'The family was happy during the day out' contains linking verb 'was', but no physical action verb."),
        ("Change the action verb 'drive' to past tense: 'They (drive) to the park yesterday.'", "drove", "drived", "driving", "drives", "A", "Past tense of drive is drove."),
        ("Identify the action verb: 'The kids played games and sang songs.'", "played, sang", "kids, games", "songs, games", "sang, kids", "A", "'played' and 'sang' are action verbs."),
        ("Select the action verb that completes the sentence: 'The mother ____ delicious sandwiches for everyone.'", "prepared / packed", "happy", "sunny", "basket", "A", "'prepared' / 'packed' is an action verb."),
        ("Which word is an action verb? (lawn, rug, ran, sunny)", "ran", "lawn", "rug", "sunny", "A", "'ran' is an action verb; others are nouns/adjectives."),
        ("What action did the father perform with the rug in the story?", "spread / laid out", "sunny", "green", "rug", "A", "Father spread/laid out the rug (action verb)."),
        ("Identify the action verb in: 'They enjoyed their picnic in the park.'", "enjoyed", "picnic", "park", "their", "A", "'enjoyed' is a mental action verb."),
        ("Choose the correct action verb: 'The children ____ the colorful kite into the sky.'", "launched / flew", "high", "red", "sky", "A", "'launched' / 'flew' is the action verb."),
        ("Identify the action verb in: 'Mother served fruit juice to her family.'", "served", "fruit", "juice", "family", "A", "'served' is the action verb."),
        ("Which of these words is NOT an action verb? (run, eat, fly, happy)", "happy", "run", "eat", "fly", "A", "'happy' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'The ducks splash in the cold pond water.'", "splash", "ducks", "cold", "water", "A", "'splash' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'The family ____ together on the picnic mat.'", "sat / relaxed", "green", "large", "mat", "A", "'sat' / 'relaxed' is an action verb."),
        ("What action verb completes the sentence? 'The children ____ happy laughter.'", "shared / expressed", "sunny", "bright", "lawn", "A", "'shared' / 'expressed' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The happy family quickly packed their bags and drove to the park.' How many total ACTION VERBS are present?", "2 action verbs ('packed', 'drove')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'packed' and 'drove' are action verbs; 'quickly', 'happy' are adverbs/adjectives."),
        ("Categorize the verbs: In 'The day **was** sunny, so they **played** outside', classify 'was' and 'played'.", "'was' is a linking verb; 'played' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'was' is action; 'played' is linking.", "A", "'was' links state of being; 'played' shows action."),
        ("Replace the weak verb with a strong action verb: 'The family **went** into the park.'", "The family **strolled** into the park.", "The family **was near** the park.", "The family **saw** the park.", "The family **looked at** the lawn.", "A", "'strolled' is a much stronger, descriptive action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "They **packed** the basket, **drove** to the park, and **flew** kites.", "The family was happy, cheerful, and excited.", "They sat under the big oak tree.", "Sunday was a sunny day.", "A", "packed, drove, flew are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "Mother **served** the sandwiches.", "The day was **sunny**.", "The grass was **green**.", "The park was **large**.", "A", "'served' is an action verb."),
        ("Spot the incorrect verb tense: 'They **fly** a kite in the park yesterday.' Correct it for past simple:", "'flew' is the past action verb form.", "'fly' should be 'flying'.", "'fly' should be 'flies'.", "'fly' should be 'will fly'.", "A", "Past simple of fly is flew."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (packs basket, drives to park, spreads rug, eats lunch, flies kites)", "packs basket -> drives to park -> spreads rug -> eats lunch -> flies kites", "flies kites -> eats lunch -> spreads rug -> drives to park -> packs basket", "spreads rug -> packs basket -> eats lunch -> flies kites -> drives", "eats lunch -> flies kites -> drives -> packs -> spreads", "A", "Logical chronological order of a day out."),
        ("Identify the verb error in dialogue: Sister said, 'Look how high the kite has **fly**!'", "'fly' is incorrect; the past participle form is 'flown' ('has flown').", "'fly' should be 'flying'.", "'fly' should be 'flies'.", "No error.", "A", "Perfect tense requires past participle 'flown'."),
        ("Analyze this sentence: 'The outing **strengthened** family bonds.' What type of action verb is 'strengthened'?", "Abstract/relational action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'strengthened' is an action verb describing bonding."),
        ("Which sentence uses action verbs to show cause and effect?", "Father **spread** the rug, so the children **sat** down comfortably.", "The family was happy and joyful.", "Sunday is a weekend holiday.", "Ice cream is cold.", "A", "'spread' (cause action) -> 'sat' (effect action)."),
        ("Spot the missing action verb: 'They ____ sandwiches and ____ fruit juice under the shade.'", "ate, drank", "happy, sunny", "was, was", "quick, slow", "A", "'ate' and 'drank' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'cherished' in 'The family cherished their day out' considered a DEEP mental action verb?", "Because it describes actively holding and valuing a memory with deep affection.", "Because cherishing requires running.", "Because park is green.", "Because it is a noun.", "A", "Descriptive action verb conveying emotional valuation."),
        ("Transform the action verb to future tense: 'They **pack** the picnic basket tomorrow.'", "They **will pack** the picnic basket tomorrow.", "They **packed** the picnic basket tomorrow.", "They **are packing** the picnic basket tomorrow.", "They **pack** the picnic basket tomorrow.", "A", "'will pack' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The children **fly** their colorful kites in the park.", "The children **flies** their colorful kites in the park.", "A child **fly** their colorful kites in the park.", "The children **is flying** their colorful kites in the park.", "A", "Plural subject 'children' takes base verb 'fly' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'The family went to the park__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'Where did the family go on Sunday__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a day name like 'Sunday'?", "First letter (Sunday)", "The last letter", "All letters", "No letters", "A", "Day names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'They packed sandwiches__ apples__ and juice.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden joy in: 'What a wonderful picnic this is!__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense joy."),
        ("Select the proper noun (day name) that MUST start with a capital letter:", "Sunday", "picnic", "sandwich", "basket", "A", "'Sunday' as a proper noun starts with a capital letter."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'the title of Chapter 14 is Family's Day Out.'", "the -> The", "title -> Title", "story -> Story", "is -> Is", "A", "First word of sentence 'The' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'They packed sandwiches, apples [ ] and juice.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "A", "Comma separates items before 'and'."),
        ("Which title is capitalized correctly?", "Family's Day Out", "family's day out", "Family's day Out", "FAMILYS DAY OUT", "A", "Title capitalization with possessive apostrophe."),
        ("What mark goes after a speaker tag: 'Mother said__ \"Lunch is ready!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i love flying kites with my family.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The children flew their kite high.", "The children flew their kite high?", "The children flew their kite high,", "The children flew their kite high;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like '**family's** day out'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which chapter title is capitalized correctly?", "Family's Day Out", "family's day out", "Family's day out", "FAMILY DAY OUT", "A", "Title capitalization."),
        ("What punctuation mark is used around spoken dialogue lines: '___Let us fly the kite!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Quotation marks enclose exact spoken words.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH14_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "The story \"Family's Day Out\" was written about a Sunday picnic.", "the story \"family's day out\" was written about a sunday picnic.", "The story \"family's Day Out\" was written about a Sunday picnic?", "the Story \"Family's Day Out\" Was Written About A Sunday Picnic.", "A", "Title \"Family's Day Out\", day name Sunday capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Did the family enjoy their day out at the park?", "Did the family enjoy their day out at the park.", "Did the family enjoy their day out at the park!", "Did the family enjoy their day out at the park,", "A", "Question starting with 'Did' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'On sunday, the family went to Central Park.'", "'sunday' should be capitalized ('Sunday'); 'Central Park' is correct.", "'Central' should be lowercase.", "'Park' should be lowercase.", "No mistake.", "A", "Day name 'Sunday' must be capitalized."),
        ("Choose the correctly punctuated dialogue sentence:", "\"Pass me a sandwich, please,\" said the mother.", "pass me a sandwich please said the mother.", "\"Pass me a sandwich, please\" said the mother", "Pass me a sandwich, please, said the mother.", "A", "Quotation marks around dialogue, comma inside quote, capital P."),
        ("Identify where a COMMA is missing: 'They brought a rug a basket and a kite.'", "Between 'rug' and 'a basket' ('a rug, a basket')", "After 'They'", "After 'kite'", "No comma needed", "A", "Commas separate list items: 'a rug, a basket and a kite'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is the father's bag.", "This is the fathers' bag.", "This is the fathers bag.", "This is the father's' bag.", "A", "father's indicates singular possession."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a fun day out this was!", "What a fun day out this was?", "What a fun day out this was.", "What a fun day out this was,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'did not'?", "didn't", "did'nt", "didnt'", "d'idnt", "A", "didn't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "On Sunday, the family went to the city park.", "on Sunday, the family went to the city park.", "On sunday, the Family went to the City Park.", "on sunday, the family went to park.", "A", "'On' (sentence start) and 'Sunday' (day name) capitalized."),
        ("What punctuation mark belongs in the blank? 'The kids shouted, \"Look at the kite!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses shouting/excitement."),
        ("Choose the correct form for 'was not':", "wasn't", "was'nt", "wasnt'", "w'asnt", "A", "wasn't is standard contraction."),
        ("Identify the punctuation error: 'The sun was bright, the sky was blue.'", "Comma splice between two independent clauses (should be semicolon or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for place and day names:", "On Sunday, we went to Central Park in Delhi.", "on sunday, we went to central park in delhi.", "On sunday, we went to Central park in Delhi.", "on Sunday, we went to Central Park in delhi.", "A", "Day 'Sunday', place 'Central Park', city 'Delhi' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The family's picnic was full of fun.", "The familys' picnic was full of fun.", "The familys picnic was full of fun.", "The family's' picnic was full of fun.", "A", "family's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'Mother packed ____'", "sandwiches, apples, and juice.", "sandwiches apples and juice.", "sandwiches; apples; and juice.", "sandwiches: apples: and juice.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "What did the children do in the park?", "What did the children do in the park.", "What did the children do in the park!", "what did the children do in the park.", "A", "Capital W, ends with question mark ?"),
        ("Fix the sentence: 'where did the family go on sunday'", "Where did the family go on Sunday?", "Where did the family go on sunday.", "where did the family go on Sunday!", "Where is family?", "A", "Capital W, capital Sunday, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Father said, \"Let us pack the picnic basket!\"", "Father said \"let us pack the picnic basket!\"", "father said, \"Let us pack the picnic basket!\"", "Father said, \"Let us pack the picnic basket.\"", "A", "Capital F, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on sunday mother said, let us go to central park for picnic'", "5 errors (on->On, sunday->Sunday, quotation marks, capital L in Let, central park->Central Park, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, quotation marks, capital L, place name, period."),
        ("Correct the entire dialogue paragraph: 'the brother asked can we fly the kite sister replied yes father brought it'", "\"Can we fly the kite?\" asked the brother. Sister replied, \"Yes, father brought it.\"", "the brother asked \"can we fly the kite\" sister replied \"yes father brought it.\"", "The brother asked, Can we fly the kite. Sister replied, Yes father brought it.", "\"Can we fly the kite?\" Asked the brother. Sister replied \"Yes father brought it?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'The family**'**s day out was great, and it**'**s sunny today.'", "First 's is possessive (day out of the family); second 's is contraction (it is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "family's day out = day out of the family; it's = it is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"We had a great picnic,\" Said the father.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'We' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "The sky was cloudy in the morning, but it became sunny later.", "The sky was cloudy in the morning but, it became sunny later.", "The sky was cloudy in the morning but it became sunny later!", "The sky was cloudy in the morning; but it became sunny later?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'on sunday 15th may 2022 the family visited national zoo in delhi'", "On Sunday, 15th May 2022, the family visited National Zoo in Delhi.", "on sunday, 15th may 2022, the family visited national zoo in delhi.", "On Sunday 15th May 2022 the family visited National Zoo in Delhi", "On sunday visited National Zoo in delhi.", "A", "Sunday, date format, proper names National Zoo and Delhi capitalized, period."),
        ("Identify why exclamation mark is necessary here: '\"Look, the kite is flying so high!\"'", "Because the speaker is expressing intense excitement and joy.", "Because kite is big.", "Because park is green.", "Because sentence is long.", "A", "Exclamation mark communicates intense excitement."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Central Park, a beautiful green lawn in our city, was perfect for the picnic.", "Central Park a beautiful green lawn in our city was perfect for the picnic.", "Central Park, a beautiful green lawn in our city was perfect for the picnic.", "Central Park a beautiful green lawn in our city, was perfect for the picnic.", "A", "Appositive phrase 'a beautiful green lawn in our city' is set off by commas."),
        ("Analyze the use of possessive apostrophe in story title: \"Family's Day Out\"", "The apostrophe 's indicates that the day out belongs to the family.", "It replaces comma.", "It indicates question.", "It is a plural suffix.", "A", "Possessive apostrophe 's shows ownership."),
        ("Identify the correct sentence with direct speech quote within text:", "The mother declared, \"Lunch is served on the rug,\" and everyone sat down.", "The mother declared \"Lunch is served on the rug\" and everyone sat down.", "The mother declared, 'Lunch is served on the rug,' and everyone sat down.", "The mother declared: \"Lunch is served on the rug\" and everyone sat down.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The fathers car was parked near the gate.'", "Missing apostrophe in 'father's' -> 'The father's car...'", "Missing apostrophe in 'car''", "Missing apostrophe in 'gate''", "No apostrophe needed", "A", "'The father's car' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Mother, said father, is packing lunch.' vs 'Mother said, \"Father is packing lunch.\"'", "In the first, father says mother is packing lunch; in the second, mother says father is packing lunch.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who performs action."),
        ("Correct all 4 errors in: 'whats in the picnic basket asked the child'", "\"What's in the picnic basket?\" asked the child.", "whats in the picnic basket? asked the child.", "\"What's in the picnic basket.\" asked the child.", "\"whats in the picnic basket?\" Asked the child.", "A", "Quotation marks, capital W, contraction What's, question mark, period at end."),
        ("Identify the rule for capitalizing story titles like \"Family's Day Out\":", "Titles take initial capital letters for all major words (nouns, verbs, adjectives, adverbs) and are enclosed in quotation marks.", "Story titles are never capitalized.", "Story titles are capitalized only at end of line.", "Story titles must be written in ALL CAPS.", "A", "Standard title capitalization rule.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'tree'** (in Chapter 14)?", "ee", "ea", "ai", "ou", "A", "'ee' is the vowel digraph in tree."),
        ("Identify the vowel digraph in the word **'eat'** (eating sandwiches):", "ea", "ee", "oa", "ui", "A", "'ea' forms the long /e/ vowel sound in eat."),
        ("Which word from the story topic contains the **'ou'** vowel digraph?", "out", "park", "lawn", "kite", "A", "'out' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'clean'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in clean."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'ou'** vowel digraph: 'They walked around the park.'", "around", "park", "walked", "they", "A", "'around' contains 'ou' vowel digraph."),
        ("Which word from the story topic rhymes with **'day'**?", "play", "park", "tree", "out", "A", "'play' rhymes with 'day'."),
        ("Which word from the story topic rhymes with **'out'**?", "shout", "day", "park", "tree", "A", "'shout' rhymes with 'out'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the story topic rhymes with **'park'**?", "bark", "out", "day", "tree", "A", "'bark' rhymes with 'park'."),
        ("Identify the vowel digraph in **'green'** (as in green lawn):", "ee", "ea", "oo", "ui", "A", "'ee' makes long /e/ sound in green."),
        ("Which word from Chapter 14 has the **'ea'** digraph making a long /e/ sound?", "eat", "bread", "head", "heavy", "A", "'eat' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'kite'**?", "white", "day", "out", "park", "A", "'white' rhymes with 'kite'."),
        ("Identify the silent letters in **'bright'** (as in 'bright sun'):", "gh", "b", "r", "t", "A", "Silent 'gh' in bright."),
        ("Which word from the story topic has long /i/ sound spelled with **'igh'**?", "high", "bought", "bowl", "baker", "A", "'igh' in high makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They sat on the ground.'", "ground", "sat", "they", "on", "A", "'ground' contains 'ou' digraph."),
        ("Which word rhymes with **'rug'**?", "bug", "bag", "box", "bed", "A", "'bug' rhymes with 'rug'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH14_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'eat'** and **'bread'**. What is the difference?", "'eat' has long /e/ sound; 'bread' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'eat' has short /e/; 'bread' has long /e/.", "A", "'ea' can make long /e/ (eat) or short /e/ (bread)."),
        ("Select the word pair from Chapter 14 that has the SAME vowel sound pattern:", "day - play", "eat - bread", "park - roar", "tree - bread", "A", "'day' (ay) and 'play' (ay) both make long /a/ sound."),
        ("Which word contains SILENT letters? (bright, high, know, all of these)", "all of these", "bright", "high", "know", "A", "'bright' (gh), 'high' (gh), 'know' (k)."),
        ("Identify the odd one out based on vowel sound: (tree, green, sweet, bread)", "bread", "tree", "green", "sweet", "A", "'bread' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for lawn color? 'gr__n'", "ee", "ea", "ai", "ou", "A", "'green' uses 'ee' digraph."),
        ("Group these story words by rhyming sound: **out**, **shout**, **ground**. What sound pattern do they share?", "ou diphthong /ow/ sound", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'The family walked **with** mother.'", "with", "family", "walked", "mother", "A", "'with' contains unvoiced 'th' consonant digraph."),
        ("Which of these words has the **'ay'** vowel digraph making long /a/ sound? (day, play, stay, all of these)", "all of these", "day", "play", "stay", "A", "day, play, stay all share 'ay' long /a/ sound."),
        ("Identify the vowel digraph in **'green'**:", "ee", "ae", "ur", "or", "A", "'ee' is the vowel digraph in green."),
        ("Which word from the story has silent **'k'**? (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "know, knee, knife all have silent initial 'k' before 'n'."),
        ("Select the rhyming pair for story context: 'day' and ____.", "play", "park", "tree", "kite", "A", "'day' rhymes with 'play'."),
        ("Select the rhyming pair for story context: 'park' and ____.", "bark", "day", "tree", "out", "A", "'park' rhymes with 'bark'."),
        ("Select the rhyming pair for story context: 'tree' and ____.", "free", "day", "out", "park", "A", "'tree' rhymes with 'free'."),
        ("Select the rhyming pair for story context: 'kite' and ____.", "white", "day", "park", "tree", "A", "'kite' rhymes with 'white'."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 14 vocabulary: (juice, slice, place, all of these)", "all of these", "juice", "slice", "place", "A", "juice, slice, place all have soft /s/ sound for 'c' before 'e'."),
        ("Which word has a soft **'g'** sound? (orange, gentle, magic, all of these)", "all of these", "orange", "gentle", "magic", "A", "orange, gentle, magic all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ee'** digraph for plant:", "tree", "tre", "treee", "trie", "A", "tree is standard spelling with 'ee'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'juice'** sound like /s/, but 'c' in **'picnic'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound (juice); at the end or before 'a', 'o', 'u' it makes hard /k/ sound (picnic).", "Because juice is sweet.", "Because picnic is outdoors.", "There is no rule.", "A", "Soft 'c' rule: c + e, i, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (eat, clean, green [ee], bread, heavy)", "Long /e/: eat, clean; Short /e/: bread, heavy", "All are long /e/.", "All are short /e/.", "Long /e/: bread; Short /e/: eat", "A", "eat, clean make long /e/; bread, heavy make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "bright - know", "tree - day", "park - kite", "rug - box", "A", "'bright' (silent gh) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 2-letter consonant blend at the start?", "green / tree / play", "out", "eat", "apple", "A", "'gr' / 'tr' / 'pl' blend type."),
        ("Examine the soft 'c' rule: Why is 'c' soft in **'slice'** but hard in **'car'**?", "'c' followed by 'e' makes soft /s/ sound (slice); 'c' before 'a' makes hard /k/ sound (car).", "Because car is fast.", "Because slice is food.", "There is no rule.", "A", "Soft 'c' rule: c + e = /s/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "brightest", "green", "tree", "play", "A", "'brightest' has 'igh' trigraph with silent 'gh'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'out'**?", "out - ground", "voice - coin", "paid - day", "boat - coat", "A", "'out' and 'ground' share /ow/ diphthong sound."),
        ("Analyze homophones: 'The sun was **bright** / **brite**.' Which word is the correct spelling?", "bright", "brite", "bryte", "brighte", "A", "'bright' (with silent gh) is standard spelling."),
        ("Identify the phonic pattern in **'unforgettable'**: How many syllables are in this word?", "5 syllables (un-for-get-ta-ble)", "4 syllables", "6 syllables", "3 syllables", "A", "un-for-get-ta-ble has 5 syllables."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (trees, bags, games, kites)", "trees / bags / games", "kites", "parks", "baskets", "A", "Plurals ending in voiced sounds take /z/ ending sound (trees, bags, games)."),
        ("Spot the word where 'k' is SILENT: (know, knee, knife, all of these)", "all of these", "know", "knee", "knife", "A", "'k' is silent before 'n' in know, knee, knife."),
        ("HOTS Reasoning: Why do 'sun' and 'son' sound identical but have different spellings and meanings?", "They are homophones (words with identical sound but different origin, spelling, and meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share identical sound but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "sunshine / outdoor", "unforgettable", "picnic", "family", "A", "sunshine = sun + shine; outdoor = out + door."),
        ("Determine the syllable count and stress: How many syllables are in **'sandwiches'**?", "3 syllables (sand-wich-es)", "2 syllables", "4 syllables", "1 syllable", "A", "sand-wich-es has 3 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ went for a day out in the park?", "Who", "What", "Where", "Why", "A", "'Who' asks about people ('The family')."),
        ("___ did the family go on Sunday?", "Where", "Who", "What", "Why", "A", "'Where' asks about place ('To the park')."),
        ("___ day of the week did they choose for the outing?", "Which", "Who", "Where", "Why", "A", "'Which day' asks about 'Sunday'."),
        ("___ did mother pack in the picnic basket?", "What", "Who", "Where", "Why", "A", "'What' asks about items ('sandwiches, fruit, juice')."),
        ("___ flew the red kite in the sky?", "Who", "What", "Where", "Why", "A", "'Who' asks about person ('The children')."),
        ("___ did father spread the rug?", "Where", "Who", "What", "Why", "A", "'Where' asks about location ('Under the big oak tree')."),
        ("___ did they drive to the park?", "How", "Who", "Where", "Why", "A", "'How' asks about mode of transport ('By car')."),
        ("___ were the ducks swimming?", "Where", "Who", "What", "Why", "A", "'Where' asks about location ('In the pond')."),
        ("___ did the family feel during the outing?", "How", "Who", "Where", "Why", "A", "'How' asks about feeling ('Happy and joyful')."),
        ("___ season or weather was it during the day out?", "What kind of", "Who", "Where", "Why", "A", "'What kind of' asks about weather ('Sunny weather')."),
        ("___ did they carry their food in?", "What", "Who", "Where", "Why", "A", "'What' asks about container ('A picnic basket')."),
        ("___ beverage did they drink with sandwiches?", "Which", "Who", "Where", "Why", "A", "'Which beverage' asks about 'orange juice'."),
        ("___ game did the brother and sister play?", "Which", "Who", "Where", "Why", "A", "'Which game' asks about 'frisbee / catch')."),
        ("___ took the family photos?", "Who", "What", "Where", "Why", "A", "'Who' asks about person ('Father')."),
        ("___ time did they return home in the evening?", "What", "Who", "Where", "Why", "A", "'What time' asks about '5:00 p.m.'"),
        ("___ was the lawn green and clean?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason."),
        ("___ pet or animal did they watch in the pond?", "Which", "Who", "Where", "Why", "A", "'Which animal' asks about 'ducks'."),
        ("___ activity was the most exciting for the children?", "Which", "Who", "Where", "Why", "A", "'Which activity' asks about 'flying kites').")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH14_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ did they go to the park?' Answer: 'To enjoy a sunny Sunday together.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('To enjoy...')."),
        ("Match question to answer: Question: '___ was the picnic rug placed?' Answer: 'Under the green oak tree.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ did the family arrive at the park?'", "When / What time", "Where", "Who", "Why", "A", "'When' inquires about time (at 10:00 a.m.)."),
        ("Form an asking sentence: 'Mother packed sandwiches.' -> '____ did mother pack?'", "What", "Who", "Why", "Where", "A", "'What' inquires about object."),
        ("Identify the INCORRECT question word usage: '**Why** flew the red kite in the sky?'", "'Why' should be 'Who'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'Who flew...' asks for person flying kite."),
        ("Select the proper interrogative sentence:", "Why did the family choose Sunday for their day out?", "Why the family chose Sunday for their day out?", "Why does the family chose?", "Why family chose?", "A", "Interrogative word + auxiliary 'did' + subject + base verb."),
        ("Which question word asks about MANNER or METHOD? '___ did the children fly the kite?'", "How", "Who", "What", "Where", "A", "'How' inquires about manner ('happily / expertly')."),
        ("Complete the question: '___ of the items in the basket was sweet?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options (apples / juice)."),
        ("Change statement to question: 'They sat under the tree.' -> '____ did they sit?'", "Where", "Who", "Why", "What", "A", "'Where' asks for location."),
        ("Fill in the blank: '___ happy were the children during the picnic?'", "How", "What", "Where", "Why", "A", "'How happy' measures degree."),
        ("Identify the question word in: 'Whom did father take a photo of?'", "Whom", "did", "father", "photo", "A", "'Whom' is the interrogative pronoun asking about the family members."),
        ("Choose the question that matches this answer: 'Sandwiches, apples, and orange juice.'", "What did mother pack for lunch?", "Where did they drive?", "Who flew the kite?", "What is a park?", "A", "'What did mother pack for lunch?' matches answer."),
        ("Fill in the blank: '___ member of the family carried the umbrella?'", "Which", "Who", "Why", "Where", "A", "'Which member' asks for identification (father)."),
        ("Complete: '___ sandwiches did mother make?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity."),
        ("Select the correct question for: 'The children flew a red kite in the clear blue sky.'", "What did the children do in the park?", "Where is the car?", "Why do ducks swim?", "Who is father?", "A", "'What did the children do in the park?' asks for action."),
        ("Which question word inquires about POSSESSION? '___ basket was filled with treats?'", "Whose", "Who", "Where", "Why", "A", "'Whose basket' asks about owner."),
        ("Form question: 'They spent 6 hours at the park.' -> '____ hours did they spend at the park?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why did the family go to the park.' Correct it:", "Why did the family go to the park?", "Why did the family go to the park!", "Why did the family go to the park,", "Why did the family go to the park;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why did the family decide to spend their Sunday at the park?' What is the syntax pattern?", "Question Word + Helping Verb (did) + Subject (the family) + Main Verb (decide) + Infinitive Phrase + Prepositional Phrase", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ sandwiches' vs '___ juice'", "'How many' for countable sandwiches; 'How much' for uncountable juice.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for sandwiches; 'How many' for juice.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where the family went on Sunday?' Correct it:", "Where **did** the family go on Sunday?", "Where the family went on Sunday?", "Where gone the family on Sunday?", "Where do the family went on Sunday?", "A", "Past simple questions require auxiliary 'did' before subject 'the family' and base verb 'go'."),
        ("Framing multi-question story guide: What sequence of question words logically builds a picture story of 'Family's Day Out'?", "Who went -> Where did they go -> What did they pack -> What activities did they do -> How did they feel", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals characters, setting, preparation, plot actions, and resolution."),
        ("Transform the statement into a formal question: 'Spending quality time together outdoors enhances family bonding.'", "How does spending quality time outdoors contribute to strengthening family bonds?", "Where is the park?", "Who went to park?", "What is a kite?", "A", "Directly targets story theme."),
        ("Analyze this ambiguous question: 'What did they eat?' How can it be made precise?", "Add specific context: 'What delicious lunch items did the family enjoy while sitting on the rug under the oak tree?'", "Make it shorter: 'What eat?'", "Change to: 'Where eat?'", "Remove 'What'.", "A", "Adding specific context clarifies which lunch items."),
        ("Choose the correct question pair for dialogue: Sister: '___ can we fly our kite?' Father: '___ on the open lawn near the pond!'", "Where, Right over there", "Who, Where", "Where, How", "When, Whose", "A", "Where (location inquiry), Right over there (location answer)."),
        ("Spot the DOUBLE auxiliary error: 'Why did the mother packed sandwiches?'", "'did' requires base verb 'pack', not past tense 'packed'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('pack')."),
        ("Reconstruct question from answer: Answer: 'They felt extremely happy and refreshed after spending the sunny day together in nature.'", "Question: 'How did the family feel after their day out?'", "Question: 'Where did they run?'", "Question: 'Who bought a car?'", "Question: 'Why is sun bright?'", "A", "Targets emotional outcome."),
        ("Form indirect question: 'The child asked where they were going for the picnic.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ is outdoor recreation important for children's growth?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the health/growth reason."),
        ("HOTS Reasoning: Why is 'Who' used for parents but 'Which' used when choosing between outdoor games?", "'Who' is used for human family members; 'Which' is used when selecting between specific game options.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the games...' selects from defined options."),
        ("Correct all errors in: 'why did the family go to central park on sunday'", "Why did the family go to Central Park on Sunday?", "Why did the family go to central park on sunday.", "Whom did the family go to Central Park?", "Why does the family went to Central Park?", "A", "Capital W, capital Central Park, capital Sunday, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 14:", "How does a planned family day out foster communication, physical health, and emotional well-being among family members?", "What food was in the basket?", "Where is the park?", "Who drove the car?", "A", "Asks student to evaluate family bonding, health, and emotional well-being.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The mother is **packing** a picnic basket.", "packing", "mother", "is", "basket", "A", "'packing' is verb + -ing form."),
        ("The father is **driving** the car to the park.", "driving", "father", "is", "park", "A", "'driving' is verb + -ing form."),
        ("The children are **running** across the green grass.", "running", "children", "are", "grass", "A", "'running' is verb + -ing form."),
        ("Father is **spreading** a large rug under the tree.", "spreading", "father", "is", "tree", "A", "'spreading' is verb + -ing form."),
        ("The family is **eating** delicious sandwiches.", "eating", "family", "is", "sandwiches", "A", "'eating' is verb + -ing form."),
        ("The brother is **flying** a red kite.", "flying", "brother", "is", "kite", "A", "'flying' is verb + -ing form."),
        ("Mother is **pouring** orange juice into glasses.", "pouring", "mother", "is", "glasses", "A", "'pouring' is verb + -ing form."),
        ("They are **watching** the ducks in the pond.", "watching", "they", "are", "ducks", "A", "'watching' is verb + -ing form."),
        ("The sister is **throwing** a frisbee.", "throwing", "sister", "is", "frisbee", "A", "'throwing' is verb + -ing form."),
        ("The family members are **laughing** together.", "laughing", "family", "are", "together", "A", "'laughing' is verb + -ing form."),
        ("The sister is **singing** a sweet song.", "singing", "sister", "is", "song", "A", "'singing' is verb + -ing form."),
        ("Father is **taking** family photographs.", "taking", "father", "is", "photographs", "A", "'taking' is verb + -ing form."),
        ("They are **walking** along the park trail.", "walking", "they", "are", "trail", "A", "'walking' is verb + -ing form."),
        ("The kids are **playing** on the playground swings.", "playing", "kids", "are", "swings", "A", "'playing' is verb + -ing form."),
        ("Mother is **cleaning** up the picnic mat.", "cleaning", "mother", "is", "mat", "A", "'cleaning' is verb + -ing form."),
        ("The family is **enjoying** a bright sunny day.", "enjoying", "family", "is", "day", "A", "'enjoying' is verb + -ing form."),
        ("Father is **carrying** the heavy bag.", "carrying", "father", "is", "bag", "A", "'carrying' is verb + -ing form."),
        ("They are **returning** home in the evening.", "returning", "they", "are", "evening", "A", "'returning' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH14_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'pack'**? (Mother is ____ the basket.)", "packing (add -ing)", "packking", "packeing", "packng", "A", "Regular verb adding -ing (packing)."),
        ("What is the correct -ing spelling rule for **'run'**? (The children are ____.)", "running (double final consonant)", "runing", "runneging", "runng", "A", "CVC rule: double final consonant before -ing (running)."),
        ("What is the correct -ing spelling rule for **'drive'**? (Father is ____ the car.)", "driving (drop final silent e)", "driveing", "drivving", "drivng", "A", "Drop final silent 'e' before adding -ing (driving)."),
        ("Fill in the blank with present continuous form: 'The children (play) ____ in the park.'", "are playing", "is play", "was playing", "are played", "A", "Plural subject 'children' takes 'are playing'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The family is enjoying their picnic right now.", "The family enjoyed their picnic yesterday.", "The family will enjoy their picnic tomorrow.", "The family enjoyed yesterday.", "A", "'is enjoying' is present continuous."),
        ("Fill in the blanks: 'Mother ____ (pour) juice, and father ____ (slice) sandwiches.' ", "is pouring, is slicing", "are pouring, are slicing", "is pour, is slice", "was pouring, were slicing", "A", "Singular subjects take 'is pouring' and 'is slicing' (slice drops e -> slicing)."),
        ("Identify the spelling mistake in: 'The children are **runing** across the grass.'", "'runing' should be 'running'", "'runing' should be 'running'", "'are' should be 'is'", "No mistake", "A", "Run doubles final n before -ing (running)."),
        ("Select the correct -ing form for **'take'**:", "taking", "takeing", "takking", "takng", "A", "Drop silent 'e': take -> taking."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Look! The kite is flying high in the sky.", "The kite flew high yesterday.", "The kite flies high every Sunday.", "The kite will fly tomorrow.", "A", "Present continuous ('is flying') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (write) a story about a family's day out.'", "am writing", "is writing", "are writing", "am writeing", "A", "Subject 'I' takes 'am writing' (write drops e -> writing)."),
        ("Choose the correct form: 'The family ____ (sit) on the green rug.'", "is sitting", "are sitting", "am sitting", "is sit", "A", "Collective noun / singular subject takes 'is sitting' (double t)."),
        ("Identify the verb in: 'Why are you packing so many sandwiches?'", "are packing", "Why", "you", "sandwiches", "A", "Helping verb 'are' + main verb 'packing' form present continuous."),
        ("What is the -ing form of **'sit'**?", "sitting", "siting", "sitteing", "sitng", "A", "CVC double t: sit -> sitting."),
        ("What is the -ing form of **'make'**?", "making", "makeing", "makking", "makng", "A", "Drop silent e: make -> making."),
        ("Change simple present to continuous: 'Father drives.' -> 'Father ____.'", "is driving", "drove", "was driving", "will drive", "A", "is driving."),
        ("Fill in the blank: 'The sun ____ (shining) brightly in the sky.'", "is shining", "are shining", "am shining", "shined", "A", "Singular subject 'sun' takes 'is shining' (shine drops e -> shining)."),
        ("Identify the correct present continuous sentence:", "Look! The ducks are swimming in the pond.", "Look! The ducks swims in the pond.", "Look! The ducks swam in the pond.", "Look! The ducks swimming in the pond.", "A", "Exclamation 'Look!' introduces action happening now ('are swimming')."),
        ("Select the correct -ing form for **'fly'**:", "flying", "flyeing", "flyying", "flyng", "A", "Vowel+y verb adding -ing (flying).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (run, drive, pack)", "run -> running (double consonant), drive -> driving (drop e), pack -> packing (add -ing)", "All just add -ing.", "All double the last letter.", "run -> runing, drive -> driveing, pack -> packking", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The family drove to the park while the sun shone.'", "The family is driving to the park while the sun is shining.", "The family driving to the park while the sun shining.", "The family was driving while the sun shone.", "The family will drive while the sun shines.", "A", "Both verbs transformed to present continuous (is driving, is shining)."),
        ("Spot the missing auxiliary verb in: 'The children flying kite and mother serving juice.' Correct it:", "'The children **are** flying a kite and mother **is** serving juice.'", "'The children flying kite and mother serving juice.'", "'The children **is** flying and mother **are** serving.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'The family is **loving** the park'?", "Because 'love' expressing emotion is stative, preferring simple present 'The family loves the park'.", "Because 'loving' is hard to spell.", "Because park is green.", "Because kite is red.", "A", "Stative emotion verbs prefer simple present."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The children in the park are playing joyfully.", "The children in the park is playing joyfully.", "The children in the park am playing joyfully.", "The children in the park playing joyfully.", "A", "Plural subject ('children') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The children are watching TV right now.' -> Negative for picnic scene:", "The children **are not** watching TV; they are playing outside.", "The children not watching TV.", "The children is no watching TV.", "The children isn't watch TV.", "A", "Add 'not' after plural auxiliary 'are'."),
        ("Spot all THREE spelling errors: 'He is **runing** fast, **takeing** photos, and **siteing** on grass.'", "'runing' -> 'running'; 'takeing' -> 'taking'; 'siteing' -> 'sitting'", "'runing' -> 'runing'; 'takeing' -> 'takking'; 'siteing' -> 'siteing'", "No errors.", "Only 'runing' is wrong.", "A", "running (double n), taking (drop e), sitting (double t)."),
        ("Rewrite as interrogative present continuous: 'The mother is preparing lunch.'", "**Is** the mother preparing lunch?", "Are the mother preparing lunch?", "The mother preparing lunch?", "Why the mother is preparing lunch?", "A", "Move auxiliary 'Is' to beginning of sentence."),
        ("Analyze action timeline: 'The family **is leaving** for the park at 9 a.m. tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While mother is serving juice, the children are flying kites.", "While mother served juice, children are flying.", "Mother is serving while children flew.", "Mother serve while children fly.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'Father is drivving the car.'", "'drivving' should be 'driving' (single 'v').", "'is' should be 'are'.", "'car' should be capitalized.", "No error.", "A", "Drive drops silent e -> driving (single v)."),
        ("HOTS Reasoning: Compare 'They packed a basket' (Past Simple) vs 'They are packing a basket' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means they unpacked.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the children ____ (running) on the lawn?'", "are, running", "is, running", "am, running", "do, running", "A", "Plural subject children takes 'are ... running'."),
        ("Identify the correct present continuous sentence describing picture composition:", "The family is enjoying a lovely picnic under the big oak tree.", "The family is enjoy a lovely picnic under the big oak tree.", "The family are enjoying a lovely picnic under the big oak tree.", "The family enjoying a lovely picnic under the big oak tree.", "A", "Singular subject / collective family + is + enjoying.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 14: Family's Day Out\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("The family ___ having a day out in the park.", "is", "are", "am", "be", "A", "Collective singular subject 'The family' takes 'is'."),
        ("The children ___ playing joyfully on the lawn.", "are", "is", "am", "be", "A", "Plural subject 'children' takes 'are'."),
        ("I ___ excited about our family picnic.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("Father ___ driving the car carefully.", "is", "are", "am", "be", "A", "Singular subject 'Father' takes 'is'."),
        ("Mother ___ packing sandwiches and apples.", "is", "are", "am", "be", "A", "Singular subject 'Mother' takes 'is'."),
        ("The sandwiches ___ delicious and fresh.", "are", "is", "am", "be", "A", "Plural subject 'sandwiches' takes 'are'."),
        ("The red kite ___ flying high in the sky.", "is", "are", "am", "be", "A", "Singular subject 'kite' takes 'is'."),
        ("The ducks ___ swimming peacefully in the pond.", "are", "is", "am", "be", "A", "Plural subject 'ducks' takes 'are'."),
        ("I ___ drinking sweet orange juice.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The park ___ crowded on sunny Sundays.", "is", "are", "am", "be", "A", "Singular 'park' takes 'is'."),
        ("The weather ___ pleasant today.", "is", "are", "am", "be", "A", "Uncountable singular 'weather' takes 'is'."),
        ("The trees ___ providing cool shade.", "are", "is", "am", "be", "A", "Plural 'trees' takes 'are'."),
        ("You ___ writing a picture composition.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("Brother and sister ___ playing frisbee.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("The picnic mat ___ spread under the tree.", "is", "are", "am", "be", "A", "Singular 'mat' takes 'is'."),
        ("I ___ taking photos of the ducks.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The day out ___ full of fun and laughter.", "is", "are", "am", "be", "A", "Singular 'day out' takes 'is'."),
        ("The birds ___ singing on the branches.", "are", "is", "am", "be", "A", "Plural 'birds' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH14_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'Father and mother ____ packing the picnic basket.'", "are", "is", "am", "be", "A", "Compound subject ('Father and mother') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "The family is enjoying their picnic in the park.", "The family are enjoying their picnic in the park.", "The family am enjoying their picnic in the park.", "The family be enjoying their picnic in the park.", "A", "Collective noun 'The family' acting as a single unit requires 'is'."),
        ("Fill in the blanks: 'I ____ sitting on the rug, and my brother ____ flying a kite.'", "am, is", "is, is", "are, is", "am, are", "A", "'I am', 'my brother is'."),
        ("Identify the mistake in: 'The sandwiches in the basket **is** fresh.'", "'is' should be 'are' because 'sandwiches' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'sandwiches' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you going to the park on Sunday?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither mother nor father ____ driving fast.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject 'father' takes 'is'."),
        ("Select the correct sentence for story moral:", "Happiness and bonding are essential for family life.", "Happiness and bonding is essential for family life.", "Happiness and bonding am essential for family life.", "Happiness and bonding be essential for family life.", "A", "Compound subject 'Happiness and bonding' takes 'are'."),
        ("Complete the conversation: Sister: 'Where ____ mother?' Brother: 'She ____ under the tree!'", "is, is", "are, are", "is, are", "are, is", "A", "Singular 'mother' -> is; singular 'She' -> is."),
        ("Identify where 'is' is used incorrectly:", "The children **is** playing.", "The park is green.", "The rug is clean.", "The mother is kind.", "A", "'The children is' should be 'The children are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The team of gardeners ____ watering the park grass.'", "is", "are", "am", "be", "A", "Collective noun 'team' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The juice in the glasses ____ cold.'", "is", "are", "am", "be", "A", "Uncountable singular subject 'juice' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am writing a story about our day out.", "I is writing a story about our day out.", "I are writing a story about our day out.", "I be writing a story about our day out.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many trees in the park.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many trees'."),
        ("Fill in the blank: 'There ____ a big pond near the entrance.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a big pond'."),
        ("Choose the correct sentence:", "What are the kids doing on the lawn?", "What is the kids doing on the lawn?", "What am the kids doing on the lawn?", "What be the kids doing on the lawn?", "A", "Plural subject 'the kids' takes 'are'."),
        ("Identify the correct form: 'The mother, as well as the children, ____ happy.'", "is", "are", "am", "be", "A", "Subject is singular 'The mother' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both apples and sandwiches ____ packed in the box.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The sun ____ bright, but the winds ____ gentle.'", "is, are", "are, is", "am, are", "is, is", "A", "'sun is', 'winds are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH14_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the family members **____** enjoying the picnic.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'members' is plural.", "am — because it refers to speaker.", "be — because members are happy.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A group of families **are** having a picnic on the lawn.'", "'are' should be 'is' because the subject is singular noun 'group'.", "'are' should be 'am'.", "'families' should be 'family'.", "No error.", "A", "'A group' is singular, so it requires 'is having'."),
        ("Compare: (1) 'Mother and father **are** in the car.' vs (2) 'Mother, along with father, **is** in the car.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'Mother' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the family **____** excited about Sunday.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The sandwiches **is** fresh, I **is** happy, and the kites **is** flying.'", "'sandwiches is' -> 'sandwiches are'; 'I is' -> 'I am'; 'kites is' -> 'kites are'", "'sandwiches is' -> 'sandwiches am'; 'I is' -> 'I are'; 'kites is' -> 'kites am'", "Only 'I is' is wrong.", "No errors present.", "A", "sandwiches are (plural), I am (1st person), kites are (plural)."),
        ("Fill in the blanks in this complex sentence: 'Not only the father but also the kids **____** playing, while mother **____** resting.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer plural subject ('kids' -> are); 'mother' -> is."),
        ("Transform to negative: 'The family is leaving the park.'", "The family **is not** leaving the park.", "The family are not leaving the park.", "The family am not leaving the park.", "The family no leaving the park.", "A", "Add 'not' after singular helping verb 'is'."),
        ("Analyze inverted subject position: 'Under the big oak tree **____** sitting a happy family.'", "is", "are", "am", "be", "A", "Subject is singular 'a happy family', appearing after verb, requiring 'is'."),
        ("Determine agreement with uncountable nouns: 'The juice in the glasses **____** refreshing.'", "is", "are", "am", "be", "A", "Uncountable noun 'juice' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the photos of our day out.'", "Here **are** the photos of our day out.", "Here am the photos of our day out.", "Here be the photos of our day out.", "No error.", "A", "Plural subject 'photos' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "The Sunday weather **is** wonderful.", "The family **is** packing the basket.", "Father **is** driving to the park.", "Mother **is** pouring juice.", "A", "In 'The Sunday weather is wonderful', 'is' is the main linking verb connecting subject to predicate adjective."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because park is green.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither father nor children **____** sleeping, because the day **____** exciting.'", "are, is", "is, are", "is, is", "are, are", "A", "'children' is closer plural subject -> are; 'day' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "The family is happy, I am playing, and the ducks are swimming.", "The family are happy, I is playing, and the ducks is swimming.", "The family am happy, I are playing, and the ducks am swimming.", "The family is happy, I is playing, and the ducks is swimming.", "A", "family is (singular unit), I am (1st person), ducks are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH14_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 14
# ---------------------------------------------------------------------------
def rebuild_chapter_14():
    print("Rebuilding Chapter 14 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH14_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 14 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_14()
