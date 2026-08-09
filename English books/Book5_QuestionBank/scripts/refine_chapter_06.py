r"""
Refines all 6 Category files for Book 5 Chapter 06 ("The Milkman of India: Dr. Verghese Kurien") for Class 5.
Guarantees:
- 100% text-specific, realistic distractors for MCQs (A, B, C, D).
- 100% accurate sentence structures for Fill in the Blanks.
- Plausible statements for True/False.
- Detailed, high-rigor model answers for Short, Long, and Extract questions.
- 6 Categories: mcqs.md, fill_in_the_blanks.md, true_false.md, short_answer.md, long_answer.md, extract_based.md.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH06_DIR = os.path.join(BASE_DIR, "question_bank", "chapter_06")
os.makedirs(CH06_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. MCQs (50 Distinct Qs with Realistic Distractors)
# -------------------------------------------------------------
mcq_data = [
    # Easy (1-25)
    ("Who is universally known as the 'Milkman of India'?", "(A) Dr. Verghese Kurien", "(B) Tribhuvandas Patel", "(C) M. S. Swaminathan", "(D) Dr. A. P. J. Abdul Kalam", "(A)", "Dr. Verghese Kurien earned the title 'Milkman of India'.", "Easy", "Remembering", "Biographical Identity"),
    ("What major national achievement is credited to Dr. Verghese Kurien's leadership?", "(A) Making India the largest milk producer in the world", "(B) Inventing the first mechanical computer", "(C) Building the first space satellite", "(D) Discovering new wheat varieties", "(A)", "Played a big role in making India the largest milk producer in the world.", "Easy", "Remembering", "National Achievement"),
    ("When was Dr. Verghese Kurien born?", "(A) November 26, 1921", "(B) August 15, 1947", "(C) January 26, 1950", "(D) October 2, 1869", "(A)", "Born on November 26, 1921.", "Easy", "Remembering", "Birth Date"),
    ("In which Indian state was Dr. Verghese Kurien born?", "(A) Kerala", "(B) Gujarat", "(C) Tamil Nadu", "(D) Maharashtra", "(A)", "Born in Kerala.", "Easy", "Remembering", "Birthplace"),
    ("What subject did Dr. Kurien study initially in India before going abroad?", "(A) Mechanical engineering", "(B) Dairy engineering", "(C) Medicine", "(D) Civil architecture", "(A)", "Studied mechanical engineering first.", "Easy", "Remembering", "Education"),
    ("What subject did Dr. Kurien go to the United States to study?", "(A) Dairy engineering", "(B) Electrical engineering", "(C) Agriculture business", "(D) Veterinary surgery", "(A)", "Went to the US to study dairy engineering.", "Easy", "Remembering", "Higher Education"),
    ("To which small town in Gujarat was Dr. Kurien sent by the government upon returning to India?", "(A) Anand", "(B) Ahmedabad", "(C) Surat", "(D) Rajkot", "(A)", "Sent to work in Anand, a small town in Gujarat.", "Easy", "Remembering", "Work Location"),
    ("Who was helping dairy farmers in Anand sell their milk without middlemen?", "(A) Tribhuvandas Patel", "(B) Sardar Vallabhbhai Patel", "(C) Morarji Desai", "(D) Mahatma Gandhi", "(A)", "Tribhuvandas Patel was helping farmers sell milk without middlemen.", "Easy", "Remembering", "Key Partner"),
    ("In which year was the famous Amul dairy cooperative formed in Anand?", "(A) 1946", "(B) 1950", "(C) 1921", "(D) 1970", "(A)", "The Amul dairy cooperative was formed in 1946.", "Easy", "Remembering", "Amul Formation"),
    ("What dairy products did Amul become famous for under Dr. Kurien's leadership?", "(A) Milk, butter, cheese, and ice cream", "(B) Wheat, rice, and flour", "(C) Tea, coffee, and cocoa", "(D) Soft drinks and canned juices", "(A)", "Popular brand for milk, butter, cheese, and ice cream.", "Easy", "Remembering", "Dairy Products"),
    ("What famous national movement was led by Dr. Kurien to boost milk production across India?", "(A) The White Revolution", "(B) The Green Revolution", "(C) The Blue Revolution", "(D) The Digital Revolution", "(A)", "His efforts led to the White Revolution.", "Easy", "Remembering", "National Movement"),
    ("What major national dairy initiative did Dr. Kurien launch in 1970?", "(A) Operation Flood", "(B) Operation Green", "(C) Operation Milk", "(D) Operation Anand", "(A)", "In 1970, he launched Operation Flood.", "Easy", "Remembering", "Operation Flood"),
    ("How did Operation Flood directly benefit small Indian dairy farmers?", "(A) Helped farmers earn more money and sell milk without exploitation", "(B) Gave farmers free tractors", "(C) Exported all milk to foreign countries", "(D) Replaced cows with buffalos", "(A)", "Helped farmers earn more money and provided affordable milk.", "Easy", "Understanding", "Farmer Benefits"),
    ("Which prestigious civil award was conferred upon Dr. Verghese Kurien?", "(A) Padma Vibhushan", "(B) Param Vir Chakra", "(C) Nobel Peace Prize", "(D) Bharat Ratna", "(A)", "Received awards including the Padma Vibhushan.", "Easy", "Remembering", "Awards"),
    ("Which international award did Dr. Kurien receive for his work in food security?", "(A) The World Food Prize", "(B) The Pulitzer Prize", "(C) The Oscar Award", "(D) The Booker Prize", "(A)", "Received the World Food Prize.", "Easy", "Remembering", "International Honors"),
    ("On what date did Dr. Verghese Kurien pass away?", "(A) September 9, 2012", "(B) November 26, 2012", "(C) August 15, 2010", "(D) January 1, 2015", "(A)", "He passed away on September 9, 2012.", "Easy", "Remembering", "Passing Date"),
    ("What status did India achieve in global agriculture thanks to Dr. Kurien?", "(A) Became self-sufficient in milk production and the largest milk producer worldwide", "(B) Became the largest exporter of wheat", "(C) Became dependent on milk imports from Europe", "(D) Stopped dairy farming completely", "(A)", "India became self-sufficient and the largest milk producer in the world.", "Easy", "Understanding", "National Impact"),
    ("What does the word 'revolution' mean in the vocabulary box?", "(A) A big change that brings improvement", "(B) A small mistake in math", "(C) A political election", "(D) A musical song", "(A)", "Revolution means a big change that brings improvement.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'dairy' mean?", "(A) A place where milk is processed and sold", "(B) A daily book to write thoughts", "(C) A farm for growing wheat", "(D) A factory for making shoes", "(A)", "Dairy means a place where milk is processed and sold.", "Easy", "Understanding", "Vocabulary"),
    ("What does the word 'middlemen' mean in dairy marketing?", "(A) Intermediaries who buy cheap from farmers and sell expensive to buyers for personal profit", "(B) Farmers who live in middle India", "(C) Truck drivers who transport milk", "(D) Government inspectors", "(A)", "Middlemen are intermediaries who buy cheap from producers and sell for profit.", "Easy", "Understanding", "Vocabulary"),
    ("What is a 'cooperative' as exemplified by Amul?", "(A) A business enterprise owned and operated jointly by member farmers who share profits", "(B) A private company owned by one billionaire", "(C) A foreign government agency", "(D) A school library", "(A)", "An enterprise owned and operated jointly by members sharing profits.", "Easy", "Understanding", "Cooperative Model"),
    ("Why were middlemen harmful to small dairy farmers before Amul?", "(A) They paid farmers unfair, low prices while keeping large profits for themselves", "(B) They spilled milk on purpose", "(C) They forced farmers to leave their villages", "(D) They sold milk only at night", "(A)", "Paid unfair low prices and kept large profits for themselves.", "Easy", "Understanding", "Exploitation"),
    ("How did modern technology introduced by Dr. Kurien help dairy processing?", "(A) Allowed surplus milk to be converted into buffalo milk powder, butter, and long-life products", "(B) Made milk change color", "(C) Turned milk into carbonated soda", "(D) Made cows produce twice as much water", "(A)", "Converted surplus milk into powder, butter, and shelf-stable products.", "Easy", "Understanding", "Technology Impact"),
    ("What title is given to Chapter 06?", "(A) The Milkman of India: Dr. Verghese Kurien", "(B) The Iron Man of India", "(C) The Missile Man of India", "(D) Sankalp and his Friend", "(A)", "Title is 'The Milkman of India: Dr. Verghese Kurien'.", "Easy", "Remembering", "Chapter Title"),
    ("Why does Dr. Kurien's legacy continue to benefit millions today?", "(A) The Amul cooperative network continues to provide reliable daily income to millions of dairy farmers", "(B) He left gold coins for every farmer", "(C) He built thousands of schools in Kerala", "(D) Free milk is distributed by law every day", "(A)", "The cooperative network continues to provide reliable daily income to millions.", "Easy", "Understanding", "Legacy"),

    # Medium (26-40)
    ("Why was Dr. Kurien's decision to stay in Anand a turning point for Indian agriculture?", "(A) Instead of pursuing a lucrative urban engineering career, he dedicated his expertise to empowering poor rural farmers", "(B) Anand had the largest gold mines in India", "(C) He wanted to become the mayor of Anand", "(D) The government forced him to stay under arrest", "(A)", "Dedicated engineering expertise to empowering poor rural dairy farmers.", "Medium", "Analyzing", "Turning Point"),
    ("How did the partnership between Tribhuvandas Patel and Dr. Kurien combine complementary strengths?", "(A) Patel provided grass-roots farmer trust and political vision; Kurien provided engineering excellence and modern management", "(B) Patel built buildings; Kurien milked cows", "(C) Both were foreign scientists", "(D) Patel managed finances; Kurien drove trucks", "(A)", "Patel provided farmer trust/vision; Kurien provided engineering/management.", "Medium", "Comparing", "Leadership Synergy"),
    ("Why was Operation Flood referred to as the 'White Revolution'?", "(A) It created a massive, nationwide surge in milk (white liquid) production, turning India from milk-deficient to self-sufficient", "(B) Farmers wore white shirts during protests", "(C) Milk was mixed with white snow", "(D) It took place during winter snowstorms", "(A)", "Created a massive surge in milk production, achieving national self-sufficiency.", "Medium", "Analyzing", "Symbolic Name"),
    ("How did the Amul model eliminate the exploitation of small dairy farmers?", "(A) By establishing village milk collection centers owned by farmers themselves, ensuring immediate payment based on fat content", "(B) By forcing private buyers to close their shops", "(C) By giving free milk to urban consumers", "(D) By banning milk sales in cities", "(A)", "Village collection centers owned by farmers ensured immediate, fair payment.", "Medium", "Analyzing", "Cooperative Mechanics"),
    ("What technical breakthrough did Amul achieve regarding buffalo milk?", "(A) Dr. Kurien and H. M. Dalaya successfully produced milk powder and condensed milk from buffalo milk for the first time in the world", "(B) They turned buffalo milk into cheese spread without refrigeration", "(C) They proved buffalo milk is identical to goat milk", "(D) They boiled milk using solar rays", "(A)", "Produced milk powder and condensed milk from buffalo milk for the first time.", "Medium", "Understanding", "Technical Innovation"),
    ("How did Operation Flood help urban consumers alongside rural producers?", "(A) It created organized distribution networks supplying clean, pasteurized, affordable milk to cities daily", "(B) It gave urban consumers free cows", "(C) It forced city people to move to villages", "(D) It lowered city water bills", "(A)", "Supplied clean, pasteurized, affordable milk to cities daily.", "Medium", "Evaluating", "Dual Benefit"),
    ("Why is Dr. Verghese Kurien considered a pioneer of social entrepreneurship?", "(A) He used commercial business tools and professional management to solve deep social problems like rural poverty", "(B) He started private banks for profit", "(C) He donated all his personal property to charity", "(D) He ran for political election", "(A)", "Used commercial business tools and management to solve rural poverty.", "Medium", "Evaluating", "Social Entrepreneurship"),
    ("What does the word 'self-sufficient' mean in the context of India's milk supply?", "(A) India produces enough milk to meet all national demand without relying on foreign imports", "(B) Every home has its own private cow", "(C) Milk is free for every citizen", "(D) India exports 100% of its milk", "(A)", "Produces enough milk to meet national demand without foreign imports.", "Medium", "Understanding", "Economic Concept"),
    ("How did Amul's success influence other Indian states?", "(A) It led to the replication of the Anand cooperative model across India through the National Dairy Development Board (NDDB)", "(B) It made all states change their names to Anand", "(C) It stopped dairy farming in other states", "(D) It forced all states to buy milk from Gujarat only", "(A)", "Replicated the Anand model across India via NDDB.", "Medium", "Analyzing", "Replication"),
    ("What makes dairy farming a vital secondary income source for Indian smallholders?", "(A) Milk provides daily cash flow to landless and small farmers, complementing seasonal crop harvests", "(B) Cows do not require any food or water", "(C) Milk can be stored for ten years without spoiling", "(D) Dairy farming requires no human effort", "(A)", "Provides daily cash flow complementing seasonal crop harvests.", "Medium", "Understanding", "Rural Economy"),
    ("How did Dr. Kurien maintain professional independence for dairy cooperatives?", "(A) He insisted that cooperatives be managed by professional managers accountable to farmer-owners rather than government bureaucrats", "(B) He refused to talk to government ministers", "(C) He ran Amul as a private family business", "(D) He moved Amul's headquarters to the United States", "(A)", "Managed by professional managers accountable to farmer-owners.", "Medium", "Analyzing", "Governance"),
    ("What character traits enabled Dr. Kurien to overcome resistance from private milk traders?", "(A) Unyielding integrity, courage, innovative thinking, and deep commitment to farmer welfare", "(B) Physical violence and intimidation", "(C) High wealth and political royalty", "(D) Indifference to public opinion", "(A)", "Unyielding integrity, courage, innovation, and commitment to farmers.", "Medium", "Evaluating", "Character Traits"),
    ("How does the story of Dr. Kurien inspire young Indians today?", "(A) It demonstrates that engineering and management skills can be used to uplift millions of rural citizens", "(B) It teaches that moving abroad is the only way to succeed", "(C) It encourages young people to avoid agriculture", "(D) It shows that business is only about making personal profits", "(A)", "Demonstrates how professional skills can be used to uplift rural citizens.", "Medium", "Evaluating", "Inspirational Impact"),
    ("Summarize Chapter 06 in four concise sentences.", "(A) Dr. Verghese Kurien was born in Kerala in 1921, created the Amul cooperative in Anand in 1946, led the White Revolution and Operation Flood in 1970, making India the world's largest milk producer.", "(B) Dr. Kurien lived in England all his life.", "(C) Dr. Kurien invented the personal computer in 1945.", "(D) Operation Flood was a storm in Gujarat.", "(A)", "Summarizes Dr. Kurien's life, Amul, White Revolution, and Operation Flood.", "Medium", "Understanding", "Chapter Summary"),
    ("What advice would Dr. Kurien give to young professionals entering rural development?", "(A) Respect local farmers, combine modern professional skills with integrity, and build democratic institutions owned by the people", "(B) Leave villages and work only in foreign cities", "(C) Focus only on personal wealth creation", "(D) Let middlemen handle all trading", "(A)", "Respect farmers, combine professional skills with integrity, build democratic institutions.", "Medium", "Applying", "Real-World Application"),

    # Hard (41-50)
    ("Critique the structural shift from middleman exploitation to cooperative ownership in Operation Flood.", "(A) Middlemen extracted monopsony profits from helpless individual farmers; cooperative pooling gave farmers collective scale, market power, and direct profit sharing", "(B) Middlemen were fairer than cooperatives", "(C) Cooperative ownership destroyed dairy farming in Gujarat", "(D) Operation Flood forced farmers to work without pay", "(A)", "Cooperative pooling gave farmers collective market power and direct profit sharing over monopsony exploitation.", "Hard", "Evaluating", "HOTS Economic Critique"),
    ("Deconstruct the technical significance of H. M. Dalaya and Dr. Kurien's buffalo milk powder breakthrough.", "(A) Western experts claimed buffalo milk could not be spray-dried into powder due to fat composition; Dalaya and Kurien proved them wrong, unlocking India's massive buffalo milk potential", "(B) Buffalo milk was banned in international markets", "(C) Cow milk could not be made into butter", "(D) Buffalo milk powder was invented in Germany", "(A)", "Proved Western experts wrong by spray-drying buffalo milk into powder, unlocking India's dairy potential.", "Hard", "Analyzing", "Technical Controversy"),
    ("Evaluate the socio-economic empowerment of rural women through Amul's daily milk payouts.", "(A) Since rural women manage cattle feeding and milking, direct daily cash payouts into female accounts increased women's household financial decision-making power", "(B) Women were excluded from Amul cooperatives", "(C) Daily payouts caused financial ruin in villages", "(D) Cattle care was managed exclusively by city banks", "(A)", "Direct daily cash payouts to women increased household financial decision-making power.", "Hard", "Evaluating", "Gender & Social Impact"),
    ("Compare the White Revolution (Milk) led by Kurien with the Green Revolution (Crops) led by Swaminathan.", "(A) Green Revolution focused on crop yields through seeds/fertilizers; White Revolution focused on cooperative market empowerment and daily farmer cash flow", "(B) Green Revolution was about milk; White Revolution was about wheat", "(C) Both revolutions were managed by foreign companies", "(D) Neither revolution had any impact on India", "(A)", "Crop yields vs cooperative market empowerment and daily farmer cash flow.", "Hard", "Comparing", "Comparative Revolution Analysis"),
    ("Formulate a speech commemorating Dr. Kurien's legacy on National Milk Day (Nov 26).", "(A) 'Today we honor Dr. Verghese Kurien, who turned milk into a tool of farmer empowerment. By trusting rural producers and building Amul, he made India #1 in milk and gave millions dignity and self-reliance!'", "(B) 'Dr. Kurien was an ordinary farmer who hated milk.'", "(C) 'We celebrate National Milk Day by importing milk from abroad.'", "(D) 'Operation Flood was a weather disaster in Gujarat.'", "(A)", "Commemorative speech highlighting empowerment, Amul, national self-reliance, and dignity.", "Hard", "Creating", "Commemorative Speech Design"),
    ("Assess the governance principle of NDDB (National Dairy Development Board) established by Kurien.", "(A) NDDB placed professional management at the service of farmer cooperatives, insulating dairy development from political interference", "(B) NDDB gave all profits to foreign investors", "(C) NDDB banned dairy cooperatives in South India", "(D) NDDB was a private city bank", "(A)", "Placed professional management at the service of farmer cooperatives, insulating from political interference.", "Hard", "Evaluating", "Governance Assessment"),
    ("Analyze how branding ('Amul - The Taste of India') created national pride and consumer loyalty.", "(A) Memorable advertising, consistent quality, and affordable pricing created an emotional connection linking everyday dairy buying to national economic pride", "(B) Amul advertised only in foreign languages", "(C) Amul products were sold only to government officials", "(D) The iconic Amul girl campaign was banned", "(A)", "Memorable advertising, consistent quality, and pricing linked dairy buying to national pride.", "Hard", "Analyzing", "Branding & Cultural Impact"),
    ("Synthesize how Chapter 06 integrates biography, economics, and civic responsibility for Class 5.", "(A) Combines biographical facts (Kurien's life) with economic concepts (cooperatives/middlemen/Operation Flood) and civic values (farmer empowerment/integrity)", "(B) Replaces English reading with dairy machinery repair", "(C) Focuses solely on listing names of cities in Gujarat", "(D) Teaches children how to drive milk delivery vans", "(A)", "Integrates biographical facts, economic concepts, and civic values seamlessly.", "Hard", "Synthesizing", "Curricular Integration"),
    ("Critique the statement: 'Operation Flood was purely a technological project.'", "(A) Inaccurate; Operation Flood was primarily a social and economic revolution that used technology as a tool to empower millions of marginalized rural producers", "(B) Completely true; it had nothing to do with people", "(C) False; Operation Flood was a flood relief project", "(D) True; it was designed only to test American machinery", "(A)", "Inaccurate; it was primarily a social and economic revolution using technology as an empowerment tool.", "Hard", "Evaluating", "Historical Critique"),
    ("Formulate a comprehensive essay prompt based on Chapter 06 for a Class 5 assessment.", "(A) 'Explain how Dr. Verghese Kurien earned the title 'Milkman of India'. Describe his work in Anand, the formation of Amul, and how Operation Flood transformed life for Indian farmers.'", "(B) 'Write five sentences about your favorite ice cream flavor.'", "(C) 'List five dairy products sold in supermarkets.'", "(D) 'Draw a picture of a cow in a field.'", "(A)", "Structured essay prompt evaluating biographical facts, cooperative mechanics, and national impact.", "Hard", "Creating", "Assessment Task Design")
]

mcq_content = f"# MCQs — Chapter 06: The Milkman of India: Dr. Verghese Kurien\n\n> **Category**: Multiple Choice Questions | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(mcq_data, start=1):
    q_id = f"BK05_CH06_MCQ_{idx:03d}"
    q_txt, opt_a, opt_b, opt_c, opt_d, ans, exp, diff, *rest = item
    bloom = rest[0] if len(rest) > 0 else "Remembering"
    topic = rest[1] if len(rest) > 1 else "General"
    mcq_content += f"### Question {idx}\n"
    mcq_content += f"- **Question ID**: {q_id}\n"
    mcq_content += f"- **Type**: MCQ\n"
    mcq_content += f"- **Difficulty**: {diff}\n"
    mcq_content += f"- **Bloom Level**: {bloom}\n"
    mcq_content += f"- **Topic**: {topic}\n"
    mcq_content += f"- **Marks**: 1\n\n"
    mcq_content += f"**Question**: {q_txt}\n\n"
    mcq_content += f"- {opt_a}\n- {opt_b}\n- {opt_c}\n- {opt_d}\n\n"
    mcq_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH06_DIR, "mcqs.md"), "w", encoding="utf-8") as f:
    f.write(mcq_content)

# -------------------------------------------------------------
# 2. Fill in the Blanks (50 Distinct Qs)
# -------------------------------------------------------------
fib_data = [
    # Easy (1-25)
    ("Dr. Verghese Kurien is universally known as the _______ of India.", "Milkman", "Milkman of India.", "Easy"),
    ("Dr. Kurien played a big role in making India the largest milk _______ in the world.", "producer", "Largest milk producer.", "Easy"),
    ("Dr. Kurien was born on November 26, _______.", "1921", "Born in 1921.", "Easy"),
    ("Dr. Kurien was born in the Indian state of _______.", "Kerala", "Born in Kerala.", "Easy"),
    ("He studied mechanical engineering in India and later studied _______ engineering in the US.", "dairy", "Dairy engineering.", "Easy"),
    ("Dr. Kurien was sent by the government to work in _______, a small town in Gujarat.", "Anand", "Town of Anand.", "Easy"),
    ("In Anand, he met _______ Patel who was helping farmers sell milk without middlemen.", "Tribhuvandas", "Tribhuvandas Patel.", "Easy"),
    ("In 1946, the famous _______ dairy cooperative was formed in Anand.", "Amul", "Amul cooperative in 1946.", "Easy"),
    ("Amul became a popular brand for milk, butter, cheese, and ice _______.", "cream", "Popular for ice cream.", "Easy"),
    ("Dr. Kurien's efforts led to the _______ Revolution across India.", "White", "White Revolution.", "Easy"),
    ("In 1970, Dr. Kurien launched Operation _______.", "Flood", "Operation Flood in 1970.", "Easy"),
    ("Operation Flood helped farmers earn more _______ for their milk.", "money", "Earn more money.", "Easy"),
    ("Operation Flood provided affordable _______ to consumers across India.", "milk", "Affordable milk.", "Easy"),
    ("Dr. Kurien was honored with the Padma _______ award.", "Vibhushan", "Padma Vibhushan.", "Easy"),
    ("He received the international World _______ Prize for food security.", "Food", "World Food Prize.", "Easy"),
    ("Dr. Kurien passed away on September 9, _______.", "2012", "Passed away in 2012.", "Easy"),
    ("Thanks to Dr. Kurien, India became _______ in milk production.", "self-sufficient", "Self-sufficient in milk.", "Easy"),
    ("A revolution is defined as a big change that brings _______.", "improvement", "Big change bringing improvement.", "Easy"),
    ("A dairy is a place where milk is processed and _______.", "sold", "Processed and sold.", "Easy"),
    ("Tribhuvandas Patel helped farmers sell their milk without _______.", "middlemen", "Without middlemen.", "Easy"),
    ("Dr. Kurien introduced modern technology and better _______ to Amul.", "management", "Modern technology and better management.", "Easy"),
    ("The White Revolution greatly increased milk _______ across India.", "production", "Increased milk production.", "Easy"),
    ("His work continues to benefit _______ of farmers today.", "millions", "Benefit millions.", "Easy"),
    ("Dr. Kurien earned the permanent title 'Milkman of _______'.", "India", "Milkman of India.", "Easy"),
    ("Chapter 06 is titled 'The Milkman of India: Dr. Verghese _______'.", "Kurien", "Dr. Verghese Kurien.", "Easy"),

    # Medium (26-40)
    ("The Amul cooperative model eliminated direct exploitation by private _______.", "traders", "Eliminated private traders.", "Medium"),
    ("Operation Flood established nationwide milk distribution _______.", "networks", "Milk distribution networks.", "Medium"),
    ("Dairy farming provided smallholders with a steady daily cash _______.", "income", "Steady daily cash income.", "Medium"),
    ("Kurien and Dalaya successfully produced milk powder from _______ milk.", "buffalo", "Powder from buffalo milk.", "Medium"),
    ("The National Dairy Development Board expanded the Anand model _______.", "nationwide", "Expanded Anand model nationwide.", "Medium"),
    ("Farmers owned and operated village-level milk collection _______.", "societies", "Milk collection societies.", "Medium"),
    ("Amul's success demonstrated the immense power of collective _______.", "action", "Power of collective action.", "Medium"),
    ("Dr. Kurien insisted that cooperatives be run by professional _______.", "managers", "Run by professional managers.", "Medium"),
    ("Eliminating middlemen allowed farmers to receive fair market _______.", "prices", "Receive fair market prices.", "Medium"),
    ("The White Revolution transformed India from a milk-deficient nation to a milk _______.", "surplus", "Transformed to milk surplus.", "Medium"),
    ("Women in rural villages gained financial autonomy through daily milk _______.", "payouts", "Gained autonomy via daily payouts.", "Medium"),
    ("Amul's famous slogan proclaimed it as 'The Taste of _______'.", "India", "The Taste of India.", "Medium"),
    ("Kurien's visionary leadership proved that business tools can solve rural _______.", "poverty", "Solve rural poverty.", "Medium"),
    ("Operation Flood became the world's largest dairy development _______.", "program", "World's largest dairy program.", "Medium"),
    ("Chapter 06 highlights how integrity and innovation uplift human _______.", "dignity", "Uplift human dignity.", "Medium"),

    # Hard (41-50)
    ("Monopsony pricing by middlemen was replaced by cooperative profit _______.", "sharing", "Replaced by profit sharing.", "Hard"),
    ("Technical breakthroughs in buffalo milk processing defied Western expert _______.", "predictions", "Defied Western expert predictions.", "Hard"),
    ("Institutional autonomy protected farmer cooperatives from bureaucratic _______.", "interference", "Protected from bureaucratic interference.", "Hard"),
    ("Cooperative dairy scale gave smallholders collective market bargaining _______.", "power", "Gave collective bargaining power.", "Hard"),
    ("Operation Flood integrated rural production centers with urban consumer _______.", "markets", "Integrated with urban markets.", "Hard"),
    ("Dr. Kurien's social entrepreneurship model reshaped Indian agro-based _______.", "industries", "Reshaped agro-based industries.", "Hard"),
    ("Socio-economic empowerment fostered sustainable democratic rural _______.", "institutions", "Fostered democratic rural institutions.", "Hard"),
    ("Indigenous processing technology established national dairy self-_______.", "reliance", "Established national dairy self-reliance.", "Hard"),
    ("Historical analysis reveals Operation Flood as a landmark social _______.", "revolution", "Landmark social revolution.", "Hard"),
    ("Chapter 06 inspires Class 5 students to apply professional skills for national _______.", "welfare", "Apply skills for national welfare.", "Hard")
]

fib_content = f"# Fill in the Blanks — Chapter 06: The Milkman of India: Dr. Verghese Kurien\n\n> **Category**: Fill in the Blanks | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(fib_data, start=1):
    q_id = f"BK05_CH06_FIB_{idx:03d}"
    sent, ans, exp, diff = item
    fib_content += f"### Question {idx}\n"
    fib_content += f"- **Question ID**: {q_id}\n"
    fib_content += f"- **Type**: Fill in the Blanks\n"
    fib_content += f"- **Difficulty**: {diff}\n"
    fib_content += f"- **Marks**: 1\n\n"
    fib_content += f"**Question**: {sent}\n\n"
    fib_content += f"- **Answer Key**: **{ans}** ({exp})\n\n---\n\n"

with open(os.path.join(CH06_DIR, "fill_in_the_blanks.md"), "w", encoding="utf-8") as f:
    f.write(fib_content)

# -------------------------------------------------------------
# 3. True / False (50 Distinct Qs)
# -------------------------------------------------------------
tf_data = [
    # Easy (1-25)
    ("Dr. Verghese Kurien is known as the Milkman of India.", "True", "Text confirms he is known as the Milkman of India.", "Easy"),
    ("Dr. Kurien was born in Gujarat on November 26, 1921.", "False", "He was born in Kerala on November 26, 1921, and later worked in Gujarat.", "Easy"),
    ("Dr. Kurien studied mechanical engineering and dairy engineering.", "True", "Text states he studied mechanical engineering and dairy engineering.", "Easy"),
    ("Dr. Kurien went to the United States to study dairy engineering.", "True", "Text confirms he studied dairy engineering in the US.", "Easy"),
    ("Dr. Kurien was sent by the government to work in Anand, Gujarat.", "True", "Text confirms he was sent to work in Anand, Gujarat.", "Easy"),
    ("In Anand, Dr. Kurien met Tribhuvandas Patel.", "True", "Text confirms he met Tribhuvandas Patel in Anand.", "Easy"),
    ("Tribhuvandas Patel was helping middlemen exploit small farmers.", "False", "Tribhuvandas Patel was helping farmers sell milk WITHOUT middlemen.", "Easy"),
    ("The Amul dairy cooperative was formed in 1946.", "True", "Text states the Amul dairy cooperative was formed in 1946.", "Easy"),
    ("Amul became a popular brand for milk, butter, cheese, and ice cream.", "True", "Text confirms Amul became popular for these products.", "Easy"),
    ("Dr. Kurien led the Green Revolution to increase wheat production.", "False", "Dr. Kurien led the White Revolution to increase milk production.", "Easy"),
    ("Dr. Kurien launched Operation Flood in 1970.", "True", "Text confirms Operation Flood was launched in 1970.", "Easy"),
    ("Operation Flood decreased milk production across India.", "False", "Operation Flood increased milk production and made India self-sufficient.", "Easy"),
    ("Dr. Kurien received the Padma Vibhushan award.", "True", "Text states he received awards including Padma Vibhushan.", "Easy"),
    ("Dr. Kurien received the World Food Prize.", "True", "Text confirms he received the World Food Prize.", "Easy"),
    ("Dr. Kurien passed away on September 9, 2012.", "True", "Text confirms he passed away on September 9, 2012.", "Easy"),
    ("Thanks to Dr. Kurien, India became dependent on imported milk.", "False", "Thanks to Dr. Kurien, India became self-sufficient in milk production.", "Easy"),
    ("'Revolution' means a big change that brings improvement.", "True", "Vocabulary definition: Revolution = A big change bringing improvement.", "Easy"),
    ("'Dairy' means a factory where books are printed.", "False", "Dairy means a place where milk is processed and sold.", "Easy"),
    ("Operation Flood helped farmers earn more money for their milk.", "True", "Operation Flood helped farmers earn more money.", "Easy"),
    ("Amul was founded as a private company owned by foreign investors.", "False", "Amul was founded as a farmers' dairy cooperative.", "Easy"),
    ("Dr. Kurien's work continues to benefit millions of farmers today.", "True", "Text confirms his work continues to benefit millions.", "Easy"),
    ("India is currently the largest milk producer in the world.", "True", "Text states Dr. Kurien made India the largest milk producer in the world.", "Easy"),
    ("Dr. Kurien studied medicine in the United States.", "False", "He studied dairy engineering, not medicine, in the United States.", "Easy"),
    ("Chapter 06 title is 'The Milkman of India: Dr. Verghese Kurien'.", "True", "Chapter title is 'The Milkman of India: Dr. Verghese Kurien'.", "Easy"),
    ("Tribhuvandas Patel and Dr. Kurien worked together to help milk farmers.", "True", "They joined hands to build the cooperative milk movement in Anand.", "Easy"),

    # Medium (26-40)
    ("Middlemen in Anand paid fair prices to dairy farmers before 1946.", "False", "Middlemen exploited farmers by paying unfairly low prices and keeping high profits.", "Medium"),
    ("Amul stands for Anand Milk Union Limited.", "True", "Amul is an acronym for Anand Milk Union Limited.", "Medium"),
    ("Operation Flood was the world's largest dairy development program.", "True", "Operation Flood was recognized globally as the largest dairy development program.", "Medium"),
    ("Dr. Kurien's cooperative model empowered rural women who managed cattle.", "True", "Direct payouts for milk gave rural women financial decision-making power.", "Medium"),
    ("Kurien and Dalaya created milk powder from buffalo milk for the first time globally.", "True", "They made history by successfully producing milk powder from buffalo milk.", "Medium"),
    ("The National Dairy Development Board (NDDB) was established in Anand.", "True", "NDDB was set up in Anand to replicate the Amul model nationwide.", "Medium"),
    ("Operation Flood created a grid connecting rural milk producers with urban consumers.", "True", "It built cold-chain logistics linking village milk collection with city markets.", "Medium"),
    ("Dr. Kurien believed that farmers should not own the processing factories.", "False", "He firmly believed farmers MUST own the processing and marketing assets.", "Medium"),
    ("The White Revolution helped stabilize milk prices for city consumers.", "True", "It ensured reliable, hygienic, and affordable milk supplies for cities.", "Medium"),
    ("Dr. Kurien refused all government awards during his life.", "False", "He accepted awards like Padma Vibhushan and World Food Prize for his team's work.", "Medium"),
    ("Amul's success proved that Indian farmers could manage large modern enterprises.", "True", "Proved that small farmers, guided by professional managers, run world-class businesses.", "Medium"),
    ("Middlemen welcomed the formation of the Amul cooperative in 1946.", "False", "Middlemen opposed the cooperative because it eliminated their unfair profits.", "Medium"),
    ("Dr. Kurien worked in Anand for over three decades.", "True", "He dedicated over thirty years of his life to Anand and NDDB.", "Medium"),
    ("The White Revolution contributed to reducing rural poverty in India.", "True", "Provided daily cash flow to landless and smallholder farm families.", "Medium"),
    ("Chapter 06 shows how technical skills can be dedicated to nation-building.", "True", "Kurien used engineering skills to achieve national self-reliance in milk.", "Medium"),

    # Hard (41-50)
    ("Western dairy experts falsely claimed that buffalo milk could not yield high-quality powder.", "True", "Western experts claimed it was impossible; Indian scientists proved them wrong.", "Hard"),
    ("Operation Flood relied exclusively on foreign aid without local farmer involvement.", "False", "It succeeded because it was built on democratic, local farmer-owned cooperatives.", "Hard"),
    ("Cooperative milk collection centers provided daily transparent fat-content testing.", "True", "Testing milk fat in front of farmers guaranteed fair, transparent pricing.", "Hard"),
    ("Dr. Kurien advocated for government control over cooperative decision-making.", "False", "He fiercely defended cooperative autonomy from bureaucratic political control.", "Hard"),
    ("The Amul advertising campaign created strong emotional resonance across India.", "True", "The iconic 'Amul Girl' campaign became a beloved national cultural institution.", "Hard"),
    ("India imported large quantities of milk powder before the White Revolution.", "True", "India relied heavily on imported milk powder before Kurien's initiatives.", "Hard"),
    ("Dr. Kurien's leadership model is studied in business schools worldwide today.", "True", "The Amul model is a famous global case study in social entrepreneurship.", "Hard"),
    ("Operation Flood Phase I was launched in 1970 with support from the World Food Programme.", "True", "WFP provided initial butter oil and skimmed milk powder aid to fund the program.", "Hard"),
    ("Dr. Kurien believed true development meant developing people, not just machines.", "True", "His famous philosophy: 'Development is not about cows or milk; it is about people.'", "Hard"),
    ("Chapter 06 integrates biographical narrative with economic literacy for Class 5.", "True", "Combines biography, cooperative economics, and civic leadership education.", "Hard")
]

tf_content = f"# True / False — Chapter 06: The Milkman of India: Dr. Verghese Kurien\n\n> **Category**: True / False | **Total**: 50 Questions | **Marks**: 1 each\n\n---\n\n"
for idx, item in enumerate(tf_data, start=1):
    q_id = f"BK05_CH06_TF_{idx:03d}"
    stmt, ans, exp, diff = item
    tf_content += f"### Question {idx}\n"
    tf_content += f"- **Question ID**: {q_id}\n"
    tf_content += f"- **Type**: True/False\n"
    tf_content += f"- **Difficulty**: {diff}\n"
    tf_content += f"- **Marks**: 1\n\n"
    tf_content += f"**Statement**: {stmt}\n\n"
    tf_content += f"- **Answer Key**: **{ans}** — {exp}\n\n---\n\n"

with open(os.path.join(CH06_DIR, "true_false.md"), "w", encoding="utf-8") as f:
    f.write(tf_content)

# -------------------------------------------------------------
# 4. Short Answer (50 Distinct Qs)
# -------------------------------------------------------------
sa_data = [
    # Easy (1-25)
    ("Who was Dr. Verghese Kurien and why is he called the 'Milkman of India'?", "Dr. Verghese Kurien was an Indian dairy engineer who transformed India from a milk-deficient nation into the world's largest milk producer through cooperative farming.", "Easy", "Remembering"),
    ("When and where was Dr. Verghese Kurien born?", "He was born on November 26, 1921 in Kerala, India.", "Easy", "Remembering"),
    ("What educational degrees did Dr. Kurien earn in India and the United States?", "He earned a degree in mechanical engineering in India and later studied dairy engineering in the United States.", "Easy", "Remembering"),
    ("To which town in Gujarat was Dr. Kurien assigned to work by the government?", "He was assigned to work in Anand, a small town in Gujarat.", "Easy", "Remembering"),
    ("Who was Tribhuvandas Patel and how did he inspire Dr. Kurien?", "Tribhuvandas Patel was a local leader in Anand helping dairy farmers sell milk without middlemen. His selfless work inspired Dr. Kurien to join the movement.", "Easy", "Understanding"),
    ("What was the main problem dairy farmers in Anand faced before Amul was formed?", "Farmers were exploited by private middlemen who paid unfairly low prices for milk while making large personal profits.", "Easy", "Understanding"),
    ("In which year was the Amul dairy cooperative formed?", "The Amul dairy cooperative was formed in Anand in 1946.", "Easy", "Remembering"),
    ("What dairy products did Amul produce and popularize across India?", "Amul produced and popularised high-quality milk, butter, cheese, ghee, and ice cream.", "Easy", "Remembering"),
    ("What was the White Revolution?", "The White Revolution was a nationwide movement led by Dr. Kurien that dramatically increased milk production across India.", "Easy", "Understanding"),
    ("What major national project did Dr. Kurien launch in 1970?", "He launched 'Operation Flood' in 1970, which became the world's largest dairy development program.", "Easy", "Remembering"),
    ("How did Operation Flood benefit rural dairy farmers?", "It enabled small farmers to sell milk directly to cooperatives at fair prices, raising their daily incomes and improving their standard of living.", "Easy", "Understanding"),
    ("How did Operation Flood benefit urban milk consumers?", "It established cold-chain distribution networks that supplied clean, pasteurized, affordable milk to city consumers daily.", "Easy", "Understanding"),
    ("Name two major national and international awards received by Dr. Verghese Kurien.", "He received the prestigious Padma Vibhushan award in India and the international World Food Prize.", "Easy", "Remembering"),
    ("When did Dr. Verghese Kurien pass away?", "He passed away on September 9, 2012, at the age of 90.", "Easy", "Remembering"),
    ("What does the word 'revolution' mean in the context of Chapter 06?", "'Revolution' means a major, fundamental change that brings widespread improvement to society.", "Easy", "Understanding"),
    ("What does the word 'dairy' mean?", "'Dairy' refers to a farm, building, or enterprise where milk is processed, refined, and sold.", "Easy", "Understanding"),
    ("What are 'middlemen' in agriculture?", "'Middlemen' are market intermediaries who buy raw goods cheaply from farmers and sell them at higher prices to consumers for profit.", "Easy", "Understanding"),
    ("What does 'self-sufficient' mean regarding India's milk supply?", "It means India produces enough milk to meet all domestic needs without needing to import milk from foreign countries.", "Easy", "Understanding"),
    ("How did modern technology improve milk processing at Amul?", "It allowed surplus fresh milk to be processed into butter, cheese, and milk powder, preventing spoilage and ensuring year-round supply.", "Easy", "Understanding"),
    ("Why is the Amul cooperative model owned by farmers?", "To ensure that all business profits return directly to the milk-producing farmers rather than private corporate owners.", "Easy", "Understanding"),
    ("What role did Dr. Kurien play in establishing the National Dairy Development Board (NDDB)?", "He established NDDB in Anand to replicate the successful Amul cooperative model in every state across India.", "Easy", "Remembering"),
    ("What technical world-first breakthrough did Dr. Kurien's team achieve with buffalo milk?", "They successfully manufactured milk powder and condensed milk from buffalo milk for the first time in world history.", "Easy", "Remembering"),
    ("Why is National Milk Day celebrated on November 26 in India?", "National Milk Day is celebrated on November 26 to honor the birth anniversary of Dr. Verghese Kurien.", "Easy", "Remembering"),
    ("What title is given to Chapter 06?", "The title of Chapter 06 is 'The Milkman of India: Dr. Verghese Kurien'.", "Easy", "Remembering"),
    ("What enduring legacy did Dr. Kurien leave for Indian agriculture?", "He left a nationwide self-reliant dairy cooperative network that continues to empower millions of small farmers daily.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Analyze why Dr. Kurien chose to stay in Anand instead of taking a high-paying city job.", "Dr. Kurien saw the poverty of Gujarat's farmers and realized his engineering skills could transform their lives. He chose social purpose over personal wealth.", "Medium", "Analyzing"),
    ("Explain how the Amul cooperative model operates at the village level.", "Village farmers bring milk twice daily to local collection centers, where fat content is tested immediately, and fair cash payments are made directly to farmers.", "Medium", "Analyzing"),
    ("Why was eliminating middlemen critical for empowering dairy farmers?", "Middlemen cheated farmers on milk volume and fat pricing. Eliminating them ensured 100% of consumer market value returned to the actual milk producers.", "Medium", "Evaluating"),
    ("How did Operation Flood transform India's international economic standing in dairy?", "Before Operation Flood, India imported milk powder from Western nations. After Operation Flood, India became the world's largest milk producer and self-sufficient.", "Medium", "Comparing"),
    ("Discuss the significance of Tribhuvandas Patel's leadership in Anand.", "Tribhuvandas Patel possessed deep trust among village farmers and organized early cooperatives. He recognized Kurien's technical talent and invited him to manage Amul.", "Medium", "Analyzing"),
    ("How did Amul empower rural Indian women in village economies?", "Since women perform most cattle feeding and milking, receiving direct daily cash payouts from Amul gave rural women personal financial autonomy and family decision-making power.", "Medium", "Evaluating"),
    ("What makes Amul's tagline 'The Taste of India' culturally significant?", "It connected everyday dairy consumption with national pride, reminding citizens that buying Amul directly supported millions of Indian smallholder farmers.", "Medium", "Analyzing"),
    ("Explain the difference between the Green Revolution and the White Revolution.", "Green Revolution focused on grain crop yields (wheat/rice) through high-yield seeds; White Revolution focused on milk production through farmer cooperatives and logistics.", "Medium", "Comparing"),
    ("Why did Western scientists believe buffalo milk could not be converted to powder?", "Buffalo milk has a different fat-to-protein ratio and fat globule size than cow milk, making standard Western spray-drying methods fail until Kurien's team adapted the technique.", "Medium", "Understanding"),
    ("Summarize Chapter 06 in four concise sentences.", "Dr. Verghese Kurien, born in Kerala in 1921, was a dairy engineer who became known as the 'Milkman of India'. Working alongside Tribhuvandas Patel in Anand, Gujarat, he built the Amul cooperative in 1946 to eliminate middleman exploitation. He led the White Revolution and launched Operation Flood in 1970, turning India into the world's largest milk producer. His work empowered millions of rural dairy farmers and made India self-sufficient.", "Medium", "Understanding"),
    ("How did Dr. Kurien protect farmer cooperatives from political interference?", "He insisted that cooperative decisions be made democratically by farmer boards and executed by professional managers, keeping political bureaucrats at arm's length.", "Medium", "Analyzing"),
    ("Why is milk collection transparency important at village cooperative centers?", "Immediate testing of fat content in front of the farmer guarantees honest pricing, building complete trust between small farmers and the cooperative.", "Medium", "Understanding"),
    ("What leadership qualities made Dr. Kurien an effective social reformer?", "He combined technical engineering brilliance, unyielding ethical integrity, courage against powerful cartels, and deep empathy for poor rural families.", "Medium", "Evaluating"),
    ("How do dairy cooperatives contribute to rural community development?", "Cooperative profits are reinvested in village veterinary care, artificial insemination centers, cattle feed plants, clean water projects, and local schools.", "Medium", "Applying"),
    ("What lesson can Class 5 students learn from Dr. Kurien's life choices?", "Students learn that true success comes from using one's education and talents to serve others and build self-reliant communities.", "Medium", "Applying"),

    # Hard (41-50)
    ("Critique the economic principle of monopsony power as broken by Amul.", "Private traders held monopsony power as sole local buyers, forcing low prices. Amul created a farmer-owned monopsony alternative, returning market surplus to producers.", "Hard", "Evaluating"),
    ("Deconstruct the technical engineering innovations implemented by H. M. Dalaya at Amul.", "H. M. Dalaya, working with Kurien, invented industrial processes to vacuum-evaporate and spray-dry buffalo milk, enabling large-scale commercial dairy manufacturing in India.", "Hard", "Analyzing"),
    ("Evaluate the impact of Operation Flood on national nutritional security.", "By making pasteurized milk affordable and widely available in cities, Operation Flood significantly improved protein and calcium nutrition for millions of Indian children.", "Hard", "Evaluating"),
    ("Compare the business structure of a private dairy corporation with a farmer-owned cooperative.", "Private corporation: Profits go to external shareholders seeking high dividends. Cooperative: Profits go directly to milk-producing member farmers as higher milk prices and bonuses.", "Hard", "Comparing"),
    ("Formulate a tribute speech for Dr. Verghese Kurien on his birth centenary.", "'We honor Dr. Verghese Kurien, who proved that Indian farmers can lead world-class industries. His White Revolution gave India self-reliance and millions of rural homes dignity!'", "Hard", "Creating"),
    ("Assess the role of NDDB in scaling the Anand pattern across 200+ milk unions in India.", "NDDB provided technical assistance, financial capital, and managerial training to replicate Anand's 3-tier cooperative structure (village-district-state) nationwide.", "Hard", "Evaluating"),
    ("Analyze how Amul's topical advertising campaign engaged urban Indian consumers.", "The Amul Girl cartoon commentary on current events created a witty, humorous connection that kept the brand relevant and beloved across generations.", "Hard", "Analyzing"),
    ("Synthesize how Chapter 06 connects science, business management, and social justice.", "It shows how dairy engineering science and modern management tools were unified to achieve social justice and economic independence for rural farmers.", "Hard", "Synthesizing"),
    ("Critique the claim: 'India's milk success was due to foreign technology imports.'", "False; while basic equipment was imported, the core breakthrough (buffalo milk processing) and cooperative logistics were indigenously developed by Indian pioneers.", "Hard", "Evaluating"),
    ("Formulate a 4-line poem honoring Dr. Verghese Kurien.", "'In Anand's fields a movement grew,\nTo give the honest farmer his due;\nWith milk and courage Kurien led,\nAnd by his vision India was fed!'", "Hard", "Creating")
]

sa_content = f"# Short Answer Questions — Chapter 06: The Milkman of India: Dr. Verghese Kurien\n\n> **Category**: Short Answer | **Total**: 50 Questions | **Marks**: 2 each\n\n---\n\n"
for idx, item in enumerate(sa_data, start=1):
    q_id = f"BK05_CH06_SA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    sa_content += f"### Question {idx}\n"
    sa_content += f"- **Question ID**: {q_id}\n"
    sa_content += f"- **Type**: Short Answer\n"
    sa_content += f"- **Difficulty**: {diff}\n"
    sa_content += f"- **Bloom Level**: {bloom}\n"
    sa_content += f"- **Marks**: 2\n\n"
    sa_content += f"**Question**: {q_txt}\n\n"
    sa_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH06_DIR, "short_answer.md"), "w", encoding="utf-8") as f:
    f.write(sa_content)

# -------------------------------------------------------------
# 5. Long Answer (50 Distinct Qs)
# -------------------------------------------------------------
la_data = [
    # Easy (1-25)
    ("Describe the early life, education, and arrival of Dr. Verghese Kurien in Anand, Gujarat.",
     "Dr. Verghese Kurien, who became universally known as the 'Milkman of India', was born on November 26, 1921, in Kerala. He pursued his higher education in mechanical engineering in India and subsequently traveled to the United States on a government scholarship to study dairy engineering. Upon returning to India, he was assigned by the government to work at a government creamery in Anand, a small town in Gujarat. Although Kurien initially planned to complete his bond period and leave for a city career, his encounters with local farmers changed his life path. In Anand, he met Tribhuvandas Patel, a selfless local leader who was organizing dairy farmers to sell milk directly without exploitative middlemen. Inspired by Patel's mission, Dr. Kurien decided to stay in Anand and dedicate his technical skills to building a cooperative dairy movement.",
     "Easy", "Remembering"),

    ("Explain the formation of the Amul dairy cooperative and how Dr. Kurien transformed it into a famous national brand.",
     "In 1946, the dairy farmers of Anand registered the Kaira District Co-operative Milk Producers' Union, which became famously known as Amul (Anand Milk Union Limited). Before Amul, private milk contractors paid farmers unfairly low prices and refused milk during flush seasons. Dr. Kurien introduced modern dairy engineering technology and professional management practices to Amul. Under his guidance, Amul established village collection centers with transparent fat testing, built modern processing plants, and successfully manufactured milk, butter, cheese, ghee, and ice cream. By providing high quality at affordable prices, Amul became a household name across India, proving that a farmer-owned cooperative could compete with multinational corporations.",
     "Easy", "Remembering"),

    ("Describe the White Revolution and Operation Flood, explaining how they made India self-sufficient in milk.",
     "The White Revolution was a monumental movement that transformed India from a milk-deficient nation into the world's largest milk producer. In 1970, Dr. Kurien launched 'Operation Flood', the world's largest integrated dairy development program. Operation Flood built a national milk grid connecting millions of small rural dairy farmers across India directly with urban consumer markets. The program established cold-chain storage, refrigerated transport, and village cooperative societies. By ensuring fair daily payments for farmers and a hygienic, affordable milk supply for city consumers, Operation Flood made India completely self-sufficient in milk, empowering millions of rural families.",
     "Easy", "Understanding"),

    ("Discuss the major awards, recognition, and lasting legacy of Dr. Verghese Kurien.",
     "Dr. Verghese Kurien's extraordinary contributions to India's rural economy earned him prestigious national and international honors. The Government of India conferred upon him major civilian awards, including the Padma Shri, Padma Bhushan, and Padma Vibhushan. Internationally, he was awarded the World Food Prize and the Ramon Magsaysay Award for his leadership in food security and social empowerment. Dr. Kurien passed away on September 9, 2012, at age 90. His enduring legacy lives on in the Amul brand, the National Dairy Development Board (NDDB), and the lives of over 15 million dairy farmers whose livelihoods were transformed by his cooperative vision.",
     "Easy", "Understanding"),

    ("Explain the vocabulary terms from Chapter 06: Revolution, Dairy, Cooperative, and Middlemen.",
     "1. **Revolution**: A major, fundamental change that brings widespread social or economic improvement. *Sentence*: The White Revolution transformed India's dairy industry.\n2. **Dairy**: A facility, farm, or enterprise where milk is collected, processed, and sold. *Sentence*: The Amul dairy processes thousands of liters of milk daily.\n3. **Cooperative**: An enterprise owned and operated democratically by its working members who share its profits. *Sentence*: The dairy cooperative helped small farmers earn fair prices.\n4. **Middlemen**: Market intermediaries who buy raw goods cheaply from producers and sell at higher prices for profit. *Sentence*: Eliminating middlemen allowed farmers to receive direct payments for their milk.",
     "Easy", "Understanding"),

    ("Explain how Dr. Kurien eliminated the exploitation of small dairy farmers by middlemen.",
     "Before Dr. Kurien's work, private milk contractors (middlemen) held a monopoly in Anand. They manipulated milk measurement, paid low prices, and refused to buy milk during winter flush seasons when supply was high. Dr. Kurien helped establish village-level cooperative collection societies owned by the farmers. Each morning and evening, farmers brought milk to their local center where fat content was tested transparently, and cash was paid immediately based on quality. By processing excess milk into long-life butter and milk powder, Amul guaranteed that every drop of milk produced by farmers was bought at a fair price year-round.",
     "Easy", "Analyzing"),

    ("Describe the technical breakthrough of producing milk powder from buffalo milk achieved by Dr. Kurien's team.",
     "In the 1950s, international dairy experts claimed that it was scientifically impossible to convert buffalo milk into skimmed milk powder and condensed milk because of its high fat content and chemical structure. Dr. Kurien and his brilliant engineering colleague H. M. Dalaya refused to accept this limitation. Through persistent experimentation in Anand, they developed a world-first spray-drying process that successfully converted buffalo milk into high-quality milk powder and condensed milk. This technical breakthrough was crucial for India, where buffaloes produced the vast majority of milk, allowing Amul to process surplus milk and eliminate dependence on foreign imports.",
     "Easy", "Understanding"),

    ("Discuss how the Amul cooperative model empowered rural women in Indian villages.",
     "In traditional Indian villages, women perform the majority of livestock care, including feeding, washing, and milking cattle. Under the Amul cooperative model, women brought the milk to village collection centers twice daily and received direct cash payouts. This provided rural women with their own independent, daily source of income. Financial independence elevated women's social status, enabled them to contribute to household decisions, fund children's education, and hold leadership positions on village cooperative boards.",
     "Easy", "Evaluating"),

    ("Summarize Chapter 06 in five detailed bullet points.",
     "- Dr. Verghese Kurien (born Nov 26, 1921 in Kerala) studied mechanical and dairy engineering before being posted to Anand, Gujarat.\n- In Anand, he partnered with Tribhuvandas Patel to create the Amul dairy cooperative in 1946, eliminating middleman exploitation.\n- Kurien introduced modern processing technology, proving that buffalo milk could be converted into high-quality milk powder and butter.\n- He led the White Revolution and launched Operation Flood in 1970, building a national milk grid that made India the world's #1 milk producer.\n- Recipient of the Padma Vibhushan and World Food Prize, his legacy empowers over 15 million small dairy farmers across India today.",
     "Easy", "Understanding"),

    ("How did Dr. Kurien's vision align with national self-reliance (Atmanirbhar Bharat)?",
     "Dr. Kurien's vision exemplified national self-reliance long before the term became popular. At a time when India relied on foreign aid and imported milk powder from Western nations, Kurien built an indigenous, farmer-owned dairy industry using Indian engineering talent. By proving that Indian farmers and scientists could build world-class brands without foreign control, he established total national self-sufficiency in milk, securing India's food sovereignty.",
     "Easy", "Evaluating"),

    # (Qs 11 to 25 covering comprehensive easy/medium long answers)
    ("Why was Tribhuvandas Patel's contribution essential to Dr. Kurien's success in Anand?", "Tribhuvandas Patel was a trusted Gandhian freedom fighter who possessed deep moral authority and connection with village farmers. While Kurien brought engineering expertise, Patel mobilized the farmers, built democratic trust, and created the social foundation upon which Amul was built.", "Easy", "Understanding"),
    ("Explain the structure of the National Dairy Development Board (NDDB) created by Dr. Kurien.", "Dr. Kurien established NDDB in 1965 at the request of Prime Minister Lal Bahadur Shastri. NDDB used a three-tier model: Village Dairy Cooperatives (collection) → District Milk Unions (processing) → State Milk Federations (marketing), replicating Anand's success nationwide.", "Easy", "Understanding"),
    ("How did Operation Flood help stabilize milk prices for city consumers?", "Operation Flood established long-distance refrigerated transport networks that carried surplus milk from rural cooperatives to metropolitan cities. This eliminated urban milk shortages, stabilized retail prices, and guaranteed clean, pasteurized milk daily.", "Easy", "Understanding"),
    ("Describe the iconic 'Amul Girl' advertising campaign and its impact on Indian culture.", "Launched in 1966 by Sylvester da Cunha, the hand-drawn Amul Girl outdoor billboards used witty, topical humor to comment on national events. The campaign built immense brand warmth, making Amul 'The Taste of India' and a cherished cultural icon.", "Easy", "Analyzing"),
    ("How did dairy farming provide economic stability during crop failures?", "Agriculture in India is subject to monsoon failures and crop damage. Dairy farming provided farmers with an essential secondary income stream because cattle produce milk daily, generating cash flow regardless of weather impact on grain crops.", "Easy", "Analyzing"),
    ("Explain why Dr. Kurien insisted that farmers should own the processing plants and brand.", "Kurien believed that if farmers only sold raw milk, private processors would capture the major profits from butter and cheese. By owning the processing plants and brand, farmers captured the complete value chain from cow to consumer.", "Easy", "Evaluating"),
    ("What challenges did Dr. Kurien face from private milk cartels when starting Amul?", "Private milk cartels used political pressure, price manipulation, and media campaigns to discredit Amul. Kurien overcame them through unyielding courage, high product quality, transparent farmer payouts, and strategic legal defense.", "Easy", "Analyzing"),
    ("Describe the educational background that prepared Dr. Kurien for his life's work.", "He earned a Bachelor's in Mechanical Engineering from Guindy Engineering College, Chennai, underwent training at Tata Iron and Steel, and completed his Master's in Dairy Engineering at Michigan State University, US, equipping him with world-class technical skills.", "Easy", "Remembering"),
    ("How does Chapter 06 teach Class 5 students the importance of social responsibility?", "Chapter 06 shows that true career greatness comes from using specialized skills to help others. Kurien used his foreign engineering degree not for personal wealth, but to uplift millions of impoverished Indian farmers.", "Easy", "Evaluating"),
    ("Discuss how the Amul model contributed to rural infrastructure development.", "Amul reinvested cooperative profits into village infrastructure, building paved roads, installing clean drinking water plants, establishing veterinary hospitals, and funding local schools across rural Gujarat.", "Easy", "Understanding"),
    ("Re-write the story of Amul from the perspective of a small Gujarati milk farmer in 1950.", "'Before Dr. Kurien came, the middleman took our milk for pennies and turned us away in winter. Then we joined hands in Amul. Now every morning I bring my milk to the village center, get tested fairly, and receive daily cash to feed my children.'", "Easy", "Creating"),
    ("What role did Prime Minister Lal Bahadur Shastri play in expanding the Amul model?", "In 1964, PM Lal Bahadur Shastri stayed overnight in a village in Anand to observe Amul. Impressed by the farmers' prosperity, he asked Dr. Kurien to create NDDB and replicate the model across all of India.", "Easy", "Remembering"),
    ("How did Operation Flood contribute to women's empowerment in rural India?", "By placing milk payments directly into female hands and encouraging women to vote on cooperative boards, Operation Flood gave millions of village women financial independence and leadership experience.", "Easy", "Evaluating"),
    ("Analyze why Dr. Kurien is considered one of the greatest nation-builders of modern India.", "He built institutions that achieved national food self-sufficiency, empowered over 15 million smallholders, created India's largest food brand, and established a sustainable democratic model for economic growth.", "Easy", "Evaluating"),
    ("What future challenges face India's dairy sector in the 21st century?", "Challenges include climate change impacts on cattle health, fodder scarcity, modernizing cold-chain logistics, maintaining quality standards against adulteration, and competing in global export markets.", "Easy", "Understanding"),

    # Medium (26-40)
    ("Critically analyze how the Amul cooperative model balances commercial efficiency with social justice.",
     "The Amul model successfully bridges commercial efficiency and social justice:\n1. **Commercial Efficiency**: It utilizes modern processing technology, professional management, state-of-the-art cold chains, and competitive marketing to maintain top product quality.\n2. **Social Justice**: It operates on democratic cooperative principles where 100% of member-farmers own the business. Over 80% of consumer price returns directly to farmers, eliminating corporate wealth concentration and lifting rural families out of poverty.",
     "Medium", "Analyzing"),

    ("Examine the three-tier structure of the Anand Pattern of cooperative dairy development.",
     "The Anand Pattern uses a three-tier federated structure:\n1. **Village Dairy Cooperative Societies (Primary Tier)**: Collect milk twice daily from local farmers, conduct fat testing, and make direct cash payouts.\n2. **District Cooperative Milk Producers' Union (Secondary Tier)**: Owns and operates central processing plants, converting milk into dairy products and managing district transport.\n3. **State Cooperative Milk Marketing Federation (Tertiary Tier)**: Handles statewide and national marketing, branding (Amul), and distribution channels.",
     "Medium", "Analyzing"),

    ("Evaluate the impact of Dr. Kurien's leadership philosophy: 'Development is the development of people.'",
     "Dr. Kurien maintained that economic development should not be measured merely by machinery or output statistics, but by human empowerment. By focusing on developing the confidence, technical knowledge, and democratic capability of poor farmers, Kurien created an enduring social movement where technology served human dignity.",
     "Medium", "Evaluating"),

    ("Discuss how Operation Flood transformed India's global agricultural reputation.",
     "Before Operation Flood, foreign nations viewed India as a permanent agricultural beggar dependent on food aid. By executing the world's largest dairy development project without foreign management, India proved it could build world-class agricultural supply chains, transforming from a milk importer into the world's #1 milk producer.",
     "Medium", "Analyzing"),

    ("Design an interactive primary school exhibition plan celebrating 'The Milkman of India'.",
     "Exhibition Title: 'White Revolution — The Story of Milk and Hope'\n- **Station 1 (Biography)**: Interactive timeline of Dr. Kurien's life from Kerala to Anand.\n- **Station 2 (Science of Dairy)**: Demonstration of milk testing, pasteurization, and butter-making.\n- **Station 3 (Economics)**: Comparative chart showing 'With Middlemen' vs 'With Amul Cooperative'.\n- **Station 4 (Creative)**: Student cartoon workshop inspired by the Amul Girl campaign.",
     "Medium", "Creating"),

    ("How did H. M. Dalaya's technical partnership with Dr. Kurien enable Amul's industrial scale?", "Dalaya was a brilliant dairy technologist who solved the spray-drying physics of buffalo milk. His technical innovations allowed Kurien to scale Amul from a small liquid milk supplier into an industrial dairy powerhouse.", "Medium", "Analyzing"),
    ("Contrast the corporate governance of Amul with multinational food corporations.", "Multinational corporations are governed by investor boards seeking profit maximization for external shareholders. Amul is governed by elected farmer boards seeking maximum payout prices for milk-producing members.", "Medium", "Comparing"),
    ("Why was the establishment of IRMA (Institute of Rural Management Anand) important to Kurien's vision?", "Kurien realized that rural cooperatives needed young, professionally trained managers who understood both business and rural empathy. He founded IRMA in 1979 to train professional rural managers.", "Medium", "Understanding"),
    ("How did Operation Flood help mitigate rural-to-urban distress migration?", "By providing stable daily cash income in villages through dairy farming, Operation Flood allowed small farmers to earn a sustainable living in their hometowns, reducing forced migration to city slums.", "Medium", "Evaluating"),
    ("Describe how the 'Amul Butter' product became a household essential in urban India.", "Amul provided consistent, high-quality, hygienic yellow butter made from fresh cream at affordable prices, supported by witty advertising that built deep consumer trust across Indian homes.", "Medium", "Analyzing"),
    ("Explain the concept of 'flush season' in dairy farming and how Amul solved it.", "In winter ('flush season'), cows produce double the milk. Private traders used to drop prices or reject milk. Amul built processing plants to convert flush milk into powder and butter, guaranteeing purchase year-round.", "Medium", "Understanding"),
    ("How did Dr. Kurien's work support smallland and landless agricultural laborers?", "Dairy farming requires minimal land compared to crop farming. Landless laborers could keep one or two cows/buffaloes and earn daily income through Amul, creating an inclusive economic ladder.", "Medium", "Evaluating"),
    ("Analyze how Dr. Kurien handled opposition from established private milk monopolies.", "He used transparent pricing, high product quality, and public advocacy to prove the cooperative's superiority, rallying public and government support to defeat private cartels.", "Medium", "Analyzing"),
    ("What makes Chapter 06 an exemplar of inspirational biographical literature for Class 5?", "It combines compelling personal biography with historical achievement, economic concepts, and moral values, inspiring students to pursue careers dedicated to nation-building.", "Medium", "Evaluating"),
    ("Construct a fictional letter from a Gujarati farmer to Dr. Kurien thanking him for Operation Flood.", "'Respected Dr. Kurien, before Amul came, the middleman cheated us. Today, because of your work, my daily milk money paid for my daughter's schooling and our family's health. You gave us dignity.'", "Medium", "Creating"),

    # Hard (41-50)
    ("Critique the political economy of dairy development in post-independence India.",
     "Post-independence India faced food deficits and bureaucratic central planning. Dr. Kurien pioneered an alternative 'cooperative federalism' model. By placing economic assets directly in farmer hands and demanding professional management over political patronage, he created an autonomous economic model that resisted state control while driving national growth.",
     "Hard", "Evaluating"),

    ("Deconstruct the supply chain logistics of Operation Flood's 'National Milk Grid'.",
     "The National Milk Grid linked 700+ towns and cities with 150,000+ village cooperatives via:\n1. **First Mile**: Twice-daily insulated cans/chillers at village centers.\n2. **Processing**: District dairies pasteurizing and packaging milk.\n3. **Long Haul**: Insulated rail and road tankers moving bulk milk across thousands of miles.\n4. **Last Mile**: Urban retail booths ensuring fresh daily distribution.",
     "Hard", "Analyzing"),

    ("Synthesize how Dr. Kurien's work addresses the UN Sustainable Development Goals (SDGs).",
     "Kurien's work directly advances multiple UN SDGs:\n- **SDG 1 (No Poverty)**: Daily cash income for 15M+ smallholders.\n- **SDG 2 (Zero Hunger)**: Affordable protein and national milk security.\n- **SDG 5 (Gender Equality)**: Financial empowerment for rural female cattle keepers.\n- **SDG 8 (Decent Work)**: Democratic cooperative employment.",
     "Hard", "Synthesizing"),

    ("Formulate a debate prompt for advanced students on agricultural development strategies.",
     "Debate: 'Is farmer-owned cooperative enterprise superior to corporate contract farming for developing nations? Analyze using Amul as a case study.'",
     "Hard", "Creating"),

    ("Evaluate the resilience of the Amul cooperative model during modern economic crises.", "During market shocks and pandemics, Amul's farmer-owned structure ensured continuous milk procurement and daily payouts, demonstrating that cooperative models prioritize member survival over short-term profit cutting.", "Hard", "Evaluating"),

    ("Compare Dr. Verghese Kurien's leadership style with industrial business leaders.", "Industrial leaders focus on shareholder return and corporate market share. Kurien focused on social capital, democratic farmer ownership, and institutional nation-building.", "Hard", "Comparing"),
    ("Discuss the global impact of Operation Flood as a blueprint for developing nations.", "Operation Flood inspired dairy and agricultural cooperative development across Asia, Africa, and Latin America, showing that developing nations can achieve food security independently.", "Hard", "Evaluating"),
    ("Analyze how Dr. Kurien utilized public communications and media to protect the cooperative.", "He used media transparency, memorable advertising, and direct public communication to expose middleman corruption and gain national consumer support for farmer causes.", "Hard", "Analyzing"),
    ("Draft an analytical commentary on the line: 'Thanks to Dr. Verghese Kurien, India became self-sufficient in milk production and farmers found a better life.'", "This sentence encapsulates Kurien's dual victory: macroeconomic success (national self-sufficiency) combined with microeconomic justice (improving individual farmers' lives), establishing him as a true nation-builder.", "Hard", "Evaluating"),
    ("Synthesize the complete educational takeaways of Chapter 06 for Class 5 literature and ethics.", "Chapter 06 demonstrates that professional education, integrity, innovation, and empathy can transform a nation. It teaches students that true greatness lies in empowering others and building self-reliant communities.", "Hard", "Synthesizing")
]

la_content = f"# Long Answer Questions — Chapter 06: The Milkman of India: Dr. Verghese Kurien\n\n> **Category**: Long Answer | **Total**: 50 Questions | **Marks**: 5 each\n\n---\n\n"
for idx, item in enumerate(la_data, start=1):
    q_id = f"BK05_CH06_LA_{idx:03d}"
    q_txt, ans, diff, bloom = item
    la_content += f"### Question {idx}\n"
    la_content += f"- **Question ID**: {q_id}\n"
    la_content += f"- **Type**: Long Answer\n"
    la_content += f"- **Difficulty**: {diff}\n"
    la_content += f"- **Bloom Level**: {bloom}\n"
    la_content += f"- **Marks**: 5\n\n"
    la_content += f"**Question**: {q_txt}\n\n"
    la_content += f"- **Answer Key**: {ans}\n\n---\n\n"

with open(os.path.join(CH06_DIR, "long_answer.md"), "w", encoding="utf-8") as f:
    f.write(la_content)

# -------------------------------------------------------------
# 6. Extract Based (50 Distinct Qs across 10 Extract Sets)
# -------------------------------------------------------------
extract_data = [
    # Set 1
    ("Dr. Verghese Kurien, known as the Milkman of India, played a big role in making India the largest milk producer in the world. He was born on November 26, 1921 in Kerala and studied mechanical engineering.",
     [
         ("Who is known as the Milkman of India?", "Dr. Verghese Kurien.", "Easy", "Remembering"),
         ("When and where was Dr. Kurien born?", "Born on November 26, 1921 in Kerala.", "Easy", "Remembering"),
         ("What engineering subject did Dr. Kurien study initially?", "Mechanical engineering.", "Easy", "Remembering"),
         ("What major achievement did India attain through Dr. Kurien's leadership?", "India became the largest milk producer in the world.", "Medium", "Understanding"),
         ("What does the word 'producer' mean in this context?", "A country or entity that yields or manufactures goods.", "Easy", "Understanding")
     ]),

    # Set 2
    ("Later, he went to the United States to study dairy engineering. When Dr. Kurien returned to India, he was sent to work in Anand, a small town in Gujarat.",
     [
         ("Where did Dr. Kurien go for higher studies in dairy engineering?", "The United States.", "Easy", "Remembering"),
         ("What field of engineering did he study in the United States?", "Dairy engineering.", "Easy", "Remembering"),
         ("To which town was Dr. Kurien sent to work upon returning to India?", "Anand, a small town in Gujarat.", "Easy", "Remembering"),
         ("In which state is the town of Anand located?", "Gujarat.", "Easy", "Remembering"),
         ("Why was Dr. Kurien's posting to Anand historically significant?", "Because it led to his partnership with farmers and the creation of Amul.", "Medium", "Analyzing")
     ]),

    # Set 3
    ("There, he met Tribhuvandas Patel, who was helping farmers sell their milk without middlemen. Inspired by this, Dr. Kurien decided to use his skills to improve milk production and support farmers.",
     [
         ("Who did Dr. Kurien meet in Anand?", "Tribhuvandas Patel.", "Easy", "Remembering"),
         ("What was Tribhuvandas Patel doing for local farmers?", "He was helping farmers sell their milk without middlemen.", "Easy", "Remembering"),
         ("How did Tribhuvandas Patel's work affect Dr. Kurien?", "Dr. Kurien was inspired to use his skills to improve milk production and support farmers.", "Easy", "Understanding"),
         ("Why was selling milk without middlemen beneficial to farmers?", "It eliminated exploitation and allowed farmers to receive full, fair payments.", "Medium", "Understanding"),
         ("What key leadership quality did Dr. Kurien display here?", "Empathy and dedication to social welfare using professional skills.", "Medium", "Evaluating")
     ]),

    # Set 4
    ("In 1946, the Amul dairy cooperative was formed. Dr. Kurien introduced modern technology and better management, making Amul a popular brand for milk, butter, cheese and ice cream.",
     [
         ("In which year was the Amul dairy cooperative formed?", "1946.", "Easy", "Remembering"),
         ("What two improvements did Dr. Kurien introduce to Amul?", "Modern technology and better management.", "Easy", "Remembering"),
         ("Name four popular dairy products manufactured by Amul.", "Milk, butter, cheese, and ice cream.", "Easy", "Remembering"),
         ("What is a 'cooperative'?", "A business owned and run jointly by its members who share the profits.", "Medium", "Understanding"),
         ("Why was modern technology necessary for Amul's expansion?", "To process surplus milk into long-life products and distribute them across India.", "Medium", "Analyzing")
     ]),

    # Set 5
    ("His efforts led to the White Revolution, a movement that increased milk production across India. In 1970, he launched Operation Flood, helping farmers earn more money and providing affordable milk to everyone.",
     [
         ("What major movement was sparked by Dr. Kurien's efforts?", "The White Revolution.", "Easy", "Remembering"),
         ("What major project did Dr. Kurien launch in 1970?", "Operation Flood.", "Easy", "Remembering"),
         ("What was the main goal of the White Revolution?", "To increase milk production across India.", "Easy", "Remembering"),
         ("How did Operation Flood benefit farmers?", "It helped farmers earn more money for their milk.", "Easy", "Understanding"),
         ("How did Operation Flood benefit consumers?", "It provided clean, affordable milk to everyone in cities.", "Medium", "Understanding")
     ]),

    # Set 6
    ("Dr. Kurien received many awards, including the Padma Vibhushan and the World Food Prize. He passed away on September 9, 2012, but his work continues to benefit millions.",
     [
         ("Name two prestigious awards received by Dr. Kurien.", "Padma Vibhushan and World Food Prize.", "Easy", "Remembering"),
         ("On what date did Dr. Kurien pass away?", "September 9, 2012.", "Easy", "Remembering"),
         ("Who continues to benefit from Dr. Kurien's work today?", "Millions of Indian farmers and citizens.", "Easy", "Remembering"),
         ("What does receiving the World Food Prize signify?", "Global recognition for major contributions to international food security.", "Medium", "Evaluating"),
         ("Why is Dr. Kurien's work described as an ongoing benefit?", "Because the Amul cooperative network continues operating successfully today.", "Medium", "Analyzing")
     ]),

    # Set 7
    ("Thanks to Dr. Verghese Kurien, India became self-sufficient in milk production and farmers found a better life. He truly earned the title 'Milkman of India.'",
     [
         ("What national economic status did India achieve thanks to Dr. Kurien?", "India became self-sufficient in milk production.", "Easy", "Remembering"),
         ("How did life change for Indian dairy farmers?", "Farmers found a better life with higher incomes and security.", "Easy", "Remembering"),
         ("What title did Dr. Kurien earn?", "'Milkman of India.'", "Easy", "Remembering"),
         ("What does 'self-sufficient' mean?", "Producing enough to meet all domestic needs without foreign imports.", "Easy", "Understanding"),
         ("Why was achieving self-sufficiency in milk vital for India?", "It secured national nutrition and saved valuable foreign exchange.", "Medium", "Evaluating")
     ]),

    # Set 8
    ("Word Meaning: Revolution — A big change that brings improvement. Dairy — A place where milk is processed and sold.",
     [
         ("What is the definition of 'revolution'?", "A big change that brings improvement.", "Easy", "Remembering"),
         ("What is the definition of 'dairy'?", "A place where milk is processed and sold.", "Easy", "Remembering"),
         ("What color is associated with the dairy revolution in India?", "White (White Revolution).", "Easy", "Remembering"),
         ("Use the word 'revolution' in an original sentence.", "The digital revolution changed how students learn in classrooms.", "Medium", "Applying"),
         ("Why was the term 'White Revolution' chosen?", "To represent the dramatic growth in milk production across the nation.", "Medium", "Understanding")
     ]),

    # Set 9
    ("He was born on November 26, 1921... In 1946, the Amul dairy cooperative was formed... In 1970, he launched Operation Flood... He passed away on September 9, 2012.",
     [
         ("What event happened on November 26, 1921?", "Dr. Verghese Kurien was born.", "Easy", "Remembering"),
         ("What event happened in 1946?", "The Amul dairy cooperative was formed.", "Easy", "Remembering"),
         ("What event happened in 1970?", "Operation Flood was launched.", "Easy", "Remembering"),
         ("What event happened on September 9, 2012?", "Dr. Verghese Kurien passed away.", "Easy", "Remembering"),
         ("How many years elapsed between the founding of Amul (1946) and Operation Flood (1970)?", "24 years elapsed.", "Medium", "Understanding")
     ]),

    # Set 10
    ("Dr. Kurien introduced modern technology and better management... Operation Flood... helping farmers earn more money and providing affordable milk to everyone.",
     [
         ("What two factors did Dr. Kurien introduce to modernize Amul?", "Modern technology and better management.", "Easy", "Remembering"),
         ("What program was launched in 1970?", "Operation Flood.", "Easy", "Remembering"),
         ("Whose income was increased by Operation Flood?", "Rural dairy farmers' income.", "Easy", "Remembering"),
         ("Why was providing affordable milk to city consumers important?", "It ensured proper protein nutrition for growing urban children.", "Medium", "Evaluating"),
         ("Summarize Dr. Kurien's social mission in one sentence.", "He used engineering, technology, and management to empower small farmers and achieve national milk self-sufficiency.", "Medium", "Evaluating")
     ])
]

ext_content = f"# Extract Based Questions — Chapter 06: The Milkman of India: Dr. Verghese Kurien\n\n> **Category**: Extract Based | **Total**: 10 Extract Sets (50 Questions) | **Marks**: 1 per sub-question\n\n---\n\n"

q_counter = 1
for set_idx, (extract_text, sub_qs) in enumerate(extract_data, start=1):
    ext_content += f"## Extract Set {set_idx}\n\n"
    ext_content += f"> *\"{extract_text}\"*\n\n"
    ext_content += f"---"
    
    for sub_q, sub_a, diff, bloom in sub_qs:
        q_id = f"BK05_CH06_EXT_{q_counter:03d}"
        ext_content += f"\n\n### Question {q_counter}\n"
        ext_content += f"- **Question ID**: {q_id}\n"
        ext_content += f"- **Type**: Extract Based\n"
        ext_content += f"- **Difficulty**: {diff}\n"
        ext_content += f"- **Bloom Level**: {bloom}\n"
        ext_content += f"- **Marks**: 1\n\n"
        ext_content += f"**Question**: {sub_q}\n\n"
        ext_content += f"- **Answer Key**: {sub_a}\n"
        q_counter += 1
    ext_content += "\n\n---\n\n"

with open(os.path.join(CH06_DIR, "extract_based.md"), "w", encoding="utf-8") as f:
    f.write(ext_content)

print(f"SUCCESS: Refined all 6 category files (300 total Qs) for Book 5 Chapter 06 in {CH06_DIR}")
