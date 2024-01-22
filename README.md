# LAB - Class 06

## Project: Ten Thousand

### Author: Lana Z

### Project Links
- [Ten Thousand](https://github.com/lana-z/ten-thousand)

### Resources
- Starter code, tests [Class-06](https://github.com/codefellows/seattle-code-python-401d24/tree/main/class-06/demo/parametrized-tests)
- ChatGPT
- Wikipedia [Dice 10000](https://en.wikipedia.org/wiki/Dice_10000)
- Collaboration with Kaitlyn for version planning and code review

## Setup

### AI 
A key component of this project is utlizing AI. 
Learn more about the initial prompts I created in [prompt.md](prompt.md)

### How to initialize/run your application
- Play the game: `python -m ten_thousand.game`

### Tests

- install and run `pytest` for tests found in ten-thousand/ten_thousand/[tests](https://github.com/lana-z/ten-thousand/tree/main/tests) 


### Log

- Sun: reviewed project requirements, set up files, initial prompts and code, tests passing
- Tues: added new testing files JB added to repo - 24 failing and 38 passing 
- Wed: solved for passing new calculation tests, except for 3 pairs, replaced correct score for 3 pairs to pass all Version_1 tests, collaborated with Kaitlyn to plan for lab 07, wrote game logic code based on simulations provided in Version_2 test folder. 
    - made it to bank_one_roll_then_quit sim, running correctly
- Thurs: 
    - roller branch: added roller for testing, and made adjustments to pass all v.2 tests
    - continue-rolling branch: broke everything. Will deal with it tomorrow. 
- Fri/Sun: 
    - went back to roller branch merge, didn't merge continue-rolling branch, and started fresh with hot-dice branch
    - 4 failing, 76 passing tests and several game functionality issues
    - commented out code for features that are causing other tests to fail
