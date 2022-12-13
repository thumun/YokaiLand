import random
from random import choice

# global var

# occupancyMap = [1, 1, 1, 1, 10, 1, 2, 2, 2, 2, 10, 2, 3, 3, 3, 3, 3, 10, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

# test version below 
occupancyMap = [1, 2, 10, 3, 4, 10]

heal = [
    {"name": "Cucumber", 
     "Info": "Not the most delicious cucumber in the world but it could be a healthy meal-or at least part of one.", 
     "Healing": 4, 
     "Yokai": ["Kappa"], 
     "Count": 99, 
     "category": "heal"},
    
    {"name": "Candy", 
     "Info": "A sweet piece of hard candy! Sure to lift up your spirits in a dark time.", 
     "Healing": 2, 
     "Yokai": ["Kuchisake-onna"], 
     "Count": 99, 
     "category": "heal"},
    
    {"name": "Deep-fried food", 
     "Info": "A fried snack that you got from a street vendor. Hopefully it tastes as good as it smells.", 
     "Healing": 5, 
     "Yokai": ["Kitsune"], 
     "Count": 99, 
     "category": "heal"},
    
    {"name": "Rice cooked with azuki beans", 
     "Info": "Some leftovers from a rather nice meal that you had at a local restraunt.", 
     "Healing": 10, 
     "Yokai": ["Kitsune"], 
     "Count": 99, 
     "category": "heal"},
    
    {"name": "Buddhist Teachings", 
     "Info": "A monk from a shrine gave this to you to help when you need a way to center yourself.", 
     "Healing": 7, 
     "Yokai": ["Woman with a Hannya mask"], 
     "Count": 99, 
     "category": "heal"},
    
    {"name": "Banishment Prayer", 
     "Info": "A handy prayer that you learned-it is said to banish yokai that possess a certain level of bloodlust from this world. (Will not heal you.)", 
     "Healing": 0, 
     "Yokai": ["Woman with a Hannya mask"], 
     "Count": 99, 
     "category": "heal"},
    
    {"name": "Liver", 
     "Info": "Not recommended to be eaten without being cooked first but hopefully it would not cause too much damage.", 
     "Healing": 3, 
     "Yokai": ["Moryo"], 
     "Count": 99, 
     "category": "heal"},
    
    {"name": "Smoked Meat", 
     "Info": "A mystery meat that you cooked yourself.", 
     "Healing": 9, 
     "Yokai": ["Amanojaku"], 
     "Count": 99, 
     "category": "heal"}
    ]

curses = [
            {"name": "Picture with needles", 
           "Info": "You have a picture of one of the other players. You can hinder their journey by sticking pins and needles into their limbs. This will injure them each turn until they go to a shrine.", 
           "isHarmful": [True, -2], 
           "selfHarm":[False, 0], 
           "Count": 99, 
           "category":"curse"},
          
            {"name": "Steal a weapon", 
             "Info": "You go to the shrine and pray that your opponent's weapon becomes your own.", 
             "isHarmful": [False, "weapon"], 
             "selfHarm": [False, 0], 
             "Count": 99,
             "category":"curse"}, 
            
            {"name": "Steal an item", 
             "Info": "You notice that another person on the same quest as you has an item of interest.. perhaps you can be successful in acquiring it.", 
             "isHarmful": [False, "heal"], 
             "selfHarm":[False, 0], 
             "Count": 99, 
             "category":"curse"},
            
            {"name": "Change Places", 
             "Info": "You manipulate the space around you to be able to swap places with another player.", 
             "isHarmful": [False, "other"], 
             "selfHarm":[False, 0], 
             "Count": 99, 
             "category":"curse"},
            
            {"name": "Talisman of Harm", 
             "Info": "You learn the art of making a talisman to harm another player. You can plan to leave this along a route that the player is expected to traverse. This is a powerful curse, and everything has a consequence.", 
             "isHarmful": [True, -10], 
             "selfHarm":[True, -5], 
             "Count": 99, 
             "category":"curse"}
            
            ]

weapons = [
            {"name": "Sword of Kusanagi", 
            "Info": "The legendary Sword of Kusanagi has appeared before you...and its your to wield in battle. It will do a tremendous amount of damage but be cautious as a terrible curse may befall those who lose it...", 
            "ATK":15, 
            "Yokai":[],
            "Count": 1, 
            "category":"weapon"},
            
            {"name": "Rusty Iron Scissors", 
            "Info": "Some rather bent scissors that you found on the side of the road. They do not seem very practical in a fight.", 
            "ATK":3, 
            "Yokai":["Kappa"],
            "Count": 99, 
            "category":"weapon"},
            
            {"name": "Pomade", 
            "Info": "An empty tin of hair gel..well someone else's trash could be your treasure?", 
            "ATK":1, 
            "Yokai":["Kuchisake-onna"],
            "Count": 99, 
            "category":"weapon"},
            
            {"name": "Oak Stake", 
            "Info": "A stake fashioned from the wood of an oak tree.", 
            "ATK":4, 
            "Yokai":["Moryo"],
            "Count": 99, 
            "category":"weapon"},
            
            {"name": "Chains", 
            "Info": "Can be used to hold something in place or could be used to land a heavy blow.", 
            "ATK":6, 
            "Yokai":["Kamaitachi"],
            "Count": 99, 
            "category":"weapon"},
            
            {"name": "Summon Rain", 
            "Info": "The ancient magic art of summoning rain! ...Perhaps this could be useful in a specific circumstance?", 
            "ATK":0, 
            "Yokai":["Ushirogami"],
            "Count": 99, 
            "category":"weapon"},
            
            {"name": "Lute", 
            "Info": "If you knew how to play this instrument, it could be used to make some beautiful music. However, it seems you are more interested in using it as a weapon..perhaps hitting a yokai with it?", 
            "ATK":5, 
            "Yokai":["Umizato"],
            "Count": 99, 
            "category":"weapon"},
            
            {"name": "Bottomless Barrel", 
            "Info": "One man's trash is another man's treasure!", 
            "ATK":4, 
            "Yokai":["Umibozu"],
            "Count": 99, 
            "category":"weapon"}
            ]

