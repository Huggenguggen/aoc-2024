# Day 19 (2024)

`Linen Layout` ([prompt](https://adventofcode.com/2024/day/19))

Every towel at this onsen is marked with a pattern of colored stripes. There are only a few patterns, but for any particular pattern, the staff can get you as many towels with that pattern as you need. Each stripe can be white (w), blue (u), black (b), red (r), or green (g). So, a towel with the pattern ggr would have a green stripe, a green stripe, and then a red stripe, in that order. (You can't reverse a pattern by flipping a towel upside-down, as that would cause the onsen logo to face the wrong way.)

The Official Onsen Branding Expert has produced a list of designs - each a long sequence of stripe colors - that they would like to be able to display. You can use any towels you want, but all of the towels' stripes must exactly match the desired design. So, to display the design rgrgr, you could use two rg towels and then an r towel, an rgr towel and then a gr towel, or even a single massive rgrgr towel (assuming such towel patterns were actually available).

To start, collect together all of the available towel patterns and the list of desired designs (your puzzle input). For example:
```
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
```

The first line indicates the available towel patterns; in this example, the onsen has unlimited towels with a single red stripe (r), unlimited towels with a white stripe and then a red stripe (wr), and so on.

After the blank line, the remaining lines each describe a design the onsen would like to be able to display. In this example, the first design (brwrr) indicates that the onsen would like to be able to display a black stripe, a red stripe, a white stripe, and then two red stripes, in that order.

Not all designs will be possible with the available towels. In the above example, the designs are possible or impossible as follows:

brwrr can be made with a br towel, then a wr towel, and then finally an r towel.
bggr can be made with a b towel, two g towels, and then an r towel.
gbbr can be made with a gb towel and then a br towel.
rrbgbr can be made with r, rb, g, and br.
ubwu is impossible.
bwurrg can be made with bwu, r, r, and g.
brgr can be made with br, g, and r.
bbrgwb is impossible.

## Part 1
To get into the onsen as soon as possible, consult your list of towel patterns and desired designs carefully. How many designs are possible?

### Approach
Break into sub-problems and use caching/memoizing

## Part 2
The staff don't really like some of the towel arrangements you came up with. To avoid an endless cycle of towel rearrangement, maybe you should just give them every possible option.

Here are all of the different ways the above example's designs can be made:

brwrr can be made in two different ways: b, r, wr, r or br, wr, r.

bggr can only be made with b, g, g, and r.

gbbr can be made 4 different ways:

g, b, b, r
g, b, br
gb, b, r
gb, br
rrbgbr can be made 6 different ways:

r, r, b, g, b, r
r, r, b, g, br
r, r, b, gb, r
r, rb, g, b, r
r, rb, g, br
r, rb, gb, r
bwurrg can only be made with bwu, r, r, and g.

brgr can be made in two different ways: b, r, g, r or br, g, r.

ubwu and bbrgwb are still impossible.

Adding up all of the ways the towels in this example could be arranged into the desired designs yields 16 (2 + 1 + 4 + 6 + 1 + 2).

### Approach
- same but use caching/memoize again