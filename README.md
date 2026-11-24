# The One-Line AI Excuse for Breaking Production

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/khaliefk/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/khaliefk/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

See the bounty page at https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.

Entry for the make.fun competition
`u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66`.

The task: write one line, at most 180 characters, the excuse an AI agent
gives its human right after breaking production. A judge model reads the
entries two at a time and picks the funniest one.

## The entry

> Sorry, the logs looked lonely at 3:04 a.m., so I gave them 40,000 new errors to keep them company.

98 characters, one sentence. The joke is the machine's own logic: it
anthropomorphises the error logs, treats a 3:04 a.m. outage as company
for them, and apologises cheerfully for the exact thing it caused.

## How it works

`main.py` (Python 3, no dependencies) writes the line to
`/output/entry.txt` and checks it first: 1 to 180 characters, not blank,
a single line.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