waterYokai = [
        {"name":"Kappa", 
         "attacks":["The kappa reaches out and firmly grips your arm which it then tries to pull you into the water. You are able to wriggle out of its grip but are left with some bruises.", "The kappa manages to tip you over with its brute strength and you crash onto the ground.", "It ends up bringing you into the water and tries to drown you but you are able to use the current to get away."], 
         "attackDMG":[2, 4, 8], 
         "Convo":"Will you wrestle with me?", 
         "CYes":["You agree to the kappa's request and face off next to the shore of a river. The kappa easily overpowers you and although you attempt to pull its limbs (since you heard its arms are connected and can fall out) this does not help. You are helplessly dragged into the river. [You have lost all of your hit points due to drowning.", ["P", 300]], 
         "CNo":["You decline this challenge by bowing as not only a sign of deference but also in hopes that the Kappa will mimic your action. To your relief, the kappa bows to you as well and the water from the sara on its head spills which causes it to flee immediately.", ["M", [300]]], 
         "Run":13, 
         "Item":["Rusty Iron Scissors", "Cucumber"], 
         "DC":11, 
         "Intro":"A dark shape flitting around near the water's edge catches your eye. It seems to be swimming too swiftly to be a child yet it seems to be covered in...hair? You get a closer look and realize that its also seems to have scales and has an odd blue-yellow hue. It quickly makes its way towards you and you can smell a sharp fishy scent in the air. The being watches you closely seeing what move you decide to make..", 
         "DefeatATK":"You are finally able land a blow on its head-with a distinctive crack, the disk on its head shatters and the kappa immediately flees the scene. It seems to be devoid of its strength now. All that's left of the kappa's appearance are odd webbed prints going back into the river.", 
         "Rusty Iron Scissors":"You fling the iron scissors at the kappa. When the kappa touches it, it recoils and flees the scene.", 
         "Cucumber":"You toss the cucumber at the kappa and it happily takes it. Its attention is turned to munching on the cucumber which you take as the perfect way to escape the scene.", 
         "Health":15},
        
        {"name":"Umibozu", 
         "attacks":["It controls the weather to whip up a storm around the boat-which throws you around the deck.", "It slams against the hull-forcing you to hang on for dear life.", "It hits the side of the ship with several blows which leads you to hit the mast."], 
         "attackDMG":[7, 9, 6], 
         "Convo":"You open your mouth to speak...", 
         "CYes":["You continue speaking and with one swift motion your boat is overturned and you feel yourself being dragged to the bottom of the sea...", ["P", 300]], 
         "CNo":["You notice a change in demeanor of the yokai and quickly shut your mouth but it is too late. You feel yourself fly off the boat and into the ocean. The roaring waves drag you under..", ["P", 300]], 
         "Run":19, 
         "Item":["Bottomless Barrel"], 
         "DC":2, 
         "Intro":"You commandeer a boat to make your travels easier and found the sea to be eerily quiet. The water is completely still and you feel a chill go down your spine. You look out into the darkness to see two eyes staring back at you.", 
         "DefeatATK":"Your last attack seems to stun it long enough for you to jump onto a lifeboat and try to get to safety. You look back to see the umibozu continue attacking the ship and realize how massive that yokai truly is..thankfully you got out of its way before it was too late.", 
         "Bottomless Barrel":"You give it a barrel with no bottom. The umibozu attempts to scoop water with the barrel and dump it onto your boat but fails. You take this opportunity to paddle out of there quickly.", 
         "Health":10},
        
          {"name":"Umizato", 
         "attacks":["The yokai strums a little tune.", "The water becomes choppy and pushes you farther to shore.", "The yokai used his cane to tap the water."], 
         "attackDMG":[0, 2, 0], 
         "Convo":"(Instead of talking the yokai simply continues playing the beautiful song.)", 
         "CYes":["You listen along quietly and once the song ends, the yokai vanishes.", ["M", 300]], 
         "CNo":["You gear up ready to fight and get knocked to your feet by waves. When you get back up the yokai has vanished.", ["M", 300]], 
         "Run":0, 
         "Item":["Lute"], 
         "DC":0, 
         "Intro":"A beautiful melody rings in the air drawing your attention to the clear sea. You spend some time listening to the melody while looking out towards the sky. A humanoid shape catches your eye. You look closer to see an old man playing a lute while somehow sitting on the surface of the water.", 
         "DefeatATK":"Can you truly defeat this yokai? None of your attacks seem to be doing any damage-they do not even seem to be hitting the yokai. A wave appears before you and the yokai and you see that it has vanished...", 
         "Lute":"You bring out the beautiful lute that you found and attempt to play it. Beautiful sounds come from it although the melody is rather discordant. The yokai changes its tune and plays along with you. You both create a haunting song at the end of which the yokai and your lute vanish.", 
         "Health":8},
          
        {"name":"Iso Onna", 
         "attacks":["She uses her massive tail to create a wave that hits you.", "She slashes you with one of her clawed hands.", "She uses her snake like fangs to slice into your skin."], 
         "attackDMG":[4, 5, 6], 
         "Convo":"She hands you a child to hold.", 
         "CYes":["You take the child and look down to see that it has turned to stone and the stone seems to spreading to you. Try as you might, you are unable to shake off the stone and feel yourself suffocating.", ["P", 300]], 
         "CNo":["You take the child and immediately throw it. The child, which was stone, shatters and you use that opportunity escape. As you run, you can hear the angry yelling of the yokai behind and the sound of hoofbeats. You glance back and see a bull racing towards you which only makes you run faster.", ["M", 300]], 
         "Run":15, 
         "Item":[], 
         "DC":6, 
         "Intro":"You are walking close to the shore and see an odd sort of sparkling in the water. After a closer look, it almost appears to be giant scales but that could only be from something like a sea serpent? A loud hissing sound comes from behind you and you turn to see a gigantic snake with a woman's face.", 
         "DefeatATK":"You can see the yokai becoming disoriented after the amount of blows it received from you. You use that chance to get its attention and run farther inland. It attempts to follow and instead collapses onto the ground.", 
         "Health":21}
        ]
    
