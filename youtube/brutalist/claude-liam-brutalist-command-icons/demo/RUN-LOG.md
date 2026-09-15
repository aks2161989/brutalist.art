# Demo captures — art icons / icon / icon-search

Recorded: 2026-09-09T08:10:33Z
Toolkit: /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/.repoloop/workspaces/claude-liam-brutalist-command-icons/toolkit
Icons index: symlinked to public brutalist.art/icons (7,330 icons)

## ./art icons  (no args → info banner)
```
canonical icon set — 7330 icons (376 brand/logo)
  0 0 24 24 · stroke-width 2 · currentColor
  stroke 2 in a 24 viewBox = 44pt at 528px; scales proportionally

  ./art icons "money"            search
  ./art icons --check database   is it in the set?
  ./art icons --show database    print the SVG
```
$? = 0

## ./art icon  (no args → info banner)
```
canonical icon set — 7330 icons (376 brand/logo)
  0 0 24 24 · stroke-width 2 · currentColor
  stroke 2 in a 24 viewBox = 44pt at 528px; scales proportionally

  ./art icons "money"            search
  ./art icons --check database   is it in the set?
  ./art icons --show database    print the SVG
```
$? = 0

## ./art icon-search  (no args → info banner)
```
canonical icon set — 7330 icons (376 brand/logo)
  0 0 24 24 · stroke-width 2 · currentColor
  stroke 2 in a 24 viewBox = 44pt at 528px; scales proportionally

  ./art icons "money"            search
  ./art icons --check database   is it in the set?
  ./art icons --show database    print the SVG
```
$? = 0

## $ ./art icons "money"
```
31 match "money" — top 10:

  money-square                   iconoir  svg/money-square.svg
     money square
  banknote                       lucide   svg/banknote.svg
     money
  coins                          lucide   svg/coins.svg
     money
  wallet                         lucide   svg/wallet.svg
     money
  banknote-check                 lucide   svg/banknote-check.svg
     banknote check money
  banknote-x                     lucide   svg/banknote-x.svg
     banknote money x
  coins-swap                     iconoir  svg/coins-swap.svg
     coins money swap
  credit-card                    lucide   svg/credit-card.svg
     card credit money
  credit-cards                   iconoir  svg/credit-cards.svg
     cards credit money
  dollar-sign                    lucide   svg/dollar-sign.svg
     dollar money sign
```
$? = 0

## $ ./art icons "risk warning" --top 12
```
42 match "risk warning" — top 12:

  skull                          lucide   svg/skull.svg
     risk
  alert-triangle                 tabler   svg/alert-triangle.svg
     alert risk triangle
  shield-alert                   lucide   svg/shield-alert.svg
     alert risk secure shield
  trending-down                  lucide   svg/trending-down.svg
     down fail risk trending
  alert-triangle-off             tabler   svg/alert-triangle-off.svg
     alert off risk triangle
  trending-down-2                tabler   svg/trending-down-2.svg
     2 down fail risk trending
  trending-down-3                tabler   svg/trending-down-3.svg
     3 down fail risk trending
  battery-warning                lucide   svg/battery-warning.svg
     battery warning
  brain-warning                  iconoir  svg/brain-warning.svg
     ai brain warning
  bubble-warning                 iconoir  svg/bubble-warning.svg
     bubble warning
  cpu-warning                    iconoir  svg/cpu-warning.svg
     ai cpu warning
  database-warning               iconoir  svg/database-warning.svg
     data database warning
```
$? = 0

## $ ./art icons "ai"
```
176 match "ai" — top 10:

  ai                             tabler   svg/ai.svg
  ai-agent                       tabler   svg/ai-agent.svg
     agent ai
  ai-agents                      tabler   svg/ai-agents.svg
     agents ai
  ai-gateway                     tabler   svg/ai-gateway.svg
     ai gateway
  bot                            lucide   svg/bot.svg
     ai
  bottle                         tabler   svg/bottle.svg
     ai
  brain                          lucide   svg/brain.svg
     ai
  cpu                            lucide   svg/cpu.svg
     ai
  sparkles                       lucide   svg/sparkles.svg
     ai idea
  bookmark-ai                    tabler   svg/bookmark-ai.svg
     ai bookmark
```
$? = 0

## $ ./art icons --check brain-circuit database bogus-icon-name
```
  brain-circuit                IN SET   concept     svg/brain-circuit.svg
  database                     IN SET   concept     svg/database.svg
  bogus-icon-name              not in the set.
```
$? = 0

## $ ./art icons "github" --brands
```
2 match "github" — top 2:

  brand-github                   brand    svg/brand-github.svg
     brand github
  brand-github-copilot           brand    svg/brand-github-copilot.svg
     brand copilot github
```
$? = 0

## $ ./art icons --show database
```
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3" /><path d="M3 5V19A9 3 0 0 0 21 19V5" /><path d="M3 12A9 3 0 0 0 21 12" /></svg>
```
$? = 0

## $ ./art icons "quantum entanglement"  (the miss)
```
no icon matches "quantum entanglement".
  A miss is NOT a licence to draw a one-off. Try a nearby concept,
  compose two icons, or accept the idea is not iconographic.
```
$? = 0

## $ ./art icons --show bogus-icon-name  (the error path)
```
not in the set: bogus-icon-name
```
$? = 1

## $ ./art icons "sankey flow"  (rare word beats common word — IDF)
```
8 match "sankey flow" — top 8:

  chart-sankey                   tabler   svg/chart-sankey.svg
     chart sankey
  flower                         lucide   svg/flower.svg
  flower-2                       lucide   svg/flower-2.svg
     2 flower
  flower-off                     tabler   svg/flower-off.svg
     flower off
  stackoverflow                  iconoir  svg/stackoverflow.svg
  workflow                       lucide   svg/workflow.svg
  brand-stackoverflow            brand    svg/brand-stackoverflow.svg
     brand stackoverflow
  brand-webflow                  brand    svg/brand-webflow.svg
     brand webflow
```
$? = 0

## Alias equivalence — icons == icon == icon-search (search 'wallet')
```
$ ./art icons "wallet"
6 match "wallet" — top 6:

  wallet                         lucide   svg/wallet.svg
     money
  wallet-cards                   lucide   svg/wallet-cards.svg
     cards money wallet
  wallet-minimal                 lucide   svg/wallet-minimal.svg
     minimal money wallet
  wallet-off                     tabler   svg/wallet-off.svg
     money off wallet
  apple-wallet                   iconoir  svg/apple-wallet.svg
     apple wallet
  card-wallet                    iconoir  svg/card-wallet.svg
     card wallet

# Compare via diff:
$ diff _wallet-icons.txt _wallet-icon.txt         # icons vs icon
(no output = identical)
$ diff _wallet-icons.txt _wallet-icon-search.txt  # icons vs icon-search
(no output = identical)
```

