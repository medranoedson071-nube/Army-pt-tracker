"""
ASVAB Question Bank
-------------------
Covers the five subtests that feed the Army GT and ST composite scores.

  GT  (General Technical)  = VE + AR
  ST  (Skilled Technical)  = MC + AO + VE
  VE  (Verbal Expression)  = WK + PC (combined into VE here)

Subtests included
  WK  – Word Knowledge
  PC  – Paragraph Comprehension
  AR  – Arithmetic Reasoning
  MC  – Mechanical Comprehension
  AO  – Assembling Objects
"""

# ---------------------------------------------------------------------------
# Metadata for each subtest
# ---------------------------------------------------------------------------
SUBTEST_INFO = {
    "WK": {
        "name": "Word Knowledge",
        "composite": ["GT", "ST (via VE)"],
        "description": (
            "Tests your vocabulary. You must choose the word or phrase "
            "closest in meaning to the underlined or given word."
        ),
        "tips": [
            "Learn common prefixes/suffixes (pre-, un-, -tion, -ous …)",
            "Study Latin and Greek roots (bene=good, mal=bad, port=carry …)",
            "Read daily – newspapers, manuals, novels",
            "Use new words in sentences to lock them in memory",
            "Make flash cards for every word you don't know",
        ],
    },
    "PC": {
        "name": "Paragraph Comprehension",
        "composite": ["GT", "ST (via VE)"],
        "description": (
            "Tests your ability to read a short passage and answer "
            "questions about its content, main idea, or implied meaning."
        ),
        "tips": [
            "Read the questions BEFORE reading the passage",
            "Identify the main idea in the first and last sentences",
            "Look for transition words (however, therefore, in contrast …)",
            "Never choose an answer based on outside knowledge – stick to the text",
            "Practice active reading: underline key facts as you read",
        ],
    },
    "AR": {
        "name": "Arithmetic Reasoning",
        "composite": ["GT"],
        "description": (
            "Tests your ability to solve word problems using arithmetic "
            "and basic mathematics."
        ),
        "tips": [
            "Re-read each problem carefully; underline the question",
            "Draw diagrams for distance/rate/time problems",
            "Convert units before calculating",
            "Eliminate obviously wrong answers first",
            "Check your work by back-substituting your answer",
            "Master percentages, ratios, and basic algebra",
        ],
    },
    "MC": {
        "name": "Mechanical Comprehension",
        "composite": ["ST"],
        "description": (
            "Tests your understanding of basic mechanical and physical "
            "principles: levers, gears, pulleys, fluid pressure, electricity."
        ),
        "tips": [
            "Review Newton's three laws of motion",
            "Understand gear ratios: small drives large = slower, more torque",
            "Pulleys: each additional supporting rope reduces required force",
            "Remember Ohm's Law: V = IR",
            "Study simple machines: lever, pulley, inclined plane, wheel & axle",
        ],
    },
    "AO": {
        "name": "Assembling Objects",
        "composite": ["ST"],
        "description": (
            "Tests your ability to visualize how parts fit together "
            "or how a shape would look when its pieces are connected."
        ),
        "tips": [
            "Mentally rotate shapes before committing to an answer",
            "Look for unique anchor points (dots) that must align",
            "Eliminate answers where the scale of parts is wrong",
            "Practice puzzles and 3-D visualization exercises daily",
            "Sketch quick diagrams on scratch paper during the test",
        ],
    },
}

# ---------------------------------------------------------------------------
# Question format
# Each question is a dict:
#   question  – str
#   choices   – list of 4 strings labeled A-D
#   answer    – str, one of "A","B","C","D"
#   explanation – str (shown after answering)
# ---------------------------------------------------------------------------