forestYokai = [
         {"name":"Kitsune", 
         "attacks":["Her fingernails grow into claws and with the swiftness of a fox she slashes at you.", "She shifts into the form of a fox and darts towards you to bite into your flesh.", "She deftly hits her tail against the ground to summon a fireball."], 
         "attackDMG":[2, 3, 7], 
         "Convo":"Would you like to play some tricks with me-on people that deserve it of course~", 
         "CYes":["You wholeheartedly agree and join the Kitsune in conning wealthy passerby into giving up some of their wealth. As you part ways, you wishes you luck on your journey and offers you a favor for your help. You take her up on the favor and she offers a piece of advice-\"visit more shrines, they may prove to be useful in case something bad happens\".", ["M", 300]], 
         "CNo":["A frown briefly appears on her face as you reject her offer. She scoffs and shifts into a fox before prancing away. As you continue on your way, you realize that your cash is gone! You hear a snicker in the distance but try as you might the fox seems to have slipped away..", ["M", 300]], 
         "Run":10, 
         "Item":["Deep-fried food", "Rice cooked with azuki beans"], 
         "DC":10, 
         "Intro":"You approach a rather old, dilapited shrine and hear the sound of laughter but no source. A little burst of fire appears before you, seemingly inviting you to follow it. You follow the fire towards a clearing and see a beautiful woman standing there with an almost fox-like shadow.", 
         "DefeatATK":"You manage to hit the Kitsune hard enough for it to fall to the forest clearing. It slowly gets up and takes the form of a small fox before limping away into the shadows of the forest.", 
         "Deep-fried food":"You offer the Kitsune Deep-fried food and it happily accepts. You give it the snack and watch it scamper away with its' tail wagging.", 
         "Rice cooked with azuki beans":"You offer your rice cooked with azuki beans to the kitsune. It shifts into the form of a fox and sniffs the food before agreeing to the trade. You are able to safely leave the clearing.", 
         "Health":17},
         
        {"name":"Moryo", 
         "attacks":["It latches onto your arm with its strong jaw.", "It attempts to bite you but only matches to scrape you.", "It grips your arm and attempts to throw you into a grave."], 
         "attackDMG":[6, 3, 7], 
         "Convo":"\"...\" (It doesn't seem to be interested in conversing and is instead staring at your liver.)", 
         "CYes":["You misread its look and think it would be more open to talking if you were got closer to it. You crouch down to be eye level and it takes the initiative to launch itself at your liver. You feel its fangs sink into your flesh and you are unable to escape from its grasp.", ["P", 300]], 
         "CNo":["You carefully watch the yokai while slowly walking away from it. Although you are ready to react if it makes a move, it simply watches you as you leave and turns back to the meal before it.", ["M", 300]], 
         "Run":3, 
         "Item":["Liver", "Oak Stake"], 
         "DC":5, 
         "Intro":"You carefully pick your way through a battlefield and hear odd noises coming from behind a tree. You peer over some rocks to see a small child crouched near a corpse. You make your way over to it and say a greeting but stop in your tracks as you see a red and black creature munching on a liver.", 
         "DefeatATK":"You are able to scare it with your fighting prowess. It swiftly leaves the battlefield and disappears from your sight.", 
         "Liver":"You toss a liver over to it and it happily grabs it. You get out of there before it realizes that the liver you gave was not from a human.", 
         "Oak Stake":"You manage to stab the Moryo with an Oak Stake and looks at you with horror before becoming slack in your arms. You lay it to rest and continue on your way.", 
         "Health":14},
        
        {"name":"Kamaitachi", 
         "attacks":["Fierce winds whip nearby branches and debris towards you.", "It rushes you with knives and slices faster than you can dodge.", "It creates a whirlwind of blades that throws you off your feet and cuts your arms to ribbons."], 
         "attackDMG":[9, 10 ,11], 
         "Convo":"Let's fight!", 
         "CYes":["You fervently agree to its challenge and are able to follow/ match its movements for a few rounds but exhaustion quickly overtakes you. The windstorm of blades rushes you and you are unable to defend yourself.", ["P", 300]], 
         "CNo":["You reject its challenge and instead duck farther into the woods in an attempt to lose the yokai. You find a dark cave and hide there. A strong breeze whips around you but after a few minutes it subsides.", ["M", 300]], 
         "Run":19, 
         "Item":["Chains"], 
         "DC":4, 
         "Intro":"You feel a strong, fresh breeze through the trees. You look in the direction of the breeze and scramble back as a knife wielding weasel launches itself at you.", 
         "DefeatATK":"You are able to parry and land blows on the Kamaitachi. You use your momentum to throw the yokai off its rhythm by using the environment around you. You lead it farther into the forest and let it get itself tangled up in the trees.", 
         "Chains":"You toss the chains into the whirlwind and the fierce winds immediately subside as the yokai becomes tangled up in the chains. You use the chance to get past the yokai.", 
         "Health":9},
        
        {"name":"Ubume", 
         "attacks":["The ubume seems to focused on the ground before it. The blood on her clothes slowly seeps into the grass around her...", "She looks at you sadly.", "She appears to be silently contemplating the rain and watching her clothes become more drenched."], 
         "attackDMG":[0, 0, 0], 
         "Convo":"\"...\" (She offers you her child)", 
         "CYes":["You silently take the child from her and she dissipates into the rain. You journey onward with the child and find the weight in your arms becoming heavier and heavier. The rain also seems to be..increasing? You watch on in shock as the ground before you starts taking on water. Before you can do much of anything, you feel yourself sink into the mud and water burdened by the additional weight of the ubume's child.", ["P", 300]], 
         "CNo":["You do not accept the child and instead watch as the ubume disappears along with the child. You find a flower and leave it on the spot where the Ubume had been standing.", ["M", 300]], 
         "Run":0, 
         "Item":[], 
         "DC":0, 
         "Intro":"You find yourself in a makeshift graveyard near a roaring river. You stop to pay your respects and hear what sounds like a baby crying. As you make your way towards the noise you find yourself standing before a recently dug grave. With a burst of courage, you brush past the dirt and find nothing in the hole. You look back to see a ghostly woman holding a crying child with suspicious red stains covering her clothes.", 
         "DefeatATK":"As you land your final blow, the ubume disappears. You look at the spot where it was and could not help but wonder if it was the right decision to fight this yokai...", 
         "Health":10}
    ]
    
