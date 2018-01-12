# Example parse from a different file.
# Try to make sure you have templatingEngine.py in the same directory.
import templatingEngine

print(
    templatingEngine.translateToHTML(
        "TestCase3.htmlp", {
            "person": "foo",
            "friends": ["bar", "baz"],
            "bo": True,
            "something": "Chicken"
        }))
