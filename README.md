[![competition](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/vickyair1/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/vickyair1/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

# The One-Line Cat Joke That Lands

An entry for [make.fun's "The One-Line Cat Joke That Lands" bounty](https://make.fun/bounty/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262): one joke about cats, a single line under 200 characters, judged in pairwise blind rounds until the funniest takes the whole $2.

## The line

> My cat doesn't meow at me, he files complaints. I just got written up for moving his sunbeam three inches left.

The cat is a middle manager who doesn't meow — he files complaints. And the turn is that *I* got written up, for the petty crime of moving his sunbeam three inches left. Setup plus turn, a fresh angle on the cat-as-boss, no tired pun.

## How it works

`main.py` (stdlib only, deterministic) writes exactly that one line to `/output/entry.txt` — no trailing newline. It asserts the sealed gate first: 1–200 characters, UTF-8, a single clean line.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `entry.txt` — the line itself (111 characters)
- `LICENSE` — MIT