cityYokai = [
        {"name":"Kuchisake-onna", 
         "attacks":["She uses her scissors to slash at you which you block..with your arm.", "She attempts to cut your face to make it look like her own.", "Her weapon slightly scratches you."], 
         "attackDMG":[5, 9, 3], 
         "Convo":"Do you think I'm pretty?", 
         "CYes": ["You declare that she is indeed pretty. In response, she takes off her surgical mask to reveal her mouth which is horrifically sliced open. She smiles and says, \"even like this?\" You nod vigorously to try and appease her. Thankfully this seems to be the right response she turned around and vanished into the gloom.", ["M", 300]], 
         "CNo":["You quickly shake your head no and hope that is the end of the conversation with this mysterious, frankly rather creepy woman. You see a look of fury overtake her face and before you can react she stabs you with scissors..in the heart.", ["P", 300]], 
         "Run":18, "Item":["Candy", "Pomade"], "DC":5, 
         "Intro":"As you walk along the outskirts of the town, you see the sky begin to darken and feel something watching you. You make your way towards a bus stop and hear the sound of footsteps behind you. As you turn to look, a woman appears. She wears a mask that covers half her face and seems to be carrying something shiny in her hands.", 
         "DefeatATK":"You feel yourself growing tired from evading attacks and attempting attacks so you draw your strength together for a final blow. With a burst of speed you hit her in the leg and she stumbles to the ground. You feel a sense of dread as she immediately vanishes but you do not see her anywhere around you.. perhaps she is gone for good?", 
         "Candy":"You frantically dig into your pockets and fling the first thing you grab onto-hard candy. Much to your surprise, she looks at the candy with delight and picks it up. You take that moment to run as fast as you can away from her and make sure to not look back.", 
         "Pomade":"You scream the word \"Pomade\" and show a container of hair gel. She reels back in shock and you take that initiative to run as fast as you can from the fight.", 
         "Health":18}, 
        
        {"name":"Namazue", 
         "attacks":["The catfish shakes slightly which causes you to lose your footing and hit the ground rather hard.", "The catfish uses its tail to topple a nearby building-the debris unfortunately manages to hit you.", "The catfish lunges forward but you are able to keep your footing and but are dealt a few bruises."] , 
         "attackDMG":[7, 12, 5], 
         "Convo":"I have no business with you. My targets are the merchants who hoard all their wealth and only keep money circulating amongst themselves! I only wish to help the common folk find work." , 
         "CYes":["You agree with the catfishes sentiments in bringing down the merchants and redistributing wealth amongst more people", ["M", [300]]], 
         "CNo":["You may agree with the catfish but believe the amount of destruction that is caused is not worth the potential benefits. You recall that Kashima deity is the one who can keep this catfish at bay and pray for the deity to step in. However before there is any possibility of divine intervention, the destruction caused by the Namazue rains down upon you.", ["P", 300]] , 
         "Run":16, 
         "Item":[], 
         "DC":3, 
         "Intro":"When you intitally walked into town you felt a slight tremor but had thought nothing of it, but looking down you realize that the ground looks a lot like fish scales. A mysterious rock catches your eye and when you go closer to it you see a sign that declares "" (use article to see god's vacation) A giant eye stares at you and you stare back at it." , 
         "DefeatATK":"Try as you might, your attacks were hardly grazing the Namazue. It is simply too big to hurt. However you feel newfound power coursing through your veins and a voice rings out commanding you to move. You leap out of the way just in time to see a massive boulder appear and the Kashima deity astride it. It seems the deity has finally returned to his duty of keeping the Namazue under control." , 
         "Health":25},
        
        {"name":"Woman with a Hannya mask", 
         "attacks":["She turns towards you and looks you in the eyes which makes you stumble back in fright.", "She uses a mallet to hit you across the legs.", "She scoops water into her hands which quickly boils and tosses it towards you."], 
         "attackDMG":[2, 5, 6], 
         "Convo":"Will you help me with my vengeance?", 
         "CYes":["You agree to help her seek out vengeance and join her in ending the lives of her former lover and their current partner. A feeling of bloodlust begins to consume you and you feel the need to draw more blood. This urge truly consumes you and you feel horns begin to grow out of your head and scales form on your hands..but you do not realize this as it is too late.", ["P", 300]], 
         "CNo":["You are horrifed by the request and decline to take part. She turns away from you and continues on her way towards the shrine. You watch as she leaves unable to figure out how to stop her.", ["M", 300]], 
         "Run":7, 
         "Item":["Buddhist Teachings", "Banishment Prayer"], 
         "DC":18, 
         "Intro":"You hear the sound of people sprinting and stop to look back. Two monks run past you and you catch snippets of their conversation. Something about a demon who was going to make her way to the shrine at a certain hour for nefarious purposes. Curiosity strikes your heart and you decide to hide out along the path. Late in the night, you hear the forest turn silent and an ominous prescence make its way along the route. You look to see a terrifying face with two giant horns protruding from its forehead.", 
         "DefeatATK":"With a carefully aimed blow, you are able to strike her square in the face. The mask shatters and she falls back unconcious. However, the horns on her face and the red, dragon like scales remain on her..perhaps it is too late for her.", 
         "Buddhist Teachings":"You promise the ghost that it will be able to seek vengence on those that wronged her (namely her former lover and the one he is currently with). You hand her the Monk's teachings and leave-knowing that you have hopefully tricked her into repenting.", 
         "Banishment Prayer":"You recall the banishment prayer and remain in your hiding place while conducting the ritual. You see the being grab its mask in pain before fading away.", 
         "Health":20},
        
        {"name":"Akaname", 
         "attacks":["It lashes out with its tongue and hits you in the shoulder.",  "It latches onto your leg and you feel your flesh peeling.",  "It locks eyes with you and you feel gutwrenching dread."], 
         "attackDMG":[5, 8, 2], 
         "Convo":"*stares at you*", 
         "CYes":["You take the hint and get out of the bathroom as fast as you can. You can feel the monster staring at you as you leave.", ["M", 300]], 
         "CNo":["You stand your ground (remain in the bathroom) and stare back at the yokai. It slinks off and you feel a slight bit of pride", ["M", 300]], 
         "Run":3, 
         "Item":[], 
         "DC":7, 
         "Intro":"You feel the need to use the restroom and make your way towards the nearest one. You sit on the toilet and feel a rather ominous prescense watching you. You look up to see two pairs of eyes peering at you from atop the bathroom stall.", 
         "DefeatATK":"You are able to knock the yokai off its perch and land a heavy blow. It crawls away and you go back to use the restroom in peace.", 
         "Health":12}
    ]
    
