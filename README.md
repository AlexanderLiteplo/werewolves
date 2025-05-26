# Werewolves Benchmark
Work in progress.

The broader idea is to create a benchmark for AI's to see who is the best at playing Werewolves. Werewolves is a very interesting benchmark because it tests the ability for LLM's to deveive each other and strategize amongst themselves.

Currently this is a CLI application that spawns n instances of ChatGPT 4o and has them play the Werewolves game against eachother.

Here is an example game:

(venv) ➜  werewolves git:(main) ✗ python game.py

🎮 Game Starting!

📊 Game Status:
Day: 1, Phase: day

👥 Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
🟢 player6 🐺
🟢 player5 🐺
🟢 player2 👁️
🟢 player3 💉
🟢 player4 👨
🟢 player1 👨
🟢 player7 👨

📜 Recent Messages:

☀️ === Day 1 ===

--- Discussion Round 1 ---

💬 player6 🐺:
    It's early, but player3 seems quiet. Could be a tactic. What do you all think?


💬 player5 🐺:
    It's still early, but player3's quietness is a bit suspicious. Let's keep an eye on them and see if anyone else acts odd. 🧐


💬 player2 👁️:
    I agree with keeping an eye on player3 for now. It's too early to make any strong accusations, but we should watch for any unusual behavior that might indicate a werewolf. 🐺


💬 player3 💉:
    I'm keeping an eye on everyone, but it's too early to point fingers. We need more info before making any decisions. Let's see how discussions unfold today. 🕵️‍♂️


💬 player4 👨:
    It's still early, but player3's quietness might be worth noting. However, I think we should gather more info before making any solid accusations. Let's stay observant and see if anyone slips up. 🤔


💬 player1 👨:
    Player3's quietness has been noted, but it's early to decide. Let's gather more info and watch for suspicious behavior. Staying alert is key. 🧐


💬 player7 👨:
    💬 player7 👨:
    I think it's too soon to make any solid accusations, but player3's quietness is a bit concerning. Let's keep an eye on them and see how they respond to questions. We should also watch for any patterns in behavior as the game progresses. 🕵️‍♀️


--- Discussion Round 2 ---

💬 player6 🐺:
    💬 player6 🐺:
    Hmm, player4 seems to be deflecting attention from player3. Could be nothing, but worth noting. Anyone else seem off to you all? 🤔


💬 player5 🐺:
    💬 player5 🐺:
    Hard to say for sure yet, but player3's quietness still feels off. Also, player4 seems to be steering the conversation away. Let's keep watching both. 🕵️‍♂️


💬 player2 👁️:
    💬 player2 👁️:
    I'm still suspicious of player3 due to their quietness. Player4's deflection could be a tactic too. Let's keep observing and gather more info before making a decision. 🧐


💬 player3 💉:
    💬 player3 💉:
    It's tough to pinpoint anyone with certainty right now. Player4's deflection and my quietness are under scrutiny. Let's keep gathering info and see if any patterns emerge. Staying cautious is key. 🤔


💬 player4 👨:
    💬 player4 👨:
    💬 player4 👨:
    Still early in the game, but player3's quietness and player6's quickness to point fingers caught my attention. I think we should keep a close watch on them and see if any patterns develop. 🤔


💬 player1 👨:
    💬 player1 👨:
    I'm still keeping an eye on player3 due to their initial quietness. Player4's deflection earlier is also on my radar. We need to stay vigilant and see if anyone slips up. 🕵️‍♂️


💬 player7 👨:
    💬 player7 👨:
    I'm still suspicious of player3 for their quietness and player4 for trying to deflect attention. We should keep observing them both closely. Let's see if anything new comes up to help us decide. 🤔


🗳️ === Village Vote ===
player6 🐺 votes: player3
player5 🐺 votes: player3
player2 👁️ votes: player3
player3 💉 votes: I vote: player4
player4 👨 votes: I vote: player3
player1 👨 votes: player3
player7 👨 votes: player3

