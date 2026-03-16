# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game when I first opend it looked fine, when I started playing the medium difficulty game, I started with 50 and progressively started going higher till I got to 99 and then it said wrong answer game over. When I checked the "Developer Debug Info" I understood that when it should have told me to go lower it told me to go higher essentially misguiding me.I would have expected it to properly guide me and tell me if I have to go higher or lower to actually find the number, not the other way around. Also, when I played around with it, it would let me put numbers outside of the range of 1-100. I was expecting it to say something like "Value out of range". Next, when I went to the harder difficulty, I could see that the range of numbers decreased, making it easier to find the answer, not harder (to make it harder the range of numbers should increase). 

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---

## 2. How did you use AI as a teammate?


I used Copilot AI for this project. I used Copilot AI to refactor the game logic into logic_utils.py, which was correct: we moved parse_guess and check_guess out of app.py, then verified by running python -m pytest -q and seeing the tests pass, and that fixed the guidance and range behavior, but early on the AI gave misleading hints like "Too High" -> "Go HIGHER!", which I verified by playing and seeing the direction was reversed, so that suggestion was incorrect until we fixed it.

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed by testing the exact failure mode and confirming it no longer happened in both code and gameplay; for example, I ran python -m pytest -q after adding tests in tests/test_game_logic.py (including parse_guess("10.5") now returns invalid and get_range_for_difficulty("Hard") returns a larger max than normal), and I also manually played the app to verify “Too High” now says “Go LOWER” and out-of-range guesses show an error without consuming attempts. AI helped design these tests by suggesting splitting logic into logic_utils.py and writing focused unit tests for parse/check/range behavior, which made it easy to verify the bug was fixed.

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

I learned that Stremlit reruns the whole script from the top to bottom on every single interaction that happenes, so that any non-session variable is reset unless it is saved. Session state acts like persistent memory for the interactive app. lost between reruns.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns are like re-running the app code on each user action, a state is a dictionary where we keep values so they don’t get 

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing small regression tests for each bug and running `pytest` after each fix so I can objectively verify behavior. I also want to keep the prompting strategy of asking the AI for exact broken line locations and then confirming with tests.

Next time with AI I would do more frequent manual verification early to catch misleading suggestions sooner, and then fix with tests immediately. This project showed me that AI-generated code can accelerate development, but I still need to validate and correct it carefully as a responsible developer.

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

A habbit I want to reuse in the future would be writing focused tests and using AI suggestions as a starting point, not a final solution. This project changed the way I think about AI generated code throough understanding that AI might not use the best way to write the code, it could have a extra 100 lines that are completely unnecessary and its my job to understand the edits it gives me to know if all the edits it is giving me is necessary.

- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