outskirtsYokai = [
         {"name":"Tsukumogami-sword", 
         "attacks":["The sword glows with an unearthly light and plunges itself into your leg.", "The sword attempts to slash you across the stomach-you manage to avoid serious injury but are left with a cut.", "The sword is consumed by bloodlust and attacks your face."], 
         "attackDMG":[8, 3, 6], 
         "Convo":"I love building palaces out of the flesh and blood of my foes! Why would I ever stop? ", 
         "CYes":["You encourage the Tsukumogami to pursue its life dream. It happily flies away, ready to end its next victim. At least its not you!", ["M", 300]], 
         "CNo":["You are visibly disgusted at the thought of blood palaces. The tsukumogami notices and moves to strike you down. You lay on the ground bleeding to death.", ["P", 300]], 
         "Run":12, 
         "Item":["Buddhist Teachings", "Banishment Prayer"], 
         "DC":15, 
         "Intro":"The stench of blood fills the air as you walk into a small seemingly abandoned town. You slowly walk towards the stench and are horrified to find a pile of bodies in the middle of the town square. Blood still dripping from some of the bodies collects in a gruesome pool and the bottom of the pile. You hear dreadful laughter and see a sword fly towards you.", 
         "DefeatATK":"You parry the sword's attacks and manage to stay on your feet. You notice that the sword appears to be slightly off balance and you use that moment to strike in a place where a strong blow had already been dealt. The sword breaks in two and you feel a sense of relief overtake you.", 
         "Buddhist Teachings":"You offer Buddhist Teaching to the sword in an effort to reduce its bloodlust. It reluctantly accepts it and allows you to leave. You can hear the sound of paper being ripped apart behind you...", 
         "Banishment Prayer":"While dodging the sword's rapid slashes, you conduct the banishment prayer and are successful in ridding the tsukumogami from this world. The sword itself clatters to the ground-broken and useless.", 
         "Health":12},
         
        {"name":"Tsukumogami-cup", 
         "attacks":["The cup hops up and hits you with its handle.", "It attempts to headbut your shin.", "It rolls around trying (and mostly failing) to trip you."], 
         "attackDMG":[2, 1, 1], 
         "Convo":"Is there another way for me to live my life other than to attack travelers along this route?", 
         "CYes":["You suggest that the Tsukumogami should seek out enlightenment. It takes your encouragement to heart and goes on a quest to find guidance.", ["M", 300]], 
         "CNo":["You are uncertain as to what to say and the Tsukumogami seems to interpret your silence with disappointment. It hops away rather sadly.", ["M", 300]], 
         "Run":2, 
         "Item":["Buddhist Teachings"], 
         "DC":9, 
         "Intro":"You make your way along a path and see an odd set of footprints going the same route. Unlike any animal you have ever seen before...rather, they are somehow perfectly symmetrical? Up ahead you see a slightly chipped cup hopping along. It stops in its tracks and opens a very human-like eye to stare at you.", 
         "DefeatATK":"You catch the cup's handle with your blow and shatter the Tsukumogami. It falls to the ground in pieces-effectively gone from this world.", 
         "Rusty Iron Scissors ":"You offer the tsukumogami Buddhist teachings which it accepts gratefully. You continue on your way as it pours over the teachings.", 
         "Health":6},
        
        {"name":"Amanojaku", 
         "attacks":["He throws a boulder towards you which you are able to mostly dodge.", "He reveals your greatest fear which freezes you in place just long enough for him to punch you.", "He manages to pick you up and throw you."], 
         "attackDMG":[3, 7,8], 
         "Convo":"I want revenge on the one who sealed me away! Will you help me find more about him?", 
         "CYes":["You agree as this is much better than being stuck in this situaiton. The yokai leads you to a statue that apparently it was trapped in for many years, You examine the statue and the surroundings and find a name. The yokai thanks you and goes to get revenge. You feel a slight pang of guilt but what else could you have done?", ["M", 300]], 
         "CNo":["You say no as you do not want anyone to face the wrath of such a strong monster. The yokai does not take this response well. Opting to throw the largest boulder you have seen so far-right at your face.", ["P", 300]], 
         "Run":17, 
         "Item":["Smoked Meat"], 
         "DC":8, 
         "Intro":"You carefully pick your way through a pile of rubble. Boulders the size of houses line the pathway and you cannot help but wonder how they could have gotten there in the first place. You hear a loud a crashing sound from above you and roll out of the way of an incoming boulder. You hear a booming laugh and a gigantic tengu-like creature above you.", 
         "DefeatATK":"Your attacks have done some damage but definitely not enough to fell the yokai. So, you opt for a change of tactics. You notice that 'mountain' that the yokai is atop of is merely a gigantic pile of rocks..a pile of unstable rocks. You run around to make the yokai throw boulders at you and cause the pile to collapse onto itself. You watch as the yokai is buried in its own grave.", 
         "Rusty Iron Scissors ":"You carefully take out the Smoked Meat and offer it to the yokai. The deleicious smell of it makes the yokai to come down and stand befor you. IIt snatches the food out of your hands and jumps back up the mountain.", 
         "Health":23},
        
        {"name":"Ushirogami", 
         "attacks":["She vanishes from your sight and grabs you from behind.", "She tugs the hair on the back of your neck which makes you fall over.", "She summons a strong wind that throws you against a wall."], 
         "attackDMG":[5,3,7], 
         "Convo":"\"...\" (She hands you a cactus.)", 
         "CYes":["You accept the cactus and stare at it rather confused. The cactus seems rather normal but has a few weird looking bulbs and a bright red flower atop it. You watch rather intrigued as another bulb seems to be forming on the cactus. This curiosity turns to horror as you realize the cactus is getting bigger and- (The cactus has consumed you.. it returns to a smaller state and grew some purple leaves.)", ["P", 300]], 
         "CNo":["You push the cactus away from you and take a few steps back from the yokai. The cactus falls to the ground and oozes an ominous red liquid..which looks awfully like blood. You take the chance to get out of there before the yokai can do anything else.", ["M", 300]], 
         "Run":6, 
         "Item":["Summon Rain"], 
         "DC":7, 
         "Intro":"You knock on the door of a house which creaks open. You step inside and see the dark outlines of furiture but no signs of life. As you make your way around, you find that everything is covered by a thick layer of dust. You feel a prescense behind you and turn to see a pale figure with long white hair and a darkened face-but two large eyes with pitchblack pupils.", 
         "DefeatATK":"A few drops of rain begin falling as you fight the yokai. You see the yokai flinch but continue coming after you. You give the yokai a shove and it hits a nearby a willow tree. With a horrifying scream, it gets sucked into the tree.", 
         "Rusty Iron Scissors ":"The yokai screams as it starts raining and flees from you. You do not get the sense that it was destroyed but the rain certainly harmed it somehow.", 
         "Health":14}
    ]


