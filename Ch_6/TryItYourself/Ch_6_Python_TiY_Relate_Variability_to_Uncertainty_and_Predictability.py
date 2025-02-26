#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Relate Variability to Uncertainty and Predictability ####

# Importing necessary libraries
import pandas as pd
import random
from plotnine import ggplot, aes, geom_bar, facet_wrap, ylab, xlab, ggtitle

# Perform simulations
random.seed(1234)
n = 10000
x = random.choices(['Heads', 'Tails'], k = n)
x2 = random.choices(['Heads', 'Tails'], weights = [.98, .02], k = n)
x3 = random.choices(['Heads', 'Tails'], weights = [.3, .7], k = n)

# Organize results
d = pd.DataFrame({
  'rolls' : [*x, *x2, *x3],
  'die' : [*['Coin 1']*n, *['Coin 2']*n, *['Coin 3']*n]
})

# Plot simulations
(ggplot(d, aes(x = 'rolls')) +
  geom_bar() +
  facet_wrap('die') +
  ylab('Count') +
  xlab('Flip Outcome') +
  ggtitle('Flips for Three Different Coins')
)