WK_QUESTIONS = [
    {
        "question": "CANDID most nearly means:",
        "choices": ["A. secretive", "B. honest", "C. cheerful", "D. cautious"],
        "answer": "B",
        "explanation": "Candid means truthful and straightforward.",
    },
    {
        "question": "OBSOLETE most nearly means:",
        "choices": ["A. outdated", "B. essential", "C. obscure", "D. obvious"],
        "answer": "A",
        "explanation": "Obsolete means no longer in use or out of date.",
    },
    {
        "question": "TENACIOUS most nearly means:",
        "choices": ["A. fragile", "B. timid", "C. persistent", "D. temporary"],
        "answer": "C",
        "explanation": "Tenacious means holding firmly; persistent.",
    },
    {
        "question": "BENEVOLENT most nearly means:",
        "choices": ["A. hostile", "B. kind", "C. boastful", "D. bitter"],
        "answer": "B",
        "explanation": "Benevolent means well-meaning and kindly (bene = good).",
    },
    {
        "question": "The soldier was ADEPT at map reading. ADEPT most nearly means:",
        "choices": ["A. careless", "B. slow", "C. highly skilled", "D. newly trained"],
        "answer": "C",
        "explanation": "Adept means very skilled or proficient at something.",
    },
    {
        "question": "AMBIGUOUS most nearly means:",
        "choices": ["A. unclear", "B. certain", "C. generous", "D. hostile"],
        "answer": "A",
        "explanation": "Ambiguous means open to more than one interpretation; unclear.",
    },
    {
        "question": "DILIGENT most nearly means:",
        "choices": ["A. lazy", "B. hard-working", "C. reckless", "D. dishonest"],
        "answer": "B",
        "explanation": "Diligent means showing steady, earnest effort.",
    },
    {
        "question": "INFER most nearly means:",
        "choices": ["A. to ignore", "B. to conclude from evidence", "C. to repeat", "D. to forbid"],
        "answer": "B",
        "explanation": "To infer is to deduce or conclude from evidence and reasoning.",
    },
    {
        "question": "CONCISE most nearly means:",
        "choices": ["A. wordy", "B. confused", "C. brief and clear", "D. vague"],
        "answer": "C",
        "explanation": "Concise means giving much information clearly in few words.",
    },
    {
        "question": "VOLATILE most nearly means:",
        "choices": ["A. stable", "B. loud", "C. liable to change rapidly", "D. slow-moving"],
        "answer": "C",
        "explanation": "Volatile means liable to change rapidly and unpredictably.",
    },
    {
        "question": "PRUDENT most nearly means:",
        "choices": ["A. reckless", "B. showing good judgment", "C. impatient", "D. ignorant"],
        "answer": "B",
        "explanation": "Prudent means acting with or showing care and thought.",
    },
    {
        "question": "MITIGATE most nearly means:",
        "choices": ["A. to worsen", "B. to lessen the severity of", "C. to measure", "D. to isolate"],
        "answer": "B",
        "explanation": "To mitigate means to make less severe, serious, or painful.",
    },
    {
        "question": "COLLABORATE most nearly means:",
        "choices": ["A. to compete", "B. to work jointly", "C. to surrender", "D. to command"],
        "answer": "B",
        "explanation": "To collaborate is to work jointly on an activity or project.",
    },
    {
        "question": "RESILIENT most nearly means:",
        "choices": ["A. brittle", "B. slow", "C. able to recover quickly", "D. vulnerable"],
        "answer": "C",
        "explanation": "Resilient means able to recoil or spring back after difficulty.",
    },
    {
        "question": "METICULOUS most nearly means:",
        "choices": ["A. showing great attention to detail", "B. careless", "C. gigantic", "D. fearful"],
        "answer": "A",
        "explanation": "Meticulous means taking great care; very precise and accurate.",
    },
    {
        "question": "BREVITY most nearly means:",
        "choices": ["A. courage", "B. shortness", "C. wisdom", "D. loudness"],
        "answer": "B",
        "explanation": "Brevity means shortness of time or expression.",
    },
    {
        "question": "IMPEDIMENT most nearly means:",
        "choices": ["A. assistance", "B. obstacle", "C. speed", "D. instruction"],
        "answer": "B",
        "explanation": "An impediment is a hindrance or obstruction.",
    },
    {
        "question": "EQUIVOCAL most nearly means:",
        "choices": ["A. equal", "B. doubtful or ambiguous", "C. straightforward", "D. massive"],
        "answer": "B",
        "explanation": "Equivocal means uncertain or ambiguous; open to multiple interpretations.",
    },
    {
        "question": "FORTIFY most nearly means:",
        "choices": ["A. to weaken", "B. to strengthen", "C. to abandon", "D. to confuse"],
        "answer": "B",
        "explanation": "To fortify means to strengthen a place with defensive works.",
    },
    {
        "question": "SUBORDINATE most nearly means:",
        "choices": ["A. a superior officer", "B. lower in rank", "C. an equal", "D. a civilian"],
        "answer": "B",
        "explanation": "Subordinate means lower in rank or position.",
    },
    {
        "question": "MANDATORY most nearly means:",
        "choices": ["A. optional", "B. suggested", "C. required", "D. forbidden"],
        "answer": "C",
        "explanation": "Mandatory means required by law or rules; compulsory.",
    },
    {
        "question": "VERBOSE most nearly means:",
        "choices": ["A. using more words than needed", "B. silent", "C. concise", "D. angry"],
        "answer": "A",
        "explanation": "Verbose means using or expressed in more words than are needed.",
    },
    {
        "question": "AUGMENT most nearly means:",
        "choices": ["A. to decrease", "B. to replace", "C. to increase", "D. to hide"],
        "answer": "C",
        "explanation": "To augment means to make something greater by adding to it.",
    },
    {
        "question": "DECEPTION most nearly means:",
        "choices": ["A. honesty", "B. the action of deceiving someone", "C. courage", "D. loyalty"],
        "answer": "B",
        "explanation": "Deception is the act of misleading or tricking someone.",
    },
    {
        "question": "PRAGMATIC most nearly means:",
        "choices": ["A. idealistic", "B. dealing with things sensibly and realistically", "C. pessimistic", "D. theoretical"],
        "answer": "B",
        "explanation": "Pragmatic means dealing with things practically rather than theoretically.",
    },
]