players = []

class Player():
    # items = {"heal":[], "curse":[]}
    def __init__(self, name):
        self.name = name
        self.healItems = []
        self.curseItems = []
        self.weapons = [{"name": "Trusty (slightly rusty) Knife", "Info": "The knife that you carry with you for cutting to brush.", "ATK":5, "Yokai":[], "Count": 99, "category":"weapon"}]
        self.health = 30
        self.inShrine = (False, 0)   # inshrine, turnNum
        # self.isRevive = False
        self.lastShrine = -1 
        self.playerTile = -1 # so works with occupancymap??
        self.conditions = []

def main():

    # if num == 1, then say sorry this is multiplayer game
    # but keep for now for testing
    
    numPlayers = int(input("How many players are there? "))

    for i in range(numPlayers):
        # initialize as obj of type player
        players.append(Player(i))

    i = 0 
    endReached = False 

    # players[0].items["heal"].append({"name": "Cucumber", "Info": "Can be used to heal you for 2 points. It may also be useful against a certain Yokai who lives in the water.", "Count": 2, "Healing": 2, "Yokai": ["Kappa"]})
    # players[0].healItems.append(heal[0])
    # players[0].curseItems.append({"name": "Picture with needles", "Info": "You have a picture of one of the other players. You can hinder their journey by sticking pins and needles into their limbs. This will injure them each turn until they go to a shrine.", "isHarmful": [True, -2], "selfHarm":[False, 0], "Count": 99, "category":"curse"})
    # players[0].curseItems.append(curses[1])
    # players[0].curseItems.append(curses[2])
    # players[1].weapons.append(weapons[0])
    # players[1].healItems.append(heal[0])

    # Right now assuming game over when one player reaches the end 
    while endReached is False: 
        print("Player", players[i].name, "turn \n")
        endReached = turn(players[i])
        if i == len(players)-1: 
            i = 0 
        else: 
            i+=1 
    
    # printItems(players[0], -1)
    # combat(0, players[0])
    
    # getItem(players[0])
    # printItems(players[0], -1)
    # printWeapons(players[0])
    
    # print("Player 0's curse:", players[0].curseItems[0])
    # print("Player 1's weapon (orig):")
    # printWeapons(players[1])
    
    # print("\n\n\n")
    
    # inflict(players[0], 0, players[1])
    # print("Player 1's conditions:", players[1].conditions)
    # print("\n\n")
    # print("player 0's weapons:")
    # printWeapons(players[0])
    # print("player 1's weapons:")
    # printWeapons(players[1])
    
    # inflict(players[0], 1, players[1])
    # print(players[1].conditions)
    # printItems(players[0], -1)
    # printItems(players[1], -1)
    
    # print("Game over!")
    


    pass

################################################################################
# HELPER FUNCTIONS
################################################################################

def rollDice(sides):
    num = random.randint(1, sides)
    return num

def turn(player):
    print("Current Health: ", player.health)

    endReached = False
    
    if player.playerTile == -1 and player.inShrine[1] > 0: 
        if player.inShrine[1] > 1: 
            print("You continue to regain your strength..")
            player.health = 12
                
        player.inShrine = (player.inShrine[0], player.inShrine[1]-1)

    # shrine --> player visiting 
    elif player.inShrine[0] is True:
        if player.inShrine[1] > 1: 
            print("You continue to regain your strength..")
            player.health = 12
            
        else: 
            if len(player.conditions) > 0: 
                player.conditions.clear()
                print("You feel your various ailments fade away.")
            
            input("Press enter key to roll to heal [D6] ")
            recover = rollDice(6)
            print("You recover ", recover, " health.")  # maybe change later

            if (player.health + recover) > 30:
                print("Your new total health is ", 30)
                player.health = 30 
            else: 
                print("Your new total health is ", player.health + recover)
                player.health = player.health + recover
                
        player.inShrine = (player.inShrine[0], player.inShrine[1]-1)
        

    else:
        input("Press enter key to roll the die [D6] ")
        movement = rollDice(6)
        print("\nYou move ", movement, " spaces!")

        player.playerTile += movement

        if player.playerTile < len(occupancyMap):

            if occupancyMap[player.playerTile] == 10:
                shrineChoice = int(input("You have reached a shrine. Will you choose: to stay [1] or leave [2]? "))
                if shrineChoice == 1:
                    player.inShrine = (True, 1)
                    player.lastShrine = player.playerTile 

                else:
                    print("You will continue onwards.")
            else:
                print("You see something ahead..")
                dieNum = rollDice(6)
                if dieNum == 1 or dieNum == 2:
                    print("It was just the wind")
                elif dieNum == 3 or dieNum == 4:
                    combat(player.playerTile, player)
                else:
                    print("What's this? A new item?")
                    getItem(player)
        
        else: 
            print("Congrats! You reached the end!")
            endReached = True 
            return endReached

    if len(player.conditions) != 0: 
        print("\nYou have been inflicted with various ailments..")
        conddmg = 0
        for i in player.conditions: 
            conddmg += i 
        print("You have been dealt ", conddmg, " damage!")
        player.health -= conddmg
        if player.health <= 0: 
            print("\nYou need to go see a doctor! (Head to the last shrine you've visited; if none: head to Start)")
            player.playerTile = player.lastShrine 
            
            if player.playerTile == -1: 
                player.inShrine = (False,2)
            else: 
                player.inShrine = (True, 2)

          
    
    notCmbt = int(input("\nIs there anything else you want to do? Check Items[0], Check Weapons[1], No[2] "))
    
    if notCmbt == 0: 
        useChoice = int(input("\nWould you like to see all [-1], healing items [0], curses [1], or exit [2]? "))
        if useChoice != 2: 
            if printItems(player, useChoice) != 1: 
                useItm = input("Would you like to use an item? [Y/N]")
                if useItm == "Y":
                    typeItm = input("Select what type of item you would like to use: [Input code from above or -1 to Exit]")
                    if typeItm != -1: 
                        if useChoice == -1: 
                            if typeItm[0] == 'H': 
                                print("You have chosen to use: ", player.healItems[int(typeItm[1:])])
                                
                                recover = player.healItems[int(typeItm[1:])]["Healing"]
                                print("You recover ", recover, " health.")
                                
                                if (player.health + recover) > 30:
                                    print("Your new total health is ", 30)
                                    player.health = 30 
                                else: 
                                    print("Your new total health is ", player.health + recover)
                                    player.health = player.health + recover
                                
                                del player.healItems[int(typeItm[1:])]
                                
                            else: 
                                print("You have chosen to use: ", player.curseItems[int(typeItm[1:])])
                                print("Choose which player to inflict the curse upon: \n")
                                for i in len(range(players)):
                                    print("Player [",i,"]")
                                inflictChoice = int(input(""))
                                inflict(player, int(typeItm[1:]), players[inflictChoice])
                                
                        elif useChoice == 0: 
                            print("You have chosen to use: ", player.healItems[int(typeItm)])
                            
                            recover = player.healItems[int(typeItm)]["Healing"]
                            print("You recover ", recover, " health.")
                            
                            if (player.health + recover) > 30:
                                print("Your new total health is ", 30)
                                player.health = 30 
                            else: 
                                print("Your new total health is ", player.health + recover)
                                player.health = player.health + recover
                            
                            del player.healItems[int(typeItm)]
                            
                        else: 
                            print("You have chosen to use: ", player.curseItems[int(typeItm)])
                            print("Choose which player to inflict the curse upon: \n")
                            for i in len(range(players)):
                                print("Player [",i,"]")
                            inflictChoice = int(input(""))
                            inflict(player, int(typeItm[1:]), players[inflictChoice])
            
        # should have a way to aslo see if they want to see the weapons?? 
    elif notCmbt == 1: 
        printWeapons(player)   
        # should have a way to aslo see if they want to see the items??    

    if player.inShrine[1] == 0: 
        player.inShrine = (False, player.inShrine[1]) 
    
    print("\nEnd of Turn\n")
    return endReached
    pass


