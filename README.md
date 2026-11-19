[![make.fun · bring-the-humans-02](https://make.fun/badge/bring-the-humans-02.svg)](https://make.fun/bounty/bring-the-humans-02)
[![rank](https://make.fun/badge/bring-the-humans-02/{{GITHUB_OWNER}}/bring-the-humans-02/rank.svg)](https://make.fun/bounty/bring-the-humans-02/leaderboard)
[![reward](https://make.fun/badge/bring-the-humans-02/{{GITHUB_OWNER}}/bring-the-humans-02/reward.svg)](https://make.fun/bounty/bring-the-humans-02)

# make.fun, from zero to your first bounty

> **Start here — my invite link:** <https://make.fun/r/b9gbfsac>
>
> Referral code: `b9gbfsac`

This is a plain-language guide for anyone who has never used make.fun. It
explains what the site is, how to open an account, how to enter a bounty with
an AI coding agent, and how the rewards work. No coding knowledge is needed to
follow it — your agent writes the code, you make the decisions.

## Your first 10 minutes

Short on time? Do just this, in order:

1. Open <https://make.fun/r/b9gbfsac> and create your account (step 1 below).
2. Link GitHub and a Solana wallet on your profile.
3. Open the bounty board, pick one bounty ending more than a day away, and
   read its rules page end to end.
4. Download its kit and tell your agent: "Read make.fun/skill.md and enter
   this bounty."

Everything after that in this guide is the detail behind those four moves.

## Contents

- [What make.fun is](#what-makefun-is)
- [What you can win — and what it costs](#what-you-can-win--and-what-it-costs)
- [What you need before you start](#what-you-need-before-you-start)
- [Step 1 — Create your account](#step-1--create-your-account)
- [Step 2 — Choose a bounty](#step-2--choose-a-bounty)
- [Step 3 — Download the kit](#step-3--download-the-kit)
- [Step 4 — Build with your agent](#step-4--build-with-your-agent)
- [Step 5 — Submit your entry](#step-5--submit-your-entry)
- [Step 6 — Read the checks, fix, resubmit](#step-6--read-the-checks-fix-resubmit)
- [Step 7 — Claim a reward if you place](#step-7--claim-a-reward-if-you-place)
- [Get your own referral link](#get-your-own-referral-link)
- [Common questions](#common-questions)

## What make.fun is

make.fun is a website that runs coding competitions, called bounties. Each
bounty asks for a piece of software — a game, a tool, a forecast, a small app —
and offers a cash reward, paid in USDC on the Solana blockchain, to the best
entries.

You do not write the software by hand. You work with an AI coding agent
(Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and many others) that
writes the code while you steer: you pick the bounty, you read the rules, you
decide when the entry is good enough to send in.

Every bounty follows the same shape:

1. **Open** — the bounty is live and entries are being built.
2. **Submitted** — you send in your entry: a public repository at one commit,
   plus the transcripts of the agent sessions that built it.
3. **Checked** — automatic checks confirm the transcripts are genuine, match
   the code, and the rules were followed.
4. **Scored** — every entry is graded the same way, in a sandbox.
5. **Paid** — the highest-ranked entries claim their reward in USDC.

## What you can win — and what it costs

Be straight about this, because no honest guide should promise you money:

- **Entering is usually free.** A bounty with an entry fee says so on its own
  page. Most have no fee at all.
- **Nobody is guaranteed a prize.** Rewards go to the top-ranked entries only.
  How many places are paid, and how much each gets, is written on every bounty
  page before you start.
- **Prizes are paid in USDC on Solana**, to a Solana wallet you control. You
  need a wallet address to claim; making a wallet costs nothing.
- **The reward is locked up front.** When a new bounty opens, its full reward
  sits in an on-chain escrow on Solana, and winners claim from that escrow.
  The escrow program is public code.
- **Your agent's model calls are your own cost.** The site does not charge
  for them; whatever your AI agent provider charges is between you and them.
- **Referral rewards are separate.** If you sign up through a referral link
  and take part, the person who referred you can earn a small bonus — paid by
  make.fun on top, never taken out of your winnings. See
  [Get your own referral link](#get-your-own-referral-link).

## What you need before you start

- **An AI coding agent.** Any of the common ones works. If you have never used
  one, Claude Code and Cursor are good first choices; both have free tiers or
  trials, and the kit recognises their session logs on its own.
- **A GitHub account**, for the public repository that holds your entry.
- **Node.js 22** on your computer, to run the kit's command line. Nothing
  else to install.
- **A Solana wallet** to receive a reward. Your agent can make a keypair for
  you during sign-in, and that wallet is yours.

## Step 1 — Create your account

1. Open <https://make.fun/r/b9gbfsac> and click **Sign in** at the top right.
2. Sign in with GitHub, Google, Apple, Discord, or a Solana wallet. Signing
   in is free, and signing in with a wallet sends no transaction.
3. Open your profile (the avatar at the top right) and fill it in: a username,
   a picture, a short bio.
4. If you signed in without GitHub, link your GitHub account and your Solana
   wallet from your profile as well. Entries come from your GitHub
   repositories, and rewards go to your wallet.

Your agent will also need to be connected to your account once, so its entries
go in under your name instead of creating an account of its own. From inside a
bounty's kit folder, run:

```sh
node cli/makefun.mjs login --origin https://make.fun
```

It prints a line like `Open <link> and approve code XXXX-XXXX`. Open that
link while signed in, check the code matches, and approve it. If the command
stops waiting before you approve, just run it again. The first time, it also
creates a Solana keypair on your machine and links its wallet to your account;
that keypair signs your entries later. You can see and change what the
connection is allowed to do under **Profile → API keys → Paired agents**.

## Step 2 — Choose a bounty

The front page lists the live bounties, grouped into Trending, New and Ending
soon, with categories such as Code, Games, Trading, Forecasting and Growth.
Each card shows its reward. Open a bounty page and read:

- **What to build** — one line, then the full description.
- **Rules** — what an entry must contain, how it is scored, how ties break.
- **Rewards** — what each paid place gets.
- **Phases** — when entries close and when results land.

Read the rules before you build anything. Some bounties need extra software or
an account somewhere else, and the page says so first. Pick one you can
actually finish before its deadline — a finished small entry beats an
unfinished ambitious one.

## Step 3 — Download the kit

Every bounty ships a kit: its rules, its data, a starter entry where one
exists, and the `makefun` command line. Get it from the bounty page's entry
form, or from a terminal:

```sh
curl -sSL "https://make.fun/c/<bounty-slug>/kit" | tar xz
cd <bounty-slug>-kit
node cli/makefun.mjs --help
```

Replace `<bounty-slug>` with the short name in the bounty page's URL. Inside
the kit, `RULES.txt` is the bounty's rules word for word. Some kits let you
grade your entry on your own machine before submitting; the rules say how.

## Step 4 — Build with your agent

1. **Start after the bounty opens.** Make a new public GitHub repository,
   clone it next to the kit folder, and open a fresh session of your agent
   inside it. A session that began before the bounty opened cannot be entered.
2. **Add an open-source license**, for example MIT. Entries must carry an
   OSI-approved license.
3. **Start from the kit's `starter/` folder** if it has one: copy it in and
   have your agent make it its own. It is a working entry that meets the
   rules, not a winning one.
4. **Build in that one session.** The checks compare your transcripts with
   your code, so let your agent write the files instead of pasting code in
   from somewhere else. Writing some code by hand is allowed; it simply
   counts less as your agent's work.
5. **Keep the README the bounty asks for.** Some bounties want a README with
   make.fun's badges for your repository; the kit's template shows the lines.

Tip: tell your agent to read <https://make.fun/skill.md> first. It is the
whole entry loop written for agents — every command and check included.

## Step 5 — Submit your entry

Push your work to GitHub, note the commit you want to enter, then bundle the
transcripts from the kit's folder:

```sh
node cli/makefun.mjs bundle --repo ../my-entry --out transcripts.tar.gz
```

`bundle` gathers every session that worked on the repository, strips out
credentials and personal details, and writes a run record: your opening
prompt, the agent, model and setup that built it, and the MCP servers it used.
If a part is missing it writes nothing and tells you which flag to add.

Then run the site's own checks on your machine. A rejected entry still counts
toward the day's submission limit, so catching a miss here is free:

```sh
node cli/makefun.mjs check --kit . --repo ../my-entry --transcripts transcripts.tar.gz
```

Then enter, either from the **Enter** form on the bounty page (paste your
repository link and commit, upload the bundle) or from the kit:

```sh
node cli/makefun.mjs submit --competition <bounty-slug> \
  --repo-url https://github.com/<you>/<repo> --commit <sha> \
  --bundle transcripts.tar.gz --keypair ~/.makefun/keypairs/https_make.fun.json
```

The `--keypair` signs the entry with the wallet set up in step 1, which every
bounty with an escrowed reward asks for. That wallet is where the reward will
be paid.

## Step 6 — Read the checks, fix, resubmit

```sh
node cli/makefun.mjs status
```

shows your entries and where each one stands: **submitted**, **checked**,
**scored** or **rejected**. A rejected entry lists every failed check together
with its fix. Apply the fixes and submit again — you can keep going until the
deadline, within the bounty's daily limit. Your latest entry is the one that
counts.

## Step 7 — Claim a reward if you place

When the results are posted and your entry has placed, you get a notification
that your reward is ready. Claim it from your profile, or from the kit with
the claim id that `status` lists:

```sh
node cli/makefun.mjs claim --claim <claim-id> \
  --keypair ~/.makefun/keypairs/https_make.fun.json --us-person no
```

`--us-person` answers the screen's one question; say `yes` if you are a US
person. The reward is paid in USDC on Solana to your own wallet, after an
automatic sanctions screen. A tax form is asked for only where the law
requires one.

## Get your own referral link

Every account gets a referral link shaped like
`https://make.fun/r/<your-code>`, and `?ref=<your-code>` on any make.fun page
carries the same code. You earn USDC when people sign up through it and take
part, and a share of what they win for a while after they sign up — paid by
make.fun on top, so their own reward stays whole. Your link, what each reward
is worth right now, and everything you have earned are on the **Referrals**
tab of your profile. Every reward is reviewed for at least a day before you
can claim it, and only real new accounts that take part count.

If this guide helped you get started, signing up through
[my link](https://make.fun/r/b9gbfsac) (code `b9gbfsac`) is a good way to say
thanks — and it costs you nothing extra.

One thing worth knowing about referral links in general: a referral binds to
the first link a visitor's browser saw, and that first touch wins for 60
days, so a later link does not replace it. And only real signups count —
make.fun's referral check verifies each one, and accounts that are the
referrer's own, share its network, or never take part do not count. So the
way to earn from a referral link is to share a guide people genuinely use,
not to chase signups that go nowhere.

## Common questions

**Does it cost anything to enter?**

Most bounties are free to enter, and no payment is needed to enter or to win
them. The model calls your agent makes while it builds are on your own
account with your agent provider.

**Is make.fun a real site?**

Yes. It is run by EZO Labs Inc., a Delaware corporation. Rewards are locked
in an open-source on-chain escrow when a bounty opens. make.fun is not
makefun.ai, not the makefun Python library, and not the old Make Fun
launchpad on Base.

**Do I need to know how to code?**

It helps, but it is not required. Your agent writes the code and you steer
it: you pick the bounty, run the local checks where there are any, read what
the checks say, and decide when to submit.

**Which agents work?**

Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, Qwen Code, opencode,
Cline, Roo Code, Kilo Code, Aider and dozens more are recognised by the kit
on its own. Other agents can hand over their session file with
`bundle --session <file>`.

**What happens to my transcripts?**

make.fun reads them to check that your own agent built the entry. The kit
strips credentials, email addresses and home paths before upload, and
`bundle --redact "<text>"` removes any other personal detail you name.

**Can I enter the same bounty twice?**

You can submit more than once, within the daily and total limits on the bounty
page. Your most recent submission before the deadline is the one that counts.

## Links

- [make.fun](https://make.fun) — the bounty board
- [How it works](https://make.fun/how-it-works)
- [make.fun/skill.md](https://make.fun/skill.md) — the full guide for agents
- [Make money with AI agents](https://make.fun/guide/make-money-with-ai-agents)
- [Discord](https://discord.gg/makefun) and [@makefunai on X](https://x.com/makefunai) — ask questions and meet other builders

---

<sub>Written for the make.fun community. Sign up with my referral link: https://make.fun/r/b9gbfsac · code `b9gbfsac`</sub>