PC_QUESTIONS = [
    {
        "question": (
            "PASSAGE: 'The M4 carbine is the standard infantry weapon of the U.S. Army. "
            "It fires a 5.56mm NATO round and has an effective range of about 500 meters. "
            "Soldiers are required to qualify annually.'\n\n"
            "According to the passage, how often must soldiers qualify with the M4?"
        ),
        "choices": ["A. Monthly", "B. Every six months", "C. Annually", "D. Every two years"],
        "answer": "C",
        "explanation": "The passage explicitly states soldiers are required to qualify annually.",
    },
    {
        "question": (
            "PASSAGE: 'Night vision devices allow soldiers to operate effectively in low-light "
            "environments. Thermal optics detect heat signatures, while image-intensification "
            "devices amplify available light. Both types have advantages depending on the mission.'\n\n"
            "The passage implies that the choice of night vision device should depend on:"
        ),
        "choices": [
            "A. the soldier's rank",
            "B. the specific mission requirements",
            "C. the cost of the equipment",
            "D. the weight of the device",
        ],
        "answer": "B",
        "explanation": "The passage states 'both types have advantages depending on the mission.'",
    },
    {
        "question": (
            "PASSAGE: 'Proper hydration is critical during field operations. Dehydration can "
            "degrade cognitive performance by as much as 20 percent before a soldier feels "
            "thirsty. Leaders must enforce hydration discipline, especially in hot environments.'\n\n"
            "What is the main point of this passage?"
        ),
        "choices": [
            "A. Soldiers should drink water only when thirsty",
            "B. Leaders should never work in hot environments",
            "C. Staying hydrated is critical and must be actively enforced",
            "D. Dehydration has no effect on performance",
        ],
        "answer": "C",
        "explanation": "The passage emphasizes that hydration is critical and that leaders must enforce it.",
    },
    {
        "question": (
            "PASSAGE: 'The Army Values — Loyalty, Duty, Respect, Selfless Service, Honor, "
            "Integrity, and Personal Courage — form the foundation of what it means to be "
            "a soldier. These values guide behavior in garrison and in combat alike.'\n\n"
            "According to the passage, when do the Army Values apply?"
        ),
        "choices": [
            "A. Only in combat",
            "B. Only in garrison",
            "C. In garrison and in combat",
            "D. Only during inspections",
        ],
        "answer": "C",
        "explanation": "The passage states the values guide behavior 'in garrison and in combat alike.'",
    },
    {
        "question": (
            "PASSAGE: 'Camouflage is the practice of concealing military personnel and equipment "
            "from enemy observation. Effective camouflage considers shape, shadow, silhouette, "
            "surface, spacing, and movement — the six Ss of camouflage.'\n\n"
            "The passage is primarily about:"
        ),
        "choices": [
            "A. the history of military uniforms",
            "B. how enemy observation works",
            "C. the principles and practice of military camouflage",
            "D. night-time operations",
        ],
        "answer": "C",
        "explanation": "The passage focuses on camouflage — what it is and its key principles.",
    },
    {
        "question": (
            "PASSAGE: 'Sleep deprivation significantly impairs decision-making, reaction time, "
            "and situational awareness. Research shows that after 17 hours without sleep, "
            "performance equals that of someone with a 0.05% blood alcohol level. Military "
            "leaders must manage sleep as a combat resource.'\n\n"
            "The author's purpose in citing the blood alcohol comparison is to:"
        ),
        "choices": [
            "A. promote alcohol awareness",
            "B. illustrate how severely sleep loss impairs performance",
            "C. argue that soldiers should avoid alcohol",
            "D. recommend 17 hours of sleep per day",
        ],
        "answer": "B",
        "explanation": "The comparison is used to illustrate the severity of performance impairment from sleep deprivation.",
    },
    {
        "question": (
            "PASSAGE: 'Land navigation is a fundamental soldier skill. Using a topographic map "
            "and compass, a soldier can determine their exact location and plan a route through "
            "any terrain. GPS devices are useful but should never replace map-reading skills.'\n\n"
            "The passage suggests that GPS devices:"
        ),
        "choices": [
            "A. are more reliable than a map and compass",
            "B. should replace traditional navigation",
            "C. are useful but not a substitute for map-reading skills",
            "D. are unavailable to infantry soldiers",
        ],
        "answer": "C",
        "explanation": "The passage says GPS is useful but should 'never replace map-reading skills.'",
    },
    {
        "question": (
            "PASSAGE: 'The chain of command exists to ensure unity of effort on the battlefield. "
            "Each soldier is responsible to their immediate superior. Orders flow downward while "
            "information flows upward. Breaking the chain of command creates confusion and can "
            "cost lives.'\n\n"
            "According to the passage, what flows upward in the chain of command?"
        ),
        "choices": ["A. Orders", "B. Promotions", "C. Information", "D. Supplies"],
        "answer": "C",
        "explanation": "The passage states 'information flows upward' through the chain of command.",
    },
    {
        "question": (
            "PASSAGE: 'First aid training can mean the difference between life and death on the "
            "battlefield. The most common preventable cause of combat death is hemorrhage. "
            "Applying a tourniquet within minutes of a wound can prevent a soldier from "
            "bleeding out before they reach medical care.'\n\n"
            "What does the passage identify as the most common preventable cause of combat death?"
        ),
        "choices": ["A. Infection", "B. Dehydration", "C. Hemorrhage", "D. Head trauma"],
        "answer": "C",
        "explanation": "The passage states 'the most common preventable cause of combat death is hemorrhage.'",
    },
    {
        "question": (
            "PASSAGE: 'Fitness is not merely a physical requirement in the Army; it is a "
            "professional obligation. A fit soldier is more alert, more resilient under stress, "
            "and makes better decisions. Physical readiness underpins every other aspect of "
            "warrior performance.'\n\n"
            "The word 'underpins' as used in the passage most nearly means:"
        ),
        "choices": ["A. undermines", "B. replaces", "C. supports", "D. ignores"],
        "answer": "C",
        "explanation": "To underpin means to support or strengthen from below; here it means physical readiness supports all other performance.",
    },
    {
        "question": (
            "PASSAGE: 'Communications security (COMSEC) is essential to mission success. "
            "Adversaries constantly monitor radio frequencies to gather intelligence. "
            "Soldiers must use brevity codes, encryption, and proper radio discipline to "
            "protect sensitive information.'\n\n"
            "The passage implies that failure to practice COMSEC could:"
        ),
        "choices": [
            "A. improve communications speed",
            "B. allow adversaries to gather intelligence",
            "C. cause radio equipment to fail",
            "D. reduce the need for encryption",
        ],
        "answer": "B",
        "explanation": "The passage states adversaries 'monitor radio frequencies to gather intelligence,' implying poor COMSEC helps them succeed.",
    },
    {
        "question": (
            "PASSAGE: 'Urban warfare presents unique challenges not found in open terrain. "
            "Buildings provide cover and concealment for the enemy but restrict the movement "
            "of friendly forces. Civilian presence further complicates the application of fire "
            "and maneuver tactics.'\n\n"
            "According to the passage, what makes urban warfare uniquely complex?"
        ),
        "choices": [
            "A. The absence of enemy fighters",
            "B. The open terrain",
            "C. Buildings and the presence of civilians",
            "D. The lack of cover for friendly forces",
        ],
        "answer": "C",
        "explanation": "The passage cites buildings that restrict movement and civilian presence as the unique complexities of urban warfare.",
    },
    {
        "question": (
            "PASSAGE: 'The Geneva Conventions are a set of international treaties that establish "
            "standards for the humanitarian treatment of war victims. They protect wounded "
            "soldiers, prisoners of war, and civilians. Violations of the Conventions are "
            "considered war crimes.'\n\n"
            "Which of the following is NOT mentioned as being protected by the Geneva Conventions?"
        ),
        "choices": [
            "A. Wounded soldiers",
            "B. Civilians",
            "C. Military vehicles",
            "D. Prisoners of war",
        ],
        "answer": "C",
        "explanation": "The passage mentions wounded soldiers, prisoners of war, and civilians — not military vehicles.",
    },
]