def combat(tileNumber, player):
    
    regions = {1: waterYokai, 2: forestYokai, 3: outskirtsYokai, 4: cityYokai}

    currentRegion = regions[occupancyMap[tileNumber]]
    monster = random.randint(1, len(currentRegion))-1
    print(currentRegion[monster]["Intro"])
    print("A ", currentRegion[monster]["name"], " has appeared!")
    originalHealth = currentRegion[monster]["Health"]
        
    # playerDC = rollDice(20)
    
    prevChoices = [0,0]
    
    while (player.health > 0 and currentRegion[monster]["Health"] > 0):
        
        print("\nMonster's Current Health: ", currentRegion[monster]["Health"], "\nPlayer's current health: ", player.health, "\n")
        
        if prevChoices[0]== 0 and prevChoices[1] == 0: 
            playerChoice = int(input("What will you do? Attack[0], Talk[1], Run[2] "))
        elif prevChoices[0]== 1 and prevChoices[1] == 0: 
            playerChoice = int(input("What will you do? Attack[0], Run[2] "))
        elif prevChoices[0]== 0 and prevChoices[1] == 1: 
            playerChoice = int(input("What will you do? Attack[0], Talk[1] "))
        else: 
            playerChoice = int(input("What will you do? Attack[0] "))
    
        if playerChoice == 0: 
            prevChoices[0] = 1
            attack(player, currentRegion[monster])            
            
        elif playerChoice == 1:
            print("You attempt to talk with the yokai before you... will you be successful in conversing?\n")
            input("Press enter key to roll the die [D20] ")
            playerDC = rollDice(20)
            # playerDC = 20
            print("You rolled a ", playerDC, "!\n")
            if playerDC >= currentRegion[monster]["DC"]:
                print("You are successful in talking!")
                print(currentRegion[monster]["Convo"])
                convoResponse = input("[Y/N] ")
                
                if convoResponse == "Y":
                    print(currentRegion[monster]["CYes"][0])
                    if currentRegion[monster]["CYes"][1][0] == "P":
                        player.health -= currentRegion[monster]["CYes"][1][1]
                        # print(player.health)
                    else: 
                        monster.health -= currentRegion[monster]["CYes"][1][1]
                        # print(monster.health)
                else: 
                    print(currentRegion[monster]["CNo"][0])
                    if currentRegion[monster]["CNo"][1][0] == "P":
                        player.health -= currentRegion[monster]["CNo"][1][1]
                        # print(player.health)
                    else: 
                        monster.health -= currentRegion[monster]["CNo"][1][1]
                        # print(monster.health)

            else: 
                print("Unfortunately the yokai does not seem interested in talking..")
                prevChoices[0] = 1
            
        elif playerChoice == 2: 
            print("You try your best to get out of the situation.. hopefully you can slip away unnoticed..")
            input("Press enter key to roll the die [D20] ")
            playerDC = rollDice(20)
            print("You rolled a ", playerDC, "!\n")
            if playerDC >= currentRegion[monster]["Run"]:
                print("You are able to run away!")
                currentRegion[monster]["Health"] = 0 
                runSpace = rollDice(4)
                print("[You must move back ", runSpace, " spaces.]")
                player.playerTile = runSpace
            else: 
                print("The monster catches you attempting to escape! [You are unable to run]")
                prevChoices[1] = 1
        
    if player.health <= 0:
        print("\nYou need to go see a doctor! (Head to the last shrine you've visited; if none: head to Start)")
        player.playerTile = player.lastShrine 
            
        if player.playerTile == -1: 
            player.inShrine = (False, 2)
        else: 
            player.inShrine = (True, 2)

    else: 
        print("\nCongrats! You were able to defeat the yokai.")
        currentRegion[monster]["Health"] = originalHealth
        
    
    pass

