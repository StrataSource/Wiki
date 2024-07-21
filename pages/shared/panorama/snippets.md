---
title: Snippets
---

# Snippets

Snippets are reusable layouts defined within the layout file of another panel. They are most often used with `Panel.LoadLayoutSnippet` to dynamically populate a panel from JavaScript.

The snippets defined within a panel's layout are only accessible to code running within that panel's context. That is, panel A will not be able to reference panel B's snippets using `LoadLayoutSnippet`.

# Example Code

The following code shows how to define a snippet in a layout file:

```xml
<!-- layout/pages/mycoolpage.xml -->
<root>

    <styles>
        <include src="file://{resources}/styles/main.scss">
    </styles>

    <!-- Include the script that will make use of the snippet -->
    <scripts>
        <include src="file://{scripts}/mypage.js">
    </snippets>

    <!-- Define the snippets for this panel -->
    <snippets>
        <snippet name="MyCoolSnippet">
            <Panel class="flow-down">
                <!-- We're using a dialog variable to display the name -->
                <Label text="Hello, {s:name}"/>
                <Label text="Another line of {s:other_line}"/>
            </Panel>
        </snippet>
    </snippets>


    <Panel class="full flow-down" id="MyRoot">
        <!-- The snippets will be added here by the code -->
    </Panel>

</root>
```

The following script populates the above panel with children:

```js
// scripts/mypage.js

class MyPage {

    static {
        // Get the root panel
        const root = $("#MyRoot");

        const names = ['Billy', 'Joe', 'Bob', 'Sean', 'Sussy'];

        // Create a few panels
        for (let i = 0; i < 5; ++i) {
            // Create a new panel with the root and a unique name
            const panel = $.CreatePanel('Panel', root, 'myid_' + i);

            // Load the snippet on the panel
            panel.LoadLayoutSnippet('MyCoolSnippet');

            // Now, we'll set the dialog vars
            panel.SetDialogVariable('name', names[i]);
            panel.SetDialogVariable('other_line', 'CHEESE');
        }
    }
}
```