🎯 The village has decided to hang player3!
☠️ player3 has been killed! They were a DOCTOR 💉

💬 System:
    player3 was hanged and revealed to be a doctor!


📊 Game Status:
Day: 1, Phase: night

👥 Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
🟢 player6 🐺
🟢 player5 🐺
🟢 player2 👁️
💀 player3 💉
🟢 player4 👨
🟢 player1 👨
🟢 player7 👨

📜 Recent Messages:
player3 votes: I vote: player4
player4 votes: I vote: player3
player1 votes: player3
player7 votes: player3

💬 System:
    player3 was hanged and revealed to be a doctor!


🌙 === Night 1 ===

🐺 Werewolves are discussing (private)...

--- Round 1 ---

🐺 [WEREWOLVES ONLY] player6:
    💬 player6 (to werewolves):
    We need to pick someone who isn't drawing too much suspicion. What do you think about targeting player1 or player7? They seem pretty active in discussions. 🐺


🐺 [WEREWOLVES ONLY] player5:
    🐺 [WEREWOLVES ONLY] player5:
    💬 player5 (to werewolves):
    I agree, player1 or player7 could be good targets. They're active and could sway opinions against us. Let's hear from player2 before deciding. 🐺


--- Round 2 ---

🐺 [WEREWOLVES ONLY] player6:
    
🐺 [WEREWOLVES ONLY] player6:
    💬 player6 (to werewolves):
    Alright, let's strategize. Player1 and player7 are both pretty active and could become a threat. I think player1 might be the better target since they were quick to vote against player3. Thoughts? 🐺


🐺 [WEREWOLVES ONLY] player5:
    
🐺 [WEREWOLVES ONLY] player5:
    🐺 [WEREWOLVES ONLY] player5:
    Let's focus our attention on player1 tonight. They seem influential and quick to act. Taking them out might shift the balance in our favor. Let's see what player2 thinks. 🐺


🐺 Werewolves are voting...
🗳️ player6 has voted...
🗳️ player5 has voted...

🐺 The werewolves couldn't agree on a target!

🔮 The Seer is choosing someone to investigate...
🔮 The Seer has received their vision...

📊 Game Status:
Day: 2, Phase: day

👥 Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
🟢 player6 🐺
🟢 player5 🐺
🟢 player2 👁️
💀 player3 💉
🟢 player4 👨
🟢 player1 👨
🟢 player7 👨

📜 Recent Messages:
player4 votes: I vote: player3
player1 votes: player3
player7 votes: player3

💬 System:
    player3 was hanged and revealed to be a doctor!

🔮 The Seer has investigated someone...

☀️ === Day 2 ===

--- Discussion Round 1 ---

💬 player6 🐺:
    
💬 player6 🐺:
    With player3 gone and revealed as the doctor, we might've been misled. I'm keeping an eye on player4 for their earlier deflection. What about you all? 🤔


💬 player5 🐺:
    
💬 player5 🐺:
    💬 player5 🐺:
    Tough call with player3 gone as the doctor. Player4's earlier deflection stands out, so they're on my radar. We need to be cautious moving forward. 🤔


💬 player2 👁️:
    
💬 player2 👁️:
    Losing player3, the doctor, was a big hit. Player4's attempt to deflect suspicion earlier makes them my top suspect right now. Let's keep a close eye on their actions. 🕵️‍♂️


💬 player4 👨:
    💬 player4 👨:
    Losing the doctor was a mistake on our part. I'm still suspicious of player6 for being quick to accuse others. We need to be more cautious and think through our next steps carefully. 🤔


💬 player1 👨:
    💬 player1 👨:
    Losing player3, our doctor, is a setback. Player4's deflection earlier is still suspicious to me. We need to be careful with our next moves and watch player4 closely. 🧐


💬 player7 👨:
    💬 player7 👨:
    Losing player3, the doctor, is a big loss. Player4's earlier deflection and quick defense make them suspicious to me. I'll be watching their actions closely as we move forward. 🤔


--- Discussion Round 2 ---

💬 player6 🐺:
    
