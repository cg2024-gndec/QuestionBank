r"""
=============================================================================
Script: rebuild_chapter_09.py
Description: Generates 50 rich, non-duplicate, multi-tiered (Easy, Medium, Hard)
             questions for each of the 9 category files in Chapter 09:
             "The Himalayas" (450 Qs total).
=============================================================================
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH09_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_09")
os.makedirs(CH09_DIR, exist_ok=True)

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
    header = "# Category 1: Plural Nouns & Spelling Rules — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("mountain", "mountains", "mountaines", "mountainies", "mountainz", "A", "Regular noun adding -s."),
        ("peak", "peaks", "peakes", "peakies", "peakz", "A", "Regular noun adding -s."),
        ("river", "rivers", "riveres", "riveries", "riverz", "A", "Regular noun adding -s."),
        ("kilometer", "kilometers", "kilometeres", "kilometeries", "kilometerz", "A", "Regular noun adding -s."),
        ("meter", "meters", "meteres", "meteries", "meterz", "A", "Regular noun adding -s."),
        ("climber", "climbers", "climberes", "climberies", "climberz", "A", "Regular noun adding -s."),
        ("mountaineer", "mountaineers", "mountaineeres", "mountaineeries", "mountaineerz", "A", "Regular noun adding -s."),
        ("border", "borders", "borderes", "borderies", "borderz", "A", "Regular noun adding -s."),
        ("region", "regions", "regiones", "regionies", "regionz", "A", "Regular noun adding -s."),
        ("range", "ranges", "rangies", "rangees", "rangez", "A", "Regular noun ending in -e adds -s."),
        ("country", "countries", "countrys", "countryes", "countriz", "A", "Consonant + y changes to -ies."),
        ("valley", "valleys", "valleies", "valleyes", "valleyz", "A", "Vowel + y adds -s."),
        ("year", "years", "yeares", "yearies", "yearz", "A", "Regular noun adding -s."),
        ("day", "days", "daies", "dayes", "dayz", "A", "Vowel + y adds -s."),
        ("glacier", "glaciers", "glacieres", "glacieries", "glacierz", "A", "Regular noun adding -s."),
        ("summit", "summits", "summites", "summities", "summitz", "A", "Regular noun adding -s."),
        ("person", "people", "persons", "peoples", "persones", "A", "Irregular plural: person becomes people."),
        ("child", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children.")
    ]
    
    for idx, (word, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH09_CAT01_Q{idx:02d}"
        qtxt = f"What is the correct plural form of the noun **'{word}'** from or related to Chapter 09 (*The Himalayas*)?"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Plural Noun Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The Himalayas have lofty snow-covered (peak / peaks).", "peaks", "peak", "peakes", "peakies", "A", "Plural noun 'peaks'."),
        ("Three important (river / rivers) originate in the Himalayas.", "rivers", "river", "riveres", "riveries", "A", "'three' requires plural noun 'rivers'."),
        ("Mount Everest lies between two (country / countries).", "countries", "country", "countrys", "countryes", "A", "Consonant + y changes to -ies (countries)."),
        ("Identify the INCORRECT plural spelling in this list: mountains, rivers, countrys, glaciers.", "countrys", "mountains", "rivers", "glaciers", "A", "Plural of country is 'countries', not 'countrys'."),
        ("Choose the sentence with the correct plural noun form:", "Nine of Earth's highest peaks are Himalayan.", "Nine of Earth's highest peakes are Himalayan.", "Nine of Earth's highest peakies are Himalayan.", "Nine of Earth's highest peakz are Himalayan.", "A", "peaks is the correct plural of peak."),
        ("Which noun forms its plural by changing consonant + y to -ies?", "country -> countries", "valley -> valleys", "peak -> peaks", "river -> rivers", "A", "Country ends in consonant + y, so plural is countries."),
        ("Change the singular noun in brackets to plural: 'The mountaineers climbed many ____ (glacier).' ", "glaciers", "glacieres", "glacieries", "glacierz", "A", "Regular noun adding -s (glaciers)."),
        ("Select the sentence where ALL plural nouns are spelt correctly:", "The climbers crossed rivers and valleys.", "The climberes crossed rivers and valleies.", "The climbers crossed riveres and valleyes.", "The climberees crossed rivers and vallez.", "A", "climbers, rivers, valleys are all correctly spelt plurals."),
        ("What is the correct plural of 'mountain range'?", "mountain ranges", "mountain rangies", "mountain rangees", "mountain rangez", "A", "Regular noun ending in -e adds -s."),
        ("The Himalayas have stood for millions of (year / years).", "years", "yeares", "yearies", "yearz", "A", "Regular noun adding -s (years)."),
        ("The snow covers the lofty (peak / peaks) all year round.", "peaks", "peakes", "peakies", "peakz", "A", "Plural of peak is peaks."),
        ("Many (person / people) attempt to climb Mount Everest.", "people", "persons", "peoples", "persones", "A", "Irregular plural of person is people."),
        ("How many (kilometer / kilometers) do the Himalayas stretch?", "kilometers", "kilometer", "kilometeres", "kilometeries", "A", "Plural noun 'kilometers'."),
        ("The two (mountaineer / mountaineers) reached the summit.", "mountaineers", "mountaineer", "mountaineeres", "mountaineeries", "A", "Plural of mountaineer is mountaineers."),
        ("Which plural noun rule applies to the word **'boxes'**?", "Add -es to nouns ending in -x", "Add -s to vowel + y", "Change -f to -ves", "Change -y to -ies", "A", "Box ends in -x, so it adds -es."),
        ("They took many (photo / photos) at the top.", "photos", "photoes", "photies", "photoz", "A", "Regular noun adding -s (photos)."),
        ("Identify the correct plural form of 'child':", "children", "childs", "childes", "childrens", "A", "Irregular plural: child becomes children."),
        ("The Indus and Ganges are major (waterway / waterways).", "waterways", "waterwaies", "waterwayes", "waterwayz", "A", "Vowel + y adds -s (waterways).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT01_Q{idx:02d}"
        qtxt = f"Contextual Plural Rule Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Plural Noun Application", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Rewrite the sentence in PLURAL form: 'The climber crossed a river in the valley.'", "The climbers crossed rivers in the valleys.", "The climberes crossed riveres in the valleies.", "The climbers crossed river in the valleys.", "The climberees crossed rivers in the valleyz.", "A", "Plural of climber->climbers, river->rivers, valley->valleys."),
        ("Analyze the error: 'The Himalayas have much snows.' Why is 'snows' inappropriate here?", "'snow' is an uncountable material noun, so singular 'snow' should be used.", "'snows' should be 'snowes'.", "'snows' should be 'snowies'.", "No error.", "A", "Mass nouns like snow do not normally take plural form."),
        ("Complete the paragraph with correct plurals: 'The two ____ (mountaineer) explored three ____ (peak) across two ____ (country).'", "mountaineers, peaks, countries", "mountaineeres, peakes, countrys", "mountaineers, peak, countriz", "mountaineeres, peaks, countries", "A", "mountaineers (-s), peaks (-s), countries (-y -> -ies)."),
        ("Identify the sentence where ALL three underlined nouns are correctly pluralized:", "The **mountaineers** crossed **glaciers** and **valleys**.", "The **mountaineeres** crossed **glacieries** and **valleies**.", "The **mountaineers** crossed **glacieres** and **valleyes**.", "The **mountaineerees** crossed **glaciers** and **vallez**.", "A", "mountaineers (-s), glaciers (-s), valleys (vowel + y -> -s)."),
        ("Which group contains ONLY irregular plural nouns?", "children, people, men, feet", "mountains, peaks, rivers, glaciers", "countries, valleys, cities, armies", "leaves, thieves, wolves, knives", "A", "children, people, men, feet change forms without standard -s/-es."),
        ("Why does 'valley' become 'valleys' but 'country' becomes 'countries'?", "Because 'valley' has a vowel before y (e+y -> -s), while 'country' has a consonant before y (r+y -> -ies).", "Because 'valley' is short and 'country' is long.", "Because 'valley' is land and 'country' is nation.", "Both follow the exact same rule.", "A", "Vowel+y adds -s; Consonant+y changes y to -ies."),
        ("Find the TWO grammatical mistakes in: 'The two mountaineeres saw many mouses near the camp.'", "'mountaineeres' should be 'mountaineers' and 'mouses' should be 'mice'.", "'mountaineeres' should be 'mountaineer' and 'mouses' should be 'mices'.", "'camp' should be 'camps' only.", "There are no mistakes in the sentence.", "A", "mountaineers (regular -s) and mice (irregular plural)."),
        ("Replace the singular words in brackets: 'The climbers wiped their ____ (hand) and rested their ____ (foot).'", "hands, feet", "handes, foots", "hands, feets", "handies, foots", "A", "Plural of hand is hands, plural of foot is feet."),
        ("Analyze this sentence: 'The mountains provide water.' Can 'water' be pluralized as 'waters' in general contexts?", "No, 'water' is an uncountable material noun; 'waters' is only used in special literary contexts for bodies of water.", "Yes, 'waters' is standard.", "No, it becomes 'wateress'.", "Yes, 'a water' is correct.", "A", "Water is an uncountable mass noun."),
        ("Fill in the blanks: 'The two ____ (climber) reached three ____ (summit) of the mountain.'", "climbers, summits", "climberes, summites", "climbers, summities", "climberes, summits", "A", "climber -> climbers; summit -> summits."),
        ("Select the option that shows correct plural transformation for ALL three words: 'shelf', 'city', 'box'", "shelves, cities, boxes", "shelfs, citys, boxs", "shelves, cityes, boxies", "shelfes, cities, foxen", "A", "shelf -> shelves; city -> cities; box -> boxes."),
        ("HOTS Reasoning: Why do we say 'snow covers the peak' rather than 'snows cover the peak'?", "Because 'snow' is an uncountable mass noun taking a singular verb.", "Because snow is cold.", "Because Mount Everest is tall.", "Because Nepal is near.", "A", "Uncountable mass noun takes singular verb."),
        ("Transform into singular: 'The mountaineers climbed the peaks in the countries.'", "The mountaineer climbed the peak in the country.", "The mountaineers climbed the peak in the country.", "The mountaineer climb the peak in the country.", "The mountaineer climbed the peaks in the country.", "A", "Singular forms: mountaineer, peak, country."),
        ("Identify the correct rule for forming the plural of **'peak'**:", "Add -s because it is a regular noun ending in a consonant (peaks).", "Add -es (peakes).", "Change -k to -ves (peavs).", "Change vowel sound.", "A", "Regular noun adding -s.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT01_Q{idx:02d}"
        qtxt = f"Higher Order Thinking Skills (HOTS) & Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Plural & Spelling Analysis", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 2. Articles Grammar (50 Qs)
# ---------------------------------------------------------------------------
def build_articles_grammar():
    header = "# Category 2: Articles (A, An, The) — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_data = [
        ("___ Himalayas are the highest mountain range in the world.", "The", "A", "An", "No article", "A", "Mountain ranges take definite article 'The'."),
        ("Mount Everest is ___ lofty peak in Asia.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'lofty'."),
        ("___ Indus is an important river.", "The", "A", "An", "No article", "A", "River names take definite article 'The'."),
        ("___ Ganges originates in the Himalayas.", "The", "A", "An", "No article", "A", "River names take definite article 'The'."),
        ("___ Brahmaputra flows through India.", "The", "A", "An", "No article", "A", "River names take definite article 'The'."),
        ("___ Panchatantra/Geography lesson teaches us about mountains.", "A", "An", "The", "No article", "A", "Use 'A' before consonant sound 'Panchatantra/Geography'."),
        ("Himalaya means ___ abode of snow.", "the", "a", "an", "no article", "A", "Use 'the' for specific definition 'the abode of snow'."),
        ("Edmund Hillary was ___ honest mountaineer.", "an", "a", "the", "no article", "A", "Use 'an' before silent 'h' sound in 'honest'."),
        ("___ world's highest peak is Mount Everest.", "The", "A", "An", "No article", "A", "Superlative 'The world's highest' takes 'The'."),
        ("They faced ___ unusual challenge while climbing.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'unusual'."),
        ("Mount Everest lies on ___ border between Nepal and Tibet.", "the", "a", "an", "no article", "A", "Use 'the' for specific border."),
        ("It is ___ impressive mountain range.", "an", "a", "the", "no article", "A", "Use 'an' before vowel sound 'impressive'."),
        ("___ snow covers the lofty peaks all year round.", "The", "A", "An", "No article", "A", "Use 'The' for specific snow on Himalayan peaks."),
        ("Tenzing Norgay was ___ Sherpa guide.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'Sherpa'."),
        ("They created ___ historical record in 1953.", "a", "an", "the", "no article", "A", "Use 'a' before consonant sound 'historical'."),
        ("Edmund Hillary came from ___ island nation of New Zealand.", "the", "a", "an", "no article", "A", "Use 'the' for specific nation description."),
        ("Glaciers bring ___ freshwater to millions of people.", "no article", "a", "an", "the", "A", "Uncountable mass noun 'freshwater' takes no indefinite article here."),
        ("___ sun shines brightly over the snow-covered peaks.", "The", "A", "An", "No article", "A", "Use 'The' for unique celestial object 'sun'.")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_data, start=1):
        qid = f"BK02_CH09_CAT02_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct article (a / an / the / no article):\n\n\"{q_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Basic Article Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("___ Himalayas are ___ mountain range in Asia.", "The, a", "A, a", "An, the", "The, the", "A", "'The Himalayas' (mountain range takes 'The'), 'a mountain range' (consonant sound)."),
        ("Why do we say '**the** Himalayas' but '**Mount** Everest' without 'the'?", "Because plural mountain ranges take 'the', but individual mountain peaks named 'Mount X' do not take 'the'.", "Because Everest is taller.", "Because Himalayas are cold.", "Because Nepal is near.", "A", "Grammar rule: Plural mountain ranges take 'the'; individual peak names starting with 'Mount' do not."),
        ("Select the sentence with CORRECT article usage:", "The Ganges is a major river in India.", "A Ganges is a major river in India.", "The Ganges is an major river.", "An Ganges is a major river.", "A", "'The Ganges' (river takes 'the'), 'a major' (consonant sound)."),
        ("Fill in the blanks: 'They climbed ___ mountain and reached ___ summit.'", "a, the", "an, a", "the, a", "a, an", "A", "'a mountain' (consonant /m/), 'the summit' (specific peak summit)."),
        ("Identify the INCORRECT article in: 'Mount Everest is **a** highest peak.'", "'a' should be 'the'", "'a' should be 'an'", "'highest' should be 'a highest'", "No mistake", "A", "Superlative adjective 'highest' requires definite article 'the'."),
        ("Which article completes the sentence? 'Climbing requires ___ active team.'", "an", "a", "the", "no article", "A", "'active' starts with vowel sound /a/, requiring 'an'."),
        ("Choose the correct pair of articles: '___ river flows down ___ mountain.'", "The, the", "A, a", "An, an", "The, a", "A", "'The river' (specific river), 'the mountain' (specific mountain)."),
        ("Why do we use 'a' before 'lofty peak' in 'It is **a** lofty peak'?", "Because 'lofty' begins with the consonant sound /l/.", "Because peak is a noun.", "Because snow is cold.", "Because Everest is high.", "A", "'lofty' starts with consonant sound /l/."),
        ("Complete the dialogue: Climber: 'Is that ___ glacier?' Guide: 'Yes, it is ___ largest one!'", "a, the", "a, an", "an, the", "the, the", "A", "'a glacier' (consonant sound), 'the largest' (superlative takes 'the')."),
        ("Select the sentence:", "A river originates in the mountains.", "An river originates in the mountains.", "The river originates in an mountains.", "An river originates in an mountains.", "A", "'A river' (consonant sound), 'the mountains' (plural range)."),
        ("Fill in the blank: 'Mountaineers stayed at base camp for ___ long time.'", "a", "an", "the", "no article", "A", "Idiomatic phrase 'for a long time'."),
        ("Identify where NO article is needed:", "The peaks are covered with **___ snow**.", "He climbed ___ peak.", "They crossed ___ river.", "She saw ___ glacier.", "A", "Uncountable mass noun 'snow' takes no article here."),
        ("Choose the correct sentence for story summary:", "courage and teamwork conquer high peaks.", "A courage and a teamwork conquer high peaks.", "An courage and an teamwork conquer high peaks.", "The courage a conquers peaks.", "A", "Abstract concepts take no indefinite articles in general moral sense."),
        ("Fill in the blanks: 'The team spent ___ hour climbing ___ steep slope.'", "an, a", "a, a", "an, an", "the, an", "A", "'an hour' (silent h), 'a steep slope' (consonant s)."),
        ("Which sentence uses 'the' correctly for river systems?", "The Indus, the Ganges, and the Brahmaputra are rivers in Asia.", "An Indus, a Ganges, and a Brahmaputra are rivers in Asia.", "Indus, Ganges, and Brahmaputra are rivers in Asia.", "A Indus, an Ganges, and a Brahmaputra are rivers.", "A", "All specific river names take 'the'."),
        ("Identify the article error: 'The climber gave **a** explanation after **an** short delay.'", "'an short' should be 'a short' and 'a explanation' should be 'an explanation'", "'a explanation' should be 'an explanation'", "'an short' should be 'a short'", "No error", "A", "'an explanation' (vowel /e/) and 'a short delay' (consonant /s/)."),
        ("Complete: 'It was ___ unexpected victory at ___ summit.'", "an, the", "a, an", "the, the", "an, an", "A", "an unexpected (/u/), the summit (specific)."),
        ("Choose the correct option: '___ sun rose above Mount Everest.'", "The", "A", "An", "No article", "A", "'The sun' (unique celestial body).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT02_Q{idx:02d}"
        qtxt = f"Contextual Article Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Article Usage in Context", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze article usage in: 'Mount Everest is **the** highest peak in **the** Himalayas.' Is this correct?", "Yes, 'the highest' is superlative and 'the Himalayas' is a plural mountain range.", "No, 'the Himalayas' should be 'a Himalayas'.", "No, 'Mount Everest' needs 'The'.", "No, 'the highest' should be 'a highest'.", "A", "Superlatives and plural mountain ranges require 'the'."),
        ("Fill in all three blanks: '___ river flows down ___ valley into ___ ocean.'", "The, the, the", "A, an, a", "An, a, the", "The, a, a", "A", "'The river' (specific), 'the valley' (specific), 'the ocean' (specific)."),
        ("Identify why 'the' is NOT used before 'Mount Everest' in 'Mount Everest is 8,849 metres high':", "Because proper names of individual single mountain peaks starting with 'Mount' do not take 'the'.", "Because Everest is a noun.", "Because Nepal is small.", "Because snow is white.", "A", "Individual mountain peak names with 'Mount' omit 'the'."),
        ("Spot the TWO article errors: 'It took **a** hour for **a** eagle to fly over the Himalayas.'", "'a hour' should be 'an hour' and 'a eagle' should be 'an eagle'.", "'a hour' should be 'the hour' and 'a eagle' should be 'a eagle'.", "No errors.", "Only 'a hour' is wrong.", "A", "Both 'hour' (silent h) and 'eagle' (vowel e) require 'an'."),
        ("Choose the paragraph with PERFECT article usage throughout:", "The Himalayas are a great mountain system. Mount Everest is the highest peak. A climber reached the summit.", "An Himalayas are a mountain system. A Mount Everest is a highest peak.", "Himalayas are the great system. The Mount Everest is an highest peak.", "A Himalayas are the mountain system.", "A", "The Himalayas (plural range), a great mountain system (consonant), Mount Everest (no 'the'), the highest peak (superlative), A climber (consonant), the summit (specific)."),
        ("Why is it correct to write 'a unique mountain' but 'an unusual mountain'?", "Because 'unique' begins with consonant sound /j/ (yoo), while 'unusual' begins with vowel sound /u/.", "Because unique is longer.", "Because mountain is noun.", "Both take 'an'.", "A", "Sound determines article: /yoo/ is a consonant sound."),
        ("Select the option that correctly completes the story moral: '___ brave climber faces ___ extreme cold to reach ___ summit.'", "A, an, the", "An, a, an", "The, the, the", "A, a, a", "A", "A brave climber, an extreme cold, the summit."),
        ("Analyze this sentence: 'They climbed in **the** 1900s.' Why is 'the' appropriate?", "Because decade/century designations (the 1900s, the 20th century) take 'the'.", "Because 1900s is in Nepal.", "Because climbing is hard.", "Because peaks are tall.", "A", "Decade and century time references take 'the'."),
        ("Correct the sentence: 'An mountaineer reached a top of Mount Everest.'", "A mountaineer reached the top of Mount Everest.", "The mountaineer reached an top of Mount Everest.", "An mountaineer reached the top of Mount Everest.", "A mountaineer reached a top of Mount Everest.", "A", "'A mountaineer' (/m/ sound), 'the top' (specific highest point)."),
        ("Fill in the blanks: '___ rivers originating in ___ Himalayas provide water to ___ millions of people.'", "The, the, no article", "A, a, a", "No article, a, an", "An, the, a", "A", "'The rivers' (specific), 'the Himalayas' (plural range), millions (no article before number pronoun)."),
        ("Spot the missing article: 'Edmund Hillary reached summit of Mount Everest.'", "Missing 'the' before 'summit' -> 'reached the summit of...'", "Missing 'a' before 'Mount'", "Missing 'an' before 'Everest'", "No article is missing", "A", "Specific top point 'the summit' needs 'the'."),
        ("HOTS Reasoning: Which sentence uses 'a', 'an', and 'the' correctly in a single rule demonstration?", "An expedition reached a summit of the mountain.", "A expedition reached an summit of a mountain.", "The expedition reached an summit of an mountain.", "An expedition reached an summit of the mountain.", "A", "An expedition (vowel), a summit (consonant), the mountain (specific)."),
        ("Rewrite correctly: 'Mount Everest is a honest wonder of nature in an mountain range.'", "Mount Everest is an honest wonder of nature in a mountain range.", "Mount Everest is a honest wonder of nature in a mountain range.", "Mount Everest is an honest wonder of nature in an mountain range.", "Mount Everest is the honest wonder of nature in an mountain range.", "A", "'an honest' (silent h), 'a mountain range' (consonant /m/)."),
        ("Identify the correct rule for using 'the' with geographical rivers (the Ganges, the Indus, the Brahmaputra):", "Names of rivers, oceans, and seas always take the definite article 'the'.", "River names take 'an'.", "River names never take articles.", "River names take 'a' only.", "A", "Rivers take definite article 'the'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT02_Q{idx:02d}"
        qtxt = f"Higher Order Article Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Article Analysis & Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 3. Calendar & Days Vocabulary (50 Qs)
# ---------------------------------------------------------------------------
def build_calendar_days():
    header = "# Category 3: Calendar, Days & Abbreviations — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    days_easy = [
        ("Edmund Hillary and Tenzing Norgay reached the summit of Mount Everest in **May 1953**. What is the abbreviation for **May**?", "May (no abbreviation needed / May)", "My.", "Ma.", "My", "A", "May is a short 3-letter month and has no abbreviation."),
        ("What is the standard abbreviation for **Monday**?", "Mon.", "Mnd.", "Mo.", "Mn.", "A", "Mon. is standard abbreviation."),
        ("Which day comes right after Thursday?", "Friday", "Saturday", "Wednesday", "Tuesday", "A", "Friday follows Thursday."),
        ("What is the abbreviation for **Friday**?", "Fri.", "Frid.", "Fr.", "F.", "A", "Fri. is standard abbreviation."),
        ("If an expedition lasted for 7 days straight, how many full days was that?", "7 days (1 week)", "5 days", "10 days", "3 days", "A", "7 days = 1 week."),
        ("Which month comes right before May?", "April", "March", "June", "July", "A", "April comes before May."),
        ("What is the short abbreviation for **April**?", "Apr.", "Ap.", "Apl.", "Aprl.", "A", "Apr. is standard abbreviation."),
        ("The climbers reached the summit in the **morning**. What time of day is 12:00 PM?", "Noon / Midday", "Midnight", "Dawn", "Twilight", "A", "Noon/midday is 12:00 PM."),
        ("What is the abbreviation for **Saturday**?", "Sat.", "Satur.", "Sa.", "St.", "A", "Sat. is standard abbreviation."),
        ("How many years are in 1 century?", "100 years", "10 years", "50 years", "1000 years", "A", "1 century = 100 years."),
        ("Which month comes right after May?", "June", "July", "April", "March", "A", "June comes after May."),
        ("What is the short abbreviation for **June**?", "Jun.", "Jne.", "Ju.", "Jn.", "A", "Jun. is standard abbreviation."),
        ("If today is Thursday, what day was yesterday?", "Wednesday", "Friday", "Tuesday", "Monday", "A", "Yesterday was Wednesday."),
        ("If today is Friday, what day will tomorrow be?", "Saturday", "Thursday", "Sunday", "Monday", "A", "Tomorrow will be Saturday."),
        ("What is the abbreviation for **Tuesday**?", "Tue.", "Tues.", "Tu.", "Ts.", "A", "Tue. is standard abbreviation."),
        ("Which day comes between Tuesday and Thursday?", "Wednesday", "Friday", "Monday", "Sunday", "A", "Wednesday is between Tuesday and Thursday."),
        ("What is the abbreviation for **July**?", "Jul.", "Jly.", "Ju.", "Jl.", "A", "Jul. is standard abbreviation."),
        ("Which month comes right before June?", "May", "April", "July", "August", "A", "May comes before June.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(days_easy, start=1):
        qid = f"BK02_CH09_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Vocabulary & Time Concepts:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Days & Calendar Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("The Everest expedition reached Camp IV on **Wednesday** and reached the summit 2 days later. On which day did they reach the summit?", "Friday", "Thursday", "Saturday", "Sunday", "A", "Wednesday + 2 days = Thursday(1), Friday(2)."),
        ("Climbers trekked from **6:00 AM to 11:30 AM**. How many hours and minutes did they trek?", "5 hours 30 minutes", "4 hours", "6 hours", "3 hours 30 minutes", "A", "11:30 AM - 6:00 AM = 5 hours 30 minutes."),
        ("Match the day with its abbreviation: **Sunday**", "Sun.", "Snd.", "Su.", "Sn.", "A", "Sun. is standard."),
        ("Mount Everest was first climbed in **1953**. How many years from 1953 to 2053?", "100 years (1 century)", "50 years", "10 years", "200 years", "A", "2053 - 1953 = 100 years."),
        ("Identify the correctly spelt month name:", "May", "Mai", "Maye", "Maii", "A", "May is the correct spelling."),
        ("Identify the INCORRECT pair of day and abbreviation:", "Monday - Mon.", "Tuesday - Tue.", "Wednesday - Wed.", "Wednesday - Wds.", "D", "Wednesday abbreviation is Wed., not Wds."),
        ("Calculate: How many days are in **May**?", "31 days", "30 days", "28 days", "29 days", "A", "May has 31 days."),
        ("Which month has 31 days and comes right after April?", "May", "June", "March", "July", "A", "May has 31 days and follows April."),
        ("Rearrange in correct chronological order: Thu, Tue, Wed, Fri", "Tue, Wed, Thu, Fri", "Wed, Tue, Thu, Fri", "Tue, Thu, Wed, Fri", "Fri, Thu, Wed, Tue", "A", "Tuesday -> Wednesday -> Thursday -> Friday."),
        ("What day is 5 days before Friday?", "Sunday", "Monday", "Saturday", "Tuesday", "A", "Friday - 5 days = Thursday(1), Wednesday(2), Tuesday(3), Monday(4), Sunday(5)."),
        ("If an expedition takes 3 weeks to complete, how many days is that?", "21 days (3 x 7)", "15 days", "30 days", "14 days", "A", "3 weeks x 7 days = 21 days."),
        ("Select the month that has 30 days:", "April", "May", "July", "August", "A", "April has 30 days."),
        ("Which abbreviation stands for **March**?", "Mar.", "Marc.", "Mr.", "Mch.", "A", "Mar. is standard abbreviation."),
        ("If today is **Fri.**, what day will it be after 7 days?", "Friday", "Saturday", "Thursday", "Monday", "A", "7 days is a full week cycle, landing on Friday again."),
        ("Climbers rested from **1:00 PM to 3:00 PM**. How many hours did they rest?", "2 hours", "1 hour", "3 hours", "4 hours", "A", "3:00 PM - 1:00 PM = 2 hours."),
        ("Identify the word that means 'occurring throughout the entire year':", "Year-round / Perennial", "Daily", "Weekly", "Monthly", "A", "Year-round means all year round."),
        ("Which of the following is a weekday?", "Thursday", "Sunday", "Saturday", "Weekend", "A", "Thursday is a weekday."),
        ("Choose the correct abbreviation for **August**:", "Aug.", "Augu.", "Au.", "Ag.", "A", "Aug. is standard.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Application & Story Timeline:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Calendar & Time Reasoning", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Edmund Hillary and Tenzing Norgay climbed from **Mon., 25th May** to **Fri., 29th May 1953**. How many days was their final summit push?", "5 days", "4 days", "3 days", "7 days", "A", "25th to 29th May inclusive is 5 days (summit reached on 29th May 1953)."),
        ("The climbers stayed on the summit for **15 minutes**. What fraction of an hour is 15 minutes?", "1/4 of an hour (quarter hour)", "1/2 hour", "1/3 hour", "1/5 hour", "A", "15 / 60 = 1/4 hour."),
        ("Solve the calendar puzzle: If 29th May 1953 (Everest summit day) was a Friday, what day of the week was 22nd May 1953?", "Friday", "Saturday", "Thursday", "Monday", "A", "29 - 7 = 22nd May, landing on Friday."),
        ("Analyze this schedule: Base camp team works Mon, Wed, Fri; High altitude team works Tue, Thu, Sat. On which day do BOTH rest?", "Sunday", "Monday", "Saturday", "Wednesday", "A", "Sunday is not listed in schedule."),
        ("Complete the full series of day abbreviations: Mon., Tue., Wed., Thu., Fri., Sat., ____.", "Sun.", "Sund.", "Su.", "Sn.", "A", "Sun. completes the 7 days of the week."),
        ("If a climbing permit is valid for a fortnight, how many days is it valid?", "14 days (2 weeks)", "7 days", "30 days", "3 days", "A", "A fortnight is 14 days."),
        ("Spot the error in the calendar sequence: 'Mar, Apr, Jun, May, Jul'", "June and May are in wrong order.", "April is in wrong position.", "July should be first.", "No error.", "A", "May comes before June (Mar, Apr, May, Jun, Jul)."),
        ("May has **31 days**. What date was the day right after 31st May?", "1st June", "32nd May", "30th May", "1st July", "A", "May has 31 days, so next day is 1st June."),
        ("If yesterday was two days before Monday, what day is tomorrow?", "Monday", "Sunday", "Tuesday", "Saturday", "A", "Two days before Monday = Saturday (yesterday). Today = Sunday. Tomorrow = Monday."),
        ("Calculate: How many days are there in total during **April** and **May** combined?", "61 days (30 + 31)", "60 days", "62 days", "59 days", "A", "April (30) + May (31) = 61 days."),
        ("HOTS Reasoning: Why do mountaineers choose May for climbing Mount Everest rather than winter months?", "May offers a brief weather window between winter blizzards and summer monsoon rains.", "Because May is short.", "Because Nepal is closed in winter.", "Because snow melts completely.", "A", "May offers favorable weather window before monsoons."),
        ("Identify the correct statement about a non-leap year:", "A non-leap year has 365 days and February has 28 days.", "A non-leap year has 366 days.", "February has 30 days.", "A non-leap year occurs every 4 years.", "A", "Standard year has 365 days (Feb = 28 days)."),
        ("Climbers climbed 2,500 meters in 5 days. How many meters did they climb per day on average?", "500 meters per day", "250 meters", "1,000 meters", "100 meters", "A", "2,500 / 5 = 500 meters per day."),
        ("Which month pair both have 31 days and come right after each other in mid-summer?", "July and August", "June and July", "August and September", "May and June", "A", "July (31) and August (31) are consecutive 31-day summer months.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT03_Q{idx:02d}"
        qtxt = f"Calendar Logic & Mathematical Time Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Calendar & Time Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 4. Action Verbs Identification (50 Qs)
# ---------------------------------------------------------------------------
def build_action_verbs():
    header = "# Category 4: Action Verbs Identification — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_verbs = [
        ("The word Himalaya **means** abode of snow.", "means", "Himalaya", "abode", "snow", "A", "'means' is the action/definition verb."),
        ("The lofty peaks are **covered** with snow.", "covered", "peaks", "snow", "lofty", "A", "'covered' is the action verb."),
        ("The mountain range **stretches** for 2,500 kilometers.", "stretches", "range", "kilometers", "mountain", "A", "'stretches' is the action verb."),
        ("Three important rivers **originate** in the Himalayas.", "originate", "three", "rivers", "Himalayas", "A", "'originate' is the action verb."),
        ("Edmund Hillary and Tenzing Norgay **climbed** Mount Everest.", "climbed", "Edmund Hillary", "Mount Everest", "Tenzing", "A", "'climbed' is the physical action verb."),
        ("They **reached** the summit in 1953.", "reached", "they", "summit", "1953", "A", "'reached' is the action verb."),
        ("No other mountain range **compares** to the Himalayas.", "compares", "mountain", "range", "Himalayas", "A", "'compares' is the action verb."),
        ("Mount Everest **lies** on the border between Nepal and Tibet.", "lies", "Mount Everest", "border", "Nepal", "A", "'lies' is the action verb."),
        ("Rivers **flow** down from the glaciers.", "flow", "rivers", "down", "glaciers", "A", "'flow' is the physical action verb."),
        ("Snow **melts** during warm months.", "melts", "snow", "warm", "months", "A", "'melts' is the action verb."),
        ("Mountaineers **explore** high peaks.", "explore", "mountaineers", "high", "peaks", "A", "'explore' is the physical action verb."),
        ("The mountains **protect** the northern plains.", "protect", "mountains", "northern", "plains", "A", "'protect' is the action verb."),
        ("Climbers **carry** heavy packs on their backs.", "carry", "climbers", "heavy", "packs", "A", "'carry' is the physical action verb."),
        ("The peaks **rise** high into the sky.", "rise", "peaks", "high", "sky", "A", "'rise' is the action verb."),
        ("Mountaineers **stand** on top of the world.", "stand", "mountaineers", "top", "world", "A", "'stand' is the physical action verb."),
        ("Glaciers **feed** major rivers in Asia.", "feed", "glaciers", "major", "rivers", "A", "'feed' is the action verb."),
        ("Climbers **conquer** dangerous heights.", "conquer", "climbers", "dangerous", "heights", "A", "'conquer' is the action verb."),
        ("People **admire** the beauty of the Himalayas.", "admire", "people", "beauty", "Himalayas", "A", "'admire' is the mental action verb.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_verbs, start=1):
        qid = f"BK02_CH09_CAT04_Q{idx:02d}"
        qtxt = f"Identify the **action verb** in this sentence from or related to Chapter 09:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the action verb."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Action Verb Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Which word from the sentence is an **action verb**? 'The mountaineers **bravely** **climbed** the **steep** **peak**.'", "climbed", "bravely", "steep", "peak", "A", "'climbed' shows physical action; 'bravely' is adverb, 'steep' is adjective, 'peak' is noun."),
        ("Identify BOTH action verbs in: 'The rivers **originate** in glaciers and **flow** into the ocean.'", "originate, flow", "rivers, glaciers", "ocean, originate", "flow, glaciers", "A", "'originate' and 'flow' are both action verbs."),
        ("What is the past tense action verb of 'reach' as used in story ('reached the summit')?", "reached", "reach", "reaching", "reaches", "A", "Past tense of reach is reached."),
        ("Choose the sentence where the underlined word is used as an ACTION VERB:", "Climbers will **climb** the high peak tomorrow.", "They made a steep **climb**.", "It was a tough **climb**.", "I watched their **climb**.", "A", "In (A), 'climb' acts as the main action verb."),
        ("Find the action verb in: 'Mount Everest stands as the highest peak.'", "stands", "Mount Everest", "highest", "peak", "A", "'stands' is the action verb."),
        ("Which sentence contains NO physical action verb?", "The Himalayas are a great mountain range.", "They stretch for 2,500 kilometers.", "Climbers reached the top.", "Rivers flow from the snow.", "A", "'The Himalayas are a great mountain range' contains linking verb 'are', but no physical action verb."),
        ("Change the action verb 'reach' to past tense: 'They (reach) the summit in 1953.'", "reached", "reach", "reaching", "reaches", "A", "Past tense of reach is reached."),
        ("Identify the action verb: 'Mountaineers climb peaks and cross glaciers.'", "climb, cross", "mountaineers, peaks", "glaciers, climb", "cross, peaks", "A", "'climb' and 'cross' are action verbs."),
        ("Select the action verb that completes the sentence: 'The Himalayas ____ North India from cold winds.'", "shield / protect", "tall", "snowy", "mountain", "A", "'shield' / 'protect' is an action verb."),
        ("Which word is an action verb? (mountains, glaciers, stretches, lofty)", "stretches", "mountains", "glaciers", "lofty", "A", "'stretches' is an action verb; others are nouns/adjectives."),
        ("What action did Edmund Hillary and Tenzing Norgay perform?", "reached", "lofty", "abode", "snow", "A", "They reached the summit (action verb)."),
        ("Identify the action verb in: 'Climbers thought about the cold weather.'", "thought", "climbers", "about", "weather", "A", "'thought' is a mental action verb."),
        ("Choose the correct action verb: 'The Indus ____ through deep valleys.'", "carves / flows", "steep", "high", "river", "A", "'carves' / 'flows' is the action verb."),
        ("Identify the action verb in: 'Snow covers the lofty peaks all year.'", "covers", "snow", "lofty", "peaks", "A", "'covers' is the action verb."),
        ("Which of these words is NOT an action verb? (climb, flow, lofty, stretch)", "lofty", "climb", "flow", "stretch", "A", "'lofty' is an adjective; others are action verbs."),
        ("Identify the action verb in: 'Glaciers melt under the warm sun.'", "melt", "glaciers", "under", "sun", "A", "'melt' is the action verb."),
        ("Fill in the blank with an appropriate action verb: 'Mountaineers ____ flags on the summit.'", "planted / placed", "cold", "high", "peak", "A", "'planted' / 'placed' is an action verb."),
        ("What action verb completes the sentence? 'The three rivers ____ water to millions.'", "supply / provide", "deep", "snow", "mountain", "A", "'supply' / 'provide' is an action verb.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT04_Q{idx:02d}"
        qtxt = f"Action Verb Grammar Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Action Verb Context & Tense", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence: 'The brave mountaineers carefully climbed the ice wall and reached the summit.' How many total ACTION VERBS are present?", "2 action verbs ('climbed', 'reached')", "1 action verb", "3 action verbs", "0 action verbs", "A", "'climbed' and 'reached' are action verbs; 'brave', 'carefully' are adjectives/adverbs."),
        ("Categorize the verbs: In 'The Himalayas **are** majestic, so they **attract** climbers', classify 'are' and 'attract'.", "'are' is a linking verb; 'attract' is an action verb.", "Both are action verbs.", "Both are linking verbs.", "'are' is action; 'attract' is linking.", "A", "'are' links state of being; 'attract' shows action."),
        ("Replace the weak verb with a strong action verb: 'The rivers **go** down the mountains.'", "The rivers **cascade** down the mountains.", "The rivers **were near** the mountains.", "The rivers **saw** the mountains.", "The rivers **looked at** the valley.", "A", "'cascade' is a much stronger, vivid action verb."),
        ("Identify the sentence with THREE distinct action verbs:", "Mountaineers **scaled** the ice, **crossed** the crevasse, and **reached** the peak.", "The Himalayas are tall, cold, and snowy.", "Mount Everest is high, steep, and famous.", "The range is located in Asia.", "A", "scaled, crossed, reached are 3 distinct action verbs."),
        ("Differentiate verb types: Which underlined word is an ACTION verb?", "The team **conquered** Mount Everest.", "Mount Everest was **tall**.", "The snow was **white**.", "The weather was **cold**.", "A", "'conquered' is an action verb."),
        ("Spot the incorrect verb tense: 'Hillary and Tenzing **reach** the summit in 1953.' Correct it:", "'reach' should be 'reached' (past action verb).", "'reach' should be 'reaching'.", "'reach' should be 'reaches'.", "'reach' should be 'will reach'.", "A", "Past time indicator 'in 1953' requires past tense action verb 'reached'."),
        ("Form an action chain: Rearrange the story action verbs in correct order of occurrence: (prepares expedition, climbs ice, reaches summit, plants flag)", "prepares expedition -> climbs ice -> reaches summit -> plants flag", "plants flag -> reaches summit -> climbs ice -> prepares expedition", "reaches summit -> prepares expedition -> plants flag -> climbs ice", "climbs ice -> reaches summit -> prepares expedition -> plants flag", "A", "Chrono order: prepare, climb, reach, plant flag."),
        ("Identify the verb error in dialogue: Hillary said, 'We have **reach** the summit!'", "'reach' is incorrect; the past participle form is 'reached' ('have reached').", "'reach' should be 'reaching'.", "'reach' should be 'reaches'.", "No error.", "A", "Perfect tense requires past participle 'reached'."),
        ("Analyze this sentence: 'The Himalayas **influence** Asia's climate.' What type of action verb is 'influence'?", "Environmental/impact action verb", "Physical movement verb", "Linking verb", "State of being verb", "A", "'influence' is an action verb describing climate impact."),
        ("Which sentence uses action verbs to show cause and effect?", "Snow **melts** in the sun, so rivers **flow** down to the plains.", "The Himalayas are tall and snow is cold.", "Mount Everest is in Nepal and Ganges is a river.", "West to east is 2,500 kilometers.", "A", "'melts' (cause action) -> 'flow' (effect action)."),
        ("Spot the missing action verb: 'The rivers ____ down the slopes and ____ fertile soil.'", "rush, deposit", "snowy, cold", "was, was", "quick, slow", "A", "'rush' and 'deposit' complete sentence with vivid actions."),
        ("HOTS Reasoning: Why is 'sustains' in 'The Himalayas sustain life in Asia' considered a VITAL action verb?", "Because it describes actively supporting, nourishing, and maintaining life through water supply.", "Because sustaining requires climbing.", "Because Everest is high.", "Because it is a noun.", "A", "Descriptive action verb conveying life-giving support."),
        ("Transform the action verb to future tense: 'Climbers **reach** the summit tomorrow.'", "Climbers **will reach** the summit tomorrow.", "Climbers **reached** the summit tomorrow.", "Climbers **are reaching** the summit tomorrow.", "Climbers **reach** the summit tomorrow.", "A", "'will reach' expresses future action."),
        ("Identify the sentence where the action verb matches the plural subject:", "The rivers **originate** in the glaciers.", "The rivers **originates** in the glaciers.", "A river **originate** in the glaciers.", "The rivers **is originating** in the glaciers.", "A", "Plural subject 'rivers' takes base verb 'originate' in simple present.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT04_Q{idx:02d}"
        qtxt = f"Higher Order Action Verb Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Action Verb Classification & Tense Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 5. Punctuation Marks (50 Qs)
# ---------------------------------------------------------------------------
def build_punctuation_marks():
    header = "# Category 5: Punctuation Marks & Capitalization — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_punct = [
        ("What punctuation mark should be placed at the end of: 'The Himalayas means abode of snow__'", "Full stop (.)", "Question mark (?)", "Exclamation mark (!)", "Comma (,)", "A", "A statement ends with a full stop."),
        ("Which mark is used at the end of an asking sentence: 'What is the highest mountain peak on Earth__'", "Question mark (?)", "Full stop (.)", "Comma (,)", "Exclamation mark (!)", "A", "A question ends with a question mark."),
        ("Which letter should ALWAYS be capitalized in a mountain name like 'Mount Everest'?", "First letter of each word (e.g., Mount Everest)", "The last letter", "All letters", "No letters", "A", "Proper names require capitalized initial letters."),
        ("Identify the punctuation mark used to separate items in a list: 'The Indus__ the Ganges__ and the Brahmaputra originate in the Himalayas.'", "Comma (,)", "Full stop (.)", "Question mark (?)", "Hyphen (-)", "A", "Commas separate items in a list."),
        ("Which punctuation mark shows sudden awe: 'What a magnificent mountain range this is__'", "Exclamation mark (!)", "Full stop (.)", "Comma (,)", "Question mark (?)", "A", "Exclamation marks express intense awe/admiration."),
        ("Select the proper noun that MUST start with a capital letter:", "Nepal", "mountain", "river", "peak", "A", "'Nepal' as a country name starts with capital 'N'."),
        ("Which of the following is the symbol for a **full stop**?", ".", "?", "!", ",", "A", "Period/full stop is '.'"),
        ("Which of the following is the symbol for a **question mark**?", "?", ".", "!", ",", "A", "Question mark is '?'"),
        ("Which of the following is the symbol for an **exclamation mark**?", "!", "?", ".", ",", "A", "Exclamation mark is '!'"),
        ("Which word in this sentence should start with a CAPITAL letter? 'edmund Hillary reached the summit.'", "edmund -> Edmund", "reached -> Reached", "summit -> Summit", "the -> The", "A", "First name 'Edmund' must start with a capital letter."),
        ("What punctuation mark goes in the box? 'Mount Everest is 8,849 metres high [ ]'", "Full stop (.)", "Question mark (?)", "Comma (,)", "Exclamation mark (!)", "A", "Full stop ends the statement."),
        ("Which river name is capitalized correctly?", "Ganges", "ganges", "GAnges", "GANGES", "A", "Capital letter for proper river name."),
        ("What mark goes after a speaker tag: 'Tenzing Norgay said__ \"We have reached the top!\"'", "Comma (,)", "Question mark (?)", "Full stop (.)", "Exclamation mark (!)", "A", "Comma follows dialogue speaker tags."),
        ("Identify the correct capital letter for the pronoun 'I': 'he said, \"i can see Mount Everest.\"'", "I", "i", "i'm", "I'm", "A", "Standalone pronoun 'I' is always capitalized."),
        ("Which option shows a sentence ending correctly?", "The Himalayas stretch for 2,500 kilometers.", "The Himalayas stretch for 2,500 kilometers?", "The Himalayas stretch for 2,500 kilometers,", "The Himalayas stretch for 2,500 kilometers;", "A", "Full stop at end of simple statement."),
        ("What mark is used in possessives like 'the **mountain's** peak'?", "Apostrophe (')", "Comma (,)", "Full stop (.)", "Hyphen (-)", "A", "Apostrophe indicates possession."),
        ("Which book chapter title is capitalized correctly?", "The Himalayas", "the himalayas", "The himalayas", "THE HIMALAYAS", "A", "Major words in titles are capitalized."),
        ("What punctuation mark is used around single titles: 'Himalaya means ___abode of snow___.'", "Double or single quotation marks ( \" \" or ' ' )", "Parentheses ( )", "Full stops ( . . )", "Commas ( , , )", "A", "Quotation marks enclose exact translated meanings.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_punct, start=1):
        qid = f"BK02_CH09_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Punctuation & Capitalization Rules", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Identify the sentence with CORRECT capitalization and punctuation:", "Mount Everest lies on the border between Nepal and Tibet on Monday.", "mount everest lies on the border between nepal and tibet on monday.", "Mount Everest lies on the border between nepal and Tibet on monday?", "mount Everest Lies On The Border Between Nepal And Tibet On Monday.", "A", "Mount Everest, Nepal, Tibet (proper names), Monday (day) capitalized; period at end."),
        ("Which sentence is punctuated as a CORRECT question?", "Which rivers originate in the Himalayas?", "Which rivers originate in the Himalayas.", "Which rivers originate in the Himalayas!", "Which rivers originate in the Himalayas,", "A", "Question starting with 'Which' ends with question mark ?"),
        ("Spot the capitalization mistake in: 'edmund Hillary came from New Zealand.'", "'edmund' should be capitalized ('Edmund'); 'New Zealand' is correct.", "'New Zealand' should be lowercase.", "'Hillary' should be lowercase.", "No mistake.", "A", "First name 'Edmund' must be capitalized."),
        ("Choose the correctly punctuated dialogue sentence:", "\"We reached the summit,\" said Tenzing Norgay.", "we reached the summit said Tenzing Norgay.", "\"We reached the summit\" said Tenzing Norgay", "We reached the summit, said Tenzing Norgay.", "A", "Quotation marks around dialogue, comma inside quote, capital W."),
        ("Identify where a COMMA is missing: 'The Indus the Ganges and the Brahmaputra are major rivers.'", "Between 'Indus' and 'the Ganges' ('The Indus, the Ganges')", "After 'The'", "After 'rivers'", "No comma needed", "A", "Commas separate items in list: 'The Indus, the Ganges and the Brahmaputra'."),
        ("Which sentence uses the apostrophe correctly for possession?", "This is Earth's highest peak.", "This is Earths' highest peak.", "This is Earths highest peak.", "This is Earth's' highest peak.", "A", "Earth's indicates singular possession."),
        ("Select the sentence with CORRECT punctuation for an exclamatory statement:", "What a tall and majestic mountain range the Himalayas are!", "What a tall and majestic mountain range the Himalayas are?", "What a tall and majestic mountain range the Himalayas are.", "What a tall and majestic mountain range the Himalayas are,", "A", "Exclamatory statement ends with exclamation mark !"),
        ("Which contraction is written correctly for 'did not'?", "didn't", "did'nt", "didnt'", "d'idnt", "A", "didn't is standard contraction."),
        ("Find the sentence with NO capitalization errors:", "Edmund Hillary and Tenzing Norgay reached Mount Everest in 1953.", "edmund hillary and tenzing norgay reached mount everest in 1953.", "Edmund Hillary And Tenzing Norgay Reached Mount Everest In 1953.", "edmund Hillary reached Mount Everest in 1953.", "A", "'Edmund Hillary', 'Tenzing Norgay', and 'Mount Everest' capitalized as proper nouns."),
        ("What punctuation mark belongs in the blank? 'The climber shouted, \"We made it__ We are on the summit!\"'", "!", ".", "?", ",", "A", "Exclamation mark ! expresses triumph."),
        ("Choose the correct form for 'could not':", "couldn't", "could'nt", "couldnt'", "c'ouldnt", "A", "couldn't is standard contraction."),
        ("Identify the punctuation error: 'The snow is deep, the peaks are high.'", "Comma splice between two independent clauses (should be full stop or 'and').", "Missing question mark.", "Missing capital letters.", "No error.", "A", "Two complete sentences separated only by comma."),
        ("Select the sentence with proper use of capital letters for names and places:", "Mount Everest is located between Nepal and China.", "mount everest is located between nepal and china.", "Mount Everest is located between nepal and China.", "mount Everest is located between Nepal and china.", "A", "Names 'Mount Everest', 'Nepal', 'China' all capitalized."),
        ("Which sentence correctly uses an apostrophe for possessive noun?", "The mountain's peak was covered with snow.", "The mountains' peak was covered with snow.", "The mountains peak was covered with snow.", "The mountain's' peak was covered with snow.", "A", "mountain's indicates singular possession."),
        ("Identify the correct punctuation for a list of items: 'The range spans across ____'", "India, Nepal, and Bhutan.", "India Nepal and Bhutan.", "India; Nepal; and Bhutan.", "India: Nepal: and Bhutan.", "A", "Commas separate items in list."),
        ("Choose the sentence that correctly asks a question about the story:", "How high is Mount Everest?", "How high is Mount Everest.", "How high is Mount Everest!", "how high is Mount Everest.", "A", "Capital H, ends with question mark ?"),
        ("Fix the sentence: 'where is mount everest located'", "Where is Mount Everest located?", "Where is mount everest located.", "where is Mount Everest located!", "Where is Mount Everests' located?", "A", "Capital W, capital M, capital E, ends with ?"),
        ("Which of these sentences is punctuated PERFECTLY?", "Hillary said, \"We have conquered Mount Everest!\"", "Hillary said \"we have conquered Mount Everest!\"", "hillary said, \"We have conquered Mount Everest!\"", "Hillary said, \"We have conquered Mount Everest.\"", "A", "Capital H, comma after said, speech marks around dialogue with ! inside.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT05_Q{idx:02d}"
        qtxt = f"Punctuation & Capitalization Context Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Punctuation Application & Dialogue Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze and count ALL capitalization and punctuation errors in: 'on friday edmund hillary arrived in nepal and said, we will climb mount everest'", "5 errors (on->On, friday->Friday, edmund hillary->Edmund Hillary, nepal->Nepal, mount everest->Mount Everest, quotation marks, capital W in We, period)", "2 errors", "3 errors", "7 errors", "A", "Starts sentence, day name, person name, country name, mountain name, quotation marks, capital W, period."),
        ("Correct the entire dialogue paragraph: 'tenzing asked is that the summit hillary replied yes we are standing on the top of earth'", "\"Is that the summit?\" asked Tenzing. Hillary replied, \"Yes, we are standing on the top of Earth.\"", "tenzing asked \"is that the summit\" hillary replied \"yes we are standing on the top of earth.\"", "Tenzing asked, Is that the summit. Hillary replied, Yes we are standing on the top of Earth.", "\"Is that the summit?\" Asked Tenzing. Hillary replied \"Yes we are standing on the top of Earth?\"", "A", "Full proper quotation, dialogue tags, capitalization, and terminal punctuation."),
        ("Distinguish between singular possessive and contraction: 'Everest**'**s peak is tall, and it**'**s famous.'", "First 's is possessive (peak belonging to Everest); second 's is contraction (it is).", "Both are possessive.", "Both are contractions.", "First is contraction; second is possessive.", "A", "Everest's peak = peak of Everest; it's = it is."),
        ("Spot the subtle punctuation flaw in this dialogue: '\"We reached the summit,\" Said Edmund Hillary.'", "'Said' should be lowercase 'said' because it continues the dialogue tag outside quotation marks.", "'We' should be lowercase.", "Commas should be outside quotes.", "No flaw.", "A", "Dialogue tags following quotes start with lowercase unless proper nouns."),
        ("Which sentence correctly uses punctuation to show contrast?", "The climb was dangerous, but they reached the summit.", "The climb was dangerous but, they reached the summit.", "The climb was dangerous but they reached the summit!", "The climb was dangerous; but they reached the summit?", "A", "Comma before coordinating conjunction 'but' joining two independent clauses."),
        ("Reconstruct with perfect punctuation: 'hillary and tenzing reached mount everest on friday 29th may 1953'", "Hillary and Tenzing reached Mount Everest on Friday, 29th May 1953.", "hillary and tenzing reached mount everest on friday, 29th may 1953.", "Hillary and Tenzing reached Mount Everest on Friday 29th May 1953", "Hillary and tenzing reached mount everest on friday 29th may 1953.", "A", "Hillary, Tenzing, Mount Everest, Friday, 29th May 1953, period."),
        ("Identify why exclamation mark is necessary here: '\"Summit! We stand on top of the world!\"'", "Because the mountaineers are expressing monumental triumph and joy.", "Because mountain is cold.", "Because snow is white.", "Because sentence is long.", "A", "Exclamation mark communicates monumental triumph."),
        ("Choose the correctly punctuated sentence containing an appositive phrase:", "Mount Everest, the world's highest peak, lies between Nepal and Tibet.", "Mount Everest the world's highest peak lies between Nepal and Tibet.", "Mount Everest, the world's highest peak lies between Nepal and Tibet.", "Mount Everest the world's highest peak, lies between Nepal and Tibet.", "A", "Appositive phrase 'the world's highest peak' is set off by commas."),
        ("Analyze the use of hyphen in: 'Himalaya peaks have snow-covered slopes.'", "Hyphen joins compound adjective (snow-covered).", "Hyphen replaces comma.", "Hyphen indicates question.", "Hyphen is an apostrophe.", "A", "Compound adjectives modifying nouns take hyphens."),
        ("Identify the correct sentence with direct speech quote within text:", "Edmund Hillary declared, \"We did it,\" and they celebrated.", "Edmund Hillary declared \"We did it\" and they celebrated.", "Edmund Hillary declared, 'We did it,' and they celebrated.", "Edmund Hillary declared: \"We did it\" and they celebrated.", "A", "Comma before quote, double quotation marks around direct speech, comma inside quote."),
        ("Spot the missing apostrophe: 'Earths highest peak is Mount Everest.'", "Missing apostrophe in 'Earth's' -> 'Earth's highest peak'", "Missing apostrophe in 'peaks''", "Missing apostrophe in 'is''", "No apostrophe needed", "A", "'Earth's highest peak' requires possessive apostrophe."),
        ("HOTS Reasoning: Why does putting a comma in different places change meaning? Compare: 'Hillary, said Tenzing, is brave.' vs 'Hillary said, \"Tenzing is brave.\"'", "In the first, Tenzing says Hillary is brave; in the second, Hillary says Tenzing is brave.", "Both mean the exact same thing.", "The first is a question.", "Commas do not affect meaning.", "A", "Punctuation alters who speaks and who is praised."),
        ("Correct all 4 errors in: 'whats the mountains height asked the climber'", "\"What's the mountain's height?\" asked the climber.", "whats the mountains height? asked the climber.", "\"What's the mountains height.\" asked the climber.", "\"whats the mountains height?\" Asked the climber.", "A", "Quotation marks, capital W, possessive mountain's, question mark, period at end."),
        ("Identify the rule for capitalizing geographical mountain names like 'Himalayas' and 'Mount Everest':", "Specific proper names of mountain ranges and individual peaks take initial capital letters.", "Mountain names are never capitalized.", "Mountain names are capitalized only at end of sentence.", "Mountain names must be written in ALL CAPS.", "A", "Proper geographical names take initial capitals.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT05_Q{idx:02d}"
        qtxt = f"Higher Order Punctuation Analysis & Dialogue Formatting:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Punctuation & Dialogue Editing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 6. Phonics & Vowel Digraphs (50 Qs)
# ---------------------------------------------------------------------------
def build_phonics_digraphs():
    header = "# Category 6: Phonics & Vowel Digraphs — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_phonics = [
        ("Which vowel digraph is present in the word **'peak'** (in Chapter 09)?", "ea", "ee", "ai", "ou", "A", "'ea' is the vowel digraph in peak."),
        ("Identify the vowel digraph in the word **'reach'**:", "ea", "ee", "oa", "ui", "A", "'ea' forms the long /e/ vowel sound in reach."),
        ("Which word from the story contains the **'ou'** vowel digraph?", "mountain", "peak", "river", "snow", "A", "'mountain' contains the 'ou' digraph."),
        ("Identify the vowel digraph in the word **'clean'**:", "ea", "ee", "ow", "oo", "A", "'ea' forms long /e/ sound in clean."),
        ("Which vowel digraph appears in the word **'paid'**?", "ai", "ay", "ea", "oa", "A", "'ai' makes long /a/ sound in paid."),
        ("Find the word with the **'oo'** vowel digraph: 'The peaks are covered in snow all year round.'", "round", "peaks", "covered", "snow", "A", "'round' contains 'ou' / 'oo' vowel sound pattern."),
        ("Which word from the story rhymes with **'peak'**?", "seek", "pack", "poke", "pick", "A", "'seek' rhymes with 'peak'."),
        ("Which word from the story rhymes with **'high'**?", "sky", "he", "hey", "hay", "A", "'sky' rhymes with 'high'."),
        ("Identify the vowel digraph in the word **'boasted'**:", "oa", "ou", "ow", "oo", "A", "'oa' makes long /o/ sound in boasted."),
        ("Which word from the story rhymes with **'town'**?", "down", "tan", "to", "ton", "A", "'down' rhymes with 'town'."),
        ("Identify the vowel digraph in **'abode'**:", "o-e (split vowel digraph)", "ae", "ur", "or", "A", "Split vowel digraph 'o_e' makes long /o/ sound in abode."),
        ("Which word from Chapter 09 has the **'ea'** digraph making a long /e/ sound?", "reach", "head", "heavy", "dead", "A", "'reach' has 'ea' making long /e/ sound."),
        ("Which word rhymes with **'day'**?", "away", "die", "due", "door", "A", "'away' rhymes with 'day'."),
        ("Identify the silent letters in **'high'** (as in 'high peaks'):", "gh", "h", "i", "g", "A", "Silent 'gh' in high."),
        ("Which word from the story has long /i/ sound spelled with **'igh'**?", "highest", "bought", "bowl", "baker", "A", "'igh' in highest makes long /i/ sound."),
        ("Find the word with **'ou'** digraph: 'They climbed around the ridge.'", "around", "ridge", "they", "climbed", "A", "'around' contains 'ou' digraph."),
        ("Which word rhymes with **'cold'**?", "bold", "call", "cool", "code", "A", "'bold' rhymes with 'cold'."),
        ("Identify the silent letter in the word **'climb'** (as in 'climbed Everest'):", "b", "c", "l", "m", "A", "Final 'b' after 'm' is silent in climb.")
    ]
    
    for idx, (qtxt_item, optA, optB, optC, optD, correct, explanation) in enumerate(easy_phonics, start=1):
        qid = f"BK02_CH09_CAT06_Q{idx:02d}"
        qtxt = f"Phonics & Vowel Digraph Identification:\n\n{qtxt_item}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Vowel Digraphs & Rhyming Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Compare the **'ea'** digraph sound in **'peak'** and **'bread'**. What is the difference?", "'peak' has long /e/ sound; 'bread' has short /e/ sound.", "Both have short /e/ sound.", "Both have long /a/ sound.", "'peak' has short /e/; 'bread' has long /e/.", "A", "'ea' can make long /e/ (peak) or short /e/ (bread)."),
        ("Select the word pair from Chapter 09 that has the SAME vowel digraph sound:", "peak - reach", "high - bread", "abode - roar", "mountain - sweet", "A", "'peak' and 'reach' both have 'ea' long /e/ sound."),
        ("Which word contains SILENT letters? (high, peak, river, snow)", "high", "peak", "river", "snow", "A", "'high' has silent 'gh'."),
        ("Identify the odd one out based on vowel sound: (peak, reach, clean, bread)", "bread", "peak", "reach", "clean", "A", "'bread' has short /e/ sound; others have long /e/ sound."),
        ("Which digraph completes the word for mountain top? 'p__k'", "ea", "ee", "ai", "ou", "A", "'peak' uses 'ea' digraph."),
        ("Group these story words by digraph: **mountain**, **out**, **around**. What digraph do they all share?", "ou", "ow", "oo", "oi", "A", "All share 'ou' making /ow/ diphthong sound."),
        ("Find the word with consonant digraph **'th'** from the story: 'Mount Everest is **the** highest peak.'", "the", "highest", "peak", "Everest", "A", "'the' contains voiced 'th' consonant digraph."),
        ("Which of these words has the **'ow'** vowel digraph making long /o/ sound? (snow, grow, blow, all of these)", "all of these", "snow", "grow", "blow", "A", "snow, grow, blow all share 'ow' long /o/ sound."),
        ("Identify the vowel digraph in **'mountain'**:", "ou", "ai", "ou and ai", "none", "C", "'ou' and 'ai' are vowel digraphs in mountain."),
        ("Which word from the story has silent **'b'**? (climb, thumb, lamb, all of these)", "all of these", "climb", "thumb", "lamb", "A", "climb, thumb, lamb all have silent final 'b' after 'm'."),
        ("Select the word that rhymes with **'peak'** and fits sentence: 'The mountain has a high ____.'", "peak", "seek", "leak", "meek", "A", "'peak' fits the sentence."),
        ("Identify the digraph in **'reached'**:", "ea", "ee", "ai", "oa", "A", "'ea' makes long /e/ sound."),
        ("Which word has the short /u/ sound made by **'ou'**? (tough, mountain, out, shout)", "tough", "mountain", "out", "shout", "A", "'tough' has short /u/ sound with 'ou'."),
        ("Find the R-controlled vowel sound in: 'Nepal is in **part** of Asia.'", "ar sound", "ea", "ou", "ai", "A", "R-controlled vowel in part."),
        ("Which word contains the **'oi'** diphthong/digraph? (choice, voice, point, all of these)", "all of these", "choice", "voice", "point", "A", "choice, voice, point all contain 'oi'."),
        ("Identify the soft **'c'** sound in Chapter 09 vocabulary: (place, ice, center, all of these)", "all of these", "place", "ice", "center", "A", "place, ice, center all have soft /s/ sound for 'c' before 'e' or 'i'."),
        ("Which word has a soft **'g'** sound? (region, Ganges, magic, all of these)", "all of these", "region", "Ganges", "magic", "A", "region, Ganges, magic all have soft /j/ sound for 'g'."),
        ("Choose the correct spelling with **'ea'** digraph for mountain summit:", "peak", "peek", "peke", "piek", "A", "peak is standard spelling for mountain summit.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT06_Q{idx:02d}"
        qtxt = f"Phonics Analysis & Sound Pattern Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Phonic Rules & Sound Discrimination", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the phonics rule: Why does 'c' in **'glacier'** sound like /sh/, but 'c' in **'climber'** sounds like /k/?", "Because 'c' followed by 'ia' or 'ie' often makes soft /sh/ sound (glacier); before 'l', 'a', 'o', 'u' it makes hard /k/ sound.", "Because glacier is ice.", "Because climber is a person.", "There is no rule.", "A", "Palatalization rule: c + ie/ia = /sh/ sound."),
        ("Categorize the 'ea' digraphs into long /e/ vs short /e/: (peak, reach, bread, heavy, lead [metal])", "Long /e/: peak, reach; Short /e/: bread, heavy, lead [metal]", "All are long /e/.", "All are short /e/.", "Long /e/: bread; Short /e/: peak", "A", "peak, reach make long /e/; bread, heavy, lead (metal) make short /e/."),
        ("Identify the word pair where SILENT letters exist in BOTH words:", "high - climb", "peak - river", "snow - mountain", "range - summit", "A", "'high' (silent gh) and 'climb' (silent b)."),
        ("Decode the phonics blend: Which word contains a 3-letter consonant blend at the start?", "stretches / stream", "peak", "climb", "snow", "A", "'str' blend type."),
        ("Examine the hard vs soft 'g' rule: Why is 'g' soft in **'Ganges' (second g)** but hard in **'Ganges' (first g)**?", "First 'g' before 'a' makes hard /g/ sound; second 'g' before 'e' makes soft /j/ sound.", "Because Ganges is a river.", "Because India is hot.", "There is no rule.", "A", "Soft 'g' rule: g + e, i, y = /j/ sound; g + a, o, u = /g/ sound."),
        ("Find the word with BOTH a vowel digraph AND a silent letter:", "highest", "peak", "river", "snow", "A", "'highest' has 'igh' trigraph with silent 'gh'."),
        ("Differentiate diphthongs: Which pair produces the /ow/ sound as in **'mountain'**?", "mountain - around", "voice - coin", "paid - day", "boat - coat", "A", "'mountain' and 'around' share /ow/ diphthong sound."),
        ("Analyze homophones: 'They reached the **peak** / **peek**.' Which word means mountain top?", "peak", "peek", "peke", "piek", "A", "'peak' (top of mountain) and 'peek' (quick look) are homophones."),
        ("Identify the phonic pattern in **'autonomous'**: What vowel sound does the first 'au' make?", "Aw / Or sound", "Short /a/ sound", "Silent sound", "Short /u/ sound", "A", "'au' makes /aw/ sound in autonomous."),
        ("Sort by ending sound: Which word ends with the /z/ sound? (peaks, rivers, mountains, glaciers)", "rivers / mountains / glaciers", "peaks", "summits", "climbs", "A", "Plurals ending in voiced consonants take /z/ ending sound (rivers, mountains)."),
        ("Spot the word where 'b' is SILENT: (climb, thumb, lamb, all of these)", "all of these", "climb", "thumb", "lamb", "A", "'b' is silent after 'm' in climb, thumb, lamb."),
        ("HOTS Reasoning: Why do 'peak' and 'peek' sound identical but have different spellings and meanings?", "They are homophones (same sound, different spelling/meaning).", "They are synonyms.", "They are antonyms.", "They are plurals.", "A", "Homophones share pronunciation but differ in spelling/meaning."),
        ("Identify the compound word from story concepts containing two simple words:", "snowfall / landmark", "Himalayas", "Everest", "glacier", "A", "snowfall = snow + fall; landmark = land + mark."),
        ("Determine the syllable count and stress: How many syllables are in **'mountaineers'**?", "3 syllables (moun-tain-eers)", "2 syllables", "4 syllables", "1 syllable", "A", "moun-tain-eers has 3 syllables.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT06_Q{idx:02d}"
        qtxt = f"Higher Order Phonics & Orthographic Analysis:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Phonetic Rules & Homophone Logic", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 7. Question Words & Interrogatives (50 Qs)
# ---------------------------------------------------------------------------
def build_question_words():
    header = "# Category 7: Question Words & Interrogatives — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_qwords = [
        ("___ does the word 'Himalaya' mean in Sanskrit?", "What", "Who", "Where", "Why", "A", "'What' asks about meaning ('abode of snow')."),
        ("___ is the highest mountain peak on Earth?", "Which", "Who", "Where", "Why", "A", "'Which' asks about specific peak (Mount Everest)."),
        ("___ is Mount Everest located?", "Where", "Who", "What", "Why", "A", "'Where' asks about location (border between Nepal and Tibet)."),
        ("___ was the first person from New Zealand to reach Mount Everest's summit?", "Who", "What", "Where", "Why", "A", "'Who' asks about person (Edmund Hillary)."),
        ("___ was the Sherpa guide who climbed Mount Everest with Hillary?", "Who", "What", "Where", "Why", "A", "'Who' asks about person (Tenzing Norgay)."),
        ("___ high is Mount Everest?", "How", "Who", "Where", "Why", "A", "'How high' asks about elevation (8,849 metres)."),
        ("___ far do the Himalayas stretch from west to east?", "How long / How far", "Who", "Where", "Why", "A", "'How far' asks about distance (2,500 kilometers)."),
        ("___ year did Hillary and Tenzing reach the summit?", "Which / In what year", "Who", "Where", "Why", "A", "'Which' asks about year (1953)."),
        ("___ of Earth's 10 highest peaks are in the Himalayas?", "How many", "Who", "Where", "Why", "A", "'How many' asks about number (nine peaks)."),
        ("___ important rivers originate in the Himalayas?", "How many", "Who", "Where", "Why", "A", "'How many' asks about number (three rivers: Indus, Ganges, Brahmaputra)."),
        ("___ is the Himalayas called the 'abode of snow'?", "Why", "Who", "Where", "What", "A", "'Why' asks for reason (peaks covered with snow all year round)."),
        ("___ rivers originate in the Himalayas?", "Which", "Who", "Where", "Why", "A", "'Which rivers' asks for identification (Indus, Ganges, Brahmaputra)."),
        ("___ region of China borders Nepal at Mount Everest?", "Which", "Who", "Why", "When", "A", "'Which' asks about region (Tibet Autonomous Region)."),
        ("___ country was Edmund Hillary from?", "Which", "Who", "Where", "Why", "A", "'Which country' asks about nation (New Zealand)."),
        ("___ season do mountaineers usually climb Mount Everest?", "Which", "Who", "Where", "Why", "A", "'Which season' asks about timing (spring / May)."),
        ("___ created the major river systems in North India?", "What", "Who", "Where", "Why", "A", "'What' asks about source (Himalayan glaciers)."),
        ("___ did mountaineers first start climbing the high Himalayan peaks?", "When", "Who", "Where", "Why", "A", "'When' asks about era (in the 1900s)."),
        ("___ does the snow on lofty peaks melt into?", "What", "Who", "Where", "Why", "A", "'What' asks about result (rivers like Ganges, Indus, Brahmaputra).")
    ]
    
    for idx, (q_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_qwords, start=1):
        qid = f"BK02_CH09_CAT07_Q{idx:02d}"
        qtxt = f"Choose the correct **question word** (Who, What, Where, Why, How, When):\n\n\"{q_blank} _____?\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Question Word Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Match question to answer: Question: '___ are the peaks called lofty?' Answer: 'Because they are extremely tall and covered with snow.'", "Why", "What", "Where", "Who", "A", "'Why' asks for reasons ('Because...')."),
        ("Match question to answer: Question: '___ is Mount Everest situated?' Answer: 'On the border between Nepal and Tibet.'", "Where", "Who", "Why", "When", "A", "'Where' asks for location."),
        ("Choose the correct question word for TIME: '___ did Hillary and Tenzing reach the summit?'", "When", "Where", "Who", "Why", "A", "'When' inquires about time (in May 1953)."),
        ("Form an asking sentence: 'The Himalayas stretch 2,500 km.' -> '____ far do the Himalayas stretch?'", "How", "Who", "Why", "Where", "A", "'How far' inquires about distance."),
        ("Identify the INCORRECT question word usage: '**Why** is the height of Mount Everest?'", "'Why' should be 'What'", "'Why' should be 'Where'", "'Why' should be 'When'", "No error", "A", "'What is the height of Mount Everest?' asks for elevation measurement."),
        ("Select the proper interrogative sentence:", "Why is Mount Everest famous around the world?", "Why Mount Everest is famous around the world?", "Why does Mount Everest is famous?", "Why Everest famous?", "A", "Interrogative word + verb 'is' + subject + predicate."),
        ("Which question word asks about MANNER or METHOD? '___ did the mountaineers climb the steep mountain?'", "How", "Who", "What", "Where", "A", "'How' inquires about method/manner (with ropes, ladders, and oxygen)."),
        ("Complete the question: '___ of the three rivers flows into the Arabian Sea?'", "Which", "What", "Where", "Why", "A", "'Which' chooses between specific options (the Indus)."),
        ("Change statement to question: 'Mount Everest is the highest peak.' -> '____ is the highest peak?'", "Which / What", "Who", "Where", "Why", "A", "'Which' asks for specific mountain peak."),
        ("Fill in the blank: '___ tall is Mount Everest?'", "How", "What", "Where", "Why", "A", "'How tall' measures height."),
        ("Identify the question word in: 'Whom did Edmund Hillary climb Mount Everest with?'", "Whom", "did", "Hillary", "Everest", "A", "'Whom' is the interrogative pronoun asking about climbing partner."),
        ("Choose the question that matches this answer: 'Because its lofty peaks are covered with snow all year round.'", "Why is Himalaya called the abode of snow?", "Where is Himalaya located?", "Who climbed Himalaya?", "What is a glacier?", "A", "'Why...' matches answer starting with 'because...'."),
        ("Fill in the blank: '___ river originates in the Himalayas and flows through India?'", "Which", "Who", "Why", "Where", "A", "'Which river' asks for identification (Ganges, Brahmaputra)."),
        ("Complete: '___ kilometers do the Himalayas cover?'", "How many", "How much", "Who", "Where", "A", "'How many' asks about countable quantity (kilometers)."),
        ("Select the correct question for: 'The Himalayas stretch from west to east.'", "In which direction do the Himalayas stretch?", "Where is New Zealand?", "Why are rivers cold?", "Who was Tenzing Norgay?", "A", "'In which direction...' asks for orientation."),
        ("Which question word inquires about POSSESSION? '___ summit was conquered in 1953?'", "Whose", "Who", "Where", "Why", "A", "'Whose' asks about mountain identity/ownership."),
        ("Form question: 'Nine of Earth's 10 highest peaks are in the Himalayas.' -> '____ peaks are in the Himalayas?'", "How many", "How much", "Why", "Where", "A", "'How many' asks for countable number."),
        ("Identify the question mark error: 'Why are the Himalayas important.' Correct it:", "Why are the Himalayas important?", "Why are the Himalayas important!", "Why are the Himalayas important,", "Why are the Himalayas important;", "A", "Questions must end with question mark ?")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT07_Q{idx:02d}"
        qtxt = f"Question Formation & Context Alignment:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Interrogative Sentence Formation", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze the sentence structure: 'Why do three major rivers originate in the Himalayas?' What is the syntax pattern?", "Question Word + Helping Verb (do) + Subject (three major rivers) + Main Verb (originate) + Prepositional Phrase", "Question Word + Main Verb + Subject", "Subject + Question Word + Verb", "Helping Verb + Question Word + Subject", "A", "Standard English question syntax."),
        ("Differentiate between 'How many' vs 'How much': '___ peaks' vs '___ snow'", "'How many' for countable peaks; 'How much' for uncountable snow.", "Both use 'How many'.", "Both use 'How much'.", "'How much' for peaks; 'How many' for snow.", "A", "Countable nouns take 'How many'; uncountable nouns take 'How much'."),
        ("Spot the syntax error in question: 'Where Edmund Hillary climbed Mount Everest?' Correct it:", "Where **did** Edmund Hillary climb Mount Everest?", "Where Edmund Hillary climb Mount Everest?", "Where climbed Edmund Hillary Mount Everest?", "Where does Edmund Hillary climbed Mount Everest?", "A", "Past simple questions require auxiliary 'did' before subject and base verb 'climb'."),
        ("Framing multi-question interview: What sequence of question words logically reveals the mountain geography?", "What does Himalaya mean -> Where is it located -> How high is Mount Everest -> Who climbed it first", "How -> Who -> Why -> What", "Where -> Where -> Where -> Where", "Why -> Why -> Why -> Why", "A", "Reveals meaning, location, scale, and human conquest."),
        ("Transform the statement into a formal question: 'Himalayan glaciers act as the water tower of Asia.'", "How do the Himalayan glaciers function as a vital water tower for Asia?", "Where is Asia?", "Who is Tenzing?", "What is snow?", "A", "Directly targets the ecological function."),
        ("Analyze this ambiguous question: 'What did they climb?' How can it be made precise?", "Add specific context: 'What peak did Edmund Hillary and Tenzing Norgay climb on 29th May 1953?'", "Make it shorter: 'What peak?'", "Change to: 'Where peak?'", "Remove 'What'.", "A", "Adding specific context clarifies which climb."),
        ("Choose the correct question pair for dialogue: Climber: '___ is the snow so deep here?' Guide: '___ about using snowshoes for safety?'", "Why, How", "Who, Where", "Where, How", "When, Whose", "A", "Why (reason for deep snow), How about (suggestion)."),
        ("Spot the DOUBLE auxiliary error: 'Why did Edmund Hillary reached the summit?'", "'did' requires base verb 'reach', not past tense 'reached'.", "'did' should be 'was'.", "'Why' should be 'How'.", "No error.", "A", "Auxiliary 'did' must be followed by base form of verb ('reach')."),
        ("Reconstruct question from answer: Answer: 'Mount Everest is 8,849 metres high.'", "Question: 'What is the exact height of Mount Everest?'", "Question: 'Where did they fly?'", "Question: 'Who is Edmund Hillary?'", "Question: 'Why is snow cold?'", "A", "Targets exact height measurement."),
        ("Form indirect question: 'The student asked how high Mount Everest was.' What is the sentence type?", "Assertive statement containing an embedded indirect question.", "Direct question requiring question mark.", "Exclamatory sentence.", "Command.", "A", "Indirect questions are statements ending with full stop."),
        ("Identify the correct question word for moral reasoning: '___ is protecting the Himalayan ecosystem vital for future generations?'", "Why", "What", "Who", "Where", "A", "'Why' inquires into the ecological reason for conservation."),
        ("HOTS Reasoning: Why is 'Who' used for climbers but 'Which' used when selecting from a specific group of mountain peaks?", "'Who' is general for people; 'Which' is used when choosing from a defined limited set of objects.", "'Who' is for inanimate objects.", "'Which' is only for numbers.", "Both are identical.", "A", "'Which of the peaks...' selects from a defined group."),
        ("Correct all errors in: 'why is mount everest called the highest peak'", "Why is Mount Everest called the highest peak?", "Why is mount everest called the highest peak.", "Whom is Mount Everest called?", "Why does Mount Everest called highest peak?", "A", "Capital W, capital M, capital E, question mark at end."),
        ("Select the question that evaluates Higher Order Thinking (HOTS) about Chapter 09:", "How does the melting of Himalayan glaciers threaten the water security of millions of people living downstream?", "What is the height of Mount Everest?", "Where is Nepal?", "Are the peaks cold?", "A", "Asks student to evaluate ecological cause-and-effect.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT07_Q{idx:02d}"
        qtxt = f"Higher Order Interrogative Analysis & Syntax:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Question Syntax & Analytical Framing", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 8. Present Continuous Tense (-ing) (50 Qs)
# ---------------------------------------------------------------------------
def build_present_continuous():
    header = "# Category 8: Present Continuous Tense (-ing) — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_ing = [
        ("The mountaineers are **climbing** Mount Everest.", "climbing", "mountaineers", "are", "Mount Everest", "A", "'climbing' is verb + -ing form."),
        ("The snow is **melting** into fresh water rivers.", "melting", "snow", "is", "rivers", "A", "'melting' is verb + -ing form."),
        ("The river is **flowing** down the valley.", "flowing", "river", "is", "valley", "A", "'flowing' is verb + -ing form."),
        ("The mountain range is **stretching** for 2,500 km.", "stretching", "range", "is", "km", "A", "'stretching' is verb + -ing form."),
        ("The wind is **blowing** across the snowy peaks.", "blowing", "wind", "is", "peaks", "A", "'blowing' is verb + -ing form."),
        ("Climbers are **crossing** dangerous glaciers.", "crossing", "climbers", "are", "glaciers", "A", "'crossing' is verb + -ing form."),
        ("The temperature is **dropping** rapidly near the summit.", "dropping", "temperature", "is", "summit", "A", "'dropping' is verb + -ing form."),
        ("The guide is **leading** the team to base camp.", "leading", "guide", "is", "team", "A", "'leading' is verb + -ing form."),
        ("The sun is **shining** on the snow-capped mountains.", "shining", "sun", "is", "mountains", "A", "'shining' is verb + -ing form."),
        ("Mountaineers are **packing** their supplies for the climb.", "packing", "mountaineers", "are", "supplies", "A", "'packing' is verb + -ing form."),
        ("The clouds are **gathering** around the lofty peaks.", "gathering", "clouds", "are", "peaks", "A", "'gathering' is verb + -ing form."),
        ("Climbers are **resting** inside their tents.", "resting", "climbers", "are", "tents", "A", "'resting' is verb + -ing form."),
        ("The glacier is **moving** slowly down the slope.", "moving", "glacier", "is", "slope", "A", "'moving' is verb + -ing form."),
        ("The scientists are **studying** Himalayan climate change.", "studying", "scientists", "are", "climate", "A", "'studying' is verb + -ing form."),
        ("The rivers are **feeding** agriculture in the plains.", "feeding", "rivers", "are", "plains", "A", "'feeding' is verb + -ing form."),
        ("Climbers are **wearing** heavy warm jackets.", "wearing", "climbers", "are", "jackets", "A", "'wearing' is verb + -ing form."),
        ("The guide is **checking** the safety ropes.", "checking", "guide", "is", "ropes", "A", "'checking' is verb + -ing form."),
        ("The snow is **accumulating** on the mountain top.", "accumulating", "snow", "is", "top", "A", "'accumulating' is verb + -ing form.")
    ]
    
    for idx, (sent, optA, optB, optC, optD, correct, explanation) in enumerate(easy_ing, start=1):
        qid = f"BK02_CH09_CAT08_Q{idx:02d}"
        qtxt = f"Identify the **present continuous (-ing) verb** in this sentence:\n\n\"{sent}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — '{optA}' is the present continuous verb form."
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Present Continuous Identification", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("What is the correct -ing spelling rule for **'climb'**? (They are ____ Mount Everest.)", "climbing (add -ing)", "climbbing", "climbeing", "climbng", "A", "Regular verb adding -ing (climbing)."),
        ("What is the correct -ing spelling rule for **'shine'**? (The sun is ____.)", "shining (drop final silent e)", "shineing", "shinning", "shinng", "A", "Drop final silent 'e' before adding -ing (shining)."),
        ("What is the correct -ing spelling rule for **'drop'**? (The temp is ____.)", "dropping (double final consonant)", "droping", "droppping", "dropeing", "A", "CVC rule: double final consonant before -ing (dropping)."),
        ("Fill in the blank with present continuous form: 'The river (flow) ____ down the valley.'", "is flowing", "was flow", "are flow", "is flowed", "A", "Singular subject takes 'is flowing'."),
        ("Choose the sentence in PRESENT CONTINUOUS tense:", "The team is climbing Mount Everest right now.", "The team climbed Mount Everest in 1953.", "The team will climb Mount Everest next year.", "The team climbed yesterday.", "A", "'is climbing' is present continuous."),
        ("Fill in the blanks: 'The rivers ____ (flow) down, and the glaciers ____ (melt).' ", "are flowing, are melting", "is flowing, is melting", "are flow, is melt", "was flowing, were melting", "A", "Plural 'rivers' takes 'are flowing'; plural 'glaciers' takes 'are melting'."),
        ("Identify the spelling mistake in: 'The sun is **shineing** on the snow.'", "'shineing' should be 'shining'", "'shineing' should be 'shining'", "'is' should be 'are'", "No mistake", "A", "Shine drops silent e before -ing (shining)."),
        ("Select the correct -ing form for **'explore'**:", "exploring", "exploreing", "explorring", "explorng", "A", "Drop silent 'e': explore -> exploring."),
        ("Which sentence describes an action HAPPENING RIGHT NOW?", "The mountaineers are crossing the icy ridge.", "The mountaineers crossed the ridge yesterday.", "The mountaineers cross the ridge every year.", "The mountaineers will cross the ridge tomorrow.", "A", "Present continuous ('are crossing') describes ongoing action right now."),
        ("Fill in the blank: 'I ____ (watch) a documentary about Mount Everest.'", "am watching", "is watching", "are watching", "am watcheing", "A", "Subject 'I' takes 'am watching'."),
        ("Choose the correct form: 'The glaciers ____ (recede) due to global warming.'", "are receding", "is receding", "am receding", "are recede", "A", "Plural subject 'glaciers' takes 'are receding'."),
        ("Identify the verb in: 'Why are you trekking in high altitude?'", "are trekking", "Why", "you", "altitude", "A", "Helping verb 'are' + main verb 'trekking' form present continuous."),
        ("What is the -ing form of **'trek'**?", "trekking", "treking", "trekkking", "trekeing", "A", "CVC rule: trek -> trekking."),
        ("What is the -ing form of **'freeze'**?", "freezing", "freezeing", "freezzing", "freezng", "A", "Drop silent e: freeze -> freezing."),
        ("Change simple present to continuous: 'Snow melts in spring.' -> 'Snow ____ in spring.'", "is melting", "melted", "was melting", "will melt", "A", "is melting."),
        ("Fill in the blank: 'The expedition ____ (approaching) the summit.'", "is approaching", "are approaching", "am approaching", "approached", "A", "is approaching."),
        ("Identify the correct present continuous sentence:", "Look! The mountaineers are reaching the peak.", "Look! The mountaineers reach the peak.", "Look! The mountaineers reached the peak.", "Look! The mountaineers reaching the peak.", "A", "Exclamation 'Look!' introduces action happening now ('are reaching')."),
        ("Select the correct -ing form for **'scale'** (a mountain):", "scaling", "scaleing", "scalving", "scalng", "A", "Drop silent e: scale -> scaling.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT08_Q{idx:02d}"
        qtxt = f"Present Continuous Grammar & Spelling Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Present Continuous Formation & Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze spelling rules for adding -ing to verbs: Group them correctly: (trek, shine, flow)", "trek -> trekking (double consonant), shine -> shining (drop e), flow -> flowing (add -ing)", "All just add -ing.", "All double the last letter.", "trek -> treking, shine -> shineing, flow -> flowwing", "A", "3 distinct orthographic rules for -ing derivation."),
        ("Convert past tense narrative to present continuous picture scene: 'The river flowed while snow melted.'", "The river is flowing while snow is melting.", "The river flowing while snow melting.", "The river was flowing while snow melted.", "The river will flow while snow melts.", "A", "Both verbs transformed to present continuous (is flowing, is melting)."),
        ("Spot the missing auxiliary verb in: 'Climbers trekking up and wind blowing hard.' Correct it:", "'Climbers **are** trekking up and wind **is** blowing hard.'", "'Climbers trekking up and wind blowing hard.'", "'Climbers **is** trekking and wind **are** blowing.'", "No error.", "A", "Present continuous requires auxiliary (is/am/are) before -ing verb."),
        ("Differentiate state vs action: Why don't we usually say 'Mount Everest is **belonging** to Nepal and Tibet'?", "Because 'belong' is a stative verb expressing ownership/location, not an ongoing physical action.", "Because 'belonging' is hard to spell.", "Because Everest is high.", "Because Nepal is cold.", "A", "Stative verbs (belong, own, exist) do not usually take continuous form."),
        ("Identify the sentence with CORRECT present continuous subject-verb agreement:", "The rivers of the Himalayas are flowing rapidly.", "The rivers of the Himalayas is flowing rapidly.", "The rivers of the Himalayas am flowing rapidly.", "The rivers of the Himalayas flowing rapidly.", "A", "Plural subject ('rivers') takes plural auxiliary 'are'."),
        ("Form negative present continuous: 'The glaciers are expanding today.' -> Negative:", "The glaciers are **not** expanding today.", "The glaciers not expanding today.", "The glaciers is no expanding today.", "The glaciers aren't expand today.", "A", "Add 'not' between auxiliary 'are' and main verb 'expanding'."),
        ("Spot all THREE spelling errors: 'He is **shineing** light, **runing** up, and **dieing** of cold.'", "'shineing' -> 'shining'; 'runing' -> 'running'; 'dieing' -> 'dying'", "'shineing' -> 'shinning'; 'runing' -> 'runing'; 'dieing' -> 'dieing'", "No errors.", "Only 'runing' is wrong.", "A", "shining (drop e), running (double n), dying (-ie to -y)."),
        ("Rewrite as interrogative present continuous: 'The mountaineers are reaching the summit.'", "**Are** the mountaineers reaching the summit?", "Is the mountaineers reaching the summit?", "The mountaineers reaching the summit?", "Why the mountaineers are reaching summit?", "A", "Move auxiliary 'Are' to beginning of sentence."),
        ("Analyze action timeline: 'The expedition **is starting** tomorrow morning.' What does present continuous express here?", "A fixed future arrangement / planned action.", "Past completed action.", "Action that happened long ago.", "Uncertain rumor.", "A", "Present continuous can express planned future actions."),
        ("Choose the sentence showing PARALLEL present continuous actions:", "While the sun is shining, the glaciers are melting.", "While sun shone, glaciers are melting.", "Sun is shining while glaciers melted.", "Sun shine while glaciers melt.", "A", "Both parallel ongoing actions use present continuous."),
        ("Correct the error: 'The water is flowwing into the valley.'", "'flowwing' should be 'flowing' (single 'w').", "'is' should be 'are'.", "'valley' should be capitalized.", "No error.", "A", "Flow + ing = flowing."),
        ("HOTS Reasoning: Compare 'Glaciers melted' (Past Simple) vs 'Glaciers are melting' (Present Continuous). How does the meaning change?", "Past simple states a completed past event; present continuous describes an action currently in progress.", "Both mean the exact same thing.", "Past simple is for future; continuous is for past.", "Continuous means snow went away.", "A", "Tense changes temporal aspect (completed vs ongoing)."),
        ("Form question: 'Why ____ the glaciers ____ (melting) so fast?'", "are, melting", "is, melting", "am, melting", "do, melting", "A", "Plural subject glaciers takes 'are ... melting'."),
        ("Identify the correct present continuous sentence describing environmental change:", "The entire Himalayan region is changing rapidly.", "The entire Himalayan region is change rapidly.", "The entire Himalayan region are changing rapidly.", "The entire Himalayan region changing rapidly.", "A", "Collective singular subject 'Himalayan region' + is + changing.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT08_Q{idx:02d}"
        qtxt = f"Higher Order Present Continuous Analysis & Editing:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Continuous Tense Aspect & Error Correction", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# 9. Helping Verbs (Is, Am, Are) (50 Qs)
# ---------------------------------------------------------------------------
def build_helping_verbs():
    header = "# Category 9: Helping Verbs (Is, Am, Are) — Chapter 09: The Himalayas\n\n> **Target**: 50 Questions | 18 Easy, 18 Medium, 14 Hard/HOTS\n\n---\n\n"
    content = ""
    
    # 18 Easy Qs (Q01 - Q18)
    easy_hv = [
        ("The Himalayas ___ a great mountain system in Asia.", "are", "is", "am", "be", "A", "Plural noun 'The Himalayas' takes 'are'."),
        ("Mount Everest ___ the highest peak on Earth.", "is", "are", "am", "be", "A", "Singular subject 'Mount Everest' takes 'is'."),
        ("I ___ fascinated by the Himalayas.", "am", "is", "are", "be", "A", "Pronoun 'I' takes 'am'."),
        ("The lofty peaks ___ covered with snow.", "are", "is", "am", "be", "A", "Plural subject 'peaks' takes 'are'."),
        ("The Indus ___ a major river in Asia.", "is", "are", "am", "be", "A", "Singular river subject 'The Indus' takes 'is'."),
        ("The Ganges and Brahmaputra ___ important rivers.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("Edmund Hillary ___ a mountaineer from New Zealand.", "is", "are", "am", "be", "A", "Singular subject 'Edmund Hillary' takes 'is'."),
        ("Tenzing Norgay and Edmund Hillary ___ the first summiters.", "are", "is", "am", "be", "A", "Compound subject takes 'are'."),
        ("I ___ learning about Mount Everest today.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The elevation of Mount Everest ___ 8,849 metres.", "is", "are", "am", "be", "A", "Singular 'elevation' takes 'is'."),
        ("The glaciers ___ melting due to warm weather.", "are", "is", "am", "be", "A", "Plural 'glaciers' takes 'are'."),
        ("Nepal ___ a beautiful country in Asia.", "is", "are", "am", "be", "A", "Singular 'Nepal' takes 'is'."),
        ("You ___ studying Chapter 09.", "are", "is", "am", "be", "A", "Pronoun 'You' always takes 'are'."),
        ("The mountaineer ___ climbing the steep slope.", "is", "are", "am", "be", "A", "Singular 'mountaineer' takes 'is'."),
        ("Nine peaks ___ higher than 8,000 metres.", "are", "is", "am", "be", "A", "Plural 'Nine peaks' takes 'are'."),
        ("I ___ proud to read about Sherpa Tenzing.", "am", "is", "are", "be", "A", "Subject 'I' takes 'am'."),
        ("The valley ___ peaceful and green.", "is", "are", "am", "be", "A", "Singular 'valley' takes 'is'."),
        ("The climbers ___ resting at base camp.", "are", "is", "am", "be", "A", "Plural 'climbers' takes 'are'.")
    ]
    
    for idx, (sent_blank, optA, optB, optC, optD, correct, explanation) in enumerate(easy_hv, start=1):
        qid = f"BK02_CH09_CAT09_Q{idx:02d}"
        qtxt = f"Fill in the blank with the correct helping verb (is / am / are):\n\n\"{sent_blank}\""
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Easy", "Remembering", "Helping Verb Basics", 1, qtxt, opts, ans)
        
    # 18 Medium Qs (Q19 - Q36)
    medium_data = [
        ("Choose the correct helping verb: 'The Himalayas and the Andes ____ major mountain ranges on Earth.'", "are", "is", "am", "be", "A", "Compound subject ('The Himalayas and the Andes') is plural, taking 'are'."),
        ("Select the sentence with CORRECT helping verb agreement:", "Mount Everest is the highest peak in the world.", "Mount Everest are the highest peak in the world.", "Mount Everest am the highest peak in the world.", "Mount Everest be the highest peak in the world.", "A", "Singular noun 'Mount Everest' requires 'is'."),
        ("Fill in the blanks: 'I ____ reading a book on Everest, and my friends ____ watching a video.'", "am, are", "is, are", "are, is", "am, is", "A", "'I am', 'friends are'."),
        ("Identify the mistake in: 'The rivers originating in the Himalayas **is** long.'", "'is' should be 'are' because 'rivers' is a plural noun.", "'is' should be 'am'", "'is' should be 'was'", "No mistake", "A", "'rivers' is plural, requiring 'are'."),
        ("Which helping verb completes the question? '____ you interested in mountaineering?'", "Are", "Is", "Am", "Be", "A", "Subject 'you' takes 'Are'."),
        ("Fill in the blank: 'Neither ice nor cold wind ____ stopping the brave climbers.'", "is", "are", "am", "be", "A", "'Neither...nor' with singular second subject 'cold wind' takes 'is'."),
        ("Select the correct sentence for story moral:", "Courage and endurance are necessary for mountaineers.", "Courage and endurance is necessary for mountaineers.", "Courage and endurance am necessary for mountaineers.", "Courage and endurance be necessary for mountaineers.", "A", "Compound subject 'Courage and endurance' takes 'are'."),
        ("Complete the conversation: Climber: 'Where ____ our guides?' Leader: 'They ____ at camp!'", "are, are", "is, is", "is, are", "are, is", "A", "Plural 'our guides' -> are; plural 'They' -> are."),
        ("Identify where 'is' is used incorrectly:", "The peaks **is** snowy.", "Mount Everest is tall.", "Nepal is scenic.", "The glacier is large.", "A", "'The peaks is' should be 'The peaks are'."),
        ("Choose the correct helping verb for collective noun used as a single unit: 'The team of climbers ____ resting.'", "is", "are", "am", "be", "A", "Collective noun 'team' treated as singular unit takes 'is'."),
        ("Fill in the blank: 'The summit of Mount Everest ____ reached by many today.'", "is", "are", "am", "be", "A", "Singular 'summit' takes 'is'."),
        ("Select the sentence with correct helping verb for 'I':", "I am planning a trek in Nepal.", "I is planning a trek in Nepal.", "I are planning a trek in Nepal.", "I be planning a trek in Nepal.", "A", "Subject 'I' takes 'am'."),
        ("Fill in the blank: 'There ____ many high peaks in Asia.'", "are", "is", "am", "be", "A", "'There are' before plural noun 'many high peaks'."),
        ("Fill in the blank: 'There ____ a massive glacier on the slope.'", "is", "are", "am", "be", "A", "'There is' before singular noun 'a massive glacier'."),
        ("Choose the correct sentence:", "What are the climbers doing at base camp?", "What is the climbers doing at base camp?", "What am the climbers doing at base camp?", "What be the climbers doing at base camp?", "A", "Plural subject 'the climbers' takes 'are'."),
        ("Identify the correct form: 'Hillary, as well as Tenzing, ____ famous worldwide.'", "is", "are", "am", "be", "A", "Subject is singular 'Hillary' ('as well as...' does not change subject number), taking 'is'."),
        ("Fill in the blank: 'Both the Ganges and the Indus ____ major river systems.'", "are", "is", "am", "be", "A", "'Both ... and ...' takes plural verb 'are'."),
        ("Select the option with correct helping verbs: 'The peak ____ high, but the climbers ____ brave.'", "is, are", "are, is", "am, are", "is, is", "A", "'peak is', 'climbers are'.")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(medium_data, start=19):
        qid = f"BK02_CH09_CAT09_Q{idx:02d}"
        qtxt = f"Helping Verb Subject-Verb Agreement Task:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Medium", "Applying", "Subject-Verb Agreement Rules", 1, qtxt, opts, ans)
        
    # 14 Hard / HOTS Qs (Q37 - Q50)
    hard_data = [
        ("Analyze subject-verb agreement: 'Each of the Himalayan peaks **____** covered with snow.' Choose the correct verb and reason:", "is — because 'Each' is a singular indefinite pronoun requiring singular verb 'is'.", "are — because 'Himalayan peaks' is plural.", "am — because it refers to speaker.", "be — because peaks are high.", "A", "'Each' is singular indefinite pronoun taking singular verb 'is'."),
        ("Spot the subtle agreement error in: 'A chain of high mountain peaks **are** visible from space.'", "'are' should be 'is' because the subject is singular noun 'chain'.", "'are' should be 'am'.", "'peaks' should be 'peak'.", "No error.", "A", "'A chain' is singular, so it requires 'is visible'."),
        ("Compare: (1) 'Edmund Hillary and Tenzing Norgay **are** famous.' vs (2) 'Edmund Hillary, along with Tenzing Norgay, **is** famous.' Why are the verbs different?", "In (1), 'and' creates a plural subject (are); in (2), 'along with' is a prepositional phrase, leaving 'Edmund Hillary' as sole singular subject (is).", "They mean different things.", "Sentence (2) is grammatically wrong.", "Both should use 'are'.", "A", "Prepositional phrases like 'along with' do not change subject number."),
        ("Identify the correct agreement for indefinite pronouns: 'Everyone on the team **____** ready for the summit.'", "is", "are", "am", "be", "A", "'Everyone' is a singular indefinite pronoun requiring 'is'."),
        ("Spot all THREE subject-verb errors in: 'The rivers **is** long, I **is** climbing, and the mountains **is** tall.'", "'rivers is' -> 'rivers are'; 'I is' -> 'I am'; 'mountains is' -> 'mountains are'", "'rivers is' -> 'rivers am'; 'I is' -> 'I are'; 'mountains is' -> 'mountains am'", "Only 'I is' is wrong.", "No errors present.", "A", "rivers are (plural), I am (1st person), mountains are (plural)."),
        ("Fill in the blanks in this complex sentence: 'Not only the leader but also the climbers **____** trekking, while the guide **____** watching.'", "are, is", "is, are", "is, is", "are, are", "A", "'Not only...but also' agrees with closer plural subject ('climbers' -> are); 'guide' -> is."),
        ("Transform to negative: 'The Himalayas and the Andes are mountain ranges.'", "The Himalayas and the Andes **are not** mountain ranges.", "The Himalayas and the Andes is not mountain ranges.", "The Himalayas and the Andes am not mountain ranges.", "The Himalayas and the Andes not mountain ranges.", "A", "Add 'not' after plural helping verb 'are'."),
        ("Analyze inverted subject position: 'Beyond the clouds **____** standing the summit of Mount Everest.'", "is", "are", "am", "be", "A", "Subject is singular 'the summit of Mount Everest', appearing after verb, requiring 'is'."),
        ("Determine agreement with uncountable nouns: 'The water from Himalayan rivers **____** clean and fresh.'", "is", "are", "am", "be", "A", "Uncountable noun 'water' is treated as singular, taking 'is'."),
        ("Correct the sentence: 'Here **is** the mountain maps you requested.'", "Here **are** the mountain maps you requested.", "Here am the mountain maps you requested.", "Here be the mountain maps you requested.", "No error.", "A", "Plural subject 'mountain maps' requires 'Here are...''"),
        ("Identify the sentence where 'is' acts as a MAIN linking verb rather than a helping verb:", "Mount Everest **is** the highest peak on Earth.", "Mount Everest **is** standing above the clouds.", "Edmund Hillary **is** climbing the ridge.", "The snow **is** melting in spring.", "A", "In 'Mount Everest is the highest peak on Earth', 'is' is the main linking verb connecting subject to predicate noun."),
        ("HOTS Reasoning: Why does English use 'am' ONLY with the subject pronoun 'I'?", "Because 'am' is the unique 1st person singular present indicative form of the verb 'to be'.", "Because 'I' is capitalized.", "Because Everest is high.", "There is no reason.", "A", "'am' is exclusively reserved for 1st person singular 'I'."),
        ("Fill in the blanks: 'Neither Hillary nor his companions **____** quitting, because the mountain **____** challenging.'", "are, is", "is, are", "is, is", "are, are", "A", "'companions' is closer plural subject -> are; 'mountain' -> is."),
        ("Select the option with PERFECT helping verb agreement throughout:", "Mount Everest is high, I am climbing, and the rivers are flowing.", "Mount Everest are high, I is climbing, and the rivers is flowing.", "Mount Everest am high, I are climbing, and the rivers am flowing.", "Mount Everest is high, I is climbing, and the rivers is flowing.", "A", "Mount Everest is (singular), I am (1st person), rivers are (plural).")
    ]
    
    for idx, (q_context, optA, optB, optC, optD, correct, explanation) in enumerate(hard_data, start=37):
        qid = f"BK02_CH09_CAT09_Q{idx:02d}"
        qtxt = f"Higher Order Helping Verb Reasoning:\n\n{q_context}"
        opts = [f"(A) {optA}", f"(B) {optB}", f"(C) {optC}", f"(D) {optD}"]
        ans = f"**({correct}) {optA}** — {explanation}"
        content += make_q_block(qid, "MCQ", "Hard", "Analyzing", "Complex Subject-Verb Agreement & Syntax", 2, qtxt, opts, ans)
        
    return header + content

# ---------------------------------------------------------------------------
# MAIN EXECUTION FOR REBUILDING CHAPTER 09
# ---------------------------------------------------------------------------
def rebuild_chapter_09():
    print("Rebuilding Chapter 09 category files with high-quality, multi-tiered (Easy/Medium/Hard) non-duplicate questions...")

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
        filepath = os.path.join(CH09_DIR, fname)
        print(f"  Generating {fname}...")
        content = gen_func()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  [OK] {fname} created successfully.")

    print("\n[SUCCESS] Completed rebuilding all 9 category files for Chapter 09 (450 total high-quality questions)!")

if __name__ == "__main__":
    rebuild_chapter_09()