AR_QUESTIONS = [
    {
        "question": (
            "A convoy travels 240 miles in 4 hours. "
            "At the same speed, how far will it travel in 7 hours?"
        ),
        "choices": ["A. 360 miles", "B. 400 miles", "C. 420 miles", "D. 480 miles"],
        "answer": "C",
        "explanation": "Speed = 240 ÷ 4 = 60 mph. Distance = 60 × 7 = 420 miles.",
    },
    {
        "question": (
            "A platoon of 36 soldiers is split into equal teams of 4. "
            "How many teams are formed?"
        ),
        "choices": ["A. 7", "B. 8", "C. 9", "D. 10"],
        "answer": "C",
        "explanation": "36 ÷ 4 = 9 teams.",
    },
    {
        "question": (
            "A soldier earns $2,400 per month. "
            "If 15% is withheld for taxes, how much does the soldier take home?"
        ),
        "choices": ["A. $1,980", "B. $2,040", "C. $2,100", "D. $2,160"],
        "answer": "B",
        "explanation": "Taxes = 15% of $2,400 = $360. Take-home = $2,400 − $360 = $2,040.",
    },
    {
        "question": (
            "A field ration weighs 1.5 pounds. "
            "How much do 8 rations weigh in total?"
        ),
        "choices": ["A. 9.5 lbs", "B. 10 lbs", "C. 12 lbs", "D. 14 lbs"],
        "answer": "C",
        "explanation": "8 × 1.5 = 12 pounds.",
    },
    {
        "question": (
            "A soldier runs a 5K (5,000 meters) in 25 minutes. "
            "What is the soldier's average pace in meters per minute?"
        ),
        "choices": ["A. 150", "B. 175", "C. 200", "D. 225"],
        "answer": "C",
        "explanation": "5,000 ÷ 25 = 200 meters per minute.",
    },
    {
        "question": (
            "A military truck gets 8 miles per gallon. "
            "If the fuel tank holds 40 gallons, what is the truck's maximum range?"
        ),
        "choices": ["A. 280 miles", "B. 300 miles", "C. 320 miles", "D. 360 miles"],
        "answer": "C",
        "explanation": "Range = 8 × 40 = 320 miles.",
    },
    {
        "question": (
            "There are 3 squads in a platoon, each with 9 soldiers. "
            "A fourth squad of 7 soldiers joins. How many soldiers are in the platoon now?"
        ),
        "choices": ["A. 30", "B. 32", "C. 34", "D. 36"],
        "answer": "C",
        "explanation": "3 × 9 = 27 soldiers + 7 = 34 soldiers.",
    },
    {
        "question": (
            "An ammo crate weighs 60 pounds. "
            "If a soldier can carry at most 45 pounds, what percentage of the crate's weight "
            "can the soldier carry in one trip?"
        ),
        "choices": ["A. 65%", "B. 70%", "C. 75%", "D. 80%"],
        "answer": "C",
        "explanation": "45 ÷ 60 = 0.75 = 75%.",
    },
    {
        "question": (
            "A map uses a scale of 1:50,000. "
            "If two checkpoints are 4 cm apart on the map, what is the actual distance?"
        ),
        "choices": ["A. 1 km", "B. 2 km", "C. 4 km", "D. 5 km"],
        "answer": "B",
        "explanation": "4 cm × 50,000 = 200,000 cm = 2,000 m = 2 km.",
    },
    {
        "question": (
            "A soldier saves $150 per month. "
            "How many months will it take to save $1,350?"
        ),
        "choices": ["A. 7", "B. 8", "C. 9", "D. 10"],
        "answer": "C",
        "explanation": "$1,350 ÷ $150 per month = 9 months.",
    },
    {
        "question": (
            "A helicopter travels at 120 mph. "
            "How long will it take to travel 300 miles?"
        ),
        "choices": ["A. 2 hours", "B. 2.5 hours", "C. 3 hours", "D. 3.5 hours"],
        "answer": "B",
        "explanation": "Time = 300 ÷ 120 = 2.5 hours.",
    },
    {
        "question": (
            "A squad uses 6 gallons of water per day. "
            "How much water (in gallons) will they need for a 5-day mission?"
        ),
        "choices": ["A. 25", "B. 30", "C. 35", "D. 40"],
        "answer": "B",
        "explanation": "6 × 5 = 30 gallons.",
    },
    {
        "question": (
            "If a soldier completes 80% of a 25-question test correctly, "
            "how many questions did the soldier answer correctly?"
        ),
        "choices": ["A. 15", "B. 18", "C. 20", "D. 22"],
        "answer": "C",
        "explanation": "80% of 25 = 0.80 × 25 = 20 questions.",
    },
    {
        "question": (
            "A patrol covers 12 km on the first day and 9 km on the second day. "
            "What is the total distance covered?"
        ),
        "choices": ["A. 18 km", "B. 20 km", "C. 21 km", "D. 24 km"],
        "answer": "C",
        "explanation": "12 + 9 = 21 km.",
    },
    {
        "question": (
            "A soldier is paid $3,000 per month and receives a 10% raise. "
            "What is the new monthly pay?"
        ),
        "choices": ["A. $3,100", "B. $3,200", "C. $3,300", "D. $3,500"],
        "answer": "C",
        "explanation": "Raise = 10% × $3,000 = $300. New pay = $3,000 + $300 = $3,300.",
    },
    {
        "question": (
            "A rifle squad has 9 soldiers. Each carries 210 rounds of ammunition. "
            "How many total rounds does the squad carry?"
        ),
        "choices": ["A. 1,680", "B. 1,800", "C. 1,890", "D. 2,100"],
        "answer": "C",
        "explanation": "9 × 210 = 1,890 rounds.",
    },
    {
        "question": (
            "An obstacle course is 400 meters long. "
            "A soldier completes it in 80 seconds. "
            "What is the soldier's average speed in meters per second?"
        ),
        "choices": ["A. 4", "B. 5", "C. 6", "D. 8"],
        "answer": "B",
        "explanation": "Speed = 400 ÷ 80 = 5 meters per second.",
    },
    {
        "question": (
            "If a 15-gallon fuel drum is 2/3 full, how many gallons of fuel are in the drum?"
        ),
        "choices": ["A. 8", "B. 9", "C. 10", "D. 12"],
        "answer": "C",
        "explanation": "2/3 × 15 = 10 gallons.",
    },
    {
        "question": (
            "A soldier completes 3 sets of push-ups: 42, 38, and 40. "
            "What is the average number of push-ups per set?"
        ),
        "choices": ["A. 38", "B. 39", "C. 40", "D. 41"],
        "answer": "C",
        "explanation": "Total = 42 + 38 + 40 = 120. Average = 120 ÷ 3 = 40.",
    },
    {
        "question": (
            "A solder is ordered to dig a fighting position 3 feet deep, 4 feet wide, "
            "and 6 feet long. What is the volume of dirt to be removed (in cubic feet)?"
        ),
        "choices": ["A. 48", "B. 60", "C. 72", "D. 84"],
        "answer": "C",
        "explanation": "Volume = 3 × 4 × 6 = 72 cubic feet.",
    },
]