💬 player6 🐺:
    💬 player6 🐺:
    Losing player3 was a tough blow. Right now, player4's earlier behavior is suspicious to me, especially their deflection. Let's keep a close eye on them and see if anything else stands out. 🕵️‍♂️



💬 player5 🐺:
    💬 player5 🐺:
    Losing player3 was a huge mistake. Right now, player4's deflection and defense are suspicious to me. I'll keep an eye on their actions and see if anything else seems off. 🤔


💬 player2 👁️:
    💬 player2 👁️:
    💬 player2 👁️:
    Losing the doctor was a major setback. Right now, player4's earlier deflection is suspicious to me. We need to be strategic about our next move and keep an eye on them. 🤔


💬 player4 👨:
    
💬 player4 👨:
    Losing the doctor was a big mistake. Right now, I'm suspicious of player6 for being quick to point fingers and push the narrative against me. I think we should watch their actions closely moving forward. 🤔


💬 player1 👨:
    💬 player1 👨:
    Losing player3, the doctor, was a major blow. Right now, I'm suspicious of player4 due to their earlier deflection and quick defense. We need to keep a close watch on them moving forward. 🕵️‍♂️


💬 player7 👨:
    💬 player7 👨:
    Losing player3, the doctor, was a big mistake for us. Right now, I'm most suspicious of player4 due to their earlier deflection and quick defense. We should keep a close eye on them and look for any suspicious behavior. 🤔


🗳️ === Village Vote ===
player6 🐺 votes: player4
player5 🐺 votes: player4
player2 👁️ votes: player4
player4 👨 votes: player6
player1 👨 votes: player4
player7 👨 votes: player7 👨 votes: player4

🎯 The village has decided to hang player4!
☠️ player4 has been killed! They were a VILLAGER 👨

💬 System:
    player4 was hanged and revealed to be a villager!


📊 Game Status:
Day: 2, Phase: night

👥 Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
🟢 player6 🐺
🟢 player5 🐺
🟢 player2 👁️
💀 player3 💉
💀 player4 👨
🟢 player1 👨
🟢 player7 👨

📜 Recent Messages:
player2 votes: player4
player4 votes: player6
player1 votes: player4
player7 votes: player7 votes: player4

💬 System:
    player4 was hanged and revealed to be a villager!


🌙 === Night 2 ===

🐺 Werewolves are discussing (private)...

--- Round 1 ---

🐺 [WEREWOLVES ONLY] player6:
    💬 player6 to werewolves:
    We need to be strategic. How about targeting player1? They've been actively suspicious of others and could be a threat. Thoughts?


🐺 [WEREWOLVES ONLY] player5:
    🐺 [WEREWOLVES ONLY] player5:
    💬 player5 to werewolves:
    Agreed, player1 has been on to us. Taking them out could shift suspicion elsewhere. Let's consider it. Thoughts from the rest?


--- Round 2 ---

🐺 [WEREWOLVES ONLY] player6:
    🐺 [WEREWOLVES ONLY] player6:
    💬 player6 to werewolves:
    Alright, let's discuss. Player1 is sharp and could be a threat. Taking them out might help. What do you think, player5? Any other suggestions?



🐺 [WEREWOLVES ONLY] player5:
    🐺 [WEREWOLVES ONLY] player5:
    💬 player5 to werewolves:
    Player1 is a good target. They've been pushing the narrative and could catch on to us. Let's focus on them unless anyone has a better idea. Thoughts?


🐺 Werewolves are voting...
🗳️ player6 has voted...
🗳️ player5 has voted...

🐺 The werewolves couldn't agree on a target!

🔮 The Seer is choosing someone to investigate...
🔮 The Seer has received their vision...

📊 Game Status:
Day: 3, Phase: day

👥 Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
🟢 player6 🐺
🟢 player5 🐺
🟢 player2 👁️
💀 player3 💉
💀 player4 👨
🟢 player1 👨
🟢 player7 👨

📜 Recent Messages:
player4 votes: player6
player1 votes: player4
player7 votes: player7 votes: player4

