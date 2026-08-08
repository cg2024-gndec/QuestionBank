r"""
=============================================================================
Script: rebuild_chapter_08.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 08:
             "Diwali" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH08_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_08")
os.makedirs(CH08_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("lamp", "lamps", "lampes", "lampies", "lampz", "A", "Regular noun adding -s."),
        ("diya", "diyas", "diyaes", "diyies", "diyaz", "A", "Regular noun adding -s."),
        ("house", "houses", "housies", "housees", "housez", "A", "Regular noun ending in -e adds -s."),
        ("rangoli", "rangolis", "rangolies", "rangolieses", "rangoliz", "A", "Regular noun adding -s."),
        ("light", "lights", "lightes", "lighties", "lightz", "A", "Regular noun adding -s."),
        ("deity", "deities", "deitys", "deityes", "deitiz", "A", "Consonant + y changes to -ies."),
        ("laddoo", "laddoos", "laddooes", "laddooies", "laddooz", "A", "Vowel ending noun adding -s."),
        ("sweet", "sweets", "sweetes", "sweeties", "sweetz", "A", "Regular noun adding -s."),
        ("gift", "gifts", "giftes", "gifties", "giftz", "A", "Regular noun adding -s."),
        ("friend", "friends", "friendes", "friendies", "friendz", "A", "Regular noun adding -s."),
        ("family", "families", "familys", "familyes", "familiz", "A", "Consonant + y changes to -ies."),
        ("cracker", "crackers", "crackeres", "crackeries", "crackerz", "A", "Regular noun adding -s."),
        ("night", "nights", "nightes", "nighties", "nightz", "A", "Regular noun adding -s."),
        ("day", "days", "daies", "dayes", "dayz", "A", "Vowel + y adds -s."),
        ("box", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es."),
        ("wish", "wishes", "wishs", "wishies", "wished", "A", "Nouns ending in -sh add -es."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH08_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 08 (*Diwali*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("People light earthen (lamp / lamps) on Diwali.", "lamps", "lamp", "lampes", "lampies", "A", "Plural noun 'lamps'."),
        ("Colorful (rangoli / rangolis) are made at the doorstep.", "rangolis", "rangoli", "rangolies", "rangoliz", "A", "'rangolis' is the correct plural."),
        ("Offerings are made to the two (deity / deities).", "deities", "deity", "deitys", "deityes", "A", "Consonant + y changes to -ies (deities)."),
        ("Identify the INCORRECT plural spelling in this list: lamps, houses, familys, sweets.", "familys", "lamps", "houses", "sweets", "A", "Plural of family is 'families', not 'familys'."),
        ("Choose the sentence with the correct plural noun form:", "People distribute sweets among the poor.", "People distribute sweetes among the poor.", "People distribute sweeties among the poor.", "People distribute sweetz among the poor.", "A", "sweets is the correct plural of sweet."),
        ("Which noun forms its plural by changing consonant + y to -ies?", "deity -> deities", "diya -> diyas", "light -> lights", "lamp -> lamps", "A", "Deity ends in consonant + y, so plural is deities."),
        ("Change the singular noun in brackets to plural: 'The children received three ____ (box) of laddoos.'", "boxes", "boxs", "boxies", "boxen", "A", "Nouns ending in -x add -es (boxes)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "Families light diyas and share sweets.", "Familys light diyas and share sweetes.", "Families light diyaes and share sweeties.", "Familyes light diyaz and share sweets.", "A", "families, diyas, sweets are all correctly spelt plurals."),
        ("What is the correct plural of 'electric light'?", "electric lights", "electric lightes", "electric lighties", "electric lightz", "A", "Regular noun adding -s."),
        ("People spend many happy (day / days) preparing for Diwali.", "days", "daies", "day", "dayes", "A", "Vowel + y adds -s (days)."),
        ("The courtyard was lit with many (diya / diyas).", "diyas", "diyaes", "diyies", "diyaz", "A", "Plural of diya is diyas."),
        ("Many (person / people) distribute gifts to the poor.", "people", "persons", "peoples", "persones", "A", "Irregular plural of person is people."),
        ("How many (gift / gifts) did they exchange on Diwali?", "gifts", "gift", "giftes", "gifties", "A", "Plural noun 'gifts'."),
        ("The two (family / families) celebrated Diwali together.", "families", "family", "familys", "familyes", "A", "Consonant + y changes to -ies (families)."),
        ("Which plural noun rule applies to the word **'wishes'**?", "Add -es to nouns ending in -sh", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Wish ends in -sh, so it adds -es."),
        ("People send sweet (wish / wishes) to their friends.", "wishes", "wishs", "wishies", "wished", "A", "Wish ends in -sh, adding -es (wishes)."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("They bought ten (laddoo / laddoos) for the pooja.", "laddoos", "laddooes", "laddooies", "laddooz", "A", "Plural of laddoo is laddoos.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The child lit a diya in the house.'", "The children lit diyas in the houses.", "The childs lit diyaes in the housees.", "The children lit diya in the houses.", "The childes lit diyas in the housez.", "A", "Plural of child->children, diya->diyas, house->houses."),
        ("Analyze the error: 'People decorated the house with much lights.' Why is 'much' inappropriate here?", "'lights' is a plural countable noun, so 'many lights' should be used.", "'lights' should be 'lightes'.", "'lights' should be 'lighties'.", "No error.", "A", "Countable plural nouns take 'many', not 'much'."),
        ("Complete the paragraph with correct plurals: 'The two ____ (family) made five ____ (rangoli) and bought ten ____ (laddoo).'", "families, rangolis, laddoos", "familys, rangolies, laddooes", "families, rangoli, laddooz", "familyes, rangolis, laddoos", "A", "families (-y -> -ies), rangolis (-s), laddoos (-s)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **children** placed **diyas** on the **shelves**.", "The **childs** placed **diyaes** on the **shelfs**.", "The **childrens** placed **diyies** on the **shelfes**.", "The **childes** placed **diyas** on the **shelves**.", "A", "children (irregular), diyas (-s), shelves (-f -> -ves)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, men, teeth", "lamps, diyas, sweets, gifts", "deities, families, countries, cities", "leaves, thieves, wolves, knives", "A", "children, people, men, teeth change forms without standard -s/-es."),
        ("Why does 'day' become 'days' but 'deity' becomes 'deities'?", "Because 'day' has a vowel before y (a+y -> -s), while 'deity' has a consonant before y (t+y -> -ies).", "Because 'day' is short and 'deity' is long.", "Because 'day' is time and 'deity' is divine.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The two familys bought many mouses for Diwali.'", "'familys' should be 'families' and 'mouses' should be 'mice'.", "'familys' should be 'family' and 'mouses' should be 'mices'.", "'Diwali' should be 'Diwalis' only.", "There are no mistakes in the sentence.", "A", "families (consonant + y) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'They placed diyas at their ____ (foot) and clapped their ____ (hand).'", "feet, hands", "foots, handes", "feets, hands", "foots, handies", "A", "Plural of foot is feet, plural of hand is hands."),
        ("Analyze this sentence: 'People distributed wealth on Diwali.' Can 'wealth' be pluralized as 'wealths'?", "No, 'wealth' is an abstract uncountable noun; it stays singular.", "Yes, 'wealths' is correct.", "No, it becomes 'wealthss'.", "Yes, 'a wealth' is correct.", "A", "Wealth is an uncountable mass noun."),
        ("Fill in the blanks: 'The two ____ (child) shared three ____ (box) of sweets.'", "children, boxes", "childs, boxs", "childrens, boxies", "childes, boxes", "A", "child -> children; box -> boxes (-x + es)."),
        ("Select the option that shows correct plural transformation for ALL three words: 'leaf', 'deity', 'box'", "leaves, deities, boxes", "leafs, deitys, boxs", "leaves, deityes, boxies", "leafes, deities, foxen", "A", "leaf -> leaves; deity -> deities; box -> boxes."),
        ("HOTS Reasoning: Why do we say 'darkness is replaced by light' rather than 'darknesses are replaced by lights' in a moral summary?", "Because 'darkness' is an abstract quality noun that stays singular.", "Because darkness is night.", "Because diyas are bright.", "Because laddoos are sweet.", "A", "Uncountable abstract quality noun takes singular verb."),
        ("Transform into singular: 'The families lit the diyas in the houses.'", "The family lit the diya in the house.", "The families lit the diya in the house.", "The family light the diya in the house.", "The family lit the diyas in the house.", "A", "Singular forms: family, diya, house."),
        ("Identify the correct rule for forming the plural of **'laddoo'**:", "Add -s because it is a regular noun ending in a vowel (laddoos).", "Add -es (laddooes).", "Change -oo to -v (laddvs).", "Change vowel sound.", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("Diwali is ___ festival of lights.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'festival'."),
        ("People light ___ earthen lamp in the evening.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'earthen'."),
        ("They make ___ colourful rangoli at the entrance.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'colourful'."),
        ("Houses are decorated with ___ electric light.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'electric'."),
        ("Diwali is celebrated on ___ New Moon night.", "the", "a", "an", "no article", "A", "Use 'the' before specific lunar phase 'the New Moon'."),
        ("___ Panchatantra/Festival story tells us about light.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Festival'."),
        ("Laddoo is ___ sweet offered to deities.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'sweet'."),
        ("Diwali brings ___ honest joy to every heart.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ victory of good over evil is celebrated on Diwali.", "The", "A", "An", "No article", "A", "Use 'The' for specific victory of good over evil."),
        ("It is ___ auspicious occasion for all families.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'auspicious'."),
        ("Diwali is ___ unusual and grand celebration.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("They worship Shri Ganesh on ___ evening of Diwali.", "the", "a", "an", "no article", "A", "Use 'the' for specific time 'the evening of Diwali'."),
        ("___ earthen diya brightens the entire room.", "An", "A", "The", "No article", "A", "Use 'An' before vowel sound 'earthen'."),
        ("People share ___ gift with their neighbors.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'gift'."),
        ("They created ___ happy atmosphere at home.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'happy'."),
        ("Diwali is ___ important Indian festival.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'important'."),
        ("Diwali spreads ___ happiness everywhere.", "no article", "a", "an", "the", "A", "Abstract noun 'happiness' takes no indefinite article here."),
        ("___ sun set before people lit their diyas.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH08_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("People place ___ diya at ___ door to welcome guests.", "a, the", "an, a", "a, an", "the, a", "A", "'a diya' (consonant sound), 'the door' (specific location)."),
        ("Why do we say '**a** rangoli' but '**an** earthen lamp'?", "Because 'rangoli' begins with a consonant sound (r) and 'earthen' with a vowel sound (e).", "Because rangolis are colorful.", "Because earthen lamps use oil.", "Because New Moon is dark.", "A", "Article selection depends on initial vowel/consonant sound."),
        ("Select the sentence with CORRECT article usage:", "Diwali is a festival of lights.", "Diwali is an festival of lights.", "Diwali is the a festival of lights.", "Diwali is a an festival of lights.", "A", "'a festival' (/f/) takes 'a'."),
        ("Fill in the blanks: 'They lit ___ lamp and made ___ rangoli.'", "a, a", "an, an", "a, an", "an, a", "A", "'a lamp' (consonant /l/), 'a rangoli' (consonant /r/)."),
        ("Identify the INCORRECT article in: 'We offered **a** electric lamp.'", "'a' should be 'an'", "'a' should be 'the'", "'electric' should be 'a electric'", "No mistake", "A", "'electric' starts with vowel sound /e/, so it takes 'an'."),
        ("Which article completes the sentence? 'Diwali brings ___ active joy to all.'", "an", "a", "the", "no article", "A", "'active' starts with vowel sound /a/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ family lit ___ diya.'", "The, a", "A, a", "An, an", "The, the", "A", "'The family' (specific family in context), 'a diya' (consonant sound)."),
        ("Why do we use 'an' before 'earthen lamp' in 'He lit **an** earthen lamp'?", "Because 'earthen' begins with the vowel sound /er/.", "Because lamp is a noun.", "Because Diwali is in autumn.", "Because New Moon is night.", "A", "'earthen' starts with vowel sound /er/."),
        ("Complete the dialogue: Child: 'Can I light ___ diya?' Mother: 'Yes, put it on ___ step!'", "a, the", "a, an", "an, the", "the, the", "A", "'a diya' (consonant sound), 'the step' (specific step)."),
        ("Select the correct sentence:", "A laddoo is a sweet treat.", "An laddoo is a sweet treat.", "The laddoo is an sweet treat.", "An laddoo is an sweet treat.", "A", "'A laddoo' (consonant sound), 'a sweet treat' (consonant sound)."),
        ("Fill in the blank: 'Families celebrate for ___ long time on Diwali night.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "Diwali celebrates **___ prosperity** and wealth.", "He lit ___ diya.", "She made ___ rangoli.", "They bought ___ sweet.", "A", "Abstract noun 'prosperity' takes no indefinite article here."),
        ("Choose the correct sentence for story summary:", "Light overcomes darkness on Diwali.", "A light overcomes a darkness on Diwali.", "An light overcomes an darkness on Diwali.", "The light a overcomes darkness.", "A", "Abstract concepts 'light' and 'darkness' take no indefinite articles in general moral sense."),
        ("Fill in the blanks: 'They spent ___ hour making ___ colorful rangoli.'", "an, a", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'a colorful rangoli' (consonant c)."),
        ("Which sentence uses 'the' correctly for unique lunar phase?", "Diwali is celebrated on the New Moon night.", "Diwali is celebrated on a New Moon night.", "Diwali is celebrated on an New Moon night.", "Diwali is celebrated on New Moon night.", "A", "Unique lunar phase 'the New Moon night' takes 'the'."),
        ("Identify the article error: 'We had **a** explanation about **an** short ritual.'", "'an short' should be 'a short' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an short' should be 'a short'", "No error", "A", "'an explanation' (vowel /e/) and 'a short ritual' (consonant /s/)."),
        ("Complete: 'It was ___ unexpected delight on ___ auspicious night.'", "an, an", "a, an", "the, the", "an, a", "A", "an unexpected (/u/), an auspicious night (/a/)."),
        ("Choose the correct option: '___ sun set before the moon appeared.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'People worship **a** wealth on **the** Diwali.' Correct the error:", "'worship a wealth' -> 'worship wealth' (uncountable abstract noun wealth takes no article 'a'); 'the Diwali' -> 'Diwali'.", "'the Diwali' -> 'an Diwali'.", "'worship a wealth' -> 'worship an wealth'.", "No error present.", "A", "'wealth' is uncountable; festival names like 'Diwali' take no article."),
        ("Fill in all three blanks: '___ family lit ___ diya to celebrate ___ goodness.'", "The, a, no article", "A, an, a", "An, a, the", "The, a, a", "A", "'The family' (specific), 'a diya' (consonant sound), 'goodness' (general abstract)."),
        ("Identify why 'the' is used in: 'People celebrate **the** victory of good over evil.'", "Because 'the victory' refers to the specific historical/moral victory celebrated on Diwali.", "Because victory is a proper noun.", "Because laddoos are sweet.", "Because New Moon is night.", "A", "'The' specifies the definite victory described in narrative."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly past the house.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "A family celebrated Diwali. They lit a diya. The diya illuminated the courtyard.", "An family celebrated an Diwali. They lit an diya. A diya illuminated a courtyard.", "The family celebrated an Diwali.", "A family celebrated a Diwali. The diya was an honest.", "A", "A family (first mention), Diwali (proper noun, no article), a diya (consonant), The diya (second mention)."),
        ("Why is it correct to write 'a unique celebration' but 'an unusual celebration'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because celebration is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ acts of kindness bring ___ light to ___ dark world.'", "No article, no article, a", "An, a, an", "The, the, the", "A, an, a", "A", "Plural 'acts' takes no indefinite article; mass noun 'light' takes no article; 'a dark world'."),
        ("Analyze this sentence: 'They worshiped **the** deities.' Why is 'the' appropriate?", "Because it refers to the specific deities mentioned (Shri Ganesh and Maa Laxmi).", "Because deities is in house.", "Because deities is plural.", "Because Diwali is festival.", "A", "'the' specifies the definite deities worshipped."),
        ("Correct the sentence: 'An family lit a earthen lamp in a evening.'", "A family lit an earthen lamp in the evening.", "The family lit an earthen lamp in an evening.", "An family lit the earthen lamp in a evening.", "A family lit a earthen lamp in a evening.", "A", "'A family' (/f/ sound), 'an earthen' (vowel /er/), 'the evening' (specific time of day)."),
        ("Fill in the blanks: '___ laddoos on ___ plate were offered to ___ Maa Laxmi.'", "The, the, no article", "A, a, a", "No article, a, an", "An, the, a", "A", "'The laddoos' (specific), 'the plate' (specific), Maa Laxmi (proper name, no article)."),
        ("Spot the missing article: 'People lit diya and worshipped the deities.'", "Missing 'a' before 'diya' -> 'lit a diya...'", "Missing 'an' before 'worshipped'", "Missing 'the' before 'lit'", "No article is missing", "A", "Indefinite singular noun 'a diya' needs 'a'."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An earthen lamp was placed near a window of the house.", "A earthen lamp was placed near an window of a house.", "The earthen lamp was placed near an window of an house.", "An earthen lamp was placed near an window of the house.", "A", "An earthen (vowel), a window (consonant), the house (specific)."),
        ("Rewrite correctly: 'Diwali is a honest celebration that brings an joyful mood.'", "Diwali is an honest celebration that brings a joyful mood.", "Diwali is a honest celebration that brings a joyful mood.", "Diwali is an honest celebration that brings an joyful mood.", "Diwali is the honest celebration that brings an joyful mood.", "A", "'an honest' (silent h), 'a joyful' (consonant /j/)."),
        ("Identify the correct rule for using 'the' with specific celestial/astronomical phases (the New Moon, the Full Moon):", "Unique celestial phases and bodies take 'the' because they refer to specific one-of-a-kind entities.", "Lunar phases take 'an'.", "Lunar phases never take articles.", "Lunar phases take 'a' only.", "A", "'The New Moon' takes 'the'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("Diwali usually falls in the month of **October** or **November**. What is the abbreviation for **October**?", "Oct.", "Octo.", "Oc.", "Ot.", "A", "Oct. is standard abbreviation."),
        ("What is the standard abbreviation for **November**?", "Nov.", "Nove.", "Nv.", "Nm.", "A", "Nov. is standard abbreviation."),
        ("Which day comes right after Saturday?", "Sunday", "Monday", "Friday", "Thursday", "A", "Sunday follows Saturday."),
        ("What is the abbreviation for **Sunday**?", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard abbreviation."),
        ("If Diwali celebrations last for 5 days, how many days of festivities are there?", "5 days", "2 days", "7 days", "3 days", "A", "5 days of festivities."),
        ("Which month comes right before October?", "September", "August", "November", "December", "A", "September comes before October."),
        ("What is the short abbreviation for **September**?", "Sept. or Sep.", "Spt.", "Septe.", "St.", "A", "Sept. or Sep. is standard abbreviation."),
        ("Diwali pooja is performed in the **evening**. What time of day comes right after evening?", "Night", "Morning", "Noon", "Dawn", "A", "Night follows evening."),
        ("What is the abbreviation for **Friday**?", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard abbreviation."),
        ("How many seasons are in a year?", "4 major seasons", "12 seasons", "2 seasons", "365 seasons", "A", "4 major seasons (Spring, Summer, Autumn/Fall, Winter)."),
        ("Which month comes right after October?", "November", "December", "September", "August", "A", "November comes after October."),
        ("What is the short abbreviation for **December**?", "Dec.", "Dece.", "Dc.", "Dcm.", "A", "Dec. is standard abbreviation."),
        ("If today is Saturday, what day was yesterday?", "Friday", "Sunday", "Thursday", "Wednesday", "A", "Yesterday was Friday."),
        ("If today is Sunday, what day will tomorrow be?", "Monday", "Saturday", "Tuesday", "Wednesday", "A", "Tomorrow will be Monday."),
        ("What is the abbreviation for **Monday**?", "Mon.", "Mnd.", "Mo.", "Mn.", "A", "Mon. is standard abbreviation."),
        ("Which day comes between Thursday and Saturday?", "Friday", "Wednesday", "Sunday", "Monday", "A", "Friday is between Thursday and Saturday."),
        ("What is the abbreviation for **Wednesday**?", "Wed.", "Weds.", "We.", "W.", "A", "Wed. is standard abbreviation."),
        ("Which month comes right before November?", "October", "September", "December", "August", "A", "October comes before November.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH08_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Diwali pooja started on **Friday**. Cleaning began 3 days earlier. On which day did cleaning begin?", "Tuesday", "Wednesday", "Monday", "Thursday", "A", "Friday - 3 days = Thursday(1), Wednesday(2), Tuesday(3)."),
        ("The family decorated their house from **5:00 PM to 8:00 PM** on Diwali evening. How many hours did they decorate?", "3 hours", "2 hours", "4 hours", "5 hours", "A", "8:00 PM - 5:00 PM = 3 hours."),
        ("Match the day with its abbreviation: **Saturday**", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard."),
        ("Diwali is celebrated on the New Moon night in the Hindu calendar month of **Kartik** (Oct/Nov). How many days are in October?", "31 days", "30 days", "28 days", "29 days", "A", "October has 31 days."),
        ("Identify the correctly spelt month name:", "October", "Octobre", "Octoberr", "Octobere", "A", "October is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Saturday - Std.", "D", "Saturday abbreviation is Sat., not Std."),
        ("Calculate: How many days are there in **November**?", "30 days", "31 days", "28 days", "29 days", "A", "November has 30 days."),
        ("Which month has 31 days and comes right before November?", "October", "September", "December", "August", "A", "October has 31 days and precedes November."),
        ("Rearrange in correct chronological order: Fri, Wed, Thu, Sat", "Wed, Thu, Fri, Sat", "Thu, Wed, Fri, Sat", "Fri, Thu, Wed, Sat", "Sat, Fri, Thu, Wed", "A", "Wednesday -> Thursday -> Friday -> Saturday."),
        ("What day is 2 days before Monday?", "Saturday", "Sunday", "Friday", "Tuesday", "A", "Monday - 2 days = Sunday(1), Saturday(2)."),
        ("If a sweet shop prepares for Diwali over 2 weeks, how many days is that?", "14 days (2 x 7)", "10 days", "20 days", "7 days", "A", "2 weeks x 7 days = 14 days."),
        ("Select the month that has 30 days:", "November", "October", "December", "January", "A", "November has 30 days."),
        ("Which abbreviation stands for **November**?", "Nov.", "Nove.", "Nv.", "Nm.", "A", "Nov. is standard abbreviation."),
        ("If today is **Sun.**, what day will it be after 7 days?", "Sunday", "Monday", "Saturday", "Friday", "A", "7 days is a full week cycle, landing on Sunday again."),
        ("The pooja was conducted from **7:00 PM to 8:30 PM**. How many minutes did it last?", "90 minutes (1.5 hours)", "60 minutes", "120 minutes", "45 minutes", "A", "1 hour 30 minutes = 90 minutes."),
        ("Identify the word that means 'occurring once every year':", "Yearly / Annual", "Daily", "Weekly", "Monthly", "A", "Yearly/annual means once a year."),
        ("Which of the following is a weekend day?", "Saturday", "Monday", "Tuesday", "Wednesday", "A", "Saturday is a weekend day."),
        ("Choose the correct abbreviation for **October**:", "Oct.", "Octo.", "Oc.", "Ot.", "A", "Oct. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("The Diwali holiday break lasted from **Wed., 1st Nov.** to **Sun., 5th Nov.**. How many days was the holiday break?", "5 days", "4 days", "3 days", "7 days", "A", "1st to 5th Nov inclusive is 5 days."),
        ("Families gathered for Diwali dinner from **8:00 PM to 10:00 PM**. For how many minutes did dinner last?", "120 minutes (2 hours)", "90 minutes", "60 minutes", "150 minutes", "A", "2 hours = 120 minutes."),
        ("Solve the calendar puzzle: If 1st November was a Friday, what day of the week was 8th November?", "Friday", "Saturday", "Thursday", "Monday", "A", "1 + 7 = 8th November, landing on Friday."),
        ("Analyze this schedule: Sweets made on Mon, Wed, Fri; Rangoli made on Tue, Thu, Sat. On which day do BOTH rest?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If Diwali celebrations lasted a fortnight, how many days did the entire festival period cover?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Sep, Oct, Dec, Nov, Jan'", "December and November are in wrong order.", "October is in wrong position.", "January should be first.", "No error.", "A", "November comes before December (Sep, Oct, Nov, Dec, Jan)."),
        ("October has **31 days**. What date was the day right after 31st October?", "1st November", "32nd October", "30th October", "1st December", "A", "October has 31 days, so next day is 1st November."),
        ("If yesterday was two days before Thursday, what day is tomorrow?", "Thursday", "Wednesday", "Friday", "Tuesday", "A", "Two days before Thursday = Tuesday (yesterday). Today = Wednesday. Tomorrow = Thursday."),
        ("Calculate: How many days are there in total during **October** and **November** combined?", "61 days (31 + 30)", "60 days", "62 days", "59 days", "A", "October (31) + November (30) = 61 days."),
        ("HOTS Reasoning: Why does the exact calendar date of Diwali change every year on the Gregorian calendar?", "Because Diwali is determined by the Hindu lunar calendar (New Moon night of Kartik month).", "Because winter comes early.", "Because days are shorter.", "Because people light diyas.", "A", "Diwali is based on lunar calendar phases."),
        ("Identify the correct statement about a non-leap year:", "A non-leap year has 365 days and February has 28 days.", "A non-leap year has 366 days.", "February has 30 days.", "A non-leap year occurs every 4 years.", "A", "Standard year has 365 days (Feb = 28 days)."),
        ("A family made 100 diyas in 5 hours. How many diyas did they make per hour?", "20 diyas per hour", "10 diyas", "25 diyas", "15 diyas", "A", "100 / 5 = 20 diyas per hour."),
        ("Which month pair both have 31 days and come right after each other at the end of the year and start of next year?", "December and January", "November and December", "October and November", "January and February", "A", "December (31) and January (31) are consecutive 31-day months across new year.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("People **decorate** their houses with earthen lamps.", "decorate", "people", "houses", "earthen", "A", "'decorate' is the action verb."),
        ("They **light** diyas in the evening.", "light", "they", "diyas", "evening", "A", "'light' is the action verb."),
        ("Families **worship** Shri Ganesh and Maa Laxmi.", "worship", "families", "Shri Ganesh", "Maa Laxmi", "A", "'worship' is the action verb."),
        ("Deities **bless** people with prosperity.", "bless", "deities", "people", "prosperity", "A", "'bless' is the action verb."),
        ("They **offer** laddoos to the gods.", "offer", "they", "laddoos", "gods", "A", "'offer' is the action verb."),
        ("People **celebrate** Diwali with family and friends.", "celebrate", "people", "Diwali", "family", "A", "'celebrate' is the action verb."),
        ("Some children **burst** crackers at night.", "burst", "children", "crackers", "night", "A", "'burst' is the physical action verb."),
        ("Many families **stopped** bursting crackers to protect nature.", "stopped", "families", "crackers", "nature", "A", "'stopped' is the action verb."),
        ("People **distribute** sweets among the poor.", "distribute", "people", "sweets", "poor", "A", "'distribute' is the action verb."),
        ("Diwali **spreads** happiness and light.", "spreads", "Diwali", "happiness", "light", "A", "'spreads' is the action verb."),
        ("Children **draw** rangolis on the floor.", "draw", "children", "rangolis", "floor", "A", "'draw' is the physical action verb."),
        ("They **share** good food and laughter.", "share", "they", "good", "laughter", "A", "'share' is the action verb."),
        ("Families **clean** their homes before Diwali.", "clean", "families", "homes", "before", "A", "'clean' is the physical action verb."),
        ("People **wear** new clothes on Diwali.", "wear", "people", "new", "clothes", "A", "'wear' is the action verb."),
        ("The diyas **brighten** the dark night.", "brighten", "diyas", "dark", "night", "A", "'brighten' is the action verb."),
        ("Children **enjoy** the festival of lights.", "enjoy", "children", "festival", "lights", "A", "'enjoy' is the action verb."),
        ("Neighbors **exchange** gifts and wishes.", "exchange", "neighbors", "gifts", "wishes", "A", "'exchange' is the action verb."),
        ("People **pray** for health and wealth.", "pray", "people", "health", "wealth", "A", "'pray' is the action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH08_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 08:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'Children **happily** **light** **colourful** **diyas**.'", "light", "happily", "colourful", "diyas", "A", "'light' shows physical action; 'happily' is adverb, 'colourful' is adjective, 'diyas' is noun."),
        ("Identify BOTH action verbs in: 'People **clean** their homes and **decorate** them with lights.'", "clean, decorate", "people, homes", "lights, clean", "decorate, homes", "A", "'clean' and 'decorate' are both action verbs."),
        ("What is the past tense action verb of 'light' as used in story ('they lit earthen lamps')?", "lit", "lighted", "lighting", "lights", "A", "Past tense of light is lit (or lighted)."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "We will **light** the earthen lamps now.", "The room has a bright **light**.", "Turn off the **light**.", "That is a blue **light**.", "A", "In (A), 'light' acts as the main action verb."),
        ("Find the action verb in: 'Families worship Shri Ganesh and Maa Laxmi.'", "worship", "families", "Shri Ganesh", "Maa Laxmi", "A", "'worship' is the action verb."),
        ("Which sentence contains NO physical action verb?", "Diwali is the festival of lights.", "People decorate their houses.", "They light earthen lamps.", "They share delicious laddoos.", "A", "'Diwali is the festival of lights' contains linking verb 'is', but no physical action verb."),
        ("Change the action verb 'distribute' to past tense: 'They (distribute) sweets yesterday.'", "distributed", "distributting", "distributes", "distribut", "A", "Past tense of distribute is distributed."),
        ("Identify the action verb: 'People light diyas and share joy.'", "light, share", "people, diyas", "joy, light", "share, diyas", "A", "'light' and 'share' are action verbs."),
        ("Select the action verb that completes the sentence: 'Rangolis ____ the beauty of every home.'", "enhance / decorate", "colourful", "bright", "pattern", "A", "'enhance' / 'decorate' is an action verb."),
        ("Which word is an action verb? (lamps, rangoli, decorate, earthen)", "decorate", "lamps", "rangoli", "earthen", "A", "'decorate' is an action verb; others are nouns/adjectives."),
        ("What action do people perform to spread happiness?", "distribute", "prosperity", "deities", "laddoo", "A", "People distribute sweets and gifts (action verb)."),
        ("Identify the action verb in: 'Families think about safety while celebrating.'", "think", "families", "safety", "celebrating", "A", "'think' is a mental action verb."),
        ("Choose the correct action verb: 'They ____ laddoos to the deities during pooja.'", "offered / served", "sweet", "good", "deity", "A", "'offered' / 'served' is the action verb."),
        ("Identify the action verb in: 'Light conquers darkness on Diwali.'", "conquers", "light", "darkness", "Diwali", "A", "'conquers' is the action verb."),
        ("Which of these words is NOT an action verb? (light, worship, sweet, share)", "sweet", "light", "worship", "share", "A", "'sweet' is an adjective/noun; others are action verbs."),
        ("Identify the action verb in: 'Children burst crackers in the courtyard.'", "burst", "children", "crackers", "courtyard", "A", "'burst' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'Families ____ gifts with their neighbors.'", "exchanged / shared", "bright", "sweet", "house", "A", "'exchanged' / 'shared' is an action verb."),
        ("What action verb completes the sentence? 'Diwali ____ the victory of good over evil.'", "symbolizes / celebrates", "golden", "bright", "light", "A", "'symbolizes' / 'celebrates' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The joyful family beautifully decorated the house and lit earthen diyas.' How many total ACTION VERBS are present?", "2 action verbs ('decorated', 'lit')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'decorated' and 'lit' are action verbs; 'joyful', 'beautifully', 'earthen' are adjectives/adverbs."),
        ("Categorize the verbs: In 'Diwali **is** joyful, so people **light** diyas', classify 'is' and 'light'.", "'is' is a linking verb; 'light' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'is' is action; 'light' is linking.", "A", "'is' links state of being; 'light' shows physical action."),
        ("Replace the weak verb with a strong action verb: 'People **put** diyas around the house.'", "People **illuminated** the house with diyas.", "People **were near** the house.", "People **saw** the house.", "People **looked at** the house.", "A", "'illuminated' is a much stronger, vivid action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "People **clean** their homes, **light** diyas, and **worship** deities.", "Diwali is bright, colorful, and joyful.", "The laddoos are sweet, yellow, and delicious.", "The festival is celebrated in India.", "A", "clean, light, worship are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "People **distribute** sweets to the poor.", "The rangoli was **colourful**.", "The night was **dark**.", "The laddoos were **sweet**.", "A", "'distribute' is an action verb."),
        ("Spot the incorrect verb tense: 'They **lighted** / **light** diyas yesterday.' Correct it for past simple:", "'lit' (or 'lighted') is the past action verb form.", "'light' should be 'lighting'.", "'light' should be 'lights'.", "'light' should be 'will light'.", "A", "Past simple of light is lit (or lighted)."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (clean homes, draw rangoli, light diyas, worship deities)", "clean homes -> draw rangoli -> light diyas -> worship deities", "worship deities -> light diyas -> draw rangoli -> clean homes", "light diyas -> clean homes -> worship deities -> draw rangoli", "draw rangoli -> light diyas -> clean homes -> worship deities", "A", "Chrono preparation: clean, draw rangoli, light diyas, worship."),
        ("Identify the verb error in dialogue: Child said, 'We have **celebrate** Diwali with joy!'", "'celebrate' is incorrect; the past participle form is 'celebrated' ('have celebrated').", "'celebrate' should be 'celebrating'.", "'celebrate' should be 'celebrates'.", "No error.", "A", "Perfect tense requires past participle 'celebrated'."),
        ("Analyze this sentence: 'Diwali **symbolizes** the triumph of light.' What type of action verb is 'symbolizes'?", "Representational/symbolic action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'symbolizes' is an action verb describing symbolic representation."),
        ("Which sentence uses action verbs to show cause and effect?", "People **lit** diyas, so the dark night **became** bright.", "Diwali is the festival of lights and laddoos are sweet.", "Houses are decorated and rangolis are colourful.", "New Moon night is dark.", "A", "'lit' (cause action) -> 'became' (effect action)."),
        ("Spot the missing action verb: 'They ____ colorful powders to make rangoli and ____ laddoos.'", "sprinkled, shared", "bright, sweet", "was, was", "quick, slow", "A", "'sprinkled' and 'shared' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'embrace' in 'We embrace eco-friendly Diwali' considered a RESPONSIBLE action verb?", "Because it describes actively adopting positive, environmentally safe habits.", "Because embracing requires crackers.", "Because Diwali is in autumn.", "Because it is a noun.", "A", "Descriptive action verb conveying responsible adoption."),
        ("Transform the action verb to future tense: 'People **celebrate** Diwali tomorrow.'", "People **will celebrate** Diwali tomorrow.", "People **celebrated** Diwali tomorrow.", "People **are celebrating** Diwali tomorrow.", "People **celebrate** Diwali tomorrow.", "A", "'will celebrate' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The diyas **illuminate** every corner.", "The diyas **illuminates** every corner.", "A diya **illuminate** every corner.", "The diyas **is illuminating** every corner.", "A", "Plural subject 'diyas' takes base verb 'illuminate' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'Diwali is called the festival of lights__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'Which deities are worshipped on Diwali__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a deity's name like 'Shri Ganesh'?", "First letter of each name (e.g., Shri Ganesh)", "The last letter", "All letters", "No letters", "A", "Deity names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'People buy laddoos__ diyas__ and gifts.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden joy: 'Happy Diwali to everyone__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense joy."),
        ("Select the proper noun that MUST start with a capital letter:", "Diwali", "lamp", "house", "sweet", "A", "'Diwali' as a proper festival name starts with capital 'D'."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'maa Laxmi is worshipped on Diwali.'", "maa -> Maa", "worshipped -> Worshipped", "diwali -> Diwali", "is -> Is", "A", "Divine title 'Maa' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'Diwali is celebrated on the New Moon night [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which deity name is capitalized correctly?", "Maa Laxmi", "maa laxmi", "Maa laxmi", "MAA LAXMI", "A", "Capital letters for proper divine name."),
        ("What mark goes after a speaker tag: 'Mother said__ \"Let us light the diyas!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i love eating laddoos.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "People decorate their houses with rangoli.", "People decorate their houses with rangoli?", "People decorate their houses with rangoli,", "People decorate their houses with rangoli;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **family's** celebration'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which festival name is capitalized correctly?", "Deepavali", "deepavali", "Deepavali", "DEEPAVALI", "A", "Proper festival names are capitalized."),
        ("What punctuation mark is used around spoken greetings: '___Happy Diwali!___'", "Quotation marks / Speech marks ( \" \" )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Speech marks enclose spoken greetings.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH08_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "People worship Shri Ganesh and Maa Laxmi on Diwali.", "people worship shri ganesh and maa laxmi on diwali.", "People worship shri ganesh and Maa laxmi on diwali?", "people Worship Shri Ganesh And Maa Laxmi On Diwali.", "A", "Shri Ganesh, Maa Laxmi (deities), Diwali (festival) capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Why do people light earthen lamps on Diwali?", "Why do people light earthen lamps on Diwali.", "Why do people light earthen lamps on Diwali!", "Why do people light earthen lamps on Diwali,", "A", "Question starting with 'Why' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'diwali is celebrated on the New Moon night.'", "'diwali' should be capitalized ('Diwali'); 'New Moon' is correct.", "'New Moon' should be lowercase.", "'night' should be capitalized.", "No mistake.", "A", "Festival name 'Diwali' must be capitalized."),
        ("Choose the correctly punctuated dialogue sentence:", "\"Let's make a colourful rangoli,\" said Sita.", "let's make a colourful rangoli said Sita.", "\"Let's make a colourful rangoli\" said Sita", "Let's make a colourful rangoli, said Sita.", "A", "Quotation marks around dialogue, comma inside quote, capital L."),
        ("Identify where a COMMA is missing: 'They bought diyas laddoos and electric lights.'", "Between 'diyas' and 'laddoos' ('diyas, laddoos')", "After 'They'", "After 'lights'", "No comma needed", "A", "Commas separate items in list: 'diyas, laddoos and electric lights'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is Shri Ganesh's blessing.", "This is Shri Ganeshs' blessing.", "This is Shri Ganeshs blessing.", "This is Shri Ganesh's' blessing.", "A", "Ganesh's indicates possession."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a bright and beautiful festival Diwali is!", "What a bright and beautiful festival Diwali is?", "What a bright and beautiful festival Diwali is.", "What a bright and beautiful festival Diwali is,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'do not'?", "don't", "do'nt", "dont'", "d'ont", "A", "don't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "Shri Ganesh and Maa Laxmi bless every home on Diwali.", "shri ganesh and maa laxmi bless every home on diwali.", "Shri Ganesh And Maa Laxmi Bless Every Home On Diwali.", "shri Ganesh and Maa Laxmi bless home on Diwali.", "A", "'Shri Ganesh', 'Maa Laxmi', and 'Diwali' capitalized as proper nouns."),
        ("What punctuation mark belongs in the blank? 'Father exclaimed, \"Happy Diwali__ May your life be full of light!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses festive joy."),
        ("Choose the correct form for 'cannot':", "can't", "ca'nt", "cant'", "c'ant", "A", "can't is standard contraction."),
        ("Identify the punctuation error: 'We lit the diyas, we distributed sweets.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for names and festivals:", "People celebrate Deepavali in India with great joy.", "people celebrate deepavali in india with great joy.", "People celebrate deepavali in India with great joy.", "people Celebrate Deepavali in india with great joy.", "A", "Names 'Deepavali', 'India' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The family's house was decorated beautifully.", "The familys' house was decorated beautifully.", "The familys house was decorated beautifully.", "The family's' house was decorated beautifully.", "A", "family's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'The altar had ____'", "flowers, laddoos, and diyas.", "flowers laddoos and diyas.", "flowers; laddoos; and diyas.", "flowers: laddoos: and diyas.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "Why is Diwali called the festival of lights?", "Why is Diwali called the festival of lights.", "Why is Diwali called the festival of lights!", "why is Diwali called the festival of lights.", "A", "Capital W, ends with question mark ?"),
        ("Fix the sentence: 'where are the laddoos placed'", "Where are the laddoos placed?", "Where are the laddoos placed.", "where are the laddoos placed!", "Where are the laddoos placed;", "A", "Capital W, ends with question mark ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Mother said, \"Let us worship Maa Laxmi!\"", "Mother said \"let us worship Maa Laxmi!\"", "mother said, \"Let us worship Maa Laxmi!\"", "Mother said, \"Let us worship Maa Laxmi.\"", "A", "Capital M, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on friday mother said on diwali, lets worship shri ganesh and maa laxmi'", "5 errors (on->On, friday->Friday, diwali->Diwali, lets->let's, capital L in Let's, deity names capitalization, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, festival name, contraction let's, capital L, period."),
        ("Correct the entire dialogue paragraph: 'the child asked why do we light diyas on diwali mother replied to celebrate light over darkness'", "\"Why do we light diyas on Diwali?\" asked the child. Mother replied, \"To celebrate light over darkness.\"", "the child asked \"why do we light diyas on diwali\" mother replied \"to celebrate light over darkness.\"", "The child asked, Why do we light diyas on Diwali. Mother replied, To celebrate light over darkness.", "\"Why do we light diyas on Diwali?\" Asked the child. Mother replied \"To celebrate light over darkness?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'Diwali**'**s lights are bright, and it**'**s a joyful festival.'", "First 's is possessive (lights of Diwali); second 's is contraction (it is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "Diwali's lights = lights of Diwali; it's = it is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"Happy Diwali to all,\" Said Mother.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'Happy' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "Darkness was everywhere, but diyas brought light.", "Darkness was everywhere but, diyas brought light.", "Darkness was everywhere but diyas brought light!", "Darkness was everywhere; but diyas brought light?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'people celebrate diwali on friday 15th november 2026'", "People celebrate Diwali on Friday, 15th November 2026.", "people celebrate diwali on friday, 15th november 2026.", "People celebrate Diwali on Friday 15th November 2026", "People celebrate diwali on friday 15th november 2026.", "A", "People, Diwali, Friday, 15th November 2026, period."),
        ("Identify why exclamation mark is necessary here: '\"Shubh Deepavali! May light fill your home!\"'", "Because the speaker is expressing intense festive blessings and joy.", "Because house is big.", "Because diyas are hot.", "Because sentence is long.", "A", "Exclamation mark communicates intense festive blessings."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Diwali, the festival of lights, is celebrated with great joy.", "Diwali the festival of lights is celebrated with great joy.", "Diwali, the festival of lights is celebrated with great joy.", "Diwali the festival of lights, is celebrated with great joy.", "A", "Appositive phrase 'the festival of lights' is set off by commas."),
        ("Analyze the use of hyphen in: 'We should celebrate an eco-friendly Diwali.'", "Hyphen joins compound adjective (eco-friendly).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Compound adjectives modifying nouns take hyphens."),
        ("Identify the correct sentence with direct speech quote within text:", "Mother said, \"Distribute sweets to everyone,\" and we smiled.", "Mother said \"Distribute sweets to everyone\" and we smiled.", "Mother said, 'Distribute sweets to everyone,' and we smiled.", "Mother said: \"Distribute sweets to everyone\" and we smiled.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'The deities blessings filled the peoples hearts.'", "Missing apostrophes in both 'deities'' and 'people's' -> 'The deities' blessings filled the people's hearts.'", "Missing apostrophe in 'filled''", "Missing apostrophe in 'were''", "No apostrophe needed", "A", "Both 'deities'' (plural possessive) and 'people's' (plural possessive) require apostrophes."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Children, said mother, should light diyas safely.' vs 'Children said, \"Mother should light diyas safely.\"'", "In the first, mother instructs children; in the second, children instruct mother.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is instructed."),
        ("Correct all 4 errors in: 'whats the festivals name asked the child'", "\"What's the festival's name?\" asked the child.", "whats the festivals name? asked the child.", "\"What's the festivals name.\" asked the child.", "\"whats the festivals name?\" Asked the child.", "A", "Quotation marks, capital W, possessive festival's, question mark, period at end."),
        ("Identify the rule for capitalizing major religious festivals like 'Diwali' and 'Deepavali':", "Major festival and holiday names take initial capital letters.", "Festival names are never capitalized.", "Festival names are capitalized only at end of sentence.", "Festival names must be written in ALL CAPS.", "A", "Festival names take initial capitals.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'earthen'** (in Chapter 08)?", "ea", "ee", "ai", "ou", "A", "'ea' is the vowel digraph in earthen."),
        ("Identify the vowel digraph in the word **'deep'** (or Deepavali):", "ee", "ea", "oa", "ui", "A", "'ee' forms the long /e/ vowel sound in deep."),
        ("Which word from the story contains the **'ou'** vowel digraph?", "house", "lamp", "light", "diya", "A", "'house' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'clean'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in clean."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'oo'** vowel digraph: 'Laddoos are delicious sweets.'", "Laddoos", "sweets", "delicious", "are", "A", "'Laddoos' contains 'oo' digraph."),
        ("Which word from the story rhymes with **'light'**?", "bright", "late", "lot", "leak", "A", "'bright' rhymes with 'light'."),
        ("Which word from the story rhymes with **'joy'**?", "toy", "jay", "jew", "jaw", "A", "'toy' rhymes with 'joy'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the story rhymes with **'night'**?", "sight", "neat", "net", "not", "A", "'sight' rhymes with 'night'."),
        ("Identify the vowel digraph in **'voice'**:", "oi", "ea", "ee", "ia", "A", "'oi' is the vowel digraph in voice."),
        ("Which word from Chapter 08 has the **'ea'** digraph making a long /e/ sound?", "peace", "head", "heavy", "dead", "A", "'peace' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letters in **'light'** (as in 'festival of lights'):", "gh", "l", "i", "t", "A", "Silent 'gh' in light."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "bright", "bought", "bowl", "baker", "A", "'igh' in bright makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They cleaned around the house.'", "around", "house", "both A and B", "neither", "C", "Both 'around' and 'house' contain 'ou' digraph."),
        ("Which word rhymes with **'sweet'**?", "treat", "sat", "so", "seat", "A", "'treat' / 'seat' rhymes with 'sweet'."),
        ("Identify the silent letter in the word **'know'** (as in 'did not know'):", "k", "n", "o", "w", "A", "Initial 'k' before 'n' is silent.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH08_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'clean'** and **'bread'**. What is the difference?", "'clean' has long /e/ sound; 'bread' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'clean' has short /e/; 'bread' has long /e/.", "A", "'ea' can make long /e/ (clean) or short /e/ (bread)."),
        ("Select the word pair from Chapter 08 that has the SAME vowel digraph sound:", "deep - sweet", "light - bread", "earthen - roar", "house - sweet", "A", "'deep' and 'sweet' both have 'ee' long /e/ sound."),
        ("Which word contains SILENT letters? (light, diya, lamp, sweet)", "light", "diya", "lamp", "sweet", "A", "'light' has silent 'gh'."),
        ("Identify the odd one out based on vowel sound: (clean, sweet, deep, bread)", "bread", "clean", "sweet", "deep", "A", "'bread' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for oil lamp? 'd__ya'", "i", "ea", "ee", "ou", "A", "'diya' uses vowel 'i'."),
        ("Group these story words by digraph: **house**, **out**, **around**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'Diwali brings wealth and **health**.'", "health", "brings", "Diwali", "wealth", "A", "'health' / 'wealth' contains unvoiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (glow, show, grow, all of these)", "all of these", "glow", "show", "grow", "A", "glow, show, grow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'Laddoo'**:", "oo", "ae", "ur", "or", "A", "'oo' is the vowel digraph in Laddoo."),
        ("Which word from the story has silent **'gh'**? (light, night, bright, all of these)", "all of these", "light", "night", "bright", "A", "light, night, bright all have silent 'gh'."),
        ("Select the word that rhymes with **'night'** and fits sentence: 'The diyas shine so ____.'", "bright", "light", "sight", "white", "A", "'bright' rhymes with 'night'."),
        ("Identify the digraph in **'peaceful'**:", "ea", "ee", "ai", "oa", "A", "'ea' makes long /e/ sound."),
        ("Which word has the short /u/ sound made by **'ou'**? (touch, house, out, shout)", "touch", "house", "out", "shout", "A", "'touch' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'We make rangoli in the **yard**.'", "ar sound", "ea", "ou", "ai", "A", "R-controlled vowel in yard."),
        ("Which word contains the **'oi' / 'oy'** diphthong? (joy, choice, voice, all of these)", "all of these", "joy", "choice", "voice", "A", "joy, choice, voice all contain 'oi'/'oy' diphthong."),
        ("Identify the soft **'c'** sound in Chapter 08 vocabulary: (peace, celebrate, electric, place)", "peace", "electric", "celebrate", "peace, celebrate, place", "D", "peace, celebrate, place all have soft /s/ sound for 'c' before 'e'."),
        ("Which word has a soft **'g'** sound? (gentle, magic, danger, all of these)", "all of these", "gentle", "magic", "danger", "A", "gentle, magic, danger all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ee'** digraph for luminous lamps:", "Deepavali", "Depavali", "Deapavali", "Dipavali", "A", "Deepavali is standard spelling with 'ee'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'celebrate'** sound like /s/, but 'c' in **'cracker'** sounds like /k/?", "Because 'c' followed by 'e', 'i', or 'y' makes soft /s/ sound; before 'r', 'a', 'o', 'u' it makes hard /k/ sound.", "Because celebrate is happy.", "Because cracker is loud.", "There is no rule.", "A", "Soft 'c' rule: c + i, e, y = /s/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (clean, peace, bread, heavy, lead [metal])", "Long /e/: clean, peace; Short /e/: bread, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: bread; Short /e/: clean", "A", "clean, peace make long /e/; bread, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "light - know", "diya - lamp", "sweet - house", "gift - food", "A", "'light' (silent gh) and 'know' (silent k)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "sparkling / spread", "diya", "lamp", "sweet", "A", "'spa' / 'spr' blend types."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'gentle'** but hard in **'good'**?", "'g' followed by 'e', 'i', or 'y' makes soft /j/ sound (gentle); 'g' before 'o' or 'a','u' makes hard /g/ sound (good).", "Because gentle is soft.", "Because good is nice.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "bright", "diya", "lamp", "sweet", "A", "'bright' has 'igh' trigraph with silent 'gh'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'house'**?", "house - out", "voice - coin", "paid - day", "boat - coat", "A", "'house' and 'out' share /ow/ diphthong sound."),
        ("Analyze homophones: 'They lit **diyas** in the **night** / **knight**.' Which word means evening time?", "night", "knight", "nyte", "nite", "A", "'night' (evening/darkness) and 'knight' (armored warrior) are homophones."),
        ("Identify the phonic pattern in **'prosperity'**: What vowel sound does the first 'o' make?", "Short /o/ sound", "Long /o/ sound", "Silent sound", "Short /u/ sound", "A", "'pros-per-i-ty' first 'o' makes short /o/ sound."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (diyas, laddoos, lights, gifts)", "diyas / laddoos", "lights", "gifts", "crackers", "A", "Plurals ending in voiced vowels take /z/ ending sound (diyas, laddoos)."),
        ("Spot the word where 'gh' is SILENT: (light, night, bright, all of these)", "all of these", "light", "night", "bright", "A", "'gh' is silent in light, night, bright."),
        ("HOTS Reasoning: Why do 'sun' and 'son' sound identical but have different spellings and meanings?", "They are homophones (same sound, different spelling/meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share pronunciation but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "doorstep / courtyard", "Diwali", "Laxmi", "rangoli", "A", "doorstep = door + step; courtyard = court + yard."),
        ("Determine the syllable count and stress: How many syllables are in **'synonymous'**?", "4 syllables (sy-non-y-mous)", "3 syllables", "5 syllables", "2 syllables", "A", "sy-non-y-mous has 4 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ is Diwali called?", "What / What else", "Who", "Where", "Why", "A", "'What' asks about alternative name (Deepavali / festival of lights)."),
        ("___ do people light in the evening on Diwali?", "What", "Who", "Where", "When", "A", "'What' asks about items (earthen lamps / diyas)."),
        ("___ is Diwali celebrated?", "When", "Who", "Where", "Why", "A", "'When' asks about time (on New Moon night in autumn)."),
        ("___ deities are worshipped on Diwali evening?", "Which", "Who", "Where", "Why", "A", "'Which' asks about specific gods (Shri Ganesh and Maa Laxmi)."),
        ("___ do people decorate their houses with?", "What", "Who", "Where", "Why", "A", "'What' asks about decorations (rangolis, diyas, electric lights)."),
        ("___ sweet is synonymous with Diwali?", "Which", "Who", "Where", "Why", "A", "'Which' asks about specific sweet (laddoo)."),
        ("___ do people distribute sweets among the poor?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (to spread happiness and light)."),
        ("___ do people celebrate Diwali with?", "Whom / Who", "What", "Where", "Why", "A", "'Whom' asks about companion people (family and friends)."),
        ("___ does Diwali symbolize?", "What", "Who", "Where", "Why", "A", "'What' asks about symbolism (victory of good over evil)."),
        ("___ kind of lamps are lit on Diwali?", "What", "Who", "Where", "Why", "A", "'What kind of' asks about material (earthen lamps / diyas)."),
        ("___ do people pray for during Laxmi Pooja?", "What", "Who", "Where", "Why", "A", "'What' asks about prayers (wealth, health, and prosperity)."),
        ("___ place do people make colorful rangolis?", "Where", "Who", "Why", "When", "A", "'Where' asks about location (at the doorstep / entrance)."),
        ("___ practice have many eco-conscious people stopped?", "What", "Who", "Why", "When", "A", "'What' asks about practice (bursting crackers)."),
        ("___ moral lesson does Diwali teach us?", "What", "Who", "Where", "Why", "A", "'What' asks about lesson (light conquers darkness, good conquers evil)."),
        ("___ diyas did the family light?", "How many", "Who", "Where", "Why", "A", "'How many' asks about quantity."),
        ("___ goddess is worshipped for wealth?", "Which", "What", "Where", "Why", "A", "'Which' asks about deity (Maa Laxmi)."),
        ("___ god is worshipped alongside Maa Laxmi?", "Which", "Who", "Where", "What", "A", "'Which' asks about deity (Shri Ganesh)."),
        ("___ time of day are diyas lit?", "When", "Who", "Where", "Why", "A", "'When' asks about time (in the evening).")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH08_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ do people light diyas on Diwali?' Answer: 'To dispel darkness and bring light into their lives.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('To dispel...')."),
        ("Match question to answer: Question: '___ are the diyas placed?' Answer: 'Around the house and on the doorstep.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ is Laxmi Pooja performed?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time (in the evening of New Moon)."),
        ("Form an asking sentence: 'People light earthen lamps.' -> '____ do people light?'", "What", "Who", "Why", "Where", "A", "'What' inquires about object."),
        ("Identify the INCORRECT question word usage: '**Why** is another name for Diwali?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What is another name for Diwali?' asks for identity."),
        ("Select the proper interrogative sentence:", "Why do people light diyas on Diwali?", "Why people light diyas on Diwali?", "Why do people lit diyas on Diwali?", "Why people lights diyas?", "A", "Interrogative word + auxiliary 'do' + base verb 'light'."),
        ("Which question word asks about MANNER or METHOD? '___ do people decorate their homes for Diwali?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (with rangolis, diyas, and electric lights)."),
        ("Complete the question: '___ of the two deities is worshipped for wisdom and removing obstacles?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options (Shri Ganesh)."),
        ("Change statement to question: 'Diwali symbolizes victory.' -> '____ symbolizes victory?'", "What", "Who", "Where", "Why", "A", "'What' asks for subject (Diwali)."),
        ("Fill in the blank: '___ bright are the electric lights?'", "How", "What", "Where", "Why", "A", "'How bright' measures degree."),
        ("Identify the question word in: 'Whom do people distribute gifts to on Diwali?'", "Whom", "do", "people", "gifts", "A", "'Whom' is the interrogative pronoun asking about object people."),
        ("Choose the question that matches this answer: 'They distribute sweets to spread happiness among the poor.'", "Why do people distribute sweets on Diwali?", "Where do they buy sweets?", "Who makes laddoos?", "What are laddoos?", "A", "'Why...' matches answer starting with 'to spread...'."),
        ("Fill in the blank: '___ sweet is offered during the pooja?'", "Which", "Who", "Why", "Where", "A", "'Which sweet' asks for identification (laddoo)."),
        ("Complete: '___ diyas were placed in the courtyard?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity (diyas)."),
        ("Select the correct question for: 'Diwali celebrates the victory of good over evil.'", "What does Diwali celebrate?", "Where is Diwali celebrated?", "Why do people eat sweets?", "Who is Maa Laxmi?", "A", "'What does Diwali celebrate?' asks for significance."),
        ("Which question word inquires about POSSESSION? '___ house was decorated most beautifully?'", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about ownership."),
        ("Form question: 'Many people celebrate Diwali.' -> '____ people celebrate Diwali?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why do people celebrate Diwali.' Correct it:", "Why do people celebrate Diwali?", "Why do people celebrate Diwali!", "Why do people celebrate Diwali,", "Why do people celebrate Diwali;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why do people light earthen lamps on the New Moon night?' What is the syntax pattern?", "Question Word + Helping Verb (do) + Subject (people) + Main Verb (light) + Object + Prepositional Phrase", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ diyas' vs '___ happiness'", "'How many' for countable diyas; 'How much' for uncountable happiness.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for diyas; 'How many' for happiness.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where people place the earthen lamps?' Correct it:", "Where **do** people place the earthen lamps?", "Where people place earthen lamps?", "Where placed people earthen lamps?", "Where does people place earthen lamps?", "A", "Present simple questions require auxiliary 'do' before plural subject 'people' and base verb 'place'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the festival celebration?", "What is Diwali -> When is it celebrated -> Why do we light diyas -> How do we spread joy to the poor", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals identity, timing, core ritual, and social moral duty."),
        ("Transform the statement into a formal question: 'Sharing sweets with the needy spreads genuine light.'", "How does sharing gifts with the poor fulfill the true spirit of Diwali?", "Where is India?", "Who is Ganesh?", "What is a laddoo?", "A", "Directly targets the moral lesson."),
        ("Analyze this ambiguous question: 'What do people do?' How can it be made precise?", "Add specific context: 'What ritual decorations do families prepare on the evening of Diwali?'", "Make it shorter: 'What people?'", "Change to: 'Where people?'", "Remove 'What'.", "A", "Adding specific context clarifies which ritual."),
        ("Choose the correct question pair for dialogue: Child: '___ are we lighting diyas tonight?' Mother: '___ about placing one on every window sill?'", "Why, How", "Who, Where", "Where, How", "When, Whose", "A", "Why (reason for lighting diyas), How about (suggestion)."),
        ("Spot the DOUBLE auxiliary error: 'Why do people lit crackers on Diwali?'", "'do' requires base verb 'light', not past tense 'lit'.", "'do' should be 'is'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'do' must be followed by base form of verb ('light')."),
        ("Reconstruct question from answer: Answer: 'Diwali is celebrated on the New Moon night of Kartik month.'", "Question: 'On which lunar night is Diwali celebrated?'", "Question: 'Where did they go?'", "Question: 'Who ate laddoos?'", "Question: 'Why is rangoli colourful?'", "A", "Targets lunar timing."),
        ("Form indirect question: 'The child asked why diyas are lit on Diwali.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ is an eco-friendly celebration better for society?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the ecological reason."),
        ("HOTS Reasoning: Why is 'Who' used for people/gods but 'Which' used when selecting from a specific set of sweets?", "'Who' is general for persons/deities; 'Which' is used when choosing from a defined limited set of items.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the sweets...' selects from a defined group."),
        ("Correct all errors in: 'why do people light diyas on diwali'", "Why do people light diyas on Diwali?", "Why do people light diyas on diwali.", "Whom do people light diyas?", "Why does people light diyas on Diwali?", "A", "Capital W, capital D, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 08:", "How does the transition from bursting noisy crackers to sharing sweets with the poor reflect a deeper understanding of Diwali's moral message?", "What sweet is offered?", "Where are diyas placed?", "Is Diwali a festival?", "A", "Asks student to evaluate moral synthesis and environmental awareness.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The family is **decorating** the house with diyas.", "decorating", "family", "is", "diyas", "A", "'decorating' is verb + -ing form."),
        ("Children are **lighting** earthen lamps in the evening.", "lighting", "children", "are", "evening", "A", "'lighting' is verb + -ing form."),
        ("Mother is **making** a colourful rangoli.", "making", "mother", "is", "rangoli", "A", "'making' is verb + -ing form."),
        ("People are **worshiping** Shri Ganesh and Maa Laxmi.", "worshiping", "people", "are", "deities", "A", "'worshiping' is verb + -ing form."),
        ("The priest is **offering** laddoos to the deities.", "offering", "priest", "is", "deities", "A", "'offering' is verb + -ing form."),
        ("Families are **celebrating** Diwali with joy.", "celebrating", "families", "are", "joy", "A", "'celebrating' is verb + -ing form."),
        ("People are **distributing** sweets among the poor.", "distributing", "people", "are", "poor", "A", "'distributing' is verb + -ing form."),
        ("The diyas are **glowing** brightly at night.", "glowing", "diyas", "are", "night", "A", "'glowing' is verb + -ing form."),
        ("Children are **enjoying** the festive food.", "enjoying", "children", "are", "food", "A", "'enjoying' is verb + -ing form."),
        ("They are **sharing** gifts with friends.", "sharing", "they", "are", "friends", "A", "'sharing' is verb + -ing form."),
        ("Father is **hanging** electric lights on the walls.", "hanging", "father", "is", "walls", "A", "'hanging' is verb + -ing form."),
        ("People are **spreading** happiness in their neighborhood.", "spreading", "people", "are", "neighborhood", "A", "'spreading' is verb + -ing form."),
        ("Children are **wearing** colorful new clothes.", "wearing", "children", "are", "clothes", "A", "'wearing' is verb + -ing form."),
        ("The community is **organizing** an eco-friendly Diwali.", "organizing", "community", "is", "Diwali", "A", "'organizing' is verb + -ing form."),
        ("Neighbors are **wishing** each other a Happy Diwali.", "wishing", "neighbors", "are", "Diwali", "A", "'wishing' is verb + -ing form."),
        ("Mother is **preparing** delicious laddoos in the kitchen.", "preparing", "mother", "is", "kitchen", "A", "'preparing' is verb + -ing form."),
        ("The children are **drawing** patterns on the floor.", "drawing", "children", "are", "floor", "A", "'drawing' is verb + -ing form."),
        ("People are **praying** for wealth and prosperity.", "praying", "people", "are", "prosperity", "A", "'praying' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH08_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'decorate'**? (She is ____ the house.)", "decorating (drop final silent e)", "decorateing", "decoratting", "decoratng", "A", "Drop final silent 'e' before adding -ing (decorating)."),
        ("What is the correct -ing spelling rule for **'light'**? (He is ____ the diya.)", "lighting (add -ing)", "lighteing", "lighttng", "lightng", "A", "Regular verb adding -ing (lighting)."),
        ("What is the correct -ing spelling rule for **'make'**? (Mother is ____ rangoli.)", "making (drop final silent e)", "makeing", "makking", "makng", "A", "Drop final silent 'e' before adding -ing (making)."),
        ("Fill in the blank with present continuous form: 'People (distribute) ____ sweets to the poor.'", "are distributing", "was distribute", "is distribute", "are distributed", "A", "Plural subject takes 'are distributing'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The family is celebrating Diwali tonight.", "The family celebrated Diwali last year.", "The family will celebrate Diwali next month.", "The family celebrated yesterday.", "A", "'is celebrating' is present continuous."),
        ("Fill in the blanks: 'The children ____ (light) diyas, and mother ____ (make) laddoos.'", "are lighting, is making", "is lighting, are making", "are light, is make", "was lighting, were making", "A", "Plural 'children' takes 'are lighting'; singular 'mother' takes 'is making'."),
        ("Identify the spelling mistake in: 'People are **makeing** rangolis.'", "'makeing' should be 'making'", "'makeing' should be 'making'", "'are' should be 'is'", "No mistake", "A", "Make drops silent e before -ing (making)."),
        ("Select the correct -ing form for **'prepare'**:", "preparing", "prepareing", "preparring", "preparng", "A", "Drop silent 'e': prepare -> preparing."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "Mother is offering laddoos to Shri Ganesh.", "Mother offered laddoos yesterday.", "Mother offers laddoos every Diwali.", "Mother will offer laddoos tomorrow.", "A", "Present continuous ('is offering') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (draw) a colorful rangoli at the entrance.'", "am drawing", "is drawing", "are drawing", "am draweing", "A", "Subject 'I' takes 'am drawing'."),
        ("Choose the correct form: 'The people ____ (worship) Maa Laxmi for blessings.'", "are worshiping", "is worshiping", "am worshiping", "are worship", "A", "Plural subject 'people' takes 'are worshiping'."),
        ("Identify the verb in: 'Why are you bursting crackers?'", "are bursting", "Why", "you", "crackers", "A", "Helping verb 'are' + main verb 'bursting' form present continuous."),
        ("What is the -ing form of **'burst'**?", "bursting", "bursteing", "burstting", "burstng", "A", "Regular verb adding -ing (bursting)."),
        ("What is the -ing form of **'share'**?", "sharing", "shareing", "sharring", "sharng", "A", "Drop silent e: share -> sharing."),
        ("Change simple present to continuous: 'Families light diyas.' -> 'Families ____ diyas.'", "are lighting", "lit", "were lighting", "will light", "A", "are lighting."),
        ("Fill in the blank: 'The atmosphere ____ (becoming) bright with lights.'", "is becoming", "are becoming", "am becoming", "became", "A", "is becoming."),
        ("Identify the correct present continuous sentence:", "Look! The diyas are glowing beautifully on the porch.", "Look! The diyas glow beautifully on the porch.", "Look! The diyas glowed beautifully on the porch.", "Look! The diyas glowing beautifully on the porch.", "A", "Exclamation 'Look!' introduces action happening now ('are glowing')."),
        ("Select the correct -ing form for **'celebrate'**:", "celebrating", "celebrateing", "celebratting", "celebratng", "A", "Drop silent e: celebrate -> celebrating.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (run, decorate, light)", "run -> running (double consonant), decorate -> decorating (drop e), light -> lighting (add -ing)", "All just add -ing.", "All double the last letter.", "run -> runing, decorate -> decorateing, light -> lighteing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'People lit diyas while children played.'", "People are lighting diyas while children are playing.", "People lighting while children playing.", "People were lighting while children played.", "People will light while children play.", "A", "Both verbs transformed to present continuous (are lighting, are playing)."),
        ("Spot the missing auxiliary verb in: 'Mother decorating the house and children lighting diyas.' Correct it:", "'Mother **is** decorating the house and children **are** lighting diyas.'", "'Mother decorating house and children lighting diyas.'", "'Mother **are** decorating and children **is** lighting diyas.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'People are **wishing** for prosperity' when stating general beliefs?", "Because 'wish' can act as a stative desire, though continuous is used for active prayer scenes; in general facts, simple present is preferred.", "Because 'wishing' is hard to spell.", "Because laddoos are sweet.", "Because diyas burn.", "A", "Stative verbs expressing ongoing state take simple present for general facts."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The children of the family are drawing rangolis.", "The children of the family is drawing rangolis.", "The children of the family am drawing rangolis.", "The children of the family drawing rangolis.", "A", "Plural subject ('children') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'People are bursting crackers tonight.' -> Negative:", "People are **not** bursting crackers tonight.", "People not bursting crackers tonight.", "People is no bursting crackers tonight.", "People aren't burst crackers tonight.", "A", "Add 'not' between auxiliary 'are' and main verb 'bursting'."),
        ("Spot all THREE spelling errors: 'She is **makeing** rangolis, **runing** fast, and **dieing** of happiness.'", "'makeing' -> 'making'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'makeing' -> 'makking'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "making (drop e), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'Families are worshipping the deities.'", "**Are** families worshipping the deities?", "Is families worshipping the deities?", "Families worshipping the deities?", "Why families are worshipping deities?", "A", "Move auxiliary 'Are' to beginning of sentence."),
        ("Analyze action timeline: 'The sweet shop **is delivering** laddoos tomorrow.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While mother is making rangoli, father is hanging electric lights.", "While mother made, father is hanging.", "Mother is making while father hung.", "Mother make while father hang.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'Children are lightting diyas.'", "'lightting' should be 'lighting' (single 't').", "'are' should be 'is'.", "'diyas' should be capitalized.", "No error.", "A", "Light + ing = lighting."),
        ("HOTS Reasoning: Compare 'People lit diyas' (Past Simple) vs 'People are lighting diyas' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means diyas went out.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the families ____ (sharing) sweets with neighbors?'", "are, sharing", "is, sharing", "am, sharing", "do, sharing", "A", "Plural subject families takes 'are ... sharing'."),
        ("Identify the correct present continuous sentence describing festive preparation:", "The entire neighborhood is celebrating Diwali together.", "The entire neighborhood is celebrate Diwali together.", "The entire neighborhood are celebrating Diwali together.", "The entire neighborhood celebrating Diwali together.", "A", "Collective singular subject 'neighborhood' + is + celebrating.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 08: Diwali\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("Diwali ___ the festival of lights.", "is", "are", "am", "be", "A", "Singular subject 'Diwali' takes 'is'."),
        ("I ___ excited for Diwali celebrations.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The earthen lamps ___ glowing in the dark.", "are", "is", "am", "be", "A", "Plural subject 'earthen lamps' takes 'are'."),
        ("The rangoli ___ colourful and beautiful.", "is", "are", "am", "be", "A", "Singular subject 'rangoli' takes 'is'."),
        ("The laddoos ___ sweet and tasty.", "are", "is", "am", "be", "A", "Plural subject 'laddoos' takes 'are'."),
        ("Shri Ganesh ___ worshipped for wisdom.", "is", "are", "am", "be", "A", "Singular subject 'Shri Ganesh' takes 'is'."),
        ("The children ___ lighting diyas with care.", "are", "is", "am", "be", "A", "Plural subject 'children' takes 'are'."),
        ("Shri Ganesh and Maa Laxmi ___ the worshipped deities.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ happy to share sweets with everyone.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The New Moon night ___ dark, but diyas make it bright.", "is", "are", "am", "be", "A", "Singular 'night' takes 'is'."),
        ("The gifts ___ ready to be distributed.", "are", "is", "am", "be", "A", "Plural 'gifts' takes 'are'."),
        ("The house ___ decorated with electric lights.", "is", "are", "am", "be", "A", "Singular 'house' takes 'is'."),
        ("You ___ celebrating Diwali with family.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("Mother ___ preparing sweets in the kitchen.", "is", "are", "am", "be", "A", "Singular 'Mother' takes 'is'."),
        ("The sweets ___ distributed among the poor.", "are", "is", "am", "be", "A", "Plural 'sweets' takes 'are'."),
        ("I ___ grateful for wealth and health.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The celebration ___ full of joy and laughter.", "is", "are", "am", "be", "A", "Singular 'celebration' takes 'is'."),
        ("The neighbours ___ exchanging warm wishes.", "are", "is", "am", "be", "A", "Plural 'neighbours' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH08_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'Shri Ganesh and Maa Laxmi ____ worshipped on Diwali evening.'", "are", "is", "am", "be", "A", "Compound subject ('Shri Ganesh and Maa Laxmi') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "Diwali is celebrated with great joy.", "Diwali are celebrated with great joy.", "Diwali am celebrated with great joy.", "Diwali be celebrated with great joy.", "A", "Singular noun 'Diwali' requires 'is'."),
        ("Fill in the blanks: 'I ____ making a rangoli, and my sisters ____ lighting diyas.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'sisters are'."),
        ("Identify the mistake in: 'The laddoos on the tray **is** delicious.'", "'is' should be 'are' because 'laddoos' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'laddoos' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you ready for the Diwali pooja?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither crackers nor noise ____ needed for a happy Diwali.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject 'noise' takes 'is'."),
        ("Select the correct sentence for story moral:", "Goodness and light are victorious over evil.", "Goodness and light is victorious over evil.", "Goodness and light am victorious over evil.", "Goodness and light be victorious over evil.", "A", "Compound subject 'Goodness and light' takes 'are'."),
        ("Complete the conversation: Child: 'Where ____ the diyas?' Mother: 'They ____ in the basket!'", "are, are", "is, is", "is, are", "are, is", "A", "Plural 'the diyas' -> are; plural 'They' -> are."),
        ("Identify where 'is' is used incorrectly:", "The diyas **is** bright.", "The rangoli is beautiful.", "Diwali is festive.", "The sweet is tasty.", "A", "'The diyas is' should be 'The diyas are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The family ____ gathering for pooja.'", "is", "are", "am", "be", "A", "Collective noun 'family' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The New Moon night ____ illuminated by thousands of diyas.'", "is", "are", "am", "be", "A", "Singular 'night' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am eating a delicious laddoo.", "I is eating a delicious laddoo.", "I are eating a delicious laddoo.", "I be eating a delicious laddoo.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many earthen lamps on the porch.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many earthen lamps'."),
        ("Fill in the blank: 'There ____ a grand rangoli at the main gate.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a grand rangoli'."),
        ("Choose the correct sentence:", "What are the children doing on Diwali evening?", "What is the children doing on Diwali evening?", "What am the children doing on Diwali evening?", "What be the children doing on Diwali evening?", "A", "Plural subject 'the children' takes 'are'."),
        ("Identify the correct form: 'The host, as well as the guests, ____ enjoying the festival.'", "is", "are", "am", "be", "A", "Subject is singular 'The host' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both Shri Ganesh and Maa Laxmi ____ worshipped together.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The diyas ____ earthen, but the electric lights ____ modern.'", "are, are", "is, is", "am, are", "is, are", "A", "'diyas are', 'electric lights are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH08_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the earthen diyas **____** lit with oil.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'earthen diyas' is plural.", "am — because it refers to speaker.", "be — because diyas are bright.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A box of sweet laddoos **are** kept on the altar.'", "'are' should be 'is' because the subject is singular noun 'box'.", "'are' should be 'am'.", "'laddoos' should be 'laddoo'.", "No error.", "A", "'A box' is singular, so it requires 'is kept'."),
        ("Compare: (1) 'Shri Ganesh and Maa Laxmi **are** worshipped.' vs (2) 'Shri Ganesh, along with Maa Laxmi, **is** worshipped.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'Shri Ganesh' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone in the neighborhood **____** celebrating Diwali.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The laddoos **is** sweet, I **is** happy, and the diyas **is** bright.'", "'laddoos is' -> 'laddoos are'; 'I is' -> 'I am'; 'diyas is' -> 'diyas are'", "'laddoos is' -> 'laddoos am'; 'I is' -> 'I are'; 'diyas is' -> 'diyas am'", "Only 'I is' is wrong.", "No errors present.", "A", "laddoos are (plural), I am (1st person), diyas are (plural)."),
        ("Fill in the blanks in this complex sentence: 'Not only the parents but also the child **____** lighting diyas, while neighbors **____** watching.'", "is, are", "are, is", "is, is", "are, are", "A", "'Not only...but also' agrees with closer singular subject ('child' -> is); 'neighbors' -> are."),
        ("Transform to negative: 'The diyas and electric lights are bright.'", "The diyas and electric lights **are not** bright.", "The diyas and electric lights is not bright.", "The diyas and electric lights am not bright.", "The diyas and electric lights not bright.", "A", "Add 'not' after plural helping verb 'are'."),
        ("Analyze inverted subject position: 'On the doorstep **____** placed colorful rangolis.'", "are", "is", "am", "be", "A", "Subject is plural 'colorful rangolis', appearing after verb, requiring 'are'."),
        ("Determine agreement with uncountable nouns: 'The darkness of the night **____** dispelled by diyas.'", "is", "are", "am", "be", "A", "Uncountable noun 'darkness' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the earthen diyas you ordered.'", "Here **are** the earthen diyas you ordered.", "Here am the earthen diyas you ordered.", "Here be the earthen diyas you ordered.", "No error.", "A", "Plural subject 'earthen diyas' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "Diwali **is** the festival of lights.", "Diwali **is** spreading happiness.", "Mother **is** lighting diyas.", "Father **is** buying laddoos.", "A", "In 'Diwali is the festival of lights', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because Diwali is bright.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither crackers nor pollution **____** necessary, because love **____** enough.'", "is, is", "are, is", "is, are", "are, are", "A", "'pollution' is singular closer subject -> is; 'love' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "Diwali is joyful, I am happy, and the diyas are bright.", "Diwali are joyful, I is happy, and the diyas is bright.", "Diwali am joyful, I are happy, and the diyas am bright.", "Diwali is joyful, I is happy, and the diyas is bright.", "A", "Diwali is (singular), I am (1st person), diyas are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH08_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 08
# ---------------------------------------------------------------------------
def rebuild_chapter_08():
    print("Rebuilding Chapter 08 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH08_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 08 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_08()
