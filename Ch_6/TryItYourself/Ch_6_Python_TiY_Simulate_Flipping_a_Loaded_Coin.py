#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Simulate Flipping a Loaded Coin ####

# Importing necessary libraries
import pandas as pd
import random
from plotnine import ggplot, aes, geom_bar, facet_wrap, ylab, xlab, ggtitle, geom_segment, after_stat, ylim
random.seed(1234)

# Perform simulations
ns = [5, 10, 100, 1000] # Numbers of Flips
probs = [.7, .3] # Probability of Heads, Probability of Tails
x = random.choices(['Heads', 'Tails'], k = ns[0], weights = probs)
x2 = random.choices(['Heads', 'Tails'], k = ns[1], weights = probs)
x3 = random.choices(['Heads', 'Tails'], k = ns[2], weights = probs)
x4 = random.choices(['Heads', 'Tails'], k = ns[3], weights = probs)

# Organize results into a data frame
d = pd.DataFrame({
  'rolls' : [*x, *x2, *x3, *x4],
  'die' : [*[str(ns[0]) + ' Flips']*ns[0], *[str(ns[1]) + ' Flips']*ns[1], *[str(ns[2]) + ' Flips']*ns[2], *[str(ns[3]) + ' Flips']*ns[3]]
})

d['die'] = d['die'].astype('category').cat.reorder_categories([str(ns[0]) + ' Flips', str(ns[1]) + ' Flips', str(ns[2]) + ' Flips', str(ns[3]) + ' Flips'], ordered = True)

# Plot results
(ggplot(d, aes(x = 'rolls', y = after_stat('prop'), group = 1)) +
  geom_bar() +
  geom_segment(aes(x = .55, y = .7, xend = 1.45, yend = .7), color = 'red') +
  geom_segment(aes(x = 1.55, y = .3, xend = 2.45, yend = .3), color = 'blue') +
  facet_wrap('die', nrow = 2) +
  ylim(0, 1) +
  ylab('Proportion') +
  xlab('Flip Outcome') +
  ggtitle('Loaded Coin Flips')
)