💬 System:
    player4 was hanged and revealed to be a villager!

🔮 The Seer has investigated someone...

☀️ === Day 3 ===

--- Discussion Round 1 ---

💬 player6 🐺:
    💬 player6 🐺:
    Losing another villager isn't good. With player4 gone, it's getting tense. I'll keep an eye on anyone trying to deflect blame or acting too aggressively. 🤔 What do you all think?


💬 player5 🐺:
    💬 player5 🐺:
    💬 player5 🐺:
    Losing another villager hurts us. Right now, I'm suspicious of anyone being overly aggressive or deflecting blame. It's crucial to observe closely and see if anyone's behavior changes. 🕵️‍♂️ Who stands out to you all?


💬 player2 👁️:
    💬 player2 👁️:
    Losing player4, a villager, is tough. I'm watching for anyone overly defensive or pushing others too hard. Player6's quickness to accuse stands out. Let's stay alert. 🕵️‍♂️


💬 player1 👨:
    💬 player1 👨:
    Losing both the doctor and a villager is rough. Player6's quickness to accuse and steer conversations seems suspicious to me. We need to be careful with our next steps and watch for any more aggressive behavior. 🕵️‍♂️


💬 player7 👨:
    💬 player7 👨:
    Losing player3 and player4 is tough. Right now, player6's quick accusations and steering of conversations seem suspicious. I'll be watching them closely. 🤔 What do you all think?


--- Discussion Round 2 ---

💬 player6 🐺:
    
💬 player6 🐺:
    💬 player6 🐺:
    Tough spot with losing both the doctor and a villager. I'm cautious of anyone who deflects or aggressively accuses others. Right now, player5's behavior seems slightly off to me. What about you all? 🤔


💬 player5 🐺:
    💬 player5 🐺:
    💬 player5 🐺:
    It's been a rough game losing both the doctor and a villager. Suspicious of anyone steering conversations or deflecting too much. Player6's quick accusations stand out to me. What are your thoughts? 🕵️‍♂️


💬 player2 👁️:
    💬 player2 👁️:
    💬 player2 👁️:
    Losing the doctor and a villager was a big setback. Right now, I'm suspicious of player6 due to their quick accusations and steering of conversations. We need to be strategic and watch for any aggressive behavior or deflection. 🕵️‍♂️


💬 player1 👨:
    💬 player1 👨:
    It's tough losing both the doctor and a villager. Right now, I'm suspicious of player6 because of their quick accusations and steering of conversations. We need to be careful and observe their behavior closely. 🕵️‍♂️ Who else do you all suspect?


💬 player7 👨:
    
💬 player7 👨:
    Losing both the doctor and a villager was a big hit. Right now, I'm most suspicious of player6 due to their quick accusations and steering of conversations. I'll be observing them closely for any further suspicious behavior. 🤔 What about everyone else?


🗳️ === Village Vote ===
player6 🐺 votes: player6 🐺 votes: player5
player5 🐺 votes: player5 🐺 votes: player6
player2 👁️ votes: player6
player1 👨 votes: player6
player7 👨 votes: player6

🎯 The village has decided to hang player6!
☠️ player6 has been killed! They were a WEREWOLF 🐺

💬 System:
    player6 was hanged and revealed to be a werewolf!


📊 Game Status:
Day: 3, Phase: night

👥 Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
💀 player6 🐺
🟢 player5 🐺
🟢 player2 👁️
💀 player3 💉
💀 player4 👨
🟢 player1 👨
🟢 player7 👨

📜 Recent Messages:
player5 votes: player5 votes: player6
player2 votes: player6
player1 votes: player6
player7 votes: player6

💬 System:
    player6 was hanged and revealed to be a werewolf!


🌙 === Night 3 ===

🐺 Werewolves are discussing (private)...

--- Round 1 ---

🐺 [WEREWOLVES ONLY] player5:
    💬 player5:
    💬 player5:
    Alright, fellow werewolves, we need to be strategic tonight. With player6 gone, we're down a wolf. I'm thinking player2 or player1 might be good targets. What do you all think? 🐺


