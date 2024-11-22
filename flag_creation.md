# Flag Creation

Flags themselves need to be hard to guess, but also immediately recognizable. 

---

Specific events or entities will have their own formats for their flags.

**For CyberCWRU events** flags should follow the format:

```CYCWRU{th1s_1s_a_f14g}```

---

The `CYCWRU{...}` format will be universal across all challenges. This signals to the user that they have in fact found the correct flag.

The inner part of the flag often has to do with the challege or solution. For example:

```CYCWRU{sql_1nj3cti0n_1s_fun}```

```CYCWRU{tak1ng_c1ient_s1de_5ecrets}```

---

Sometimes, some random characters can be added to increase the difficulty in guessing the flag without finding it. For example:

```CYCWRU{sql_1nj3cti0n_1s_fun_0x8e47sd90}```

```CYCWRU{tak1ng_c1ient_s1de_5ecrets_10100001001010100}```

---

## **ACTUAL FLAGS SHOULD NEVER BE COMMITTED TO THE GITHUB REPOs**

If a flag is being stored in the code for the challenge, use a placeholder such as `CYCRWU{placeholder}` and signal that in the repository documentation it ensure it is replaced before deployment.

---

