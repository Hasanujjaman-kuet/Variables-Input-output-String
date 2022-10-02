# %% [markdown]
# # Variable and Data Types

# %% [markdown]
# ## String

# %%
name = "Alley Smith"
type(name)

# %%
email = 'alley@gmail.com'
type(email)

# %%
# indexing [start:stop:step]
name[3]
name[-2]
name[:3]

# %%
email[5:11:2]
email[-11:-5:1]
email[5::]
email[::-1]

# %%
# string methods
name = "Alley Smith"
name.upper()
name.lower()
name.title()
name.capitalize()
name.swapcase()
name.count('l')

# %%
email = 'alley@gmail.com'
email.split('@')
email.endswith('@yahoo.com')
email.startswith('a')
email.replace('@', '$')
email.replace('gmail', 'yahoo')

# %%
email.replace('@gmail', '@yahoo')

# %%
email[email.find('@'):]

# %%