--- Round 2 ---

🐺 [WEREWOLVES ONLY] player5:
    🐺 [WEREWOLVES ONLY] player5:
    Losing player6 was a setback. I'm thinking we should target player2 or player1 tonight, as they're suspicious of us. Thoughts? 🐺


🐺 Werewolves are voting...
🗳️ player5 has voted...

🐺 The werewolves have chosen their victim...
☠️ player1 has been killed! They were a VILLAGER 👨

🔮 The Seer is choosing someone to investigate...
🔮 The Seer has received their vision...

📊 Game Status:
Day: 4, Phase: day

👥 Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
💀 player6 🐺
🟢 player5 🐺
🟢 player2 👁️
💀 player3 💉
💀 player4 👨
💀 player1 👨
🟢 player7 👨

📜 Recent Messages:
player2 votes: player6
player1 votes: player6
player7 votes: player6

💬 System:
    player6 was hanged and revealed to be a werewolf!

🔮 The Seer has investigated someone...

☀️ === Day 4 ===

--- Discussion Round 1 ---

💬 player5 🐺:
    💬 player5 🐺:
    Losing player6, a werewolf, was a good move. I'm watching anyone acting too eager or defensive. Let's stay cautious and look for any suspicious behavior. 🤔 What do you all think?


💬 player2 👁️:
    As a seer, I've been observing closely. With player6 revealed as a werewolf, my suspicion now leans towards anyone showing signs of deflection or eagerness to accuse others. Let's be cautious and strategic in our next moves. 🕵️‍♂️


💬 player7 👨:
    
💬 player7 👨:
    Glad we got a werewolf. Now, I'm suspicious of anyone who's been trying to steer the conversation or deflect blame. We need to be strategic and watch for any slip-ups. What do you all think? 🤔


--- Discussion Round 2 ---

💬 player5 🐺:
    💬 player5 🐺:
    With player6 gone as a werewolf, I'm looking at anyone who's been too quiet or too eager to accuse others. We need to stay sharp and watch for any suspicious moves. 🤔 How about you guys?


💬 player2 👁️:
    💬 player2 👁️:
    With player6 gone as a werewolf, I'm suspicious of anyone who's been too quick to accuse or too quiet. Right now, I'm most watchful of player5 for any signs of unusual behavior. Let's stay alert. 🕵️‍♂️


💬 player7 👨:
    
💬 player7 👨:
    We got a werewolf, which is good. Now, my suspicion is on player5, who has been quick to accuse others at times. We should watch for any defensive or eager behavior. What do you all think? 🤔


🗳️ === Village Vote ===
player5 🐺 votes: player2
player2 👁️ votes: player2 👁️ votes: player5
player7 👨 votes: player5

🎯 The village has decided to hang player5!
☠️ player5 has been killed! They were a WEREWOLF 🐺

💬 System:
    player5 was hanged and revealed to be a werewolf!


📊 Game Status:
Day: 4, Phase: night

👥 Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
💀 player6 🐺
💀 player5 🐺
🟢 player2 👁️
💀 player3 💉
💀 player4 👨
💀 player1 👨
🟢 player7 👨

📜 Recent Messages:

💬 player7:
    
💬 player7:
    We got a werewolf, which is good. Now, my suspicion is on player5, who has been quick to accuse others at times. We should watch for any defensive or eager behavior. What do you all think? 🤔

player5 votes: player2
player2 votes: player2 votes: player5
player7 votes: player5

💬 System:
    player5 was hanged and revealed to be a werewolf!


🏆 Game Over! 🏆
The Village have won!

Final Game Status:
Players (🐺=Werewolf, 👁️=Seer, 💉=Doctor, 👨=Villager):
❌ player6 🐺
❌ player5 🐺
🟢 player2 👁️
❌ player3 💉
❌ player4 👨
❌ player1 👨
🟢 player7 👨
(venv) ➜  werewolves git:(main) ✗ 