MC_QUESTIONS = [
    {
        "question": (
            "Two gears are meshed together. Gear A has 10 teeth and Gear B has 20 teeth. "
            "If Gear A turns at 100 RPM, how fast does Gear B turn?"
        ),
        "choices": ["A. 200 RPM", "B. 100 RPM", "C. 50 RPM", "D. 25 RPM"],
        "answer": "C",
        "explanation": "Gear ratio = 10/20 = 1/2. Gear B turns at 100 × (10/20) = 50 RPM.",
    },
    {
        "question": (
            "A lever has its fulcrum at the midpoint. "
            "A 60-lb weight is placed 3 feet from the fulcrum on one side. "
            "What force must be applied 3 feet from the fulcrum on the other side to balance it?"
        ),
        "choices": ["A. 30 lbs", "B. 45 lbs", "C. 60 lbs", "D. 120 lbs"],
        "answer": "C",
        "explanation": "When arms are equal length, the balancing force equals the load: 60 lbs.",
    },
    {
        "question": (
            "A block-and-tackle system uses 4 supporting rope segments. "
            "What is the mechanical advantage of the system?"
        ),
        "choices": ["A. 2", "B. 3", "C. 4", "D. 8"],
        "answer": "C",
        "explanation": "Mechanical advantage = number of supporting ropes = 4.",
    },
    {
        "question": (
            "A ball is rolling on a flat surface. "
            "According to Newton's First Law, the ball will:"
        ),
        "choices": [
            "A. speed up on its own",
            "B. stop immediately",
            "C. continue rolling at the same speed unless acted on by a force",
            "D. reverse direction",
        ],
        "answer": "C",
        "explanation": "Newton's First Law: an object in motion stays in motion at constant velocity unless acted on by an external force.",
    },
    {
        "question": (
            "Water pressure at the bottom of a tank depends on:"
        ),
        "choices": [
            "A. the surface area of the tank",
            "B. the color of the tank",
            "C. the depth of the water",
            "D. the temperature outside the tank",
        ],
        "answer": "C",
        "explanation": "Fluid pressure = ρgh; it depends on depth (h), density (ρ), and gravity (g).",
    },
    {
        "question": (
            "A vehicle engine produces 200 lb-ft of torque. "
            "If a mechanic attaches a drive shaft with a 2:1 gear reduction, "
            "what is the output torque?"
        ),
        "choices": ["A. 100 lb-ft", "B. 200 lb-ft", "C. 300 lb-ft", "D. 400 lb-ft"],
        "answer": "D",
        "explanation": "A 2:1 reduction doubles the torque: 200 × 2 = 400 lb-ft.",
    },
    {
        "question": (
            "A circuit has a voltage of 12 volts and a resistance of 4 ohms. "
            "Using Ohm's Law, what is the current?"
        ),
        "choices": ["A. 2 amps", "B. 3 amps", "C. 4 amps", "D. 48 amps"],
        "answer": "B",
        "explanation": "V = IR → I = V/R = 12/4 = 3 amps.",
    },
    {
        "question": (
            "Which simple machine is a ramp used to slide equipment into a truck?"
        ),
        "choices": ["A. Lever", "B. Pulley", "C. Inclined plane", "D. Wedge"],
        "answer": "C",
        "explanation": "A ramp is an inclined plane; it allows you to trade distance for reduced force.",
    },
    {
        "question": (
            "A spring scale reads 50 N when holding a rock in air. "
            "When the rock is submerged in water, the scale reads 35 N. "
            "What is the buoyant force on the rock?"
        ),
        "choices": ["A. 15 N", "B. 35 N", "C. 50 N", "D. 85 N"],
        "answer": "A",
        "explanation": "Buoyant force = weight in air − weight in water = 50 − 35 = 15 N.",
    },
    {
        "question": (
            "Gear A (30 teeth) drives Gear B (10 teeth). "
            "Compared to Gear A, Gear B will rotate:"
        ),
        "choices": [
            "A. 3 times slower",
            "B. at the same speed",
            "C. 3 times faster",
            "D. 2 times faster",
        ],
        "answer": "C",
        "explanation": "Gear ratio = 30/10 = 3. Gear B rotates 3× faster than Gear A.",
    },
    {
        "question": (
            "Which of the following best describes Newton's Third Law?"
        ),
        "choices": [
            "A. Force equals mass times acceleration",
            "B. An object at rest tends to stay at rest",
            "C. For every action there is an equal and opposite reaction",
            "D. Velocity is proportional to time",
        ],
        "answer": "C",
        "explanation": "Newton's Third Law: for every action force there is an equal and opposite reaction force.",
    },
    {
        "question": (
            "A wrench handle is 1 foot long and applies 20 lb of force. "
            "What is the torque being applied?"
        ),
        "choices": ["A. 5 lb-ft", "B. 10 lb-ft", "C. 20 lb-ft", "D. 40 lb-ft"],
        "answer": "C",
        "explanation": "Torque = Force × Distance = 20 lb × 1 ft = 20 lb-ft.",
    },
    {
        "question": (
            "Which conductor has the least electrical resistance?"
        ),
        "choices": ["A. Wood", "B. Rubber", "C. Copper wire", "D. Dry air"],
        "answer": "C",
        "explanation": "Copper is an excellent conductor with very low resistance; wood, rubber, and air are insulators.",
    },
    {
        "question": (
            "Two pistons in a hydraulic system: Piston A has an area of 2 sq in, "
            "Piston B has an area of 10 sq in. A force of 50 lbs is applied to Piston A. "
            "What force is exerted by Piston B?"
        ),
        "choices": ["A. 10 lbs", "B. 50 lbs", "C. 250 lbs", "D. 500 lbs"],
        "answer": "C",
        "explanation": "Pascal's Law: F_B = F_A × (A_B / A_A) = 50 × (10/2) = 250 lbs.",
    },
    {
        "question": (
            "A valve in a water pipe is partially closed. "
            "What happens to the water pressure just downstream of the valve?"
        ),
        "choices": [
            "A. It increases",
            "B. It stays the same",
            "C. It decreases",
            "D. It becomes zero instantly",
        ],
        "answer": "C",
        "explanation": "Restricting flow reduces pressure downstream of the restriction.",
    },
    {
        "question": (
            "Which of the following best describes the purpose of a transformer?"
        ),
        "choices": [
            "A. It converts DC to AC current",
            "B. It stores electrical energy",
            "C. It steps AC voltage up or down",
            "D. It measures electrical resistance",
        ],
        "answer": "C",
        "explanation": "A transformer uses electromagnetic induction to step AC voltage up or down.",
    },
    {
        "question": (
            "A 100-lb box is pushed up an inclined plane 10 feet long to reach a height of 2 feet. "
            "Ignoring friction, what force is required?"
        ),
        "choices": ["A. 10 lbs", "B. 20 lbs", "C. 50 lbs", "D. 100 lbs"],
        "answer": "B",
        "explanation": "Mechanical advantage = length/height = 10/2 = 5. Force = 100/5 = 20 lbs.",
    },
    {
        "question": (
            "In a series circuit with three 4-ohm resistors, what is the total resistance?"
        ),
        "choices": ["A. 4/3 ohms", "B. 4 ohms", "C. 8 ohms", "D. 12 ohms"],
        "answer": "D",
        "explanation": "Series circuit: R_total = R1 + R2 + R3 = 4 + 4 + 4 = 12 ohms.",
    },
    {
        "question": (
            "A vehicle weighs 4,000 lbs. A jack raises one corner by applying 500 lbs of force. "
            "What is the mechanical advantage of the jack?"
        ),
        "choices": ["A. 2", "B. 4", "C. 8", "D. 10"],
        "answer": "C",
        "explanation": "MA = Load / Effort = 4,000 / 500 = 8.",
    },
    {
        "question": (
            "What does a fuse do in an electrical circuit?"
        ),
        "choices": [
            "A. Increases current flow",
            "B. Stores electrical energy",
            "C. Breaks the circuit when current exceeds a safe level",
            "D. Converts AC to DC",
        ],
        "answer": "C",
        "explanation": "A fuse melts and opens the circuit if current exceeds the rated amperage, protecting the circuit.",
    },
]