def attack(player, monster):
    
    # print("Monster's Current Health: ", monster["Health"], "\nPlayer's current health: ", player.health, "\n")
    
    plyAtk = int(input("You chose to attack! Would you like to use an item [0], weapon [1], or attack with your bare hands[2]? "))
    if plyAtk == 0: 
        if printItems(player, 0) == -1: 
            typeItm = int(input("Select what type of item you would like to use: [Input code from above] "))
            usrHeal = input("Is this item for yourself? [Y/N] ")
            
            if usrHeal == "Y": 
                # print("use heal")
                recover = player.healItems[typeItm]["Healing"]
                print("You recover ", recover, " health.")
                
                if (player.health + recover) > 30:
                    print("Your new total health is ", 30)
                    player.health = 30 
                else: 
                    print("Your new total health is ", player.health + recover)
                    player.health = player.health + recover
                
                del player.healItems[typeItm]

            else: 
                print("Confirmation that you want to use ", player.healItems[typeItm]["name"] ," on the yokai. [Y/N]")
                confirmation = input()
                if confirmation == "Y": 
                    if monster["name"] in player.healItems[typeItm]["Yokai"]:
                        monster["Health"] = 0 
                        print(monster[player.healItems[typeItm]["name"]])
                        # return from here?? 
                        return 
                    else:
                        print("The item was unable to be used on the Yokai.")
                        
    elif plyAtk == 1: 
        if printWeapons(player) == -1:  
            typeItm = int(input("Select what type of item you would like to use: [Input code from above] "))
            
            if monster["name"] in player.weapons[typeItm]["Yokai"]:
                monster["Health"] = 0 
                print(monster[player.weapons[typeItm]["name"]])
                return
                
            monster["Health"] -= player.weapons[typeItm]["ATK"]
            print("You deal ",player.weapons[typeItm]["ATK"]," points of damage!")
                
    elif plyAtk == 2: 
        print("You attempt to attack with your bare hands! You deal 3 points of damage!")
        monster["Health"] -= 3
        
        pass 
    else: 
        print("You do not have any usable items!")
    
    if monster["Health"] != 0:
        print("Now it is the yokai's turn to attack..\n")
        yokaiAttack = random.randint(0, 2)
        print(monster["attacks"][yokaiAttack])
        player.health -= monster["attackDMG"][yokaiAttack]
        print("\nThe yokai attacks you for,", monster["attackDMG"][yokaiAttack], " damage!")
    else: 
        print(monster["DefeatATK"])
    
    pass

def getItem(player): 
   
    availableItems = []

    for i in heal:
        if i["Count"] > 0: 
            availableItems.append(i) 
    for i in curses: 
        if i["Count"] > 0: 
            availableItems.append(i)  
    for i in weapons: 
        if i["Count"] > 0: 
            availableItems.append(i)     
    
    playerItem = random.randint(0, len(availableItems)-1)
    
    
    # code below for saying PC can only have one of each item
    # I think it's fine to have multiple.. maybe 
    
    # while True: 
    #     playerItem = random.randint(0, len(availableItems)-1)
    #     print(availableItems[playerItem])
    #     inHeal = type(next((item for item in player.healItems if item["name"] == availableItems[playerItem]["name"]), False)) is dict
    #     inCurses = type(next((item for item in player.curseItems if item["name"] == availableItems[playerItem]["name"]), False)) is dict
    #     inWeapons = type(next((item for item in player.weapons if item["name"] == availableItems[playerItem]["name"]), False)) is dict
        
        
    #     if inHeal == False and inCurses == False and inWeapons == False:
    #         break 
   
    if availableItems[playerItem]["category"] == "heal":
        player.healItems.append(availableItems[playerItem])
    elif availableItems[playerItem]["category"] == "curse":
        player.curseItems.append(availableItems[playerItem])
    else: 
        player.weapons.append(availableItems[playerItem])
    
    print("\nYou have found a", availableItems[playerItem]["category"], ":", availableItems[playerItem]["name"], "!\n")
    
    # return availableItems[playerItem] 
    
    pass 

# maybe can optimize this and weapons since everything is it's own list now.. 
def printItems(player, itmType):
    if itmType == -1: 
        if len(player.healItems) == 0 and len(player.curseItems) == 0: 
            print("You have no items currently!")
            return 1

        for i in range(len(player.healItems)):
            print("[H"+str(i)+"] ", player.healItems[i]["name"], ":", player.healItems[i]["Info"])
        
        for i in range(len(player.curseItems)):
            print("[C"+str(i)+"] ", player.curseItems[i]["name"], ":", player.curseItems[i]["Info"])
            
            
    elif itmType == 0: 
        if len(player.healItems) == 0: 
            print("You have no items currently!")
            return 1 
        
        for i in range(len(player.healItems)):
            print("["+str(i)+"] ", player.healItems[i]["name"], ":", player.healItems[i]["Info"])

    elif itmType == 1: 
        if len(player.curseItems) == 0: 
            print("You have no items currently!")
            return 1 
        
        for i in range(len(player.curseItems)):
            print("["+str(i)+"] ", player.curseItems[i]["name"], ":", player.curseItems[i]["Info"])
            
    return -1
    pass 

# separated into a new func in case decide to change data structure 
def printWeapons(player):
    if len(player.weapons) == 0: 
            print("You have no weapons currently!")
            return 1
        
    for i in range(len(player.weapons)):
        print("["+str(i)+"] ", player.weapons[i]["name"], ":", player.weapons[i]["Info"])
        
    return -1 

def inflict(player, item, target):
    if player.curseItems[item]["isHarmful"][0] == True: 
        target.conditions.append(player.curseItems[item]["isHarmful"][1])
    else: 
        if player.curseItems[item]["isHarmful"][1] == "weapon" and len(target.weapons) != 0: 
            weaponRand = random.randint(0, len(target.weapons)-1)
            player.weapons.append(target.weapons[weaponRand])
            
            if target.weapons[weaponRand]["name"] == "Sword of Kusanagi":
                target.conditions.append(-10)
            
            del target.weapons[weaponRand]
            
        elif player.curseItems[item]["isHarmful"][1] == "heal" and len(target.healItems) != 0:
            healRand = random.randint(0, len(target.healItems)-1)
            # print(healRand)
            player.healItems.append(target.healItems[healRand])
            
            del target.healItems[healRand]
            
        elif player.curseItems[item]["isHarmful"][1] == "other" and len(target.healItems) != 0:
            currentTile = player.playerTile
            player.playerTile = target.playerTile
            target.playerTile = currentTile
            
        else:
            print("Your curse dissipates and nothing happens. It would seem your target does not possess what you desire.")
    
    # for curses that have a backlash 
    if player.curseItems[item]["selfHarm"][0] == True:
        player.conditions.append(player.curseItems[item]["selfHarm"][1])
    
    del player.curseItems[item]
    
    pass 

if __name__ == "__main__":
    main()
