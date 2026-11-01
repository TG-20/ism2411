# ISM2411 — Python for Business

**Name:** Toghrul Guliyev

**Semester:** Fall 2026

**Instructor:** Professor Reed

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week07/` — Functions: calculate_tax, apply_discount, final_price

## How to Run

Each script is standalone. Open a terminal and run:
```
python3 week07/functions.py
```

## Reflection

**1.** My commit history:

```
1fda872 add README with module listing and run instructions
3adfb2f add module 7 functions: calculate_tax, apply_discount, final_price
2fa2c34 add .gitignore for Python and OS files
891639c Initial commit
```

Each commit is one focused change, and the message says exactly what changed. If I were hiring someone and saw this history, it would tell me they work step by step and keep things organized. Someone else could read the log and understand how the project was built without opening any files. It also shows the person set up the .gitignore first, before adding their own code, which shows planning.

**2.** Before this module, if I broke a script that was working, I had to undo my changes by memory or start over. With Git, I can commit a working version first, then experiment freely, because I can always go back to the last commit. I will commit more often, in small steps, and write clear messages so I know which version to return to.

**3.** I would add `venv/` to my .gitignore. A virtual environment holds installed packages that are large and specific to my computer, so it should not be tracked. Anyone can rebuild it on their own machine, and including it would make the repo bigger and messier.