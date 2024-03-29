# Alfred Target Process

Quickly navigate to Target Process tickets in [Alfred 3][alfred].

![][sample]

## Setup and Usage
* Open Alfred and click the `[x]` icon in the top right of the workflow
* Set your TP Slug as a workflow environment variable
  * eg, `https://mycompany.tpondemand.com` becomes `mycompany`
* Run `tp <id #>` to navigate to a ticket, eg: `tp 1123`

## TODOs
* Initial release.

# Thanks, License, Copyright

- The [Alfred-Workflow][alfred-workflow] library is used heavily, and it's wonderful documentation was key in building the plugin.
- The Target Process icon is used, care of Target Process.

All other code/media are released under the [MIT Licence][license].

[alfred]: http://www.alfredapp.com/
[alfred-workflow]: http://www.deanishe.net/alfred-workflow/
[license]: src/LICENSE.txt
[sample]: https://raw.github.com/lukewaite/alfred-target-process/master/docs/sample.jpg