AO_QUESTIONS = [
    {
        "question": (
            "A flat shape is cut into 3 pieces. When reassembled, which result best preserves "
            "the total area?\n"
            "A. The area increases\n"
            "B. The area decreases\n"
            "C. The area stays the same\n"
            "D. The area depends on the type of cuts"
        ),
        "choices": [
            "A. The area increases",
            "B. The area decreases",
            "C. The area stays the same",
            "D. The area depends on the type of cuts",
        ],
        "answer": "C",
        "explanation": "Cutting and reassembling a shape does not change total area; no material is added or removed.",
    },
    {
        "question": (
            "A square piece of paper is folded in half diagonally, then in half again. "
            "How many layers of paper are there?"
        ),
        "choices": ["A. 2", "B. 3", "C. 4", "D. 8"],
        "answer": "C",
        "explanation": "First fold → 2 layers. Second fold → 4 layers.",
    },
    {
        "question": (
            "You have a rectangular block viewed from the front. "
            "The block is rotated 90° to the right about its vertical axis. "
            "What do you now see?"
        ),
        "choices": [
            "A. The same front view",
            "B. The back of the block",
            "C. The right side of the block",
            "D. The top of the block",
        ],
        "answer": "C",
        "explanation": "Rotating 90° to the right brings the right side of the block to face you.",
    },
    {
        "question": (
            "A puzzle piece has a tab on the top and a blank on the right. "
            "Which slot will it fit into?"
        ),
        "choices": [
            "A. A slot with a blank on top and tab on the right",
            "B. A slot with a tab on top and blank on the right",
            "C. A slot with blanks on all sides",
            "D. A slot with tabs on all sides",
        ],
        "answer": "A",
        "explanation": "Tabs fit into blanks (indentations). A tab on top needs a blank on top of the adjacent piece, and a blank on the right needs a tab on the left of the adjacent piece.",
    },
    {
        "question": (
            "A capital letter 'T' is placed face down on a table. "
            "What does it look like from above?"
        ),
        "choices": [
            "A. T (unchanged)",
            "B. An upside-down T (⊥)",
            "C. A mirror image T",
            "D. The letter L",
        ],
        "answer": "C",
        "explanation": "Flipping a letter face-down produces its mirror image when viewed from above.",
    },
    {
        "question": (
            "Two identical triangular pieces are placed with their hypotenuses touching. "
            "What shape do they form?"
        ),
        "choices": ["A. A square", "B. A rectangle", "C. A pentagon", "D. A hexagon"],
        "answer": "B",
        "explanation": "Two right triangles with matching hypotenuses form a rectangle (or square if they are 45-45-90 triangles).",
    },
    {
        "question": (
            "A cube is painted red on all sides and then cut into 27 equal smaller cubes. "
            "How many small cubes have paint on exactly 2 faces?"
        ),
        "choices": ["A. 6", "B. 8", "C. 12", "D. 24"],
        "answer": "C",
        "explanation": "Edge cubes (not corners) have 2 painted faces. A 3×3×3 cube has 12 edge positions.",
    },
    {
        "question": (
            "A clock shows 3:00. If the clock is held up to a mirror, what time does the "
            "reflection show?"
        ),
        "choices": ["A. 3:00", "B. 6:00", "C. 9:00", "D. 12:00"],
        "answer": "C",
        "explanation": "In a mirror, the 3 on the right appears on the left, making it look like 9:00.",
    },
    {
        "question": (
            "You see a shape from the front that looks like a circle and from the side that "
            "looks like a rectangle. What 3-D solid is it most likely?"
        ),
        "choices": ["A. Sphere", "B. Cube", "C. Cylinder", "D. Cone"],
        "answer": "C",
        "explanation": "A cylinder appears as a circle when viewed end-on and as a rectangle when viewed from the side.",
    },
    {
        "question": (
            "A net (unfolded shape) consists of 6 equal squares arranged in a cross pattern. "
            "When folded, it forms a:"
        ),
        "choices": ["A. Pyramid", "B. Cylinder", "C. Cube", "D. Prism"],
        "answer": "C",
        "explanation": "Six equal squares arranged in a cross fold into a cube.",
    },
    {
        "question": (
            "A piece has a circular hole on its left side and a square peg on its right. "
            "Which connector piece joins it to another piece that has a square hole on the left "
            "and a circular peg on the right?"
        ),
        "choices": [
            "A. A piece with a circular peg on the left and square hole on the right",
            "B. A piece with two circular holes",
            "C. A piece with two square pegs",
            "D. A flat piece with no connectors",
        ],
        "answer": "A",
        "explanation": "The right side of the first piece has a square peg needing a square hole, and the left piece needs a circular peg to match the circular hole.",
    },
    {
        "question": (
            "If you look at a transparent clock from behind (through the glass), "
            "which number appears where the 12 normally is?"
        ),
        "choices": ["A. 12", "B. 6", "C. 3", "D. 9"],
        "answer": "A",
        "explanation": "Viewing through the glass from behind, the 12 is still at the top; left and right are reversed, but up/down is not.",
    },
    {
        "question": (
            "A standard die (cube) has opposite faces summing to 7. "
            "If the 1 is on top and the 2 faces you, which number is on the bottom?"
        ),
        "choices": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "D",
        "explanation": "Opposite to 1 is 6 (1+6=7), so 6 is on the bottom.",
    },
]

# ---------------------------------------------------------------------------
# Master question bank
# ---------------------------------------------------------------------------
QUESTION_BANK = {
    "WK": WK_QUESTIONS,
    "PC": PC_QUESTIONS,
    "AR": AR_QUESTIONS,
    "MC": MC_QUESTIONS,
    "AO": AO_QUESTIONS,
}
