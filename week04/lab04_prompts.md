Problem 1:
Pasted this block and the code block to gemini: "Scenario: You have two very large lists of product IDs from two different suppliers. You need to find out which product IDs are present in both lists so you know which products you can source from either supplier. The order of the final list does not matter."
**AI Recommendation:** You should use a **Set**.

**Reasoning:**
* **Speed:** Sets are designed for extremely fast lookups. Checking if an item exists in a set takes a fraction of the time compared to searching through a list.
* **Efficiency:** When you have "very large lists," converting them to sets allows you to use a mathematical "intersection" operation to instantly find matches, rather than looping through thousands of items one by one.

Problem 2:
Pasted this block and the code block to gemini: "Scenario: Your application loads a list of user profiles from a database. Each user has a unique username, an age, and an email address. You frequently need to look up a user's complete profile by their username. Performance is critical."
**AI Recommendation:** You should use a **Dictionary** (also known as a Hash Map).

**Reasoning:**
* **Instant Access:** A list requires you to scan through every single user one by one to find a match (Linear Search). A dictionary allows you to use the username as a "key" to jump directly to the user's data instantly (Constant Time, or O(1)).
* **Key-Value Pairing:** Since your usernames are unique, they serve as perfect keys to map directly to the profile data values.

Problem 3:
Pasted this block and the code block to gemini: "Scenario: You are given a list of integers representing sensor readings. You need to produce a report that contains only the even-numbered readings, and they must be presented in the exact same order they were received."
**AI Recommendation:** You should use a **List**.

**Reasoning:**
* **Order Preservation:** Unlike sets or dictionaries (in older Python versions), lists are strictly ordered. They guarantee that items remain in the sequence they were added.
* **Iteration:** Lists are optimized for iteration and filtering, which is exactly what you need to do (scan through, pick evens, keep order).