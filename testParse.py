from TemplatingParser import templatingParser

print(
    templatingParser.translateToHTML(
        "TestCase3.htmlp", {
            "person": "foo",
            "friends": ["bar", "baz"],
            "bo": True,
            "something": "Chicken"
        }))
